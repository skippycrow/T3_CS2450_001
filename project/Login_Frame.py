import tkinter as tk
from tkinter import messagebox as msg

import auth

#auth.read_auth_data(path)


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        # ID and password text boxes plus labels, save inputs to variables for future use
        # Set up the frame and create all buttons

        # Initialize tk
        tk.Frame.__init__(self, parent)

        # Initialize controller
        self.controller = controller
        

        # Style frame
        emptyrow0 = tk.Label(self, text = "").grid(row=0)
        emptyrow1 = tk.Label(self, text = "").grid(row=1)
        emptyrow2 = tk.Label(self, text = "").grid(row=2)
        emptyrow3 = tk.Label(self, text = "").grid(row=3)
        emptyrow4 = tk.Label(self, text = "").grid(row=4)
        id_label = tk.Label(self, text = "Employee ID", font = "none 20 bold").grid(row=5, column = 3)
        self.e_id = tk.StringVar()
        e_id_input = tk.Entry(self, textvariable = self.e_id, width = 70).grid(row = 5, column = 4, pady = 10)
        self.controller.add_data("user_id", self.e_id)
        password_label = tk.Label(self, text = "Password", font = "none 20 bold").grid(row = 6, column = 3)
        self.password = tk.StringVar()
        password_input = tk.Entry(self, textvariable = self.password, show = '*', width = 70).grid(row = 6, column = 4, pady = 10)
        
        # Add login button, calls checkLogin
        emptyrow3 = tk.Label(self, text = "").grid(row=3)
        login_button = tk.Button(self, text = "Login", width = 20, height = 1, command = self.check_login).grid(row = 9, column = 4, pady = 10)

    
    def check_login(self):
        self.controller.app_data["user_id"] = self.e_id;
        self.controller.present_frame("LandingFrame")

        results = auth.verify_password(self.e_id.get(), self.password.get())
        
        if results == auth.PASSWORD_CORRECT:
            self.controller.app_data["user_id"] = self.e_id;
            self.controller.present_frame("LandingFrame")

        else:
         self.fail_login()

        pass
        
    # Will call up a warning box if the credentials are invalid
    def fail_login(self):
         msg.showwarning(title="Failed Login", message="Incorrect Username or Password")
