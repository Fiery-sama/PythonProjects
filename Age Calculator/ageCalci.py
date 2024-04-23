# importing the required modules
from tkinter import *                   # importing all widgets and methods from tkinter
from tkinter import messagebox as mb    # importing the messagebox module from tkinter
from datetime import date               # importing the date module from datetime

# --------------------- Defining Functions ---------------------
# function to set different date other than the current one
def different_date():
    # configuring the state of the entry fields to normal of the given date row
    given_year_field.config(state = "normal")
    given_month_field.config(state = "normal")
    given_day_field.config(state = "normal")
    
    # temporarily disabling the different date button
    different_date_button.config(state = "disabled")
    
    # configuring the state of the current date button to normal
    current_date_button.config(state = "normal")

# function to set the current date in the entry field
def current_date():
    # temporarily disabling the entry fields of the given date row
    given_year_field.config(state = "disabled")
    given_month_field.config(state = "disabled")
    given_day_field.config(state = "disabled")
    
    # configuring the state of the different date button to normal
    different_date_button.config(state = "normal")
    
    # temporarily disabling the current date button
    current_date_button.config(state = "disabled")

    # setting the values of the objects of the StringVar() class to current date in the given date row 
    given_year_var.set(current_year)
    given_month_var.set(current_month)
    given_day_var.set(current_day)

# function to reset all the entries
def reset_entries():
    # using the delete() method to delete the entries in the date of birth row
    birth_year_field.delete(0, END)
    birth_month_field.delete(0, END)
    birth_day_field.delete(0, END)

    # temporarily disabling the entries in the given date row
    given_year_field.config(state = "disabled")
    given_month_field.config(state = "disabled")
    given_day_field.config(state = "disabled")

    # configuring the state of the different date button to normal
    different_date_button.config(state = "normal")

    # disabling the current date button
    current_date_button.config(state = "disabled")

    # setting the values of the object of the StringVar() class to current date in the given date row
    given_year_var.set(current_year)
    given_month_var.set(current_month)
    given_day_var.set(current_day)

    # setting the value of the object of the IntVar() class to empty in result row
    age_var.set("")

    # setting the focus to the birth year field
    birth_year_field.focus_set()

# reset function
def reset():
    # calling the reset_entries() function
    reset_entries()

    # displaying a message box to display success message
    mb.showinfo("Reset Entries", "All Entries are reset successfully!")

# function to check errors in entering the data
def check_for_errors():
    # if any of the field is empty return a message box to display error
    if (birth_year_field.get() == "" or birth_month_field.get() == "" or birth_day_field.get() == "" or given_year_field.get() == "" or given_month_field.get() == "" or given_day_field.get() == ""):
        # displaying a message box to display error
        mb.showerror("Input Error", "Invalid Format! Please Try Again.")
        
        # calling the reset_entries() function
        reset_entries()
        # returning -1
        return -1

# function to calculate age
def calculate_age():
    # calling the check_for_errors() function and storing the result in a variable
    val = check_for_errors()
    
    # checking if the value of the variable is equal to -1 or not 
    if val == -1:
        # return if value is -1
        return

    else:
        # retrieving the values stored in the objects of the StringVar() class in integer data types
        birth_year = int(year_var.get())
        birth_month = int(month_var.get())
        birth_day = int(day_var.get())

        given_year = int(given_year_var.get())
        given_month = int(given_month_var.get())
        given_day = int(given_day_var.get())

        # using the try-except method
        try:
            # using the date() method to check whether the input data is actual in date format or not
            birth_date = date(birth_year, birth_month, birth_day)
            given_date = date(given_year, given_month, given_day)

            # checking if the birth date is less than or equal to given date
            if (birth_date <= given_date):
                # calculating the days by subtracting birth date from given date
                days_left = given_date - birth_date
                
                # calculate the age in years
                age = int(abs((days_left.total_seconds()) / (365.242 * 24 * 3600)))

                # setting the result as the string value in the object of the StringVar() class 
                age_var.set(str(age) + " Years Old")

            else:
                # displaying the error if the birth date exceeds given date
                mb.showerror("Input Error", "Birth Date exceeds Given Date.")
                # calling the reset_entries() function to reset the data
                reset_entries()

        # raising an exception for ValueError
        except ValueError:
            # displaying the error if the entered date is out of range
            mb.showerror("Out of Range", "Entered Date is out of range.")
            # calling the reset_entries() function to reset the data
            reset_entries()

# main function
if __name__ == "__main__":

    # creating an object of the Tk() class
    gui_root = Tk()
    # setting the title of the application
    gui_root.title("Age Calculator - JAVATPOINT")
    # setting the geometry of the application
    gui_root.geometry("600x450+650+250")
    # disabling the resizable option
    gui_root.resizable(0, 0)
    # configuring the background color of the application
    gui_root.config(bg = "#FEECCF")
    # setting the icon for the application
    gui_root.iconbitmap("calendar_img.ico")

    # creating frames to provide better structure for other widgets
    header_frame = Frame(gui_root, bg = "#FEECCF")
    entry_frame = Frame(gui_root, bg = "#FEECCF")
    result_frame = Frame(gui_root, bg = "#FEECCF")

    # using the pack() method to set the position of these frames on the window
    header_frame.pack(pady = 10)
    entry_frame.pack(pady = 10)
    result_frame.pack(pady = 10)

    # --------------------- Frame 1 ---------------------
    # creating the label to display the heading of the application
    header_label = Label(
        header_frame,
        text = "AGE CALCULATOR",
        font = ("verdana", "20", "bold"),
        bg = "#FEECCF",
        fg = "#C8871E"
        )

    # using the pack() method to set the position of the label on the window
    header_label.pack(fill = "both", pady = 10)

    # --------------------- Frame 2 ---------------------
    # creating the labels to display information like year, month, day, date of birth and given date 
    year_label = Label(
        entry_frame,
        text = "Year",
        font = ("verdana", "10"),
        bg = "#FEECCF",
        fg = "#000000"
        )

    month_label = Label(
        entry_frame,
        text = "Month",
        font = ("verdana", "10"),
        bg = "#FEECCF",
        fg = "#000000"
        )

    day_label = Label(
        entry_frame,
        text = "Day",
        font = ("verdana", "10"),
        bg = "#FEECCF",
        fg = "#000000"
        )
    
    dob_label = Label(
        entry_frame,
        text = "Date of Birth:",
        font = ("verdana", "10", "bold"),
        bg = "#FEECCF",
        fg = "#000000"
        )

    given_date_label = Label(
        entry_frame,
        text = "Given Date:",
        font = ("verdana", "10", "bold"),
        bg = "#FEECCF",
        fg = "#000000"
        )
    
    # using the grid() method to set the position of these labels in the grid format on the window
    year_label.grid(row = 0, column = 1, padx = 10, pady = 10)
    month_label.grid(row = 0, column = 2, padx = 10, pady = 10)
    day_label.grid(row = 0, column = 3, padx = 10, pady = 10)    
    
    dob_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
    given_date_label.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)

    # storing the current date details like year, month, and day
    current_year = date.today().year
    current_month = date.today().month
    current_day = date.today().day

    # creating the objects of StringVar() class
    year_var = StringVar(entry_frame)
    month_var = StringVar(entry_frame)
    day_var = StringVar(entry_frame)

    given_year_var = StringVar(entry_frame)
    given_month_var = StringVar(entry_frame)
    given_day_var = StringVar(entry_frame)

    # setting the initial values for the object
    year_var.set("")
    month_var.set("")
    day_var.set("")

    given_year_var.set(current_year)
    given_month_var.set(current_month)
    given_day_var.set(current_day)

    # creating some entry fields for the user to input data
    birth_year_field = Entry(
        entry_frame,
        width = 6,
        font = ("verdana", "10"), 
        textvariable = year_var, 
        justify = CENTER, 
        relief = GROOVE
        )

    birth_month_field = Entry(
        entry_frame, 
        width = 4, 
        font = ("verdana", "10"), 
        textvariable = month_var, 
        justify = CENTER, 
        relief = GROOVE
        )

    birth_day_field = Entry(
        entry_frame, 
        width = 4, 
        font = ("verdana", "10"), 
        textvariable = day_var, 
        justify = CENTER, 
        relief = GROOVE
        )

    given_year_field = Entry(
        entry_frame, 
        width = 6, 
        font = ("verdana", "10"), 
        textvariable = given_year_var, 
        justify = CENTER, 
        relief = GROOVE, 
        state = "disabled"
        )

    given_month_field = Entry(
        entry_frame, 
        width = 4, 
        font = ("verdana", "10"), 
        textvariable = given_month_var, 
        justify = CENTER, 
        relief = GROOVE, 
        state = "disabled"
        )

    given_day_field = Entry(
        entry_frame, 
        width = 4, 
        font = ("verdana", "10"), 
        textvariable = given_day_var, 
        justify = CENTER, 
        relief = GROOVE, 
        state = "disabled"
        )

    # using the grid() method to set the positions of these entries fields in a grid manner on the window
    birth_year_field.grid(row = 1, column = 1, padx = 10, pady = 10)
    birth_month_field.grid(row = 1, column = 2, padx = 10, pady = 10)
    birth_day_field.grid(row = 1, column = 3, padx = 10, pady = 10)

    given_year_field.grid(row = 4, column = 1, padx = 10, pady = 10)
    given_month_field.grid(row = 4, column = 2, padx = 10, pady = 10)
    given_day_field.grid(row = 4, column = 3, padx = 10, pady = 10)

    # creating the buttons to manipulate entry fields data
    different_date_button = Button(
        entry_frame, 
        text = "Different Date?", 
        width = 14, 
        font = ("verdana", "10"), 
        relief = GROOVE, 
        command = different_date, 
        bg = "#FFB84B", 
        fg = "#000000", 
        disabledforeground = "#907957"
        )
        
    current_date_button = Button(
        entry_frame, 
        text = "Current Date", 
        width = 14, 
        font = ("verdana", "10"), 
        relief = GROOVE, 
        state = "disabled", 
        command = current_date, 
        bg = "#FFB84B", 
        fg = "#000000", 
        disabledforeground = "#907957"
        )

    # using the grid() method to set the position of these buttons in the grid format on the window
    different_date_button.grid(row = 4, column = 4, padx = 10, pady = 10)
    current_date_button.grid(row = 7, column = 4, padx = 10, pady = 10)

    # --------------------- Frame 3 ---------------------
    # creating an object of the IntVar() class
    age_var = StringVar(result_frame)

    # setting an initial value of the object
    age_var.set("")

    # creating the label to display result statements
    footer_label = Label(
        result_frame, 
        text = "The Calculated Age is:", 
        font = ("verdana", "10", "bold"), 
        bg = "#FEECCF", 
        fg = "#C8871E"
        )

    age_label = Label(
        result_frame, 
        textvariable = age_var, 
        font = ("verdana", "10", "bold"), 
        bg = "#FEECCF", 
        fg = "#1FA73B"
        )

    # using the grid() method to set the position of these labels in the grid manner on the window
    footer_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
    age_label.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)

    # creating the buttons to reset the entries and yield the result
    reset_button = Button(
        result_frame, 
        text = "Reset Entries", 
        width = 12, 
        font = ("verdana", "10"), 
        relief = GROOVE, 
        command = reset, 
        bg = "#FF0000", 
        fg = "#FFFFFF"
        )

    calculate_button = Button(
        result_frame, 
        text = "Calculate Age", 
        width = 12, 
        font = ("verdana", "10"), 
        relief = GROOVE, 
        command = calculate_age, 
        bg = "#00FF00", 
        fg = "#000000"
        )

    # using the grid() method to set the position of these buttons in the grid manner on the window
    reset_button.grid(row = 1, column = 0, padx = 10, pady = 10)
    calculate_button.grid(row = 1, column = 1, padx = 10, pady = 10)

    # using the mainloop() method to run the application
    gui_root.mainloop()