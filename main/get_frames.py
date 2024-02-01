import time
import open3d as o3d
import numpy as np
def get_frames():
    start = time()
    print("Input path for file: ")
    path = input()
    data = open(path,'r')
    frames = []
    counter = 0
    for frame in data:
        counter += 1
        frame_data = frame.split(',')
        for finger in frame_data:
            finger = finger.split('|')
            for joint in finger:
                joint = joint.split(' ')
                for angle in joint:
                    angle =((int(angle))*(np.pi))/180
        frames.append(frame_data)
    end = time()
    print("Finished uploading data")
    print("{} frames taking {} ms", counter, end - start)
    return frames

