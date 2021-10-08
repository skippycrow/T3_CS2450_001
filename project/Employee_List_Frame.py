import tkinter as tk

#testing

class EmployeeApp(tk.Tk):
    def __init__(self):
        #Initialize tk
        tk.Tk.__init__(self)
        
        #Initialize container options
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Initialize list to hold frames
        self.frames = {}
        

        #Initialize frame values
        page_name = EmployeeList.__name__
        frame = EmployeeList(parent = container, controller = self)
        self.frames[page_name] = frame

            #Stack each frame in same grid cell
        frame.grid(row = 0, column = 0, sticky = "nesw")

        #Show the login page
        self.present_frame("EmployeeList")

    def present_frame(self, page_name):
        #Set the frame
        frame = self.frames[page_name]
        #Raise the frame to top of list
        frame.tkraise()


#TODO
#Search results function
#have the result box be populated by employee class

class EmployeeList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.employees_database = employees_database
        tk.Label(self, text = "Search Employee ", fg = "black", font = "none 12 bold").grid(row = 1, column = 0, sticky = tk.W)
        self.searchBox = tk.Entry(self, width = 100, bg = "white").grid(row=2, column =0, sticky = tk.NW)
        #
        self.search_Results = ["John Morgan", "Matt Morgan"]
        self.resultBox = tk.Listbox(self, width = 100, bg = "white")
        self.resultBox.grid(row=3, column =0, sticky = tk.NW)
        self.selectedEmployee = None
        
        #populate the search Results
        for item in self.search_Results:
            self.resultBox.insert(tk.END, item)
        #event handler for when clicked. selectEmployee()
        self.resultBox.bind("<<ListboxSelect>>", self.selectEmployee)
        
        #copys the selected employee to selectedEmployee
    def selectEmployee(self, event):
        self.selectedEmployee = self.resultBox.get(tk.ACTIVE)
        print(self.selectedEmployee)
    
    
    
    

def main():

    app = EmployeeApp()
    app.mainloop()

if __name__ == "__main__":
    main()