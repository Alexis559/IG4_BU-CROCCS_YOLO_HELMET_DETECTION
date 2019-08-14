import json
from Object import Object
from Utils import  *

'''

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS
    Class to parse the YOLO results

'''

class ResultParser:

    """
           Parameters
           ----------
           path_json : str
                   The path where the json file produced by YOLO is stored
       """

    def __init__(self, path_json):
        self.path_json = path_json

    def parse_yolo_result(self):
        with open(self.path_json) as JsonFile:
            lines = json.loads(JsonFile.read())

            # We are parsing all the file in order to get the objects
        for line in lines:

            # List of the objects predicted by YOLO
            self.objects = []

            for object in line['objects']:

                # We add to the list the object
                self.objects.append(Object(line['filename'], object['name'], object['confidence'],
                                           object['relative_coordinates']['center_x'],
                                           object['relative_coordinates']['center_y'],
                                           object['relative_coordinates']['width'],
                                           object['relative_coordinates']['height']))

    def get_objects(self):
        return self.objects

    def get_analysis(self, images_folder):
        driver = []
        wearing_helmet = []
        objects = self.get_objects()

        for object in objects:
            object.calculaterealcoordinates(images_folder)
            object.calculaterealpredictionbox()

        for object in objects:
            if object.label == 'motorbike':
                for object2 in objects:
                    if object2.label == 'person':
                        if is_driver(object, object2):
                            driver.append(object2)

        for person in driver:
            for object2 in objects:
                if object2.label == 'helmet':
                    if wear_helmet(person, object2):
                        wearing_helmet.append(object2)

        return driver, wearing_helmet

    def get_objects_text(self):
        text = "=====   YOLO RESULTS   =====\n\n"
        for object in self.objects:
            text = text + object.label + ": " + str(round((object.confidence * 100), 2)) + "%\n"

        return text
