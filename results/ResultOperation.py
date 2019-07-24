#!python3


"""

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS
    Script to analyse the objects detected by YOLO

"""

import json
import argparse
import sys
import time


from Object import Object
from Utils import *

start_time = time.time()

"""
    Arguments
    ----------
    json_path : str
            The path of json file produced by YOLO where the predictions are written
    images_folder : str
        label : str
            The path of the folder where are stored the images used for the predictions
"""
if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--json_file", help="path to json file")
    a.add_argument("--images_folder", help="path to the images folder")
    args = a.parse_args()

    if args.json_file is None and args.images_folder is None:
        a.print_help()
        sys.exit(1)

    # We open the json file
    with open(args.json_file) as JsonFile:
        lines = json.loads(JsonFile.read())

    # We are parsing all the file in order to get the objects
    for line in lines:
        # List of the objects predicted by YOLO
        objects = []
        driver = []
        wearing_helmet = []

        for object in line['objects']:
            # We add to the list the object
            objects.append(Object(line['filename'], object['name'], object['relative_coordinates']['center_x'],
                                  object['relative_coordinates']['center_y'], object['relative_coordinates']['width'],
                                  object['relative_coordinates']['height']))

        for object in objects:
            object.calculaterealcoordinates(args.images_folder)
            object.calculaterealpredictionbox()

        for object in objects:
            if object.label == 'motorbike':
                for object2 in objects:
                    if object2.label == 'person':
                        if is_driver(object2, object):
                            driver.append(object2)

        for person in driver:
            for object2 in objects:
                if object2.label == 'helmet':
                    if wear_helmet(person, object2):
                        wearing_helmet.append(object2)

        print('===============   ' + str(line['frame_id']) + '   ===============')
        print('results: ' + str(len(driver) == len(wearing_helmet)))
        print("\n\n")

print("Execution Time : --- %s seconds ---" % (time.time() - start_time))