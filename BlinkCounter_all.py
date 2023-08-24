import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import numpy as np
import csv
import os


blinkArray = []
frame_number = 0
data =[]

def blinkcount_process(cap, dir):
    detector = FaceMeshDetector(maxFaces=1)
    ratioList = []
    blinkCounter = 0
    global blinkArray, frame_number, data
    counter = 0  # we are using this to only accept the first value of 10 frames

    while True:
        # Start the process
        try:
            success, img = cap.read()
            img, faces = detector.findFaceMesh(img, draw=True)  # not draw white lines on image #False?
            face = faces[0]  # get face 0 which we only have one

            leftUp = face[158]  # mostly 158 for all
            leftDown = face[23]  # point of bottom of eye
            leftLeft = face[130]
            leftRight = face[243]
            lengthHor, _ = detector.findDistance(leftUp, leftDown)
            lengthVer, _ = detector.findDistance(leftLeft, leftRight)

            ratio = lengthVer / lengthHor * 100  # smoother plot if in float
            ratioList.append(ratio)
            if len(ratioList) > 3:
                ratioList.pop(0)  # pop first value
            ratioAvg = sum(ratioList) / len(ratioList)

            if (ratioAvg > 315 or ratioAvg < 350) and counter == 0:  # first time only
                # 394 for CON-003
                # 345 for ASD-006
                blinkCounter += 1
                #color = (0, 200, 0)
                counter = 1  # make counter 1
                ############Add the current timestamp and count change
            if counter != 0:
                counter += 1  # keep adding
                if counter > 10:  # if more than 10
                    counter = 0  # accept again
                    #color = (255, 0, 255)
                # cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (20, 60), colorR=color)

            if not success:
                break
        except:

            continue # continue to the next frame.

        blinkArray.append(int(blinkCounter))
        # timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
        timestamp = frame_number / frame_rate * 1000
        frame_data = {'directory': dir, 'timestamp': timestamp, 'frame_number': frame_number, 'blink_count': blinkCounter}
        # print(frame_data)
        data.append(frame_data)
        frame_number += 1

        # The video reached the end
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            print("ended")
            break

    return data

array_all = []
with open("BlinkCountResults.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["directory", "timestamp", "frame_number", "blink_count"])

    video_dir = "video/Videos_full/CPPG-ASD-009"
    for root, dirs, files in os.walk(video_dir):
        for file2 in files:
            if file2 =="full_video.mp4":
                # open the video file
                video_file = os.path.join(root, file2)
                current_dir = os.getcwd()
                array_all.append(video_file)

for directory in array_all:
    print("directory: "+directory)
    result = blinkcount_process(cv2.VideoCapture(directory), directory)
    split_arr = directory.split("/")
    split_add = split_arr[3]

    with open(split_add+".csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['directory', 'timestamp', 'frame_number', 'blink_count'])
        for d in result : # write the data to the opened file
            writer.writerow([d['directory'], d['timestamp'], d['frame_number'], d['blink_count']])
