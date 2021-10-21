import tkinter as tk
from tkinter import messagebox as msg

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        #username and password text boxes plus labels, save inputs to variables for future use
        #Set up the frame and create all buttons

        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        username_label = tk.Label(self, text = "User Name").grid(row=3, column = 3)
        self.username = tk.StringVar()
        username_input = tk.Entry(self, textvariable = self.username).grid(row = 3, column = 4)
        password_label = tk.Label(self, text = "Password").grid(row = 3, column = 7)
        self.password = tk.StringVar()
        password_input = tk.Entry(self, textvariable = self.password, show = '*').grid(row = 3, column = 8)
        
        #Add login button, calls checkLogin
        login_button = tk.Button(self, text = "Login", command = self.check_login).grid(row = 8, column = 5)

    #Inputs will be passed in here to verify validity
    #Will finish implementation when username and password csv are completed
    def check_login(self):
        #placeholder for veryifying the user and password
        #results = checkCredential(self.username, self.password)
        #if results is true:
        self.controller.present_frame("LandingFrame")
        #loginPage.removeLogin()
        #else:
         
        #self.failLogin()
        return
        
    #Will call up a warning box if the credentials are invalid
    def fail_login(self):
         msg.showwarning(title="Failed Login", message="Incorrect Username or Password")
