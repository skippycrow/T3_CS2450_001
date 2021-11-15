import tkinter as tk
from tkinter import messagebox as msg

class EmployeeProfile(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        self.my_id = self.controller.app_data["user_id"]    #When a user logs in their id# is assigned to app_data {user_id:****}
        self.e_id = self.controller.app_data["selected_employee"]
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
        tk.Label(self, text=self.name, font = "none 18 bold").grid(column=0, row=0, sticky = tk.W)
        tk.Label(self, text=self.e_id, font = "none 12 bold").grid(column=0, row=1, sticky = tk.W)
        tk.Label(self, text="Position: " + self.title, font = "none 12 bold").grid(column=0, row=2, sticky = tk.W)
        tk.Label(self, text="Department: " + self.dept, font = "none 12 bold").grid(row=2, column=2, sticky=tk.W)
        tk.Label(self, text="Office Phone: " + self.phone).grid(column=0, row=3, columnspan=1, sticky=tk.W)
        tk.Label(self, text="Email: " + self.email).grid(row=3, column=2, columnspan=1, sticky=tk.W)
        tk.Label(self, text=' ').grid(row=5,column=0)

        if self.check_permission(23): #the logged-in employee's number will be passed in
            tk.Label(self, text='<<Other employee info will display here>>').grid(row=6, column=0, sticky=tk.W)
            tk.Label(self, text="Address: ").grid(row=7, column=0, sticky=tk.W)    #FIX address line then add in variable
            tk.Label(self, text="Employee Classification: " + self.classification).grid(row=8, column=0, sticky=tk.W)
            tk.Label(self, text="Pay Method: " + self.pay_method).grid(row=9, column=0, sticky=tk.W)
            tk.Label(self, text="Salary: " + self.salary).grid(row=9, column=1, sticky=tk.W)
            tk.Label(self, text="Hourly: " + self.hourly).grid(row=9, column=2, sticky=tk.W)
            tk.Label(self, text="Commission: " + self.commission).grid(row=9, column=3, sticky=tk.W)
            tk.Label(self, text="Routing Number: " + self.routing).grid(row=10, column=0, sticky=tk.W)
            tk.Label(self, text="Account Number: " + self.account).grid(row=10, column=1, sticky=tk.W)
            tk.Label(self, text="Social Security Number: ***-**-" + self.ssn[-4:-1]).grid(row=10, column=1, sticky=tk.W)
            tk.Label(self, text="Birthday: " + self.birthday[0:1] + "/" + self.birthday[2:3] + "/" + self.birthday[4:]).grid(row=11, column=0, sticky=tk.W)
            tk.Label(self, text="Start Date: " + self.start_date).grid(row=11, column=1, sticky=tk.W)

            tk.Button(self, text="Edit Employee", command=lambda: controller.present_frame("EditEmployee")).grid(column=1, row=20)

        tk.Button(self, text="Back", command = lambda: controller.present_frame("LandingFrame")).grid(column=2, row=20)

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        if self.my_id == self.e_id:
            return True
        elif self.permission == "admin":
            return True
        else:
            return False