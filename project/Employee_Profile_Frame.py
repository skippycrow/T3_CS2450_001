from tkinter import *
from tkinter import ttk

class Profile():
    def __init__(self):
        root = Tk()
        root.title("Employee Profile")
        frm = ttk.Frame(root, padding=15)
        frm.grid()
        ttk.Label(frm, text="[Employee Name]",justify='center').grid(column=0, row=0, columnspan=3)
        ttk.Label(frm, text="[Employee ID number]",justify='center').grid(column=0, row=1, columnspan=3)
        ttk.Label(frm, text="[position] -- [department]").grid(row=2, column=0, sticky=W)
        ttk.Label(frm, text="Office Phone: (555) 555-5555").grid(column=0, row=3, columnspan=1, sticky=W)
        ttk.Label(frm, text="Email: sample@uvu.edu").grid(row=4, column=0, columnspan=1, sticky=W)
        ttk.Label(frm, text=' ').grid(row=5,column=0)
        if self.check_permission(23): #the logged-in employee's number will be passed in
            ttk.Label(frm, text='<<Other employee info>>').grid(row=6, column=0, sticky=W)
            ttk.Button(frm, text="Edit Employee", command=self.standIn).grid(column=1, row=10)
        ttk.Button(frm, text="Back", command=root.destroy).grid(column=2, row=10)
        root.mainloop()
    
    def standIn():
        pass
    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False

Profile()