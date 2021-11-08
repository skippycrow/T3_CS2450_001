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

	def get_name (self): # Gets the name of this employee
		return data.get_employee(e_id).get_full_name()
	def get_pay_method (self): # Gets the pay method for this employee
		return data.get_employee_data(e_id, 'pay_method')
	def get_salary (self): # Gets the employee's salary
		return data.get_employee_data(e_id, 'salary')
	def get_hourly_rate (self): # Gets the employee's hourly rate
		return data.get_employee_data(e_id, 'hourly')
	def get_total_hours (self): # Gets the total hours the employee has worked
		return data.get_employee(e_id).timecard_data
	def get_receipt (self): # Gets receipt associated with employee id
		return data.get_employee(e_id).receipt_data
	def get_commission_rate (self): # Gets commission rate of this employee
		return data.get_employee_data(e_id, 'comission_rate')

	def get_overtime_hours(self): # Gets overtime hours
		return self.get_hours() - 40 if self.get_hours > 40 else 0
	def get_regular_hours(self): # Gets regular hours
		return self.get_hours() if self.get_hours <= 40 else 40

	def get_total_pay:
		return 12


