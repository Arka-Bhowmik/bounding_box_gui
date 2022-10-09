#-------------------------------------------------------------------------
# THIS IS A FRONTEND PROGRAM WHICH CALLS THE BACKEND PROGRAM
# NOTE: ALL DEVELOPMENT RELATED CHANGES NEED TO BE PERFORMED IN BACKEND.PY
#
# DETAILS: This is a simple program to create GUI using python
# Here, we created a GUI which allow us to create rectangular bounding box
# around 2D image. The backend program is set up in a way which accepts a
# csv/excel file and read de-identified images saved in .pickel
# User can make neccessary changes in backend file requirement
#---------------------------------------------------------------------------------
# CREATED BY: Arka Bhowmik , Memorial Sloan Kettering Cancer Center, NY (2021)
# For further information: Contact Arka Bhowmik at (arkabhowmik@yahoo.co.uk)
#
# IMPORT ESSENTIAL LIBRARIES
from tkinter import *
import os
# IMPORT BACKEND CLASS
from backend import BackEnd
#
#-------------------------------------------------------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#
#----------------------------------------------------------------------------
# OPENS A MAIN WINDOW
mainWindow = Tk()
# CHANGE MAIN WINDOW TITLE 
mainWindow.title("MSKCCImEdit: A Tiny Image Editor")
mainWindow.iconbitmap(resource_path("icon.ico"))
# CHANGE BACKGROUND COLOR OF MAIN WINDOW
mainWindow.configure(background='#0968c3')
# CHANGE MAIN WINDOW SIZE
mainWindow.geometry('540x600')
#
# CALLS THE BACKEND PROGRAM
BackEnd(mainWindow, resource_path)
#
# ENDS THE MAIN WINDOW
mainWindow.mainloop()