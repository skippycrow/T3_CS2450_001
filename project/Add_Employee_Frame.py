import tkinter as tk
from tkinter import messagebox as msg
import os
import os.path
import auth

class AddEmployee(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        #Create stringvars
        self.pay_method = tk.StringVar(self)
        self.pay_type = tk.StringVar(self)
        self.cur_perm = tk.StringVar(self)

        #Style frame
        self.title_label = tk.Label(self, text = "Add Employee")
        self.title_label.grid(row = 1, columnspan = 6, pady = 10, sticky = tk.N)
        #Emp Id
        self.add_emp_id_label = tk.Label(self, text = "ID:")
        self.add_emp_id_label.grid(row = 2, column = 1, pady = 5, sticky = tk.W)
        self.add_emp_id_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_emp_id_entry.grid(row = 2, column = 2)
        #First Name
        self.add_first_name_label = tk.Label(self, text = "First Name:")
        self.add_first_name_label.grid(row = 2, column = 3, pady = 5, sticky = tk.W)
        self.add_first_name_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_first_name_entry.grid(row = 2, column = 4)
        #Last Name
        self.add_last_name_label = tk.Label(self, text = "Last Name:")
        self.add_last_name_label.grid(row = 2, column = 5, pady = 5, sticky = tk.W)
        self.add_last_name_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_last_name_entry.grid(row = 2, column = 6)
        #Street
        self.add_street_label = tk.Label(self, text = "Street:")
        self.add_street_label.grid(row = 3, column = 1, pady = 5, sticky = tk.W)
        self.add_street_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_street_entry.grid(row = 3, column = 2)
        #City
        self.add_city_label = tk.Label(self, text = "City:")
        self.add_city_label.grid(row = 3, column = 3, pady = 5, sticky = tk.W)
        self.add_city_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_city_entry.grid(row = 3, column = 4)
        #State
        self.add_state_label = tk.Label(self, text = "State:")
        self.add_state_label.grid(row = 3, column = 5, pady = 5, sticky = tk.W)
        self.add_state_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_state_entry.grid(row = 3, column = 6)
        #Zip
        self.add_zip_label = tk.Label(self, text = "Zip:")
        self.add_zip_label.grid(row = 4, column = 1, pady = 5, sticky = tk.W)
        self.add_zip_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_zip_entry.grid(row = 4, column = 2)
        #Phone
        self.add_phone_label = tk.Label(self, text = "Phone:")
        self.add_phone_label.grid(row = 4, column = 3, pady = 5, sticky = tk.W)
        self.add_phone_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_phone_entry.grid(row = 4, column = 4)
        #Email
        self.add_email_label = tk.Label(self, text = "Email:")
        self.add_email_label.grid(row = 4, column = 5, pady = 5, sticky = tk.W)
        self.add_email_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_email_entry.grid(row = 4, column = 6)
        #Pay Method
        self.add_payment_method_label = tk.Label(self, text = "Pay Method:")
        self.add_payment_method_label.grid(row = 5, column = 1, pady = 5, sticky = tk.W)
        self.add_payment_method_entry = tk.OptionMenu(self, self.pay_method, "Mail", "ACH")
        self.add_payment_method_entry.grid(row = 5, column = 2)
        self.add_payment_method_entry.config(width = 15)
        self.pay_method.trace("w", self.show_hide_bank)
        #Routing Number
        self.add_routing_number_label = tk.Label(self, text = "Routing #:")
        self.add_routing_number_label.grid(row = 5, column = 3, pady = 5, sticky = tk.W)
        self.add_routing_number_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_routing_number_entry.grid(row = 5, column = 4)
        #Account Number
        self.add_account_number_label = tk.Label(self, text = "Account #:")
        self.add_account_number_label.grid(row = 5, column = 5, pady = 5, sticky = tk.W)
        self.add_account_number_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_account_number_entry.grid(row = 5, column = 6)
        self.types = ("Salary", "Hourly", "Commission")
        #Classification
        self.add_class_label = tk.Label(self, text = "Pay Type:")
        self.add_class_label.grid(row = 6, column = 1, pady = 5, sticky = tk.W)
        self.add_class_entry = tk.OptionMenu(self, self.pay_type, *self.types, command = self.show_hide_type)
        self.add_class_entry.grid(row = 6, column = 2)
        self.add_class_entry.config(width = 15)
        #Salary Amount
        self.add_salary_label = tk.Label(self, text = "Salary Amount:")
        self.add_salary_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
        self.add_salary_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_salary_entry.grid(row = 6, column = 4)
        self.add_salary_label.grid_forget()
        self.add_salary_entry.grid_forget()
        #Hourly rate
        self.add_hourly_label = tk.Label(self, text = "Rate:")
        self.add_hourly_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
        self.add_hourly_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_hourly_entry.grid(row = 6, column = 4)
        self.add_hourly_entry.grid_forget()
        self.add_hourly_label.grid_forget()
        #Commission rate
        self.add_comm_label = tk.Label(self, text = "Rate:")
        self.add_comm_label.grid(row = 6, column = 5, pady = 5, sticky = tk.W)
        self.add_comm_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_comm_entry.grid(row = 6, column = 6)
        self.add_comm_entry.grid_forget()
        self.add_comm_label.grid_forget()
        #Social Security
        self.add_ss_label = tk.Label(self, text = "Social Security:")
        self.add_ss_label.grid(row = 7, column = 1, pady = 5, sticky = tk.W)
        self.add_ss_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_ss_entry.grid(row = 7, column = 2)
        #Birthday
        self.add_dob_label = tk.Label(self, text = "DOB:")
        self.add_dob_label.grid(row = 7, column = 3, pady = 5, sticky = tk.W)
        self.add_dob_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_dob_entry.grid(row = 7, column = 4)
        #Password
        self.add_password_label = tk.Label(self, text = "Password:")
        self.add_password_label.grid(row = 7, column = 5, pady = 5, sticky = tk.W)
        self.add_password_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_password_entry.grid(row = 7, column = 6)
        #Start Date
        self.add_start_date_label = tk.Label(self, text = "Start Date:")
        self.add_start_date_label.grid(row = 8, column = 1, pady = 5, sticky = tk.W)
        self.add_start_date_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_start_date_entry.grid(row = 8, column = 2)
        #End Date
        self.add_end_date_label = tk.Label(self, text = "End Date:")
        self.add_end_date_label.grid(row = 8, column = 3, pady = 5, sticky = tk.W)
        self.add_end_date_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_end_date_entry.grid(row = 8, column = 4)
        #Permission
        self.add_permission_label = tk.Label(self, text = "Permission:")
        self.add_permission_label.grid(row = 9, column = 1, pady = 5, sticky = tk.W)
        self.add_permission_entry = tk.OptionMenu(self, self.cur_perm, "Admin", "Employee")
        self.add_permission_entry.grid(row = 9, column = 2)
        self.add_permission_entry.config(width = 15)
        #Title
        self.add_title_label = tk.Label(self, text = "Title:")
        self.add_title_label.grid(row = 9, column = 3, pady = 5, sticky = tk.W)
        self.add_title_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_title_entry.grid(row = 9, column = 4)
        #Department
        self.add_dept_label = tk.Label(self, text = "Dept:")
        self.add_dept_label.grid(row = 9, column = 5, pady = 5, sticky = tk.W)
        self.add_dept_entry = tk.Entry(self, width = 15, bg = "white")
        self.add_dept_entry.grid(row = 9, column = 6)
        #Buttons
        self.submit_button = tk.Button(self, text = "Submit", command = self.save_info)
        self.submit_button.grid(row = 10, column = 2, pady = 15)
        self.cancel_button = tk.Button(self, text = "Cancel", command = lambda: self.controller.present_frame("EmployeeList"))
        self.cancel_button.grid(row = 10, column = 1)

        #Set weight to surrounding row/col to center content on frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(10, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(6, weight = 1)

    def update(self):
        #Clear entry boxes
        self.add_emp_id_entry.delete(0, tk.END)
        self.add_first_name_entry.delete(0, tk.END)
        self.add_last_name_entry.delete(0, tk.END)
        self.add_street_entry.delete(0, tk.END)
        self.add_city_entry.delete(0, tk.END)
        self.add_state_entry.delete(0, tk.END)
        self.add_zip_entry.delete(0, tk.END)
        self.add_phone_entry.delete(0, tk.END)
        self.add_email_entry.delete(0, tk.END)
        self.add_routing_number_entry.delete(0, tk.END)
        self.add_account_number_entry.delete(0, tk.END)
        self.add_salary_entry.delete(0, tk.END)
        self.add_hourly_entry.delete(0, tk.END)
        self.add_comm_entry.delete(0, tk.END)
        self.add_ss_entry.delete(0, tk.END)
        self.add_dob_entry.delete(0, tk.END)
        self.add_start_date_entry.delete(0, tk.END)
        self.add_end_date_entry.delete(0, tk.END)
        self.add_title_entry.delete(0, tk.END)
        self.add_dept_entry.delete(0, tk.END)

    def show_hide_bank(self, *args):
        """Shows or hide the values for Direct Deposit based on input"""
        if self.pay_method.get() == "Mail":
            self.add_routing_number_label.grid_forget()
            self.add_routing_number_entry.grid_forget()
            self.add_account_number_label.grid_forget()
            self.add_account_number_entry.grid_forget()
        if self.pay_method.get() == "ACH":
            self.add_routing_number_label.grid(row = 5, column = 3, pady = 5, sticky = tk.W)
            self.add_routing_number_entry.grid(row = 5, column = 4)
            self.add_account_number_label.grid(row = 5, column = 5, pady = 5, sticky = tk.W)
            self.add_account_number_entry.grid(row = 5, column = 6)

    def show_hide_type(self, *args):
        """Shows or hide salary/hourly/commission based on input"""
        if self.pay_type.get() == "Salary":
            self.add_salary_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.add_salary_entry.grid(row = 6, column = 4)
            self.add_hourly_entry.grid_forget()
            self.add_hourly_label.grid_forget()
            self.add_comm_entry.grid_forget()
            self.add_comm_label.grid_forget()
        if self.pay_type.get() == "Hourly":
            self.add_salary_label.grid_forget()
            self.add_salary_entry.grid_forget()
            self.add_hourly_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.add_hourly_entry.grid(row = 6, column = 4)
            self.add_comm_entry.grid_forget()
            self.add_comm_label.grid_forget()
        if self.pay_type.get() == "Commission":
            self.add_salary_label.grid(row = 6, column = 3, pady = 5, sticky = tk.W)
            self.add_salary_entry.grid(row = 6, column = 4)
            self.add_hourly_entry.grid_forget()
            self.add_hourly_label.grid_forget()
            self.add_comm_label.grid(row = 6, column = 5, pady = 5, sticky = tk.W)
            self.add_comm_entry.grid(row = 6, column = 6)

    def save_info(self):
        """Save the new Employee in the database using the database functions"""
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
        e_id = self.add_emp_id_entry.get()
        e = self.controller.database.create_employee(e_id)
        self.controller.database.set_employee_data(e_id, 'name_first', self.add_first_name_entry.get())
        self.controller.database.set_employee_data(e_id, 'name_last', self.add_last_name_entry.get())
        self.controller.database.set_employee_data(e_id, 'contact_phone', self.add_phone_entry.get())
        self.controller.database.set_employee_data(e_id, 'contact_email', self.add_email_entry.get())
        self.controller.database.set_employee_data(e_id, 'address_street', self.add_street_entry.get())
        self.controller.database.set_employee_data(e_id, 'address_city', self.add_city_entry.get())
        self.controller.database.set_employee_data(e_id, 'address_state', self.add_state_entry.get())
        self.controller.database.set_employee_data(e_id, 'zip_code', self.add_zip_entry.get())
        self.controller.database.set_employee_data(e_id, 'classification', classification)
        self.controller.database.set_employee_data(e_id, 'pay_method', method)
        self.controller.database.set_employee_data(e_id, 'salary', self.add_salary_entry.get())
        self.controller.database.set_employee_data(e_id, 'hourly', self.add_hourly_entry.get())
        self.controller.database.set_employee_data(e_id, 'commission_rate', self.add_comm_entry.get())
        self.controller.database.set_employee_data(e_id, 'routing_number', self.add_routing_number_entry.get())
        self.controller.database.set_employee_data(e_id, 'account', self.add_account_number_entry.get())
        self.controller.database.set_employee_data(e_id, 'social_security', self.add_ss_entry.get())
        self.controller.database.set_employee_data(e_id, 'birthday', self.add_dob_entry.get())
        self.controller.database.set_employee_data(e_id, 'start_date', self.add_start_date_entry.get())
        self.controller.database.set_employee_data(e_id, 'permission', self.cur_perm)
        self.controller.database.set_employee_data(e_id, 'title', self.add_title_entry.get())
        self.controller.database.set_employee_data(e_id, 'dept', self.add_dept_entry.get())
        self.controller.database.set_employee_data(e_id, 'email', self.add_email_entry.get())
        self.controller.database.set_employee_data(e_id, 'end_date', self.add_end_date_entry.get())

        #Save password
        auth.add_password(e_id, self.add_password_entry.get())
        #Save password to csv
        if os.path.exists(os.getcwd() + "/Resources/passwords.csv"):
            auth.resave_cache(os.getcwd() + "/Resources/passwords.csv")
        if os.path.exists(os.getcwd() + "/project/Resources/passwords.csv"):
            auth.resave_cache(os.getcwd() + "/project/Resources/passwords.csv")

        #Show saved message
        msg.showinfo(title="Saved", message="Employee Added")

        #Return to previous frame
        self.controller.present_frame("EmployeeList")
