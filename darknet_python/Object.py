import os
from PIL import Image

'''

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS
    Class to store the different information of the objects predicted by YOLO

'''


class Object:
    """
        Parameters
        ----------
        label : str
                The predicted class for the object
        confidence : float
                The confidence score for this object (> 0 & < 1)
        x_center : float
                The x center of the bounding box (real value in pixel)
        y_center : float
                The y center of the bounding box (real value in pixel)
        box_width : float
                 The width of the bounding box (real value in pixel)
        box_height : float
                The height of the bounding box (real value in pixel)
    """

    def __init__(self, label, confidence, x_center, y_center, box_width, box_height):
        self.label = label
        self.confidence = confidence
        self.x_center = x_center
        self.y_center = y_center
        self.box_width = box_width
        self.box_height = box_height
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None
        self.objects_related = []

    """To calculate the top left point and the bottom right point of the prediction box which correspond to the (x_min, y_min) and (x_max, y_max)
        
        Do a diagram if you are not sure about what are doing this function
        
        Pixel count start at the top left of the image (0,0) ----------------> (x)
                                                         |
                                                         |
                                                         |
                                                         |
                                                         |
                                                         v
                                                         (y)
    """

    def calculaterealpredictionbox(self):
        self.x_min = self.x_center - self.box_width / 2
        self.x_max = self.x_center + self.box_width / 2
        self.y_min = self.y_center - self.box_height / 2
        self.y_max = self.y_center + self.box_height / 2

    """Function to calculate the area of the bounding box    
    """

    def get_area(self):
        return self.box_width * self.box_height
