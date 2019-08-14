import os
import platform

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
            if platform.system() == 'Windows':
                os.system(
                    '..\\x64_windows_darknet\darknet.exe detector test ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights -thresh 0.1 -ext_output '
                    '-dont_show -out ../results/result.json ' + str(
                        image))
            else:
                os.system(
                    '../darknet detector test ../cfg/coco.data ../cfg/yolov3.cfg ../weights/yolov3-helmet.weights -thresh 0.05 -ext_output '
                    '-dont_show -out ../results/result.json ' + str(
                        image))

    """Function to call YOLO to analyse a video

              Parameters
              ----------
              video : str
                      The path of the video to analyse
    """

    @staticmethod
    def get_yolo_detection_video(video):
        if video != '' and (video.split(".")[1] == 'mp4' or video.split(".")[1] == 'mkv' or video.split(".")[1] == 'avi'):
            if platform.system() == 'Windows':
                os.system(
                    '..\\x64_windows_darknet\darknet.exe detector demo ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights -thresh 0.05 -ext_output '
                    '-out ../results/result.json ' + str(
                        video))
            else:
                os.system(
                    '../darknet detector demo ../cfg/coco.data ../cfg/yolov3.cfg ../weights/yolov3-helmet.weights -thresh 0.05 -ext_output '
                    '-out ../results/result.json ' + str(
                        video))

    """Function to call YOLO to analyse the webcam

    """

    @staticmethod
    def get_yolo_detection_camera():
        print('yooolo')
        if platform.system() == 'Windows':
            os.system(
                '..\\x64_windows_darknet\darknet.exe detector demo ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights '
                '-thresh 0.05 -c 0')
        else:
            os.system(
                '../darknet detector demo ../cfg/coco.data ../cfg/yolov3.cfg ../weights/yolov3-helmet.weights -thresh 0.05 -ext_output '
                '-out ../results/result.json -c 0')