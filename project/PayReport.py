from tkinter import *
from tkinter.ttk import *
from database import Employee
from database import EmployeeDatabase

data = EmployeeDatabase()
data.load_from_file("Resources\\employees.csv")
data.read_timecard_data("Resources\\timecards.csv")
data.read_receipt_data("Resources\\receipts.csv")

class PayReport:
	#Employee Data
	def __init__(self, e_id):
		global data
		self.e_id = e_id

	def get_name (self):
		return data.get_employee(e_id).get_full_name()
	def get_pay_method (self):
		return data.get_employee_data(e_id, 'pay_method')
	def get_salary (self):
		return data.get_employee_data(e_id, 'salary')
	def get_hourly_rate (self):
		return data.get_employee_data(e_id, 'hourly')

	def get_hours (self):
		return data.get_employee(e_id).timecard_data
	def receipt (self):
		return data.get_employee(e_id).receipt_data
	def commission_rate (self):
		return data.get_employee_data(e_id, 'comission_rate')
	def overtime_hours(self): return 


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

