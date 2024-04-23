# importing the required modules
from tkinter import *           # importing all the widgets and modules from Tkinter
from PIL import Image, ImageTk  # importing the Image & ImageTk modules from PIL
import os                       # importing the os module
import webbrowser               # importing the webbrowser module

# ---------------------------- defining functions ----------------------------

# function to display the information
def display_info(*args):
    
    '''
    This function checks the selected key in
    the option menu and displays the information
    about that selected option for the user.
    '''
    
    # iterating through the keys in the MENU dictionary
    for key in MENU:
        if selectedOption.get() == key:
            # displaying the information from the INFO list for the selected option
            displayedInfo.set(INFO[list(MENU.keys()).index(key)])

# function to execute the desired command
def execute_command():
    
    '''
    This function uses the os module to execute the
    system shutdown command with the appropriate argument
    for the selected option from the menu
    '''

    # iterating through the keys in the MENU dictonary
    for key in MENU:
        if selectedOption.get() == key:
            # using the system() method of the os module to execute the
            # shutdown command with the argument present as the value
            # for that selected key in the MENU dictionary
            os.system("shutdown {}".format(MENU[key]))

# function to cancel the action
def cancel():

    "This function closes the application"

    # using the destroy() method to close the application
    gui_root.destroy()

# function to access the help
def help():

    "This function opens the official website for support"

    # using the open() method of the webbrowser module to access the requested URL
    webbrowser.open("https://support.microsoft.com/en-us/windows")

# ---------------------------- main function ----------------------------

if __name__ == "__main__":
    # creating an object of the Tk() class
    gui_root = Tk()
    
    # setting the title of the application 
    gui_root.title("Shut Down Windows - JAVATPOINT")

    # setting the size and position of the window
    gui_root.geometry("600x325+650+250")

    # disabling the resizable option for better UI
    gui_root.resizable(0, 0)

    # configuring the background color of the window
    gui_root.config(bg = "#FFFAF0")

    # setting the icon of the application
    gui_root.iconbitmap("D:\Learn Coding\Python Projects\Shutdown Windows\windows.ico")

    # ---------------------------- adding widgets to the application ----------------------------

    # adding frames to the window
    heading_frame = Frame(gui_root, bg = "#FFFAF0")
    menu_frame = Frame(gui_root, bg = "#FFFAF0")
    buttons_frame = Frame(gui_root, bg = "#FFFAF0")

    # using the pack() method to set the position of the above frames
    heading_frame.pack()
    menu_frame.pack(expand = True, fill = "both")
    buttons_frame.pack(side = RIGHT)

    # importing the images from the directory for the purpose of the Tkinter application
    imageOne = ImageTk.PhotoImage(Image.open("D:\Learn Coding\Python Projects\Shutdown Windows\Windows_11.png").resize((400, 75), Image.Resampling.LANCZOS))
    imageTwo = ImageTk.PhotoImage(Image.open("D:\Learn Coding\Python Projects\Shutdown Windows\computer.png").resize((50, 50), Image.Resampling.LANCZOS))

    # ----------------------- the heading_frame frame -----------------------

    # using the Label() widget to add the label to the application
    imageLabelOne = Label(
        heading_frame,
        image = imageOne,
        bg = "#FFFAF0"
        )

    # using the pack() method to set the position of the label
    imageLabelOne.pack(pady = 15)

    # ----------------------- the menu_frame frame -----------------------

    # defining a dictionary to display options and the arguments to perform the associated function
    MENU = {
        'Sign Out' : '/l',
        'Shut down' : '/s /t 1',
        'Restart' : '/r /t 1'
        }

    # defining a list to display information
    INFO = [
        'Closes all apps and signs you out.',
        'Closes all apps and turns off the PC.',
        'Closes all apps, turns off the PC, and then turns it on again.'
        ]

    # creating an object of the list() function
    default_key = list(MENU)

    # creating the objects of the StringVar class
    selectedOption = StringVar()
    displayedInfo = StringVar()

    # using the set() method to set the values in the object of the StringVar class
    selectedOption.set(default_key[1])
    displayedInfo.set(INFO[1])

    # creating some labels using the Label() widget to display the imported image and some descriptions
    imageLabelTwo = Label(
        menu_frame,
        image = imageTwo,
        bg = "#FFFAF0"
        )
    headingLabel = Label(
        menu_frame,
        text = "What do you want the computer to do?",
        bg = "#FFFAF0",
        fg = "#000000"
        )
    infoLabel = Label(
        menu_frame,
        textvariable = displayedInfo,
        bg = "#FFFAF0",
        fg = "#000000"
        )

    # creating a dropdown menu using the OptionMenu() widget
    dropdown = OptionMenu(
        menu_frame,
        selectedOption,
        *MENU.keys(),
        command = display_info
        )

    # configuring the width, background color and anchor of the option menu
    dropdown.config(width = 45, bg = "#F8F8FF", anchor = W)

    # using the grid() method to set the position of the labels and the option menu
    imageLabelTwo.grid(row = 0, column = 0, padx = 20, pady = 10, rowspan = 2)
    headingLabel.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)
    infoLabel.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = W)
    dropdown.grid(row = 1, column = 1, padx = 10, sticky = W)

    # ----------------------- the buttons_frame frame -----------------------

    # creating some buttons using the Button() widget
    ok_button = Button(
        buttons_frame,
        text = "OK",
        width = 12,
        relief = GROOVE,
        bg = "#9BFF92",
        fg = "#000000",
        activebackground = "#C0FEBA",
        command = execute_command
        )
    cancel_button = Button(
        buttons_frame,
        text = "Cancel",
        width = 12,
        relief = GROOVE,
        bg = "#F29C9D",
        fg = "#000000",
        activebackground = "#FFD7D8",
        command = cancel
        )
    help_button = Button(
        buttons_frame,
        text = "Help",
        width = 12,
        relief = GROOVE,
        bg = "#A9EFFF",
        fg = "#000000",
        activebackground = "#D9F8FF",
        command = help
        )

    # creating an empty label using the Label() widget
    anonymousLabel = Label(
        buttons_frame,
        text = "  ",
        bg = "#FFFAF0"
        )

    # using the grid() method to set the position of the buttons and the label
    ok_button.grid(row = 0, column = 0, padx = 2, pady = 10)
    cancel_button.grid(row = 0, column = 1, padx = 2, pady = 10)
    help_button.grid(row = 0, column = 2, padx = 2, pady = 10)
    anonymousLabel.grid(row = 0, column = 3, padx = 2, pady = 10)

    # running the application using the mainloop() method
    gui_root.mainloop()