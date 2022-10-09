# Python Scripts for creating Bounding Box Windows Executable Files

This repository consist of a python scripts for creating Windows or Mac graphical user interface (GUI) executable files that can be used to create rectangular bounding box around 2D images from csv file with image paths. This GUI is particularly useful for easy annotation/bounding box creation of de-identified image data without annotators knowledge of image information. This type of annotator are regularly used for creating labels or ground truth bounding box in many object detaction algorithm in deep learning or machine learning models. The entire script can be runned using python. The needed packages for creating a custom changes in the program is detailed below.

![bounding_box_gui_app](https://user-images.githubusercontent.com/56223140/194733596-11f4e32c-aa8f-4fa6-9cf4-58921b759c5a.png)


The executable file can be created in two steps: 

I. Base Python Script/Development Step

II. Executable Deployment Step

To create executable file without any custom changes refer (II. Executable Deployment Step without changes to provided script). Our executable file can be downloaded from the link provided in folder exe_file. However, in case of introducing user based custom changes in executable files all necessary modification needed to be made in (I. Base Pyton Script prior to II. Executable Deployment Step). 

Use of source/executable files, with or without modification are permitted.

1. Further information can be obtained by writing to Arka Bhowmik (arkabhowmik@yahoo.co.uk).

**Scripts are prepared using python and tkinter libraries**

### I. BASE PYTHON SCRIPT

(a) iEdit.py   --->  This is the front end script that can be used for generating the executble GUI.

(b) backend.py --->  This is a backend script. All necessary custom changes such as file system, app buttons, and app design has to be made in backend.py


**Neccessary python libraries:**

- tkinter     : pip install tk
- Pillow      : pip install Pillow
- pandas      : pip install pandas
- csv         : pip install python-csv
- cv2         : pip install opencv-python
- pickle      : pip install pickle5
- numpy       : pip install numpy

- **Refer** input folder for csv file format in case user prefer to use our executable file in exe_file folder

### II. EXECUTABLE DEPLOYMENT

command:  pyinstaller --onefile --windowed --icon=icon.ico --add-data "D:/gui/logo.png"  iEdit.py

or

command: pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data "logo.png"  iEdit.py

- **Requirement:** 
1. Pyinstaller:  pip install -U pyinstaller
2. Pyinstaller is to create executable file for windows/mac/linux. Note, this deployment step may fail in mac due to cv2 package does not support in mac. One has to replace cv2 commands in backend.py by other alternative packages such as PIL or scipy supports in mac.
