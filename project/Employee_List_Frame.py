import tkinter as tk
from tkinter import messagebox as msg
import PayReport as PR

# TODO
# have the result box be populated by employee class
# Search button doesn't utilize the database

class EmployeeList(tk.Frame):
    def __init__(self, parent, controller):
        #Initialize tk
        tk.Frame.__init__(self, parent)

        #Initialize controller
        self.controller = controller

        #Initialize variables
        self.search_results = []
        self.selected_employee = None
        self.sv = tk.StringVar()
        self.sv.trace_add("write", self.search_employee)

        ### TODO: impmlement the employee database 

        #Style frame
        tk.Label(self, text = "Search Employee ", fg = "black", font = "none 12 bold").grid(row = 1, column = 1, sticky = tk.W)
        self.search_box = tk.Entry(self, textvariable = self.sv, width = 73, bg = "white")
        self.search_box.grid(row = 2, column = 1, sticky = tk.NW)
        self.clear_button = tk.Button(self, text = "Clear", width = 20, bg = "white", command = self.clear_search)
        self.clear_button.grid(row = 2, column = 1, sticky = tk.NE)
        self.result_box = tk.Listbox(self, width = 100, bg = "white")
        self.result_box.grid(row = 3, column = 1, sticky = tk.NW)
        self.add_employee_button = tk.Button(self, text = "Add Employee", width = 20, bg = "white", command = self.clicked_add_employee)
        self.add_employee_button.grid(row = 4, column = 1, sticky = tk.NW)
        self.employee_profile_button = tk.Button(self, text = "Employee Profile", width = 20, bg = "white", command = self.clicked_profile)
        self.employee_profile_button.grid(row = 5, column = 1, sticky = tk.NW)
        # ! self.payroll_button = tk.Button(self, text = "Payroll", width = 20, bg = "white", command = lambda: controller.preset_frame("payrollFrame"))
        self.payroll_button = tk.Button(self, text = "Payroll", width = 20, bg = "white", command = self.clicked_payroll)
        self.payroll_button.grid(row = 4, column = 1, sticky = tk.E)
        self.export_employee_button = tk.Button(self, text = "Export Employee", width = 20, bg = "white", command = self.clicked_export)
        self.export_employee_button.grid(row = 5, column = 1, sticky = tk.E)
        tk.Button(self, text = "Back", width = 20, bg = "white", command = self.clicked_back).grid(column = 1, row = 6)

        #Set weight to surrounding row/col to center buttons on frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(7, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(2, weight = 1)

        # Called to set up the employee list
        self.search_employee()

    def update(self):
        pass

    def select_employee(self, event):
        #Get selected employee
        self.result_box.get(tk.ACTIVE)

    # Search function
    def search_employee(self, *args):
        self.search_results = []
        for employeee in self.controller.database.employees:
            empFirstName = self.controller.database.get_employee_data(employeee, "name_first")
            empLastName = self.controller.database.get_employee_data(employeee, "name_last")
            empNum = employeee
            if (self.search_box.get()).lower() in empNum:
                self.search_results.append([empFirstName + ' ' + empLastName, empNum])
            elif (self.search_box.get()).lower() in empLastName.lower():
                self.search_results.append([empFirstName + ' ' + empLastName, empNum])
            elif (self.search_box.get()).lower() in empFirstName.lower():
                self.search_results.append([empFirstName + ' ' + empLastName, empNum])
        self.update_list()

    # Updates the listbox to display the correct list of names.
    def update_list(self):
        self.result_box.delete(0, tk.END)
        for item in self.search_results:
            insert = (item[0] + "           ID#" + item[1])
            self.result_box.insert(tk.END, insert)

    def clear_search(self):
        self.sv.set("")

    def clicked_add_employee(self):
        #If admin
        if self.controller.app_data["LoginFrame_permission"] == "Admin":
            #Proceed to add employee frame
            self.controller.present_frame("AddEmployee")
        #Not admin
        else:
            #Show permission error
            msg.showerror("Access Denied", "You do not have permission for this action")

    def clicked_profile(self):
        #Set selected employee in app data
        self.controller.app_data["EmployeeListFrame_selectedEmployeeID"] = (self.result_box.get(tk.ACTIVE).split("ID#")[1])

        #Set show selected employee flag in app data
        self.controller.app_data["EmployeeListFrame_showSelectedEmployee"] = True

        #Proceed to employee profile
        self.controller.present_frame("EmployeeProfile")

    def clicked_export(self):
        #If admin
        if self.controller.app_data["LoginFrame_permission"] == "Admin":
            #Proceed to export employee frame
            #self.controller.present_frame("ExportEmployee")
            #Temporary functionality
            msg.showinfo("Export", "Employee Exported")
        #Not admin
        else:
            #Show permission error
            msg.showerror("Acess Denied", "You do not have permission for this action")

    def clicked_payroll(self):
        #If admin
        if self.controller.app_data["LoginFrame_permission"] == "Admin":
            #Run payroll
            PR.pay_roll(controller.database)
        #Not admin
        else:
            #Show permission error
            msg.showerror("Access Denied", "You do not have permission for this action")

    def clicked_back(self):
        #Reset show selected employee flag
        self.controller.app_data["EmployeeListFrame_showSelectedEmployee"] = False

        #Clear search bar
        self.clear_search()

        #Proceed to landing page
        self.controller.present_frame("LandingFrame")
