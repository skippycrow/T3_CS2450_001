from tkinter import *
from tkinter import ttk


class EditEmployee:
    def __init__(self):
        root = Tk()
        root.title("Edit Employee")
        frm = ttk.Frame(root, padding=15)
        frm.grid()
        cancel = ttk.Style()
        cancel.configure('C.TButton', background='white', foreground='black', font=('Arial', 14))

        submit = ttk.Style()
        submit.configure('S.TButton', background='white', foreground='black', font=('Arial', 14))

        title_label = Label(root, text="Edit Employee - Will be populated with employee info").grid(row=0, columnspan=2, pady=10, sticky="N")

        edit_first_name_label = Label(root, text="First Name:").grid(row=1, column=0, pady=5, sticky="W")
        edit_first_name_entry = Entry().grid(row=1, column=1)
        edit_last_name_label = Label(root, text="Last Name:").grid(row=2, column=0, pady=5, sticky="W")
        edit_last_name_entry = Entry().grid(row=2, column=1)
        edit_street_label = Label(root, text="Street:").grid(row=3, column=0, pady=5, sticky="W")
        edit_street_entry = Entry().grid(row=3, column=1)
        edit_city_label = Label(root, text="City:").grid(row=4, column=0, pady=5, sticky="W")
        edit_city_entry = Entry().grid(row=4, column=1)
        edit_state_label = Label(root, text="State:").grid(row=5, column=0, pady=5, sticky="W")
        edit_state_entry = Entry().grid(row=5, column=1)
        edit_zip_label = Label(root, text="Zip:").grid(row=6, column=0, pady=5, sticky="W")
        edit_zip_entry = Entry().grid(row=6, column=1)
        edit_phone_label = Label(root, text="Phone:").grid(row=7, column=0, pady=5, sticky="W")
        edit_phone_entry = Entry().grid(row=7, column=1)
        edit_routing_number_label = Label(root, text="Routing Number:").grid(row=8, column=0, pady=5, sticky="W")
        edit_routing_number_entry = Entry().grid(row=8, column=1)
        edit_account_number_label = Label(root, text="Accounting Number:").grid(row=9, column=0, pady=5, sticky="W")
        edit_account_number_entry = Entry().grid(row=9, column=1)
        edit_payment_method_label = Label(root, text="Pay Method:").grid(row=10, column=0, pady=5, sticky="W")
        edit_payment_method_entry = Entry().grid(row=10, column=1)
        submit_button = ttk.Button(text="Submit", style="S.TButton", command = self.save_info).grid(row=11, column=1, pady=15)
        cancel_button = ttk.Button(text="Cancel", style="C.TButton", command=root.destroy).grid(row=11, column=0)

        root.mainloop()

    def save_info(self):
        """Save the new Employee in the database using the database functions"""
        popup = Tk()
        popup.wm_title("Saved")
        label = Label(popup, text="Employee data will be saved")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        #todo
        #Save data to database
        #Return to previous frame


    def check_permission(self, id):
        """returns true if logged in employee matches profile id#
        returns true if logged in as administrator
        returns false otherwise"""
        return False


EditEmployee()
