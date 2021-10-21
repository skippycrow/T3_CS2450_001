import tkinter as tk
from tkinter import messagebox as msg

class LandingFrame(tk.Frame):
    #Constructor class
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        self.user_id = None
        self.login_command = None
        
        #Set the format of the buttons and all of their locations
        logout_button = tk.Button(self, text = "Logout", command = lambda: controller.present_frame("LoginFrame"))
        logout_button.grid(row = 5, column = 3)
        profile_button = tk.Button(self, text = "Go to Profile", command = lambda: controller.present_frame("EmployeeProfile"))
        profile_button.grid(row = 2, column = 0)
        employee_button = tk.Button(self, text ="Go to Employee Page", command = lambda: controller.present_frame("EmployeeList"))
        employee_button.grid(row = 2, column = 5)

    def set_user_id(self, id):
        self.user_id = id

    def set_login_command(self, command):
        self.login_command = command
    
    #Once implemented this command will take the user to his personal profile
    #Currently unavailable
    def on_profile_clicked(self):
        return
    
    #Once implemented this command will take a user with higher permission to a list of Employees page
    #Currently unavailable
    def on_employee_clicked(self):
        return
    
    #This command will return the user to the login page and remove the current frame
    def on_logout_clicked(self):
        self.login_command()