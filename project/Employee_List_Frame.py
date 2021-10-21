import tkinter as tk
from tkinter import messagebox as msg

#TODO
#Search results function
#Select employee function
#have the result box be populated by employee class
#Buttons right now do not push to next frame.
#Search button doesn't utilize the database
#Clicking on the employee doesn't select employee.

class EmployeeList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #self.employees_database = employees_database
        tk.Label(self, text = "Search Employee ", fg = "black", font = "none 12 bold").grid(row = 1, column = 0, sticky = tk.W)
        self.search_box = tk.Entry(self, width = 73, bg = "white").grid(row=2, column =0, sticky = tk.NW)
        self.search_button = tk.Button(self, text = "Search", width = 20, bg = "white", command = self.search_employee)
        self.search_button.grid(row= 2, column = 0, sticky = tk.NE)
        
        self.search_results = ["John Morgan        #91423", "Spencer Crow       #83523"]
        self.result_box = tk.Listbox(self, width = 100, bg = "white")
        self.result_box.grid(row=3, column =0, sticky = tk.NW)
        self.selected_employee = None
        
        #populate the search Results
        for item in self.search_results:
            self.result_box.insert(tk.END, item)
        #event handler for when clicked. selectEmployee()
        self.result_box.bind("<<ListboxSelect>>", self.select_employee)
        
        self.add_employee_button = tk.Button(self, text = "Add Employee", width = 20, bg = "white", command = lambda: controller.present_frame("AddEmployee"))
        self.add_employee_button.grid(row=4, column= 0, sticky = tk.NW)
        
        self.edit_employee_button = tk.Button(self, text = "Edit Employee", width = 20, bg = "white", command = lambda: controller.present_frame("EditEmployee"))
        self.edit_employee_button.grid(row=5, column= 0, sticky = tk.NW)

        self.payroll_button = tk.Button(self, text = "Payroll", width = 20, bg = "white", command = lambda: controller.preset_frame("payrollFrame"))
        self.payroll_button.grid(row=4, column= 0, sticky = tk.E)

        self.export_employee_button = tk.Button(self, text = "Export Employee", width = 20, bg = "white", command = lambda: controller.present_frame("exportEmployee"))
        self.export_employee_button.grid(row=5, column= 0, sticky = tk.E)
      
        #copys the selected employee to selectedEmployee
    def select_employee(self, event):
        self.selected_employee = self.result_box.get(tk.ACTIVE)
        print(self.selected_employee)
        
    def search_employee(self):
        pass
