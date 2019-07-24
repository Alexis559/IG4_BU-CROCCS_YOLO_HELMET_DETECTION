import os


'''

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS
    Class to handle YOLO analysis

'''


class YOLO:

    """Function to call YOLO to analyse the image

           Parameters
           ----------
           image : str
                   The path of the image to analyse
    """

    @staticmethod
    def get_yolo_detection(image):
        if image != '' and image.split(".")[1] == 'jpg':
            os.system(
                '../darknet detector test ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights -ext_output '
                '-dont_show -out ../results/result.json ' + str(
                    image))
