# ---------------------------------------------------------------------------------
# THIS IS A BACKEND CLASS THAT INCLUDES ALL THE PROGRAM FEATURES
#----------------------------------------------------------------------------------
# IMPORT ESSENTIAL LIBRARIES
from tkinter import (ttk,Tk,PhotoImage,Canvas, filedialog, RIDGE)
from tkinter.ttk import Style
from PIL import ImageTk, Image
#
import os.path
import pandas as pd
import csv
import cv2
import pickle as pkl
import numpy as np
#
# CLASS BACKEND IS CALLED IN MAIN PROGRAM (GUI.py)
#
class BackEnd:
    #
    def __init__(self, master, new_path):
        self.master = master
        self.resource_path = new_path
        self.menu_initialisation()
        self.tag_img = None
        #
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    #  ALL CHANGES FOR BUTTON INSERTION/REMOVABLE IN THE APP IS DONE IN THIS BLOCK                
    #              
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def menu_initialisation(self):
        #
        # THIS IS A STYLE FILE FOR APP BACKGROUND COLOR
        s = Style()
        s.configure('style1.TFrame', background="#0968c3")
        #------------------------------------------------------
        # FRAME 1: THIS IS A HEADER FRAME FOR APP HEADER TEXT AND LOGO
        self.frame_header = ttk.Frame(self.master, style='style1.TFrame')
        self.frame_header.pack()
        #
        k=self.resource_path("logo.png")
        # BELOW BLOCK IMPLEMENTS LOGO AND APP DESCRIPTION IN HEADER FRAME
        self.logo = PhotoImage(file=self.resource_path("logo.png")).subsample(1, 1)
        ttk.Label(
            self.frame_header, image=self.logo, background="#0968c3").grid(
            row=0, column=0, rowspan=3)
        ttk.Label(
            self.frame_header, text='Designed by Arka Bhowmik', font=("Arial", 9, "italic"), background="#0968c3", foreground="#ffffff").grid(
            row=0, column=2, columnspan=1)
        ttk.Label(
            self.frame_header, text='An Image Editor For Annotation', font=("Arial", 10, "bold"), background="#0968c3", foreground="#ffffff").grid(
            row=1, column=1, columnspan=3)
        #--------------------------------------------------------
        # FRAM 2:
        # THIS IS A BUTTON AND IMAGE WINDOW FRAME
        self.frame_menu = ttk.Frame(self.master, style='style1.TFrame')
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(10, 15))
        #
        # BELOW BLOCK IMPLEMENTS BUTTONS AND IMAGE WINDOW
        ttk.Label(
            self.frame_menu, text='Selection Menu', font=("Raleway", 9, "bold"), background="#0968c3", foreground="#ffffff").grid(
            row=0, column=0, columnspan=1, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Upload an Image", command=self.upload_action).grid(
            row=1, column=0, columnspan=1, padx=5, pady=5, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Upload a CSV", command=self.upload_action_csv).grid(
            row=4, column=0, columnspan=1, padx=5, pady=2, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Next", command=self.next_frame).grid(
            row=5, column=0, columnspan=1, padx=5, pady=2, sticky='sw')
        
        ttk.Label(
            self.frame_menu, text='Next button only works for uploaded csv file embedded with image path', wraplength=105, font=("Arial", 8, "italic"), background="#0968c3", foreground="#ffffff").grid(
            row=6, column=0, columnspan=1, rowspan=3, padx=1, pady=1, sticky='sw')
        
        ttk.Button(
            self.frame_menu, text="Save", command=self.save_action).grid(
            row=9, column=0, columnspan=1, padx=3, pady=1, sticky='sw')
        
        ttk.Label(
            self.frame_menu, text='Drag cursor from left to right on image to choose an ROI', font=("Raleway", 9, "bold"), background="#0968c3", foreground="#ffffff").grid(
            row=0, column=2, rowspan=1)
        #
        # CANVAS FOR IMAGE WINDOW
        self.x = self.y = 0                  # INITIALIZE THE X AND Y COORDINATE AS ZERO
        self.canvas = Canvas(self.frame_menu, bg="black", width=400, height=400, cursor="cross")
        self.canvas.grid(row=1, column=2, rowspan=10)
        #--------------------------------------------------------------------------
        # FRAME 3:
        # FOOTER FRAME
        self.apply_and_cancel = ttk.Frame(self.master, style='style1.TFrame')
        self.apply_and_cancel.pack()
        #
        ttk.Label(
            self.apply_and_cancel, text='Instruction:', font=("Raleway", 12, "bold"), background="#0968c3", foreground="#ffffff").grid(row=0, column=0, columnspan=1, rowspan=1)
        #
        ttk.Label(
            self.apply_and_cancel, text='Save before closing the App to retain the ROI selections', font=("Raleway", 12, "bold"), background="#0968c3", foreground="#ffffff").grid(row=1, column=0, columnspan=1, rowspan=1)
        #
        #
    #+++++++++++++++++++++++ END OF INITIALIZATION FUNCTION ++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    #
    #
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    #                        START OF ACTIONS FOR IMAGE UPLOAD BUTTON
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # (a) Image a single upload function
    def upload_action(self):
        #self.filetypes =[('image files', '*.jpg'), ('image files', '*.jpeg'), ('image files', '*.png'), ('image files', '*.pickel')]
        self.filetypes =[("all files", "*.*")]
        self.filename = filedialog.askopenfilename(title='Open an image', initialdir= os.getcwd(), filetypes=self.filetypes)
        self.tag_img = '1'
        dummyy_var = self.filename.split('.')[-1]
        print(self.filename)
        if dummyy_var == 'jpg':
            self.original_image = cv2.imread(self.filename)
            self.edited_image = cv2.imread(self.filename)
            self.display_image(self.edited_image)
        else:
            self.original_image = pkl.load(open(self.filename, "rb"))
            self.edited_image = pkl.load(open(self.filename, "rb"))
            self.display_image(self.edited_image)
        #
    #
    # (b) Display the single image in the canvas
    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image
        #
        # Define an event for canvas with mouse click
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        # Initialize the ROI parameters
        self.rect = None
        self.start_x = None
        self.start_y = None
        # Resize the selected image to default canvas size (Note: The rectangular ROI will be defined for this new size)
        # ROI parameters need to be downscaled to (224, 224) before printing to csv file.
        self.new_image  = cv2.resize(image, (400, 400))                      # Resizes the image
        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image)) # Opens the image in Tkinter
        self.canvas.config(width=400, height=400)
        self.canvas.config(scrollregion=(0,0,400,400))
        self.canvas.create_image(400 / 2, 400 / 2,  image=self.new_image) #
        #
    #
    # (c) Subfunction that saves mouse drag start position
    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        # create rectangle if not yet exist which is updated later
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red', width=3)
        #
    #
    # (d) Subfunction mouse on move events from start position   
    def on_move_press(self, event):
        # saves movement in x and y direction
        self.curX = self.canvas.canvasx(event.x)
        self.curY = self.canvas.canvasy(event.y)
        # Expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)
        #
    #
    # (e) Subfunction outputs the events on release of mouse 
    def on_button_release(self, event):
        if self.start_x < 0:
            self.start_x = 0
        elif self.start_x > 400:
            self.start_x = 400
        #
        if self.start_y < 0:
            self.start_y = 0
        elif self.start_y > 400:
            self.start_y = 400
        #
        if self.curX > 400:
            self.curX = 400
        elif self.curX < 0:
            self.curX = 0
        #
        if self.curY > 400:
            self.curY = 400
        elif self.curY < 0:
            self.curY = 0
        #
        img_scale = 224/400      # Image is caled down to 224
        self.crop_x1 = int(np.round(self.start_x*img_scale))
        self.crop_y1 = int(np.round(self.start_y*img_scale))
        self.crop_x2 = int(np.round(self.curX*img_scale))
        self.crop_y2 = int(np.round(self.curY*img_scale))
        pass
    #
    #+++++++++++++++++++++++++++ END OF UPLOAD IMAGE BUTTON ACTION++++++++++++++++++++++++++++++++++++++++++
    #
    #
    #
    #
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    #                            START ACTIONS FOR UPLOAD CSV BUTTON
    #
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # (a) CSV upload function
    def upload_action_csv(self):
        self.filetypes =[('Data file', '*.csv'), ('Data file', '*.txt'), ('Data file', '*.dat'), ('Excel file', '*.xls'), ('Excel file', '*.xlsx'), ('Excel file', '*.xl')]
        self.filenamee = filedialog.askopenfilename(title='Open a data file', initialdir= os.getcwd(), filetypes=self.filetypes)
        #
        self.df=pd.read_csv(self.filenamee)              # Read the csv file to a dataframe df
        #
        self.df_new = self.new_data_frame(self.df)      # Calls subfunction (b) that creates a 
                                                        # new dataframe with columns for bounding box
        #
        self.canvas.delete("all")                       # Clear the canvas with upload button
        self.crop_x1 = 0                                # Clear the crop data
        self.crop_y1 = 0
        self.crop_x2 = 0
        self.crop_y2 = 0
        self.display_image_4rm_csv(self.df_new)         # Calls another subfunction (c) to display the
                                                        # image from csv file
        #
    #
    #-----------------
    # (b) This subfunction returns a new dataframe which take care of
    # the case of csv file partially filled since 
    # the program was paused and resumed later 
    def new_data_frame(self, df):
        #
        flag = 1
        cols=df.columns                # IDENTIFY THE COLUMN NAMES
        for jdx in range(len(cols)):   # SEARCH ALL THE COLUMNS IN CSV FILE FOR 'bbox_x1'
            if cols[jdx] == 'bbox_x1':
                flag = 0
            else:
                pass
            #
        # IF 'bbox_x1' is absent flag = 1 else flag = 0
        # IF flag = 1 then it will add new column to the dataframe else
        # check for rows without a number where new data will be inserted
        #
        if flag == 1:
            # INSERT FOUR NEW COLUMNS THAT WILL BE POPULATED WITH EVERY ANNOTATION
            df["bbox_x1"] = ""
            df["bbox_y1"] = ""
            df["bbox_x2"] = ""
            df["bbox_y2"] = ""
            df_new = df
        else:
            is_NaN = df.isnull()
            row_has_NaN = is_NaN.any(axis=1)
            df_new = df[row_has_NaN]
        # Finally it returns the new dataframe (only rows not filled)
        return df_new
    #
    #
    #---------------------
    # (c) Display the image in the canvas from csv (in iteration)
    def display_image_4rm_csv(self, df_new):
        indexx=df_new.index
        # STORE IMAGE PATHS ONLY    
        img_paths=df_new.File_path.tolist()
        img_paths = img_paths[0]
        #
        dummy_var = img_paths.split('.')[-1]
        if dummy_var == 'jpg':
            image_org=cv2.imread(img_paths)                                     # READ THE IMAGES (CHANGE IF READING PICKEL FILE)
        else:
            image_org = pkl.load(open(img_paths, "rb"))
        #
        # Define an event for canvas with mouse click
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        # Initialize the ROI parameters
        self.rect = 0
        self.start_x = 0
        self.start_y = 0
        # Resize the selected image to default canvas size (Note: The rectangular ROI will be defined for this new size)
        # ROI parameters need to be downscaled to (224, 224) before printing to csv file.
        self.csv_image  = cv2.resize(image_org, (400, 400))                      # Resizes the image
        self.csv_image = ImageTk.PhotoImage(Image.fromarray(self.csv_image))     # Opens the image in Tkinter
        self.canvas.config(width=400, height=400)
        self.canvas.config(scrollregion=(0,0,400,400))
        self.canvas.create_image(400 / 2, 400 / 2,  image=self.csv_image)        # Displays the image in canvas
        self.ldx=indexx[0]                                                       # Actual index for the new dataframe df
    #
    #
    # (d) Display the image in the canvas from csv (with next button)
    def next_frame(self):
        self.canvas.delete("all")                       # Clear the canvas with upload button
        #
        if self.df_new is None:
            pass
        else:
            # STORE THE ANNOTATION DATA TO CSV FILE FOR EACH LOOP
            self.df.loc[self.ldx, "bbox_x1"] = self.crop_x1
            self.df.loc[self.ldx, "bbox_y1"] = self.crop_y1
            self.df.loc[self.ldx, "bbox_x2"] = self.crop_x2
            self.df.loc[self.ldx, "bbox_y2"] = self.crop_y2
            self.df.to_csv(self.filenamee, index=False)
            #
            self.dff=pd.read_csv(self.filenamee)            # Read the csv file to a dataframe df
            self.df_new = self.new_data_frame(self.dff)     # Calls subfunction (b) that creates a
            self.display_image_4rm_csv(self.df_new)         # Calls another subfunction (c) to display the
                                                            # image from csv file
            self.tag_img = '2'
        #
    #
    #
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #
    #                        START ACTIONS FOR SAVE BUTTON
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def save_action(self):
        if self.tag_img == '1':
            path = os.path.dirname(self.filename)
            #split_filename = path.split('/')
            #accs = split_filename[7]
            #mrn = split_filename[6]
            #birads = split_filename[5]
            #new_filename = path + accs + '_annotate' + '.csv'
            bname = self.filename.split('.')[0]
            new_filename=os.path.basename(bname)
            csv_rename= new_filename + '.csv'
            # np.savetxt(new_filename, np.column_stack([birads, mrn, accs, self.crop_x1, self.crop_y1, self.crop_x2, self.crop_y2]), fmt='%s', delimiter=",", header="BIRADS,MRN,Accession,x1,y1,x2,y2", comments='')
            np.savetxt(os.path.join(path, csv_rename), np.column_stack([new_filename, self.crop_x1, self.crop_y1, self.crop_x2, self.crop_y2]), fmt='%s', delimiter=",", header="ID,x1,y1,x2,y2", comments='')
            self.canvas.delete("all")
            self.canvas.create_text(195, 200, text="FILE SAVED", fill="white", font=('Helvetica 15 bold'))
        elif self.tag_img == '2':
            self.canvas.delete("all")
            self.canvas.create_text(195, 200, text="FILE SAVED", fill="white", font=('Helvetica 15 bold'))
        else:
            self.canvas.delete("all")
            self.canvas.create_text(192, 200, text="NO FILE SELECTED", fill="white", font=('Helvetica 15 bold'))
        #
    #++++++++++++++++++++++++++++++ END OF SAVE ACTION BUTTON +++++++++++++++++++++++++++++++++++++++++++++++++++
#
#
#
#
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ END OF CLASS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@