import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture("video/Videos_full/CPPG-ASD-001/202110200851_MVData_DDK_3_subj_CPPG-ASD-001-day2/full_video.mp4")
#print(cap)
#cap = cv2.VideoCapture(2) #use webcam
# only for one face, plot it for one face

#def blinkCounter(cap):
detector = FaceMeshDetector(maxFaces = 1)
plotY = LivePlot(640*5,480*5,[0,500], invert = True) #width, height , y limit

idList = [22,23,24, 26, 110, 157, 158, 159, 160, 161,130, 243] #point to test
# if too far away than it will think blinked if we just measure the distance
ratioList = []
blinkCounter = 0
counter = 0 #we are using this to only accept the first value of 10 frames
# we can also code with different idea such as using the difference between value etc.
totalCount = 0
color = (255,0,255)

while True:

    # getting object from capture --> Setting zero to not shut down the video
    #if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # position of current frame = total count of frame
    #    cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        # reset to replay
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False) #not draw white lines on image

    if faces:
        face=faces[0] #get face 0 which we only have one
        #for id in idList:
            #cv2.circle(img,face[id], 1, color, cv2.FILLED) #draw circle on our video #size 5 purple

        leftUp = face[158] #point on top of eye
        leftDown = face[23] # point of bottom of eye
        leftLeft = face[130]
        leftRight = face[243]

        lengthHor,_ = detector.findDistance(leftUp, leftDown)
        lengthVer,_ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img, leftUp, leftDown, (0,200,0),3)
        cv2.line(img, leftLeft, leftRight, (0,200,0), 3)
        print(lengthHor) # value gets lower when blink
        cv2.line(img, leftUp, leftDown, (0,200,0), 3) # dark green with thickness 3

        ratio = lengthVer/lengthHor*100 # smoother plot if in float
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0) #pop first value
        ratioAvg = sum(ratioList)/len(ratioList)

        if ratioAvg >355 and counter ==0: # first time only #value for CPPG-CON-003
            blinkCounter +=1
            color = (0,200,0)
            counter = 1 #make counter 1
            totalCount += 1
            ############Add the current timestamp and count change
        if counter != 0:
            counter +=1 #keep adding
            if counter >10: # if more than 10
                counter = 0 #accept again
                color = (255,0,255)

        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (20,60), colorR=color)
        cvzone.putTextRect(img, f'Ratio: {ratioAvg}', (20, 120), colorR=color)
        imgPlot = plotY.update(ratio) #give the value
        imgPlot = plotY.update(ratioAvg, color)
        img = cv2.resize(img, (640*5, 480*5))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 0.8) #vertically one column 1, scale 1
        # 2 on the first one for horizontal
    else:
        img = cv2.resize(img, (640*5, 480*5))
        imgStack = cvzone.stackImages([img, img], 2, 0.8)

    cv2.imshow("Image Stack", imgStack)  # show image
    #cv2.imshow("Image", img)  # show image
    cv2.waitKey(20)

        #return totalCount

#blinkCounter(cap)