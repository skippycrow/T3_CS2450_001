from tkinter import *
from tkinter.ttk import *
from database import Employee
from database import EmployeeDatabase

class PayReport(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()

		self.page_title = Label(self, text='<page name>')

		#Employee Information
		self.section_employee = Label(self, text='Employee Info')
		self.head_name = Label(self, text='Name:')
		self.head_id = Label(self, text='ID:')
		self.head_address = Label(self, text='Address:')

		#Bank Information

		#Employee Pay
		self.head_rate = Label(self, text='Rate:')
		self.head_hours = Label(self, text='Hours:')
		self.head_pay = Label(self, text='Pay:')
		self.head_overtime_pay = Label(self, text='Overtime Pay:')
		self.head_total = Label(self, text='Total Pay')

app = PayReport()
app.mainloop()


#TODO: pay_report_frame
def pay_report(user = Employee(), search = Employee(), root = Tk()):
	"""
	Description
	-----------
	Display an employee's payroll to the user

	Parameters
	----------
	user : Employee
		The user running the application.
	search : Employee
		The employee who's information is being accessed
	root : Tk
		Window to display
	"""
	# Check user information and permissions
	if(allow_access(user, search)):
		#TODO: Show searched employee payreport
		pass
	else:
		#TODO: Popup window that informs the user that they do not have the permissiosn
		pass

#FIXME: Unable to retrieve employee permission level
def allow_access(user, search):
	"""
	Description
	-----------
	Checks whether or not the user has permissions to access the
	pay report frame of a specified employee

	Parameters
	----------
	user : Employee
		The user who is running the application
	search : Employee
		The employee who's information is being accessed

	Returns
	-------
	bool
		If the employee has permission return true, otherwise return false
	"""
	if user.get_id() == search.get_id(): # or user.role == admin
		return True
	return False

#TODO: Define calculate_deductions(search)
def calculate_deductions(search):
	"""
	Description
	-----------
	Calculate the deductions to the employee's pay

	Parameters
	----------
	search : Employee
		The employee who's information is being accessed
	
	Returns
	-------
	decimal
		Deduction ammount
	"""
	pass

#FIXME: Unable to retrieve employee rate and hours
def calculate_overtime_pay(search):
	"""
	Description
	-----------
	Calculate the employee pay for overtime

	Parameters
	----------
	search : Employee
		The employee who's information is being accessed
	
	Returns
	-------
	decimal
		Overtime pay ammount
	"""
	#hours = search.hours - 40 if search.hours > 40 else 0
	#rate = search.rate * 1.5
	#return hours * rate
	pass

#FIXME: Unable to retrieve employee rate and hours
def calculate_pay(search):
	"""
	Description
	-----------
	Calculate the employee pay

	Parameters
	----------
	search : Employee
		The employee who's information is being accessed
	
	Returns
	-------
	decimal
		Pay amount
	"""
	#hours = 40 if search.hours > 40 else search.hours
	#rate = search.rate
	#return hours * rate
	pass

def calculate_total_income(search):
	"""
	Description
	-----------
	Sum of employee pay and employee overtime pay

	Parameters
	----------
	search : Employee
		The employee who's information is being accessed

	Returns
	-------
	decimal
		Total income
	"""
	return calculate_pay(search) + calculate_overtime_pay(search)

def calculate_total_pay(search):
	"""
	Description
	-----------
	Apply deductions to total employee income

	Parameters
	search : Employee
		The employee who's information is being accessed

	Returns
	-------
	decimal
		Total income - deductions
	"""
	return calculate_total_pay(search) - calculate_deductions(search)

