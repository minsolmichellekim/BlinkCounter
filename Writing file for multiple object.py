import BlinkCounter
# from BlinkCounter import (function name)
import cv2
import os
import csv

with open("BlinkCountResults.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Video File", "Blink Count"])

    video_dir = "video/Videos_full"
    for root, dirs, files in os.walk(video_dir):
        for file2 in files:
            if file2.endswith(".mp4"):
                print(f"Processing root: {root}")
                # open the video file
                video_file = os.path.join(root, file2)
                print(video_file)

                with open(video_file, mode='w', newline='') as f: #file2
                    writer = csv.writer(f)
                    writer.writerow(['timestamp', 'frame_number', 'blink_count'])
                    split = root.split("/")
                    # process video file and get the blink count
                    result = BlinkCounter.blinkCount_process(cv2.VideoCapture(str(video_file)))
                    for d in result:
                        writer.writerow([d[video_file], d['timestamp'], d['frame_number'], d['blink_count']])
                        print("result saved")



