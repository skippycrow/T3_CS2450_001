import tkinter as tk
from tkinter import messagebox as msg
import auth

#Load passwords
auth.read_auth_data('Resources/passwords.csv')

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        #Create input variables
        self.e_id = tk.StringVar()
        self.password = tk.StringVar()

        #Style frame
        tk.Label(self, text = "Employee ID", font = "none 20 bold").grid(row = 1, column = 1)
        self.e_id_input = tk.Entry(self, textvariable = self.e_id, width = 70).grid(row = 1, column = 2)
        tk.Label(self, text = "Password", font = "none 20 bold").grid(row = 2, column = 1)
        self.password_input = tk.Entry(self, textvariable = self.password, show = '*', width = 70).grid(row = 2, column = 2)
        emptyrow3 = tk.Label(self, text = "").grid(row = 3)
        self.login_button = tk.Button(self, text = "Login", width = 20, height = 1, command = self.check_login).grid(row = 3, column = 2)

        #Set weight to surrounding row/col to center buttons on frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(4, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(4, weight = 1)

    def update(self):
        pass
    
    def check_login(self):
        #Store authentication
        results = auth.verify_password(self.e_id.get(), self.password.get())
        
        #If authentication correct
        if results == auth.PASSWORD_CORRECT:
            #Set user id in app data
            self.controller.app_data["LoginFrame_userID"] = self.e_id.get()
            #Set user permission in app data
            self.controller.app_data["LoginFrame_permission"] = self.controller.database.get_employee_data(self.e_id.get(), "permission")

            #Proceed to landing frame
            self.controller.present_frame("LandingFrame")
        
        #Authentication incorrect
        else:
         self.fail_login()
        
    def fail_login(self):
         #Will call up a warning box if the credentials are invalid
         msg.showwarning(title = "Failed Login", message = "Incorrect Username or Password")
