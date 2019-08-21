import argparse
import string
import sys
from ctypes import *
import math
import random
import os
import cv2
import numpy as np
import time
import darknet
from Object import *
from Utils import *


'''

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS
    Program to analyse video with Darknet and YOLO
    
    Based on the darknet_video.py example from AlexeyAB fork of Darknet
    https://github.com/AlexeyAB/darknet
    
'''

def cvDrawBoxes(detections, img):
    for detection in detections:
        pt1 = (int(round(detection.x_min)), int(round(detection.y_min)))
        pt2 = (int(round(detection.x_max)), int(round(detection.y_max)))

        # Label color by default white
        color = [255, 255, 255]

        if detection.label == 'person':
            # If the person is related with a helmet and a motorbike then it's good we display a green bounding box
            if len(detection.objects_related) == 2:
                cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
                color = [0, 255, 0]

            # If the person is related just with a helmet or a motorbike then it's not good we display a red bounding box
            elif len(detection.objects_related) == 1:
                cv2.rectangle(img, pt1, pt2, (255, 0, 0), 2)
                color = [255, 0, 0]

            # If the person is alone we display a white bounding box
            else:
                cv2.rectangle(img, pt1, pt2, (255, 255, 255), 1)
        else:
            cv2.rectangle(img, pt1, pt2, (255, 255, 255), 1)

        # Display the label of the object next to the bounding box
        cv2.putText(img,
                    detection.label +
                    " [" + str(round(detection.confidence * 100, 2)) + "]",
                    (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    color, 2)
    return img


netMain = None
metaMain = None
altNames = None


def YOLO(cfg_file, weights_file, data_file, video_file, threshold):

    global metaMain, netMain, altNames
    configPath = cfg_file
    weightPath = weights_file
    metaPath = data_file
    if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    if netMain is None:
        netMain = darknet.load_net_custom(configPath.encode(
            "ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(video_file)
    cap.set(3, 1280)
    cap.set(4, 720)
    out = cv2.VideoWriter(
        "output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 10.0,
        (darknet.network_width(netMain), darknet.network_height(netMain)))
    print("Starting the YOLO loop...")

    # Create an image we reuse for each detect
    darknet_image = darknet.make_image(darknet.network_width(netMain),
                                    darknet.network_height(netMain),3)
    while True:
        prev_time = time.time()
        ret, frame_read = cap.read()
        frame_rgb = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb,
                                   (darknet.network_width(netMain),
                                    darknet.network_height(netMain)),
                                   interpolation=cv2.INTER_LINEAR)

        darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes())

        detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=threshold)

        # BEGINNING OF THE ANALYSIS

        objects = []  # Objects detected by YOLO
        drivers = []  # Persons considered as drivers
        wearing_helmet = []  # Persons wearing a helmet

        # We get all the objects detected by YOLO
        for obj in detections:
            objects.append(Object(obj[0].decode("utf-8") , obj[1], obj[2][0], obj[2][1], obj[2][2], obj[2][3]))

        for obj in objects:
            obj.calculaterealpredictionbox()

        for object in objects:
            if object.label == 'motorbike':
                for object2 in objects:
                    # If the object is a person and has not been already associated with a motorbike
                    if object2.label == 'person' and len(object2.objects_related) == 0:
                        if is_driver(object, object2):  # If there is a relation between the person and the motorbike
                            # We create the association between the motorbike and the person for the bounding box drawing
                            object.objects_related.append(object2)
                            object2.objects_related.append(object)
                            drivers.append(object2)

        for person in drivers:
            for object2 in objects:
                if object2.label == 'helmet':
                    if wear_helmet(person, object2):  # If there is a relation between the person and the helmet
                        # We create the association between the helmet and the person for the bounding box drawing
                        person.objects_related.append(object2)
                        object2.objects_related.append(person)
                        wearing_helmet.append(object2)

        print('There are ' + str(len(drivers)) + ' drivers and only ' + str(len(wearing_helmet)) + ' are wearing a helmet !')

        # END OF THE ANALYSIS

        image = cvDrawBoxes(objects, frame_resized)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(1/(time.time()-prev_time))
        cv2.imshow('Demo', image)
        cv2.waitKey(3)
    cap.release()
    out.release()

if __name__ == "__main__":

    a = argparse.ArgumentParser()
    a.add_argument("--cfg_file", "--c", help="path to cfg file")
    a.add_argument("--weights_file", "--w", help="path to weights file")
    a.add_argument("--data_file", "--d", help="path to data file")
    a.add_argument("--video_file", "--v", help="path to the video file")
    a.add_argument("--threshold", "--t", help="threshold for detection")
    args = a.parse_args()

    if args.cfg_file is None or args.weights_file is None or args.data_file is None or args.video_file is None or args.threshold is None:
        a.print_help()
        sys.exit(1)

    YOLO(args.cfg_file, args.weights_file, args.data_file, args.video_file, float(args.threshold))
