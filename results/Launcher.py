# coding: utf-8

import tkinter as tk
from YOLO import *
from ResultParser import *
from PIL import ImageTk, Image
import tkinter.filedialog as tkFiledialog

'''

    MADE BY ALEXIS SANCHEZ IG4 - BU-CROCCS
    GUI to analyse YOLO objects detection

'''

"""
    Class to handle the images: load and delete images to analyse
"""


class ImgManager:

    def __init__(self):
        self.clicked = False
        self.img = ''
        self.filename = ''
        self.width_max = 1040
        self.height_max = 657

    """Function to resize the images when there are too big to be displayed
        
        Parameters
        ----------
        image : ??
                The image to resize
                
        Returns
        -------
        ??
            The image resized      
    
    """

    def resize_img(self, image):
        width, height = image.size
        if width > self.width_max or height > self.height_max:
            if width > height:
                ratio = height/width
                height = int(self.width_max * ratio)
                image = image.resize((self.width_max, height), Image.ANTIALIAS)

            else:
                ratio = width/height
                width = int(self.height_max * ratio)
                image = image.resize((width, self.height_max), Image.ANTIALIAS)

        return image

    """Function called to change the current displayed image

        Parameters
        ----------
        image_path : str
                The path to the newest image

    """

    def change_image(self, image_path):
        self.img.image = ''
        self.img.pack_forget()
        load = Image.open(image_path)
        load = self.resize_img(load)
        render = ImageTk.PhotoImage(load)
        self.img = tk.Label(main_window, image=render)
        self.img.image = render
        self.img.pack(fill="both", expand=True)

    """
        Function to select an image and display it     
        
    """

    def get_file_name(self):
        if not self.clicked:

            # We open the dialog window
            self.filename = tkFiledialog.askopenfilename()

            # We do some verifications such as if it's a real image
            if self.filename != '' and self.filename.split(".")[1] == "jpg" or self.filename.split(".")[1] == "png":
                self.clicked = True
                btn_image_text.set("Clear")

                # We open the image and displaying the image
                load = Image.open(self.filename)
                load = self.resize_img(load)
                render = ImageTk.PhotoImage(load)
                self.img = tk.Label(main_window, image=render)
                self.img.image = render
                self.img.pack(fill="both", expand=True)
        else:
            self.clicked = False
            btn_image_text.set("Open image")
            yolo_infos_text.set("")
            self.img.image = ''
            self.img.pack_forget()


"""

    Function called when the detect button is pressed to analyse the image and get the YOLO's results

"""


def get_yolo_infos():
    # We call the YOLO analyse
    YOLO.get_yolo_detection(img_manager.filename)

    # We get the results
    results.parse_yolo_result()

    yolo_infos_text.set(results.get_objects_text())
    img_manager.change_image("predictions.jpg")
    print(results.get_objects_text())


"""
    MAIN FUNCION - Prepare and launch the main window
"""

if __name__ == '__main__':
    img_manager = ImgManager()
    results = ResultParser("../results/result2.json")

    # We create a new window
    main_window = tk.Tk()
    main_window.title("YOLO Helmet Detection")
    main_window.geometry("1280x720")
    main_window.resizable(False, False)

    # We create all the panes for our window
    yolo_infos_pane = tk.PanedWindow(main_window, bg="gray", height="720", width="300")
    title_pane = tk.PanedWindow(main_window)
    buttons_pane = tk.PanedWindow(main_window, height="100", width="1280")
    yolo_infos_title = tk.PanedWindow(yolo_infos_pane, height="100", width="300")

    btn_image_text = tk.StringVar()
    yolo_infos_text = tk.StringVar()
    action_detect_image = lambda: YOLO.get_yolo_detection(img_manager.filename)
    action_image_btn = lambda: img_manager.get_file_name()

    # Creation of the 2 buttons at the bottom
    detect_btn = tk.Button(buttons_pane, text="Detect", command=get_yolo_infos)
    image_btn = tk.Button(buttons_pane, textvariable=btn_image_text, command=action_image_btn)

    btn_image_text.set("Open image")
    label = tk.Label(title_pane, text="YOLO Helmet Detection")
    yolo_infos_label = tk.Label(yolo_infos_title, text="YOLO Infos")
    yolo_results_label = tk.Label(yolo_infos_title, textvariable=yolo_infos_text)

    # We add the different widgets to their pane
    buttons_pane.add(detect_btn)
    title_pane.add(label)
    buttons_pane.add(image_btn)
    yolo_infos_pane.add(yolo_infos_title)
    yolo_infos_title.add(yolo_infos_label)
    yolo_infos_title.add(yolo_results_label)

    # We place the different panes and widgets on the window
    yolo_infos_pane.pack(side="right", fill='both')
    yolo_infos_title.pack(side="top", fill='both')
    yolo_results_label.pack(side="bottom", fill='both', expand=True, pady=40)
    yolo_infos_label.pack(side="left", fill='both', expand=True, padx=80, pady=4)
    buttons_pane.pack(side="bottom")
    title_pane.pack(side="top")
    label.pack(side="top")
    detect_btn.pack(side="left", fill='both', expand=True, padx=4, pady=4)
    image_btn.pack(side="right", fill='both', expand=True, padx=4, pady=4)

    main_window.mainloop()
