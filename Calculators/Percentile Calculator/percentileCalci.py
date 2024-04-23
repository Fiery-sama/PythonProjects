# importing the required widgets and methods from the tkinter library
from tkinter import *

# function to reset all the entries
def reset():
    # using the delete() method to delete 
    # the entries in the entry fields
    total_participants_field.delete(0, END)
    rank_field.delete(0, END)
    percentile_field.delete(0, END)
    
    # setting the focus to the first entry field
    total_participants_field.focus_set()

# function to calculate the percentile
def calculate_percentile():
    # deleting the previous result
    percentile_field.delete(0, END)
    # getting the values from the entry fields
    students = int(total_participants_field.get())
    rank = int(rank_field.get())
    # calculating the percentile for the given data
    # and rounding off the result upto 3 decimals
    res = round((students - rank) / students * 100, 3)
    # printing the result in the percentile field
    percentile_field.insert(10, str(res))

# main function
if __name__ == "__main__":
    # creating an object of the Tk() class
    guiWindow = Tk()
    # setting the title to the main window
    guiWindow.title("Percentile Calculator - JAVATPOINT")
    # setting the size of the main window
    guiWindow.geometry("500x500+500+250")
    # disabling the resizable option for better GUI
    guiWindow.resizable(0, 0)
    # setting the background to #fff5ee
    guiWindow.configure(bg = "#fff5ee")

    # first frame to maintain the heading label of the application
    titleFrame = Frame(guiWindow, bg = "#fff5ee")
    # second frame to maintain the entry fields of the application
    fieldFrame = Frame(guiWindow, bg = "#fff5ee")
    # third frame to maintain the result field of the application
    resultFrame = Frame(guiWindow, bg = "#fff5ee")

    # using the pack() method to set the position
    # of the frames in the application
    titleFrame.pack(expand = True, fill = "both")
    fieldFrame.pack(expand = True, fill = "both")
    resultFrame.pack(expand = True, fill = "both")

    # defining the label that display
    # the heading in the application
    mainLabel = Label(
        titleFrame,
        text = "WELCOME TO RANK-BASED \nPERCENTILE CALCULATOR",
        font = ("cambria", 16),
        bg = "#fff5ee",
        fg = "#000000"
    )
    # using the pack() method to set the position
    # of the lable in the application
    mainLabel.pack(expand = True, fill = "both")

    # creating the "Total Participants" label
    total_participants_label = Label(
        fieldFrame,
        text = "Total No. of Participants:",
        bg = "#fff5ee",
        fg = "#a0522d"
    )
    # creating the "Rank" label
    rank_label = Label(
        fieldFrame,
        text = "Rank:",
        bg = "#fff5ee",
        fg = "#a0522d"
    )
    # creating the "Percentile" label
    percentile_label = Label(
        resultFrame,
        text = "Percentile:",
        bg = "#fff5ee",
        fg = "#a0522d"
    )

    # using the grid() method to set the position
    # of the labels in a grid manner
    total_participants_label.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = W)
    rank_label.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = W)
    percentile_label.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = W)

    # creating the entry field for total participants
    total_participants_field = Entry(
        fieldFrame,
        bg = "#fffafa"
    )
    # creating the entry field for rank
    rank_field = Entry(
        fieldFrame,
        bg = "#fffafa"
    )
    # creating the entry field for percentile
    percentile_field = Entry(
        resultFrame,
        bg = "#fffafa"
    )

    # using the grid() method to set the position
    # of the entry fields in a grid manner
    total_participants_field.grid(row = 1, column = 2, padx = 20, pady = 20, sticky = W)
    rank_field.grid(row = 2, column = 2, padx = 20, pady = 20, sticky = W)
    percentile_field.grid(row = 1, column = 2, padx = 20, pady = 20, sticky = W)

    # creating the "CALCULATE" button
    calculate_button = Button(
        fieldFrame,
        text = "CALCULATE",
        bg = "#008000",
        fg = "#ffffff",
        command = calculate_percentile
    )

    # creating the "RESET" button
    reset_button = Button(
        resultFrame,
        text = "RESET",
        bg = "#ff0000",
        fg = "#ffffff",
        command = reset
    )

    # using the grid() method to set the position
    # of the buttons in a grid manner
    calculate_button.grid(row = 3, column = 2, padx = 50, pady = 20, sticky = W)
    reset_button.grid(row = 1, column = 3, padx = 20, pady = 20, sticky = W)

    # running the main window
    guiWindow.mainloop()