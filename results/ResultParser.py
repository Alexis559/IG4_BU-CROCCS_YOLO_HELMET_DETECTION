import json
from Object import Object

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

    def get_objects_text(self):
        text = "=====   YOLO RESULTS   =====\n\n"
        for object in self.objects:
            text = text + object.to_string() + "%\n"

        return text
