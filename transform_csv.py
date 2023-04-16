import csv
from datetime import datetime, timedelta
import math

input_file = '202211180713_MVData_Reading_2_subj_CPPG-ASD-009.csv'
output_file = "output_"+input_file
interval_duration = 60*1000 #milliseconds
current_blink_count = 0
previous_blink_count =0


# define a function to convert seconds to the "min:sec" format
def format_time(time_in_seconds):
    minutes = int(time_in_seconds/60)
    seconds = int(time_in_seconds - int(minutes*60))
    return f"{minutes:02d}:{seconds:02d}"

# read original csv file
with open(input_file, 'r') as file:
    csv_reader = csv.DictReader(file)

    with open(output_file, 'w', newline='') as output:
        fieldnames = ['directory', 'minute_interval', 'blink_count']
        csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
        csv_writer.writeheader()
        # initialize variables for interval calculations
        previous_blink_count = 0
        current_interval_start = 0
        current_interval_end = 0
        rows = list(csv_reader)
        last_row =rows[-1]
        print(last_row)
        last_timestamp = float(last_row["timestamp"])

        for row in rows:

            #print(row)
            # current timestamp
            #timestamp = datetime.fromtimestamp(int(float(row["timestamp"])))
            timestamp = float(row["timestamp"])
            current_blink_count = int(row["blink_count"])

            #print(current_blink_count)

            # if there was no previous timestamp or if interval exceeded
            # check now and the previous timestamp written as interval
            if current_interval_start == 0 or (timestamp - current_interval_start) >= interval_duration:
                print("entered")
                # Write with current interval
                current_interval_end = timestamp
                print("current_blink_count")
                print(current_blink_count)
                print(current_blink_count - previous_blink_count)
                print(row["frame_number"])
                print("__________")

                if current_interval_start != current_interval_end:
                    csv_writer.writerow({
                        "directory": row["directory"],
                        "minute_interval": f"{format_time(current_interval_start/1000)} - {format_time(current_interval_end/1000)}", #interval
                        "blink_count": str(current_blink_count - previous_blink_count)
                    })
                    # get ready for next interval round
                    previous_timestamp_end = current_interval_end
                    # reset interval start and end
                    current_interval_start = previous_timestamp_end
                    # reset blink count
                    previous_blink_count = current_blink_count


            if (timestamp == last_timestamp):
                print("last entered")
                timestamp = float(row["timestamp"])
                current_blink_count = int(row["blink_count"])
                blink_count = current_blink_count - previous_blink_count

                print("current_blink_count")
                print(current_blink_count)
                print(current_blink_count - previous_blink_count)
                print(row["frame_number"])
                print("__________")

                csv_writer.writerow({
                    "directory": row["directory"],
                    "minute_interval": f"{format_time(current_interval_start / 1000)} - {format_time(timestamp / 1000)}",
                    # interval
                    "blink_count": blink_count
                })
                break

            current_interval_end = timestamp
