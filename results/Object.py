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
        image_path : str
                The path of the image
        label : str
                The predicted class for the object
        confidence : float
                The confidence score for this object (> 0 & < 1)
        x_center : float
                The x center of the bounding box (YOLO annotation > 0 && < 1)
        y_center : float
                The y center of the bounding box (YOLO annotation > 0 && < 1)
        box_width : float
                The width of the bounding box (YOLO annotation > 0 && < 1)
        box_height : float
                The height of the bounding box  (YOLO annotation > 0 && < 1)
        xcenterreal : int
                The x center of the bounding box (real value in pixel)
        ycenterreal : int
                The y center of the bounding box (real value in pixel)
        boxwidthreal : int
                 The width of the bounding box (real value in pixel)
        boxheightreal : int
                The height of the bounding box (real value in pixel)
    """

    def __init__(self, image_path, label, confidence, x_center, y_center, box_width, box_height):
        self.image_name = os.path.basename(image_path)
        self.label = label
        self.confidence = confidence
        self.x_center = x_center
        self.y_center = y_center
        self.box_width = box_width
        self.box_height = box_height
        self.xcenterreal = None
        self.ycenterreal = None
        self.boxwidthreal = None
        self.boxheightreal = None
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None

    """
        Parameters
        ----------
        images_folder : str
                The path of the folder where are stored the images used to do the prediction
    """

    def calculaterealcoordinates(self, images_folder):
        image = Image.open(images_folder + "/" + self.image_name)
        self.xcenterreal = self.x_center * image.size[0]
        self.ycenterreal = self.y_center * image.size[1]
        self.boxwidthreal = self.box_width * image.size[0]
        self.boxheightreal = self.box_height * image.size[1]

    """To calculate the top left point and the bottom right point of the bounding box which correspond to the (x_min, y_min) and (x_max, y_max)
        
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
        self.x_min = self.xcenterreal - self.boxwidthreal / 2
        self.x_max = self.xcenterreal + self.boxwidthreal / 2
        self.y_min = self.ycenterreal - self.boxheightreal / 2
        self.y_max = self.ycenterreal + self.boxheightreal / 2

    """Function to calculate the area of the bounding box    
    """

    def get_area(self):
        return self.boxwidthreal * self.boxheightreal

