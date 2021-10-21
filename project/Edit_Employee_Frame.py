import tkinter as tk
from tkinter import messagebox as msg

class EditEmployee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        title_label = tk.Label(self, text="Edit Employee - Will be populated with employee info").grid(row=0, columnspan=2, pady=10, sticky=tk.N)

        edit_first_name_label = tk.Label(self, text="First Name:").grid(row=1, column=0, pady=5, sticky=tk.W)
        edit_first_name_entry = tk.Entry(self, width = 15, bg = "white").grid(row=1, column=1)
        edit_last_name_label = tk.Label(self, text="Last Name:").grid(row=2, column=0, pady=5, sticky=tk.W)
        edit_last_name_entry = tk.Entry(self, width = 15, bg = "white").grid(row=2, column=1)
        edit_street_label = tk.Label(self, text="Street:").grid(row=3, column=0, pady=5, sticky=tk.W)
        edit_street_entry = tk.Entry(self, width = 15, bg = "white").grid(row=3, column=1)
        edit_city_label = tk.Label(self, text="City:").grid(row=4, column=0, pady=5, sticky=tk.W)
        edit_city_entry = tk.Entry(self, width = 15, bg = "white").grid(row=4, column=1)
        edit_state_label = tk.Label(self, text="State:").grid(row=5, column=0, pady=5, sticky=tk.W)
        edit_state_entry = tk.Entry(self, width = 15, bg = "white").grid(row=5, column=1)
        edit_zip_label = tk.Label(self, text="Zip:").grid(row=6, column=0, pady=5, sticky=tk.W)
        edit_zip_entry = tk.Entry(self, width = 15, bg = "white").grid(row=6, column=1)
        edit_phone_label = tk.Label(self, text="Phone:").grid(row=7, column=0, pady=5, sticky=tk.W)
        edit_phone_entry = tk.Entry(self, width = 15, bg = "white").grid(row=7, column=1)
        edit_routing_number_label = tk.Label(self, text="Routing Number:").grid(row=8, column=0, pady=5, sticky=tk.W)
        edit_routing_number_entry = tk.Entry(self, width = 15, bg = "white").grid(row=8, column=1)
        edit_account_number_label = tk.Label(self, text="Accounting Number:").grid(row=9, column=0, pady=5, sticky=tk.W)
        edit_account_number_entry = tk.Entry(self, width = 15, bg = "white").grid(row=9, column=1)
        edit_payment_method_label = tk.Label(self, text="Pay Method:").grid(row=10, column=0, pady=5, sticky=tk.W)
        edit_payment_method_entry = tk.Entry(self, width = 15, bg = "white").grid(row=10, column=1)
        submit_button = tk.Button(self, text="Submit", command = self.save_info).grid(row=11, column=1, pady=15)
        cancel_button = tk.Button(self, text="Cancel", command = lambda: controller.present_frame("EmployeeList")).grid(row=11, column=0)

    def save_info(self):
        """Save the new Employee in the database using the database functions"""
        msg.showinfo(title="Saved", message="Employee data will be saved")
        #todo

        #Save data to database

        #Return to previous frame
        self.controller.present_frame("EmployeeList")

    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False
