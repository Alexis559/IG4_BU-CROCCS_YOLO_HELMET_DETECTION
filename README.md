# [IG4] [BU-CROCCS] YOLOv3 to detect helmet

Yolo Application to detect drivers who are not wearing helmets while there are driving.

Trained on 3 classes using the [Coco dataset](https://cocodataset.org/#home):

* Person
* Motorbike
* Helmet

The training was made by using [Google Colaboratory](https://colab.research.google.com)

You can find in the **results** folder all the classes to process the YOLO's results analysis

You can launch the GUI with the following command:
`python3 Launcher.py`

You can download the `yolov3-helmet.weights` file [here](https://drive.google.com/file/d/1Ospb0zUYy-SDq3h9mtaGKDYpnP2UmnHY/view?usp=sharing)

## Linux

To launch the training use the following command:<br/>
`./darknet detector train cfg/helmet.data cfg/yolov3-helmet.cfg weights/yolov3-helmet.weights`

To test the neural network use the following command:<br/>
`./darknet detector test cfg/helmet.data cfg/yolov3-helmet.cfg weights/yolov3-helmet.weights *path to the image*`

## Windows

Go into the `x64_windows_darknet` folder

To launch the training use the following command:<br/>
`.\darknet.exe detector train ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights`

To test the neural network use the following command:<br/>
`.\darknet.exe detector test ../cfg/helmet.data ../cfg/yolov3-helmet.cfg ../weights/yolov3-helmet.weights *path to the image*`


You can find my Google colab notebook [here](https://colab.research.google.com/drive/18G9Vvop254As43gVXhPCXvP-6u6lsgqD).

### Technologies:
[YOLOv3](https://pjreddie.com/darknet/yolo/)<br/>
[Darknet fork from AlexeyAB](https://github.com/AlexeyAB/darknet)<br/>
[Python 3](https://www.python.org/download/releases/3.0/)<br/>
[tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)<br/>

### Sources:
[How to train YOLOv3 with Google Colab](https://colab.research.google.com/drive/1lTGZsfMaGUpBG4inDIQwIJVW476ibXk_#scrollTo=Cqo1gtPX6BXO)
