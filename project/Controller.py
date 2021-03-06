import tkinter as tk
import os
import os.path
from Login_Frame import LoginFrame
from Landing_Frame import LandingFrame
from Employee_List_Frame import EmployeeList
from Add_Employee_Frame import AddEmployee
from Edit_Employee_Frame import EditEmployee
from Employee_Profile_Frame import EmployeeProfile
from database import EmployeeDatabase

class EmployeeApp(tk.Tk):
    def __init__(self):
        #Initialize tk
        tk.Tk.__init__(self)
        
        #Initialize database
        self.database = EmployeeDatabase()

        #Load employees
        if os.path.exists(os.getcwd() + "/Resources/employees.csv"):
            self.database.load_from_file(os.getcwd() + "/Resources/employees.csv")
        if os.path.exists(os.getcwd() + "/project/Resources/employees.csv"):
            self.database.load_from_file(os.getcwd() + "/project/Resources/employees.csv")

        #Read reciept
        if os.path.exists(os.getcwd() + "/Resources/receipts.csv"):
            self.database.read_receipt_data(os.getcwd() + "/Resources/receipts.csv")
        if os.path.exists(os.getcwd() + "/project/Resources/receipts.csv"):
            self.database.read_receipt_data(os.getcwd() + "/project/Resources/receipts.csv")
        #Read timecard
        if os.path.exists(os.getcwd() + "/Resources/timecards.csv"):
            self.database.read_timecard_data(os.getcwd() + "/Resources/timecards.csv")
        if os.path.exists(os.getcwd() + "/project/Resources/timecards.csv"):
            self.database.read_timecard_data(os.getcwd() + "/project/Resources/timecards.csv")

        #Initialize container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Initialize dict to hold frames
        self.frames = {}

        #Initialize dict to store data - Store user, permission, current employee etc. here where it can be accessed by other frames if it needs to
        #Example: add_data("LandingPage_Permission", "Admin")
        self.app_data = {"LoginFrame_userID" : "0", "LoginFrame_permission" : "Employee", "EmployeeListFrame_selectedEmployeeID" : "0", "EmployeeListFrame_showSelectedEmployee" : False}

        #For each page
        for page in (LoginFrame, LandingFrame, EmployeeList, AddEmployee, EditEmployee, EmployeeProfile):
            #Set page name to name of its class
            page_name = page.__name__

            #Create frame
            frame = page(parent = container, controller = self)

            #Store frame in frames dict
            self.frames[page_name] = frame

            #Stack each frame on top of each other
            frame.grid(row = 0, column = 0, sticky = "nesw")

        #Show the login page
        self.present_frame("LoginFrame")

    def present_frame(self, page_name, window_title_override=''):
        #Update the frame if it needs to be ; mainly for updating employee profile
        self.frames[page_name].update()

        #Set the frame
        frame = self.frames[page_name]

        #Raise the frame on top of the others
        frame.tkraise()

        #Set frame title
        self.title(page_name if (window_title_override == '') else window_title_override)

def main():
    app = EmployeeApp()
    app.mainloop()

if __name__ == "__main__":
    main()
