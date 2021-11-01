import tkinter as tk
from tkinter import messagebox as msg

#Need to import Employee Profile Frame
#through controller add the id to the data and have it populate the profile page.

class LandingFrame(tk.Frame):
    #Constructor class
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller
        self.login_command = None
        self.user_id = self.controller.app_data["user_id"]
        
        #Set the format of the buttons and all of their locations
        logout_button = tk.Button(self, text = "Logout", command = lambda: controller.present_frame("LoginFrame"))
        logout_button.grid(row = 5, column = 3)
        profile_button = tk.Button(self, text = "Go to Profile", command = self.profile_click)
        profile_button.grid(row = 2, column = 0)
        employee_button = tk.Button(self, text ="Go to Employee Page", command = lambda: controller.present_frame("EmployeeList"))
        employee_button.grid(row = 2, column = 5)

    def profile_click(self):
        self.controller.app_data["selected_Employee"] = self.controller.app_data["user_id"]
        self.controller.present_frame("EmployeeProfile")

    def set_user_id(self, id):
        self.user_id = id

    def set_login_command(self, command):
        self.login_command = command
    
    #Once implemented this command will take the user to his personal profile
    def on_profile_clicked(self):
        #
        if EmployeeProfile.check_permission(id) == true:
            self.controller.present_frame("EmployeeProfile")

    #This command will take a user with higher permission to a list of Employees page
    def on_employee_clicked(self):
        #Permission needs to be fully implemented for this to check admin level.
        #if employee.get_employee_data(self.id, permission) == true:
        self.controller.present_frame("EmployeeList")
        
        #else:
        #    msg.showwarning(title="Insufficient Permission", message="Incorrect Permission Level")
    
    #This command will return the user to the login page and remove the current frame
    def on_logout_clicked(self):
        self.login_command()
        #close LandingPage
