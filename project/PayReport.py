from tkinter import *
from tkinter.ttk import *
from database import Employee
from database import EmployeeDatabase

class PayReport(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		row, col = 0, 0
		#Page Title
		self.page_title = Label(self, text='<page name>')

		#Employee Information
		self.section_employee = Label(self, text='Employee Info')
		self.head_name = Label(self, text='Name:')
		self.head_id = Label(self, text='ID:')
		self.head_address = Label(self, text='Address:')

		#Bank Information
		self.section_bank = Label(self, text='Bank Information')
		self.head_routing_number = Label(self, text='Routing Number:')
		self.head_account_number = Label(self, text='Account Number:')

		#Employee Pay
		self.section_pay = Label(self, text='Employee Pay')
		self.head_rate = Label(self, text='Rate:')
		self.head_hours = Label(self, text='Hours:')
		self.head_pay = Label(self, text='Pay:')
		self.head_overtime_pay = Label(self, text='Overtime Pay:')
		self.head_total_pay = Label(self, text='Total Pay')

		#Deductions
		self.section_deductions = Label(self, text='Deductions')
		self.head_deductions = []
		self.head_total_deductiosn = Label(self, text='Total Deductions:')
		
		#Taxes
		self.section_taxes = Label(self, text='Taxes')
		self.head_taxes = []
		self.head_total_taxes = Label(self, text='Total Taxes:')

		#Net Pay
		self.head_net_pay = Label(self, text='Net Pay:')

		#Place Elements

		#Grid for element placement
		page_space = [[None]*40 for _ in range(40)]

		#Header Layout
		page_layout = [
			[self.page_title],
			[self.section_employee],
			[self.head_name],
			[self.head_id],
			[self.head_address],
			[],
			[self.section_bank],
			[self.head_routing_number],
			[self.head_account_number],
			[],
			]
		#Header
		yval = 0
		for y in page_layout:
			#print(y,"\n")
			xval = 0
			for x in y:
				page_space[yval][xval] = page_layout[yval][xval]
				xval += 1
			yval += 1

		yval = 0
		for y in page_space:
			#print(y,"\n")
			xval = 0
			for x in y:
				if(x is not None):
					x.grid(column=xval, row=yval)

				xval += 1
			yval += 1



app = PayReport()
app.mainloop()


#TODO: pay_report_frame
def pay_report(user = Employee(12), search = Employee(12), root = Tk()):
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

