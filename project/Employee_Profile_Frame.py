import tkinter as tk
from tkinter import messagebox as msg

class EmployeeProfile(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller
       
        tk.Label(self, text="[Employee Name]",justify='center').grid(column=0, row=0, columnspan=3)
        tk.Label(self, text="[Employee ID number]",justify='center').grid(column=0, row=1, columnspan=3)
        tk.Label(self, text="[position] -- [department]").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self, text="Office Phone: (555) 555-5555").grid(column=0, row=3, columnspan=1, sticky=tk.W)
        tk.Label(self, text="Email: sample@uvu.edu").grid(row=4, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self, text=' ').grid(row=5,column=0)

        if self.check_permission(23): #the logged-in employee's number will be passed in
            tk.Label(self, text='<<Other employee info>>').grid(row=6, column=0, sticky=tk.W)
            tk.Button(self, text="Edit Employee", command=self.stand_in).grid(column=1, row=10)

        tk.Button(self, text="Back", command = lambda: controller.present_frame("LandingFrame")).grid(column=2, row=10)
    
    def stand_in():
        pass

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False
