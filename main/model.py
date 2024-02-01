
import open3d as o3d

import numpy as np
import get_frames
import hand

paused = False
FPS = 30
def pause():
    global pasued
    paused = not paused
def loop(subframe,fingers,frame,prevfr,vis):
    if (subframe == 0):
        for finger in fingers:
            joints = frame[frame.index(finger)]
            prevjt = prevfr[frame.index(finger)]
            finger.rotate("base",joints[0] - prevfr[0])
            finger.rotate("middle",joints[1] - prevfr[1])
            finger.rotate("tip",joints[2] - prevfr[2])
            finger.update(vis)
            vis.register_key_callback(32, pause())
            vis.register_key_callback(256,exit())

if __name__ == "__main__":
    frames = get_frames()
    pinkie = hand.Finger(-1,0,0,1)
    ring = hand.Finger(0,0,0,1)
    middle = hand.Finger(1,0,0,1)
    index = hand.Finger(2,0,0,1)
    tester = o3d.geometry.TriangleMesh.create_cylinder()
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    fingers = [pinkie,ring,middle,index]
    i = 0
    
        
    prevfr = frames[0]
    for finger in fingers:
        joints = prevfr[fingers.index(finger)]
        finger.rotate("base", joints[0])
        finger.rotate("middle", joints[1])
        finger.rotate("tip", joints[2])
        finger.draw(vis)

    while(not paused): 
        for frame in frames:
            loop(i,fingers,frame,prevfr,vis)
            i = np.mod(i+1, FPS)


