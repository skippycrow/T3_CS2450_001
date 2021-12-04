import tkinter as tk
from tkinter import messagebox as msg

class EditEmployee(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        #Create stringvars
        self.pay_method = tk.StringVar(self)
        self.pay_type = tk.StringVar(self)
        self.cur_perm = tk.StringVar(self)

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

        #Style frame
        self.title_label = tk.Label(self, text = "Edit Employee")
        self.title_label.grid(row = 1, columnspan = 6, pady = 10, sticky = tk.N)
        #Emp Id
        self.edit_emp_id_label = tk.Label(self, text = "ID:")
        self.edit_emp_id_label.grid(row = 2, column = 1, pady = 5, sticky = tk.W)
        self.edit_emp_id_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_emp_id_entry.grid(row = 2, column = 2)
        self.edit_emp_id_entry.insert(0, str(self.e_id_to_present))
        #First Name
        self.edit_first_name_label = tk.Label(self, text = "First Name:")
        self.edit_first_name_label.grid(row = 2, column = 3, pady = 5, sticky = tk.W)
        self.edit_first_name_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_first_name_entry.grid(row = 2, column = 4)
        self.edit_first_name_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "name_first")))
        #Last Name
        self.edit_last_name_label = tk.Label(self, text =" Last Name:")
        self.edit_last_name_label.grid(row = 2, column = 5, pady = 5, sticky = tk.W)
        self.edit_last_name_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_last_name_entry.grid(row = 2, column = 6)
        self.edit_last_name_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "name_last")))
        #Street
        self.edit_street_label = tk.Label(self, text = "Street:")
        self.edit_street_label.grid(row = 3, column = 1, pady = 5, sticky = tk.W)
        self.edit_street_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_street_entry.grid(row = 3, column = 2)
        self.edit_street_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "address_street")))
        #City
        self.edit_city_label = tk.Label(self, text = "City:")
        self.edit_city_label.grid(row = 3, column = 3, pady = 5, sticky = tk.W)
        self.edit_city_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_city_entry.grid(row = 3, column = 4)
        self.edit_city_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "address_city")))
        #State
        self.edit_state_label = tk.Label(self, text = "State:")
        self.edit_state_label.grid(row = 3, column = 5, pady = 5, sticky = tk.W)
        self.edit_state_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_state_entry.grid(row = 3, column = 6)
        self.edit_state_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "address_state")))
        #Zip
        self.edit_zip_label = tk.Label(self, text = "Zip:")
        self.edit_zip_label.grid(row = 4, column = 1, pady = 5, sticky = tk.W)
        self.edit_zip_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_zip_entry.grid(row = 4, column = 2)
        self.edit_zip_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "zip_code")))
        #Phone
        self.edit_phone_label = tk.Label(self, text = "Phone:")
        self.edit_phone_label.grid(row = 4, column = 3, pady = 5, sticky = tk.W)
        self.edit_phone_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_phone_entry.grid(row = 4, column = 4)
        self.edit_phone_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "contact_phone")))
        #Email
        self.edit_email_label = tk.Label(self, text = "Email:")
        self.edit_email_label.grid(row = 4, column = 5, pady = 5, sticky = tk.W)
        self.edit_email_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_email_entry.grid(row = 4, column = 6)
        self.edit_email_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "contact_email")))
        #Pay Method
        self.edit_payment_method_label = tk.Label(self, text = "Pay Method:").grid(row = 5, column = 1, pady = 5, sticky = tk.W)
        self.edit_payment_method_entry = tk.OptionMenu(self, self.pay_method, "Mail", "ACH")
        self.edit_payment_method_entry.grid(row = 5, column = 2)
        self.edit_payment_method_entry.config(width = 15)
        self.pay_method.trace("w", self.show_hide_bank)
        #Routing Number
        self.edit_routing_number_label = tk.Label(self, text = "Routing #:")
        self.edit_routing_number_label.grid(row = 5, column = 3, pady = 5, sticky = tk.W)
        self.edit_routing_number_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_routing_number_entry.grid(row = 5, column = 4)
        self.edit_routing_number_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "routing_number")))
        #Account Number
        self.edit_account_number_label = tk.Label(self, text = "Account #:")
        self.edit_account_number_label.grid(row = 5, column = 5, pady = 5, sticky = tk.W)
        self.edit_account_number_entry = tk.Entry(self, width = 15, bg = "white")
        self.edit_account_number_entry.grid(row = 5, column = 6)
        self.edit_account_number_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "account")))

        #If not admin
        if not self.controller.app_data["LoginFrame_permission"] == "Admin":
            #Style frame
            self.submit_button = tk.Button(self, text = "Submit", command = self.save_info)
            self.submit_button.grid(row = 6, column = 2, pady = 15)
            self.cancel_button = tk.Button(self, text = "Cancel", command = lambda: self.controller.present_frame("EmployeeProfile"))
            self.cancel_button.grid(row = 6, column = 1)

            #Set weight to surrounding row/col to center buttons on frame
            self.grid_rowconfigure(0, weight = 1)
            self.grid_rowconfigure(7, weight = 1)
            self.grid_columnconfigure(0, weight = 1)
            self.grid_columnconfigure(7, weight = 1)
        #User is an admin
        else:
            #Classification
            self.types = ("Salary", "Hourly", "Commission")
            self.edit_class_label = tk.Label(self, text = "Pay Type:")
            self.edit_class_label.grid(row = 6, column = 1, pady = 5, sticky = tk.W)
            self.edit_class_entry = tk.OptionMenu(self, self.pay_type, *self.types, command = self.show_hide_type)
            self.edit_class_entry.grid(row = 6, column = 2)
            self.edit_class_entry.config(width = 15)
            #Salary Amount
            self.edit_salary_label = tk.Label(self, text = "Salary Amount:")
            self.edit_salary_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.edit_salary_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_salary_entry.grid(row = 6, column = 4)
            self.edit_salary_label.grid_forget()
            self.edit_salary_entry.grid_forget()
            #Hourly rate
            self.edit_hourly_label = tk.Label(self, text = "Rate:")
            self.edit_hourly_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.edit_hourly_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_hourly_entry.grid(row = 6, column = 4)
            self.edit_hourly_entry.grid_forget()
            self.edit_hourly_label.grid_forget()
            #Commission rate
            self.edit_comm_label = tk.Label(self, text = "Rate:")
            self.edit_comm_label.grid(row = 6, column = 5, pady = 5, sticky = tk.W)
            self.edit_comm_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_comm_entry.grid(row = 6, column = 6)
            self.edit_comm_entry.grid_forget()
            self.edit_comm_label.grid_forget()
            #Social Security
            self.edit_ss_label = tk.Label(self, text = "Social Security:")
            self.edit_ss_label.grid(row = 7, column = 1, pady = 5, sticky = tk.W)
            self.edit_ss_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_ss_entry.grid(row = 7, column = 2)
            self.edit_ss_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "social_security")))
            #Birthday
            self.edit_dob_label = tk.Label(self, text = "DOB:")
            self.edit_dob_label.grid(row = 7, column = 3, pady = 5, sticky = tk.W)
            self.edit_dob_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_dob_entry.grid(row = 7, column = 4)
            self.edit_dob_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "birthday")))
            #Start Date
            self.edit_start_date_label = tk.Label(self, text = "Start Date:")
            self.edit_start_date_label.grid(row = 8, column = 1, pady = 5, sticky = tk.W)
            self.edit_start_date_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_start_date_entry.grid(row = 8, column = 2)
            self.edit_start_date_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "start_date")))
            #End Date
            self.edit_end_date_label = tk.Label(self, text = "End Date:")
            self.edit_end_date_label.grid(row = 8, column = 3, pady = 5, sticky = tk.W)
            self.edit_end_date_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_end_date_entry.grid(row = 8, column = 4)
            self.edit_end_date_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "end_date")))
            #Permission
            self.edit_permission_label = tk.Label(self, text = "Permission:")
            self.edit_permission_label.grid(row = 9, column = 1, pady = 5, sticky = tk.W)
            self.edit_permission_entry = tk.OptionMenu(self, self.cur_perm, "Admin", "Employee")
            self.edit_permission_entry.grid(row = 9, column = 2)
            self.edit_permission_entry.config(width = 15)
            #Title
            self.edit_title_label = tk.Label(self, text = "Title:")
            self.edit_title_label.grid(row = 9, column = 3, pady = 5, sticky = tk.W)
            self.edit_title_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_title_entry.grid(row = 9, column = 4)
            self.edit_title_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "title")))
            #Department
            self.edit_dept_label = tk.Label(self, text = "Dept:")
            self.edit_dept_label.grid(row = 9, column = 5, pady = 5, sticky = tk.W)
            self.edit_dept_entry = tk.Entry(self, width = 15, bg = "white")
            self.edit_dept_entry.grid(row = 9, column = 6)
            self.edit_dept_entry.insert(0, str(self.controller.database.get_employee_data(self.e_id_to_present, "dept")))
            #Buttons
            self.submit_button = tk.Button(self, text = "Submit", command = self.save_info)
            self.submit_button.grid(row = 10, column = 2, pady = 15)
            self.cancel_button = tk.Button(self, text = "Cancel", command = lambda: self.controller.present_frame("EmployeeProfile"))
            self.cancel_button.grid(row = 10, column = 1)

            #Set weight to surrounding row/col to center buttons on frame
            self.grid_rowconfigure(0, weight = 1)
            self.grid_rowconfigure(11, weight = 1)
            self.grid_columnconfigure(0, weight = 1)
            self.grid_columnconfigure(7, weight = 1)

    def show_hide_bank(self, *args):
        """Shows or hide the values for Direct Deposit based on input"""
        if self.pay_method.get() == "Mail":
            self.edit_routing_number_label.grid_forget()
            self.edit_routing_number_entry.grid_forget()
            self.edit_account_number_label.grid_forget()
            self.edit_account_number_entry.grid_forget()
        if self.pay_method.get() == "ACH":
            self.edit_routing_number_label.grid(row = 5, column = 3, pady = 5, sticky = tk.W)
            self.edit_routing_number_entry.grid(row = 5, column = 4)
            self.edit_account_number_label.grid(row = 5, column = 5, pady = 5, sticky = tk.W)
            self.edit_account_number_entry.grid(row = 5, column = 6)

    def show_hide_type(self, *args):
        """Shows or hide salary/hourly/commission based on input"""
        if self.pay_type.get() == "Salary":
            self.edit_salary_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.edit_salary_entry.grid(row = 6, column = 4)
            self.edit_hourly_entry.grid_forget()
            self.edit_hourly_label.grid_forget()
            self.edit_comm_entry.grid_forget()
            self.edit_comm_label.grid_forget()
        if self.pay_type.get() == "Hourly":
            self.edit_salary_label.grid_forget()
            self.edit_salary_entry.grid_forget()
            self.edit_hourly_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.edit_hourly_entry.grid(row = 6, column = 4)
            self.edit_comm_entry.grid_forget()
            self.edit_comm_label.grid_forget()
        if self.pay_type.get() == "Commission":
            self.edit_salary_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.edit_salary_entry.grid(row = 6, column = 4)
            self.edit_hourly_entry.grid_forget()
            self.edit_hourly_label.grid_forget()
            self.edit_comm_label.grid(row = 6, column = 5, pady = 5, sticky = tk.W)
            self.edit_comm_entry.grid(row = 6, column = 6)

    def save_info(self):
        """Save the new Employee in the database using the database functions"""
 
        #todo

        #Save data to database
        #self.controller.database.set_employee_data()
        # Do for each data field
        classification = 0
        if self.pay_type.get() == "Salary":
            classification = 1
        if self.pay_type.get() == "Hourly":
            classification = 2
        if self.pay_type.get() == "Commission":
            classification = 3

        method = 0
        if self.pay_method.get() == "ACH":
            method = 1
        if self.pay_method.get() == "Mail":
            method = 2

        #Save employee data in database
        e_id = self.edit_emp_id_entry.get()
        self.controller.database.set_employee_data(e_id, 'name_first', self.edit_first_name_entry.get())
        self.controller.database.set_employee_data(e_id, 'name_last', self.edit_last_name_entry.get())
        self.controller.database.set_employee_data(e_id, 'address_street', self.edit_street_entry.get())
        self.controller.database.set_employee_data(e_id, 'address_city', self.edit_city_entry.get())
        self.controller.database.set_employee_data(e_id, 'address_state', self.edit_state_entry.get())
        self.controller.database.set_employee_data(e_id, 'zip_code', self.edit_zip_entry.get())
        self.controller.database.set_employee_data(e_id, 'contact_phone', self.edit_phone_entry.get())
        self.controller.database.set_employee_data(e_id, 'contact_email', "email")
        self.controller.database.set_employee_data(e_id, 'email', self.edit_email_entry.get())
        self.controller.database.set_employee_data(e_id, 'pay_method', method)
        self.controller.database.set_employee_data(e_id, 'routing_number', self.edit_routing_number_entry.get())
        self.controller.database.set_employee_data(e_id, 'Account', self.edit_account_number_entry.get())

        #If user is an admin
        if self.controller.app_data["LoginFrame_permission"] == "Admin":
            #Save employee data in database
            self.controller.database.set_employee_data(e_id, 'classification', classification)
            self.controller.database.set_employee_data(e_id, 'salary', self.edit_salary_entry.get())
            self.controller.database.set_employee_data(e_id, 'hourly', self.edit_hourly_entry.get())
            self.controller.database.set_employee_data(e_id, 'commission_rate', self.edit_comm_entry.get())
            self.controller.database.set_employee_data(e_id, 'social_security', self.edit_ss_entry.get())
            self.controller.database.set_employee_data(e_id, 'birthday', self.edit_dob_entry.get())
            self.controller.database.set_employee_data(e_id, 'start_date', self.edit_start_date_entry.get())
            self.controller.database.set_employee_data(e_id, 'permission', self.cur_perm)
            self.controller.database.set_employee_data(e_id, 'title', self.edit_title_entry.get())
            self.controller.database.set_employee_data(e_id, 'dept', self.edit_dept_entry.get())
            self.controller.database.set_employee_data(e_id, 'end_date', self.edit_end_date_entry.get())

        #Show saved message
        msg.showinfo(title = "Saved", message = "Employee saved")

        #Return to employee profile
        self.controller.present_frame("EmployeeProfile")
