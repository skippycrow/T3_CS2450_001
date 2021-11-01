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
        id_label = tk.Label(self, text = "Employee ID").grid(row=3, column = 3)
        self.e_id = tk.StringVar()
        e_id_input = tk.Entry(self, textvariable = self.e_id).grid(row = 3, column = 4)
        self.controller.add_data("LoginFrame_id", self.e_id)
        password_label = tk.Label(self, text = "Password").grid(row = 3, column = 7)
        self.password = tk.StringVar()
        password_input = tk.Entry(self, textvariable = self.password, show = '*').grid(row = 3, column = 8)
        
        # Add login button, calls checkLogin
        login_button = tk.Button(self, text = "Login", command = self.check_login).grid(row = 8, column = 5)

    
    def check_login(self):
        self.controller.present_frame("LandingFrame")
        """
        results = auth.verify_password(self.e_id, self.password)
        if results == auth.PASSWORD_CORRECT:
            self.controller.present_frame("LandingFrame", ssef.e_id)
            loginPage.removeLogin()
        else:
         self.failLogin()
         """
        pass
        
    # Will call up a warning box if the credentials are invalid
    def fail_login(self):
         msg.showwarning(title="Failed Login", message="Incorrect Username or Password")
