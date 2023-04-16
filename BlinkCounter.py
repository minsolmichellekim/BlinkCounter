import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
#import numpy as np
import csv

blinkArray = []
frame_number = 0
data =[]
def blinkcount_process(cap, dir):
    detector = FaceMeshDetector(maxFaces=1)
    # plotY = LivePlot(1200, 720, [0, 500], invert=True)  # width, height , y limit
    # idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]  # point to test
    # if too far away than it will think blinked if we just measure the distance
    ratioList = []
    blinkCounter = 0
    global blinkArray, frame_number, data
    counter = 0  # we are using this to only accept the first value of 10 frames
    # we can also code with different idea such as using the difference between value etc.
    # totalCount = 0
    # color = (255, 0, 255)
    while True:
        # Start the process
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=True)  # not draw white lines on image #False?

        try: #sometimes out of range when object pass by
            face = faces[0]  # get face 0 which we only have one

            # for id in idList:
            #    cv2.circle(img, face[id], 2, color, cv2.FILLED)  # draw circle on our video #size 5 purple

            leftUp = face[158]  # point on top of eye #159 for most
            leftDown = face[23]  # point of bottom of eye
            leftLeft = face[130]
            leftRight = face[243]

            lengthHor, _ = detector.findDistance(leftUp, leftDown)
            lengthVer, _ = detector.findDistance(leftLeft, leftRight)

            # cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
            # cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)
            # print(lengthHor)  # value gets lower when blink
            # cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)  # dark green with thickness 3

            ratio = lengthVer / lengthHor * 100  # smoother plot if in float
            ratioList.append(ratio)
            if len(ratioList) > 3:
                ratioList.pop(0)  # pop first value
            ratioAvg = sum(ratioList) / len(ratioList)

            if ratioAvg > 355 and counter == 0:  # first time only #350 fo rmost
                blinkCounter += 1
                color = (0, 200, 0)
                counter = 1  # make counter 1
                ############Add the current timestamp and count change
            if counter != 0:
                counter += 1  # keep adding
                if counter > 10:  # if more than 10
                    counter = 0  # accept again
                    color = (255, 0, 255)
                # cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (20, 60), colorR=color)
                # imgPlot = plotY.update(ratio) #give the value
            #print(blinkCounter)
        except:
            continue
        if not success:
            break
        blinkArray.append(int(blinkCounter))
        # imgPlot = plotY.update(ratioAvg, color)
        # img = cv2.resize(img, (1200, 720)) #imgStack = cvzone.stackImages([img, imgPlot], 1, 1)  # vertically one column 1, scale 1 # 2 on the first one for horizontal
        #timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
        timestamp = frame_number / frame_rate * 1000
        frame_data = {'directory': dir, 'timestamp': timestamp, 'frame_number': frame_number, 'blink_count': blinkCounter}
        #print(frame_data)
        data.append(frame_data)
        frame_number +=1
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            print("ended")
            break
    # cv2.imshow("Image", img)  # show image
        #cap.release()
    return data

filename = '202110200851_MVData_DDK_3_subj_CPPG-ASD-001-day2'
dir = "video/Videos_full/CPPG-ASD-001"+"/"+filename+"/full_video.mp4"

with open(filename+".csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['directory', 'timestamp', 'frame_number', 'blink_count'])
    result = blinkcount_process(cv2.VideoCapture(dir), dir)
    for d in result: #data
       writer.writerow([d['directory'], d['timestamp'], d['frame_number'], d['blink_count']])

