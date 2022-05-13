import cv2
import os
import sys

def main(video_file):
    filename, _ = os.path.splitext(video_file)
    filename += "_output"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video file    
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(video_file, "'s fps :", fps)

    print("Frame capture start")

    # start the loop
    count = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        
        # save the frame
        cv2.imwrite(os.path.join(filename, f"frame_{count}.jpg"), frame) 

        # increment the frame count
        count += 1
    
    print("Total", count, "frames cature finished")


if __name__ == "__main__":
    video_file = sys.argv[1]
    main(video_file)