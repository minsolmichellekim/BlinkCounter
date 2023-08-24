import BlinkCounter3
# from BlinkCounter import (function name)
import cv2
import os
import csv

video_dir = "video/Videos_full"
filename = 'output_all.csv'

with open("BlinkCounter/BlinkCountResults.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Video File", "Blink Count"])

    for root, dirs, files in os.walk(video_dir):
        for file2 in files:
            if file2.endswith(".mp4"):
                print(f"Processing file: {file2}")
                # open the video file
                video_file = os.path.join(root, file2)

                with open(file2, mode='w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['timestamp', 'frame_number', 'blink_count'])
                    cap = cv2.VideoCapture(video_file)
                    # process video file and get the blink count
                    result = BlinkCounter3.blinkCount_process(cap)
                    for d in result:
                        writer.writerow([d[video_file],d['timestamp'], d['frame_number'], d['blink_count']])



