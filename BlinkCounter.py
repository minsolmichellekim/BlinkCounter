import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import csv

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
        try: #sometimes the face cannot be detected in the frame. Then, skip that frame
            success, img = cap.read()
            img, faces = detector.findFaceMesh(img, draw=True)  # not draw white lines on image #False?

            face = faces[0]  # get face 0 which we only have one

            leftUp = face[158]  # point on top of eye #159 for most
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
            print(ratioAvg)

            if (ratioAvg >320 and ratioAvg <350) and counter == 0:  # first time only #350 fo rmost
                blinkCounter += 1
                counter = 1  # make counter 1
                ############Add the current timestamp and count change
            if counter != 0:
                counter += 1  # keep adding
                if counter > 10:  # if more than 10
                    counter = 0  # accept again
            #print(blinkCounter)
        except:
            continue
        if not success:
            break
        blinkArray.append(int(blinkCounter))
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
        timestamp = frame_number / frame_rate * 1000
        print(timestamp)
        frame_data = {'directory': dir, 'timestamp': timestamp, 'frame_number': frame_number, 'blink_count': blinkCounter}
        #print(frame_data)
        data.append(frame_data)
        frame_number +=1
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            print("ended")
            break
        # Use in case the video doesn't end with person in the frame
        #if timestamp == 116300:
        #    print("ended")
        #    break

    return data

filename = '202211180719_MVData_Reading_3_subj_CPPG-ASD-009'
dir = "video/Videos_full/CPPG-ASD-009"+"/"+filename+"/full_video.mp4"

with open(filename+".csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['directory', 'timestamp', 'frame_number', 'blink_count'])
    result = blinkcount_process(cv2.VideoCapture(dir), dir)

    for d in result:
       writer.writerow([d['directory'], d['timestamp'], d['frame_number'], d['blink_count']])

