# [IG4] [BU-CROCCS] YOLOv3 to detect helmet

Yolo Application to detect drivers who are not wearing helmets while there are driving.

Trained on 3 classes using the [Coco dataset](https://cocodataset.org/#home) and [Open images](https://storage.googleapis.com/openimages/web/download.html):

* Person
* Motorbike
* Helmet

The training was made by using [Google Colaboratory](https://colab.research.google.com)

## Images

You can find in the **results** folder all the classes to process the YOLO results analysis on images

You can launch the GUI for images analysis with the following command:
`python3 Launcher.py`

## Videos

You can find in the **darknet_python** folder all the classes to process the YOLO results analysis on videos 

You can launch the GUI for videos analysis with the following command:
`python3 darknet_video_helmet.py ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights ../cfg/helmet.data *path to the video* *threshold for the objects detection*`

The threshold is used to filter the objects detected by YOLO with a confidence score lower than it. Must be between 0 and 1. As the neural network needs more training I used a threshold of 0.05.

You can download the `yolov3-helmet.weights` file [here](https://drive.google.com/file/d/12ltZYcccMbaYrAJmzhgj6IbwMraV2VqV/view?usp=sharing)

## Darknet commands with Linux

To launch the training use the following command:<br/>
`./darknet detector train cfg/helmet.data cfg/yolov3-helmet.cfg weights/yolov3-helmet.weights`

To test on images the neural network use the following command:<br/>
`./darknet detector test cfg/helmet.data cfg/yolov3-helmet.cfg weights/yolov3-helmet.weights *path to the image*`

To test on videos the neural network use the following command:<br/>
`./darknet detector demo cfg/helmet.data cfg/yolov3-helmet.cfg weights/yolov3-helmet.weights *path to the video*`

To test on your webcam the neural network use the following command:<br/>
`./darknet detector demo cfg/helmet.data cfg/yolov3-helmet.cfg weights/yolov3-helmet.weights -c 0`

## Darknet commands with Windows

Go into the `x64_windows_darknet` folder

To launch the training use the following command:<br/>
`.\darknet.exe detector train ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights`

To test on images the neural network use the following command:<br/>
`.\darknet.exe detector test ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights *path to the image*`

To test on videos the neural network use the following command:<br/>
`.\darknet.exe detector demo ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights *path to the video*`

To test on videos the neural network use the following command:<br/>
`.\darknet.exe detector demo ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights -c 0`


You can find my Google colab notebook [here](https://colab.research.google.com/drive/18G9Vvop254As43gVXhPCXvP-6u6lsgqD).


You can find a PDF manual that explains the work I did with Google colab to train my neural network [here](https://github.com/Alexis559/IG4_BU-CROCCS_YOLO_HELMET_DETECTION/blob/master/How%20to%20train%20YOLOv3%20with%20Google%20Colab.pdf)



### Technologies:
[YOLOv3](https://pjreddie.com/darknet/yolo/)<br/>
[Darknet fork from AlexeyAB](https://github.com/AlexeyAB/darknet)<br/>
[Python 3](https://www.python.org/download/releases/3.0/)<br/>
[tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)<br/>
[Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb)<br/>
[OpenCv](https://opencv.org/)

### Sources:
[How to train YOLOv3 with Google Colab](https://colab.research.google.com/drive/1lTGZsfMaGUpBG4inDIQwIJVW476ibXk_#scrollTo=Cqo1gtPX6BXO)
