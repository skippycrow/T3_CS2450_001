import tkinter as tk
from tkinter import messagebox as msg

#TODO
#have the result box be populated by employee class
#Search button doesn't utilize the database


class EmployeeList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text = "Search Employee ", fg = "black", font = "none 12 bold").grid(row = 1, column = 0, sticky = tk.W)
        self.search_results = []
        self.selected_employee = None
        ### TODO: impmlement the employee database 
        self.test_Dict = self.controller.database.employees

        #{"91423" : {"name_first" :"Jon", "name_last" : "Morgan" }, "83523" :{ "name_first" :"Spencer", "name_last" : "Crow"}}
        ###

        #Search Box
        self.search_box = tk.Entry(self, width = 73, bg = "white")
        self.search_box.grid(row=2, column =0, sticky = tk.NW)
        
        #Search Button
        self.search_button = tk.Button(self, text = "Search", width = 20, bg = "white", command = self.search_employee)
        self.search_button.grid(row= 2, column = 0, sticky = tk.NE)
        
        #Result Box
        self.result_box = tk.Listbox(self, width = 100, bg = "white")
        self.result_box.grid(row=3, column =0, sticky = tk.NW)

        #Add employee Button
        self.add_employee_button = tk.Button(self, text = "Add Employee", width = 20, bg = "white", command = self.addEmployeeFrame )
        self.add_employee_button.grid(row=4, column= 0, sticky = tk.NW)
        
        #Employee profile button
        self.employee_profile_button = tk.Button(self, text = "Employee Profile", width = 20, bg = "white", command = self.employeeProfileFrame)
        self.employee_profile_button.grid(row=5, column= 0, sticky = tk.NW)

        #Payroll Button
        self.payroll_button = tk.Button(self, text = "Payroll", width = 20, bg = "white", command = lambda: controller.preset_frame("payrollFrame"))
        self.payroll_button.grid(row=4, column= 0, sticky = tk.E)

        #Export employee button
        self.export_employee_button = tk.Button(self, text = "Export Employee", width = 20, bg = "white", command = lambda: controller.present_frame("exportEmployee"))
        self.export_employee_button.grid(row=5, column= 0, sticky = tk.E)
        
        #back button
        tk.Button(self, text = "Back", width = 20, bg = "white", command = lambda: controller.present_frame("LandingFrame")).grid(column=0, row=6)
        
        #Called to set up the employee list
        self.search_employee()
        
        #copys the selected employee to selectedEmployee
    def select_employee(self, event):
        self.result_box.get(tk.ACTIVE)
        
        #Search function
    def search_employee(self):
        self.search_results = []
        for employeee in self.test_Dict:
            empFirstName = self.test_Dict.get(employeee)["name_first"]
            empLastName = self.test_Dict.get(employeee)["name_last"]
            empNum = employeee
            if (self.search_box.get()).lower() in empNum:
                self.search_results.append([empFirstName + ' ' + empLastName, empNum])                  
            elif (self.search_box.get()).lower() in empLastName.lower():
                self.search_results.append([empFirstName + ' ' +  empLastName, empNum])            
            elif (self.search_box.get()).lower() in empFirstName.lower():
                self.search_results.append([empFirstName + ' ' +  empLastName, empNum])  
        self.update_list()
        
        #Updates the listbox to display the correct list of names.
    def update_list(self):
        self.result_box.delete(0,tk.END)
        for item in self.search_results:
            insert = (item[0] + "           ID#" + item[1]) 
            self.result_box.insert(tk.END, insert)
            
        #Transition to add employee page       
    def addEmployeeFrame(self):
        self.controller.present_frame("AddEmployee")
        
        #Transition to the employee ProfileFrame
    def employeeProfileFrame(self):
        self.controller.app_data["selected_Employee"] = (self.result_box.get(tk.ACTIVE).split("ID#")[1])
        self.controller.present_frame("EmployeeProfile")
        
        
        