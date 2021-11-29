import tkinter as tk
from tkinter import messagebox as msg

class LandingFrame(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller
        
        #Style frame
        logout_button = tk.Button(self, text = "Logout", font = "none 18 bold", command = lambda: self.controller.present_frame("LoginFrame"), width = 10, height = 5)
        logout_button.grid(row = 1, column = 2)
        profile_button = tk.Button(self, text = "Go to Profile", font = "none 18 bold", command = lambda: self.controller.present_frame("EmployeeProfile"), width = 10, height = 5)
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
