import tkinter as tk
from Landing_Frame import LoginFrame
from Landing_Frame import LandingFrame
from Employee_List_Frame import EmployeeList
from Add_Employee_Frame import AddEmployee
from Edit_Employee_Frame import EditEmployee
from Employee_Profile_Frame import EmployeeProfile

class EmployeeApp(tk.Tk):
    def __init__(self):
        #Initialize tk
        tk.Tk.__init__(self)
        
        #Initialize container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Initialize dict to hold frames
        self.frames = {}

        #Initialize dict to store data - Store user, permission, current employee etc. here where it can be accessed by other frames if it needs to
        #Example: add_data("LandingPage_Permission", "Admin")
        self.app_data = {}

        #For each page
        for page in (LoginFrame, LandingFrame, EmployeeList, AddEmployee, EditEmployee, EmployeeProfile):
            #Set page name to name of its class
            page_name = page.__name__

            #Create frame
            frame = page(parent = container, controller = self)

            #Store frame in frames dict
            self.frames[page_name] = frame

            #Stack each frame on top of each other
            frame.grid(row = 0, column = 0, sticky = "nesw")

        #Show the login page
        self.present_frame("LoginFrame")

    def add_data(self, frame_subj, data):
        self.app_data[frame_subj] = data

    def remove_data(self, frame_subj):
        del self.app_data[frame_subj]

    def present_frame(self, page_name):
        #Set the frame
        frame = self.frames[page_name]
        #Raise the frame on top of the others
        frame.tkraise()

def main():
    app = EmployeeApp()
    app.mainloop()

if __name__ == "__main__":
    main()