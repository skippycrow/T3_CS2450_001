import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk


class AddEmployee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.pay_method = tk.StringVar(self)
        self.pay_type = tk.StringVar(self)
        self.cur_perm = tk.StringVar(self)

        self.title_label = tk.Label(self, text="Add Employee")
        self.title_label.grid(row=0, columnspan=6, pady=10, sticky=tk.N)

        # Emp Id
        self.add_emp_id_label = tk.Label(self, text="ID:")
        self.add_emp_id_label.grid(row=1, column=0, pady=5, sticky=tk.W)
        self.add_emp_id_entry = tk.Entry(self, width=15, bg="white")
        self.add_emp_id_entry.grid(row=1, column=1)

        # First Name
        self.add_first_name_label = tk.Label(self, text="First Name:")
        self.add_first_name_label.grid(row=1, column=2, pady=5, sticky=tk.W)
        self.add_first_name_entry = tk.Entry(self, width=15, bg="white")
        self.add_first_name_entry.grid(row=1, column=3)

        # Last Name
        self.add_last_name_label = tk.Label(self, text="Last Name:")
        self.add_last_name_label.grid(row=1, column=4, pady=5, sticky=tk.W)
        self.add_last_name_entry = tk.Entry(self, width=15, bg="white")
        self.add_last_name_entry.grid(row=1, column=5)

        # Street
        self.add_street_label = tk.Label(self, text="Street:")
        self.add_street_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        self.add_street_entry = tk.Entry(self, width=15, bg="white")
        self.add_street_entry.grid(row=2, column=1)

        # City
        self.add_city_label = tk.Label(self, text="City:").grid(row=2, column=2, pady=5, sticky=tk.W)
        self.add_city_entry = tk.Entry(self, width=15, bg="white").grid(row=2, column=3)

        # State
        self.add_state_label = tk.Label(self, text="State:").grid(row=2, column=4, pady=5, sticky=tk.W)
        self.add_state_entry = tk.Entry(self, width=15, bg="white").grid(row=2, column=5)

        # Zip
        self.add_zip_label = tk.Label(self, text="Zip:").grid(row=3, column=0, pady=5, sticky=tk.W)
        self.add_zip_entry = tk.Entry(self, width=15, bg="white").grid(row=3, column=1)

        # Phone
        self.add_phone_label = tk.Label(self, text="Phone:").grid(row=3, column=2, pady=5, sticky=tk.W)
        self.add_phone_entry = tk.Entry(self, width=15, bg="white").grid(row=3, column=3)

        # Email
        self.add_email_label = tk.Label(self, text="Email:")
        self.add_email_label.grid(row=3, column=4, pady=5, sticky=tk.W)
        self.add_email_entry = tk.Entry(self, width=15, bg="white")
        self.add_email_entry.grid(row=3, column=5)

        # Pay Method
        self.add_payment_method_label = tk.Label(self, text="Pay Method:").grid(row=4, column=0, pady=5, sticky=tk.W)
        self.add_payment_method_entry = tk.OptionMenu(self, self.pay_method, "Mail", "ACH")
        self.add_payment_method_entry.grid(row=4, column=1)
        self.add_payment_method_entry.config(width=15)

        self.pay_method.trace("w", self.show_hide_bank)

        # Routing Number
        self.add_routing_number_label = tk.Label(self, text="Routing #:")
        self.add_routing_number_label.grid(row=4, column=2, pady=5, sticky=tk.W)
        self.add_routing_number_entry = tk.Entry(self, width=15, bg="white")
        self.add_routing_number_entry.grid(row=4, column=3)

        # Account Number
        self.add_account_number_label = tk.Label(self, text="Account #:")
        self.add_account_number_label.grid(row=4, column=4, pady=5, sticky=tk.W)
        self.add_account_number_entry = tk.Entry(self, width=15, bg="white")
        self.add_account_number_entry.grid(row=4, column=5)

        self.types = ("Salary", "Hourly", "Commission")

        # Classification
        self.add_class_label = tk.Label(self, text="Pay Type:")
        self.add_class_label.grid(row=5, column=0, pady=5, sticky=tk.W)
        self.add_class_entry = tk.OptionMenu(self, self.pay_type, *self.types, command=self.show_hide_type)
        self.add_class_entry.grid(row=5, column=1)
        self.add_class_entry.config(width=15)

        # Salary Amount
        self.add_salary_label = tk.Label(self, text="Salary Amount:")
        self.add_salary_label.grid(row=5, column=2, pady=5, sticky=tk.W)
        self.add_salary_entry = tk.Entry(self, width=15, bg="white")
        self.add_salary_entry.grid(row=5, column=3)
        self.add_salary_label.grid_forget()
        self.add_salary_entry.grid_forget()

        # Hourly rate
        self.add_hourly_label = tk.Label(self, text="Rate:")
        self.add_hourly_label.grid(row=5, column=2, pady=5, sticky=tk.W)
        self.add_hourly_entry = tk.Entry(self, width=15, bg="white")
        self.add_hourly_entry.grid(row=5, column=3)
        self.add_hourly_entry.grid_forget()
        self.add_hourly_label.grid_forget()

        # Commission rate
        self.add_comm_label = tk.Label(self, text="Rate:")
        self.add_comm_label.grid(row=5, column=4, pady=5, sticky=tk.W)
        self.add_comm_entry = tk.Entry(self, width=15, bg="white")
        self.add_comm_entry.grid(row=5, column=5)
        self.add_comm_entry.grid_forget()
        self.add_comm_label.grid_forget()

        # Social Security
        self.add_ss_label = tk.Label(self, text="Social Security:")
        self.add_ss_label.grid(row=6, column=0, pady=5, sticky=tk.W)
        self.add_ss_entry = tk.Entry(self, width=15, bg="white")
        self.add_ss_entry.grid(row=6, column=1)

        # Birthday
        self.add_dob_label = tk.Label(self, text="DOB:")
        self.add_dob_label.grid(row=6, column=2, pady=5, sticky=tk.W)
        self.add_dob_entry = tk.Entry(self, width=15, bg="white")
        self.add_dob_entry.grid(row=6, column=3)

        # Start Date
        self.add_start_date_label = tk.Label(self, text="Start Date:")
        self.add_start_date_label.grid(row=7, column=0, pady=5, sticky=tk.W)
        self.add_start_date_entry = tk.Entry(self, width=15, bg="white")
        self.add_start_date_entry.grid(row=7, column=1)

        # End Date
        self.add_end_date_label = tk.Label(self, text="End Date:")
        self.add_end_date_label.grid(row=7, column=2, pady=5, sticky=tk.W)
        self.add_end_date_entry = tk.Entry(self, width=15, bg="white")
        self.add_end_date_entry.grid(row=7, column=3)

        # Permission
        self.add_permission_label = tk.Label(self, text="Permission:")
        self.add_permission_label.grid(row=8, column=0, pady=5, sticky=tk.W)
        self.add_permission_entry = tk.OptionMenu(self, self.cur_perm, "Admin", "Employee")
        self.add_permission_entry.grid(row=8, column=1)
        self.add_permission_entry.config(width=15)

        # Title
        self.add_title_label = tk.Label(self, text="Title:")
        self.add_title_label.grid(row=8, column=2, pady=5, sticky=tk.W)
        self.add_title_entry = tk.Entry(self, width=15, bg="white")
        self.add_title_entry.grid(row=8, column=3)

        # Department
        self.add_dept_label = tk.Label(self, text="Dept:")
        self.add_dept_label.grid(row=8, column=4, pady=5, sticky=tk.W)
        self.add_dept_entry = tk.Entry(self, width=15, bg="white")
        self.add_dept_entry.grid(row=8, column=5)

        # Buttons
        self.submit_button = tk.Button(self, text="Submit", command=self.save_info)
        self.submit_button.grid(row=11, column=1, pady=15)
        self.cancel_button = tk.Button(self, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=11, column=0)

    def cancel(self):
        self.controller.present_frame("EmployeeList")

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

        e_id = self.add_emp_id_entry.get()
        e = self.controller.database.create_employee(e_id)

        self.controller.database.set_employee_data(e_id, 'name_first', self.add_first_name_entry.get())
        self.controller.database.set_employee_data(e_id, 'name_last', self.add_last_name_entry.get())
        self.controller.database.set_employee_data(e_id, 'contact_phone', self.add_phone_entry.get())
        self.controller.database.set_employee_data(e_id, 'contact_email', "email")
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
        self.controller.database.set_employee_data(e_id, 'Account', self.add_account_number_entry.get())
        self.controller.database.set_employee_data(e_id, 'social_security', self.add_ss_entry.get())
        self.controller.database.set_employee_data(e_id, 'birthday', self.add_dob_entry.get())
        self.controller.database.set_employee_data(e_id, 'start_date', self.add_start_date_entry.get())
        self.controller.database.set_employee_data(e_id, 'permission', self.cur_perm)
        self.controller.database.set_employee_data(e_id, 'title', self.add_title_entry.get())
        self.controller.database.set_employee_data(e_id, 'dept', self.add_dept_entry.get())
        self.controller.database.set_employee_data(e_id, 'email', self.add_email_entry.get())
        self.controller.database.set_employee_data(e_id, 'end_date', self.add_end_date_entry.get())

        msg.showinfo(title="Saved", message="Employee Added")

        # Return to previous frame
        self.controller.present_frame("EmployeeList")

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False

    def show_hide_bank(self, *args):
        """Shows or hide the values for Direct Deposit based on input"""
        if self.pay_method.get() == "Mail":
            self.add_routing_number_label.grid_forget()
            self.add_routing_number_entry.grid_forget()
            self.add_account_number_label.grid_forget()
            self.add_account_number_entry.grid_forget()
        if self.pay_method.get() == "ACH":
            self.add_routing_number_label.grid(row=4, column=2, pady=5, sticky=tk.W)
            self.add_routing_number_entry.grid(row=4, column=3)
            self.add_account_number_label.grid(row=4, column=4, pady=5, sticky=tk.W)
            self.add_account_number_entry.grid(row=4, column=5)

    def show_hide_type(self, *args):
        """Shows or hide salary/hourly/commission based on input"""
        if self.pay_type.get() == "Salary":
            self.add_salary_label.grid(row=5, column=2, pady=5, sticky=tk.W)
            self.add_salary_entry.grid(row=5, column=3)
            self.add_hourly_entry.grid_forget()
            self.add_hourly_label.grid_forget()
            self.add_comm_entry.grid_forget()
            self.add_comm_label.grid_forget()
        if self.pay_type.get() == "Hourly":
            self.add_salary_label.grid_forget()
            self.add_salary_entry.grid_forget()
            self.add_hourly_label.grid(row=5, column=2, pady=5, sticky=tk.W)
            self.add_hourly_entry.grid(row=5, column=3)
            self.add_comm_entry.grid_forget()
            self.add_comm_label.grid_forget()
        if self.pay_type.get() == "Commission":
            self.add_salary_label.grid(row=5, column=2, pady=5, sticky=tk.W)
            self.add_salary_entry.grid(row=5, column=3)
            self.add_hourly_entry.grid_forget()
            self.add_hourly_label.grid_forget()
            self.add_comm_label.grid(row=5, column=4, pady=5, sticky=tk.W)
            self.add_comm_entry.grid(row=5, column=5)
