import tkinter as tk
from tkinter import messagebox as msg

class EmployeeProfile(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

    def update(self):
        #For each widget in frame
        for widget in self.winfo_children():
            #Destroy the widget
            widget.destroy()

        #Get data
        self.e_id = self.controller.app_data["LoginFrame_userID"]    #Will need to get id# from login or employee list
        self.name = self.controller.database.get_employee_data(self.e_id, "name_first") + " " + self.controller.database.get_employee_data(self.e_id, "name_last")
        self.title = "Employee"     #self.controller.database.get_employee_data(self.e_id, "title")
        self.dept = "Faculty"       #self.controller.database.get_employee_data(self.e_id, "dept")
        self.phone = self.controller.database.get_employee_data(self.e_id, "contact_phone")
        self.email = self.controller.database.get_employee_data(self.e_id, "contact_email")
        #Syntax Error:
        #self.address = self.controller.database.get_employee_data(self.e_id, "address_street") + " " self.controller.database.get_employee_data(self.e_id, "address_city") + ", " + self.controller.database.get_employee_data(self.e_id, "address_state") + " " + self.controller.database.get_employee_data(self.e_id, "zip_code")
        self.classification = self.controller.database.get_employee_data(self.e_id, "classification")
        self.pay_method = self.controller.database.get_employee_data(self.e_id, "pay_method")
        self.salary = self.controller.database.get_employee_data(self.e_id, "salary")
        self.hourly = self.controller.database.get_employee_data(self.e_id, "hourly")
        self.commission = self.controller.database.get_employee_data(self.e_id, "commission_rate")
        self.routing = self.controller.database.get_employee_data(self.e_id, "routing_number")
        self.account = self.controller.database.get_employee_data(self.e_id, "Account") #database.py has this as the only capitalized field
        self.ssn = self.controller.database.get_employee_data(self.e_id, "social_security")
        self.birthday = self.controller.database.get_employee_data(self.e_id, "birthday")
        self.start_date = self.controller.database.get_employee_data(self.e_id, "start_date")
        self.permission = self.controller.database.get_employee_data(self.e_id, "permission")
        self.end_date = self.controller.database.get_employee_data(self.e_id, "end_date")
       
        #Style page
        tk.Label(self, text = self.name, font = "none 18 bold").grid(column = 0, row = 0, sticky = tk.W)
        tk.Label(self, text = self.e_id, font = "none 12 bold").grid(column = 0, row = 1, sticky = tk.W)
        tk.Label(self, text = "Position: " + self.title, font = "none 12 bold").grid(column = 0, row = 2, sticky = tk.W)
        tk.Label(self, text = "Department: " + self.dept, font = "none 12 bold").grid(row = 2, column = 2, sticky = tk.W)
        tk.Label(self, text = "Office Phone: " + self.phone).grid(column = 0, row = 3, columnspan = 1, sticky = tk.W)
        tk.Label(self, text = "Email: " + self.email).grid(row = 3, column = 2, columnspan = 1, sticky = tk.W)
        tk.Label(self, text = ' ').grid(row = 5,column = 0)
        tk.Button(self, text = "Back", command = lambda: self.controller.present_frame("LandingFrame")).grid(column = 2, row = 20)

        if self.check_permission(23): #the logged-in employee's number will be passed in
            tk.Label(self, text = '<<Other employee info will display here>>').grid(row = 6, column = 0, sticky = tk.W)
            tk.Label(self, text = "Address: ").grid(row = 7, column = 0, sticky = tk.W)    #FIX address line then add in variable
            tk.Label(self, text = "Employee Classification: " + self.classification).grid(row = 8, column = 0, sticky = tk.W)
            tk.Label(self, text = "Pay Method: " + self.pay_method).grid(row = 9, column = 0, sticky = tk.W)
            tk.Label(self, text = "Salary: " + self.salary).grid(row = 9, column = 1, sticky = tk.W)
            tk.Label(self, text = "Hourly: " + self.hourly).grid(row = 9, column = 2, sticky = tk.W)
            tk.Label(self, text = "Commission: " + self.commission).grid(row = 9, column = 3, sticky = tk.W)
            tk.Label(self, text = "<<routing #, account #, and other data fields to be implemented").grid(row = 10, column = 0, sticky = tk.W)
            tk.Button(self, text = "Edit Employee", command=lambda: self.controller.present_frame("EditEmployee")).grid(column = 1, row = 20)

    def stand_in(self):
        pass

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return True
