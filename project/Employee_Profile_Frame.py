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

        #If accessed employee profile from EmployeeList frame with another employee selected
        if self.controller.app_data["EmployeeListFrame_showSelectedEmployee"]:
            #Set employee to present as the selected employee from the EmployeeList frame
            self.e_id_to_present = self.controller.app_data["EmployeeListFrame_selectedEmployeeID"]
        #Employee profile accessed regularly through the landing page
        else:
            #Set employee to present as the currently logged in user
            self.e_id_to_present = self.controller.app_data["LoginFrame_userID"]

        #Get employee to present data
        self.name = self.controller.database.get_employee_data(self.e_id_to_present, "name_first") + " " + self.controller.database.get_employee_data(self.e_id_to_present, "name_last")
        self.title = self.controller.database.get_employee_data(self.e_id_to_present, "title")
        self.dept = self.controller.database.get_employee_data(self.e_id_to_present, "dept")
        self.phone = self.controller.database.get_employee_data(self.e_id_to_present, "contact_phone")
        self.email = self.controller.database.get_employee_data(self.e_id_to_present, "contact_email")
        self.address = self.controller.database.get_employee_data(self.e_id_to_present, "address_street") + " " + self.controller.database.get_employee_data(self.e_id_to_present, "address_city") + ", " + self.controller.database.get_employee_data(self.e_id_to_present, "address_state") + " " + self.controller.database.get_employee_data(self.e_id_to_present, "zip_code")
        self.classification = self.controller.database.get_employee_data(self.e_id_to_present, "classification")
        self.pay_method = self.controller.database.get_employee_data(self.e_id_to_present, "pay_method")
        self.salary = self.controller.database.get_employee_data(self.e_id_to_present, "salary")
        self.hourly = self.controller.database.get_employee_data(self.e_id_to_present, "hourly")
        self.commission = self.controller.database.get_employee_data(self.e_id_to_present, "commission_rate")
        self.routing = self.controller.database.get_employee_data(self.e_id_to_present, "routing_number")
        self.account = self.controller.database.get_employee_data(self.e_id_to_present, "account")
        self.ssn = self.controller.database.get_employee_data(self.e_id_to_present, "social_security")
        self.birthday = self.controller.database.get_employee_data(self.e_id_to_present, "birthday")
        self.start_date = self.controller.database.get_employee_data(self.e_id_to_present, "start_date")
        self.permission = self.controller.database.get_employee_data(self.e_id_to_present, "permission")
        self.end_date = self.controller.database.get_employee_data(self.e_id_to_present, "end_date")
       
        #Style frame
        tk.Label(self, text = self.name, font = "none 18 bold").grid(row = 1, column = 1, sticky = tk.W)
        tk.Label(self, text = self.e_id_to_present, font = "none 12 bold").grid(row = 2, column = 1, sticky = tk.W)
        tk.Label(self, text = "Position: " + self.title, font = "none 12 bold").grid(row = 3, column = 1, sticky = tk.W)
        tk.Label(self, text = "Department: " + self.dept, font = "none 12 bold").grid(row = 3, column = 3, sticky = tk.W)
        tk.Label(self, text = "Office Phone: " + self.phone).grid(row = 4, column = 1, columnspan = 1, sticky = tk.W)
        tk.Label(self, text = "Email: " + self.email).grid(row = 4, column = 3, columnspan = 1, sticky = tk.W)
        tk.Label(self, text = ' ').grid(row = 6, column = 1)
        tk.Button(self, text = "Back", command = self.clicked_back).grid(row = 21, column = 3)

        #If full view not shown
        if not self.show_permission_view():
            #Set weight to surrounding row/col to center content on frame
            self.grid_rowconfigure(0, weight = 1)
            self.grid_rowconfigure(22, weight = 1)
            self.grid_columnconfigure(0, weight = 1)
            self.grid_columnconfigure(4, weight = 1)

        #If permission level met
        if self.show_permission_view():
            #Style frame with permission widgets
            tk.Label(self, text = ' ').grid(row = 7, column = 1, sticky = tk.W)
            tk.Label(self, text = "Address: " + self.address).grid(row = 8, column = 1, sticky = tk.W)
            tk.Label(self, text = "Employee Classification: " + self.classification).grid(row = 9, column = 1, sticky = tk.W)
            tk.Label(self, text = "Pay Method: " + self.pay_method).grid(row = 10, column = 1, sticky = tk.W)
            tk.Label(self, text = "Salary: " + self.salary).grid(row = 10, column = 2, sticky = tk.W)
            tk.Label(self, text = "Hourly: " + self.hourly).grid(row = 10, column = 3, sticky = tk.W)
            tk.Label(self, text = "Commission: " + self.commission).grid(row = 10, column = 4, sticky = tk.W)
            tk.Label(self, text = "Routing#: " + self.routing + " " + "Account#: " + self.account).grid(row = 11, column = 1, sticky = tk.W)
            tk.Button(self, text = "Edit Employee", command = lambda: self.controller.present_frame("EditEmployee")).grid(row = 21, column = 2)

            #Set weight to surrounding row/col to center content on frame
            self.grid_rowconfigure(0, weight = 1)
            self.grid_rowconfigure(22, weight = 1)
            self.grid_columnconfigure(0, weight = 1)
            self.grid_columnconfigure(5, weight = 1)

    def show_permission_view(self):
        #If employee is viewing themselves
        if self.controller.app_data["EmployeeListFrame_showSelectedEmployee"] is False:
            return True
        #If employee is an admin viewing another employees info
        elif self.controller.app_data["LoginFrame_permission"] == "Admin":
            return True
        #Employee is viewing another employee without admin permission
        else:
            return False

    def clicked_back(self):
        #Reset show selected employee flag
        self.controller.app_data["EmployeeListFrame_showSelectedEmployee"] = False

        #Proceed to landing frame
        self.controller.present_frame("LandingFrame")
