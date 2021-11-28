import tkinter as tk
from tkinter import messagebox as msg

#Need to import Employee Profile Frame
#through controller add the id to the data and have it populate the profile page.

class LandingFrame(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        self.login_command = None
        self.user_id = self.controller.app_data["user_id"]
        
        #Style frame
        logout_button = tk.Button(self, text = "Logout", font = "none 18 bold", command = lambda: self.controller.present_frame("LoginFrame"), width = 10, height = 5)
        logout_button.grid(row = 1, column = 2)
        profile_button = tk.Button(self, text = "Go to Profile", font = "none 18 bold", command = self.profile_click, width = 10, height = 5)
        profile_button.grid(row = 1, column = 1)
        employee_button = tk.Button(self, text ="Go to \nEmployee \nPage", font = "none 18 bold", command = lambda: self.controller.present_frame("EmployeeList"), width = 10, height = 5)
        employee_button.grid(row = 1, column = 3)

        #Set weight to surrounding row/col to center content on frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(4, weight = 1)

    def update(self):
        pass

    def set_user_id(self, id):
        self.user_id = id

    def profile_click(self):
        self.controller.app_data["selected_Employee"] = self.controller.app_data["user_id"]

        #Proceed to employee profile
        self.controller.present_frame("EmployeeProfile")

    #This command will take a user with higher permission to a list of Employees page
    def on_employee_clicked(self):
        #Permission needs to be fully implemented for this to check admin level.
        #if employee.get_employee_data(self.id, permission) == true:

        #Proceed to employee list
        self.controller.present_frame("EmployeeList")
        
        #else:
            #msg.showwarning(title="Insufficient Permission", message="Incorrect Permission Level")
