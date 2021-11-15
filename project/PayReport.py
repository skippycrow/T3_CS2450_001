from tkinter import *
from tkinter.ttk import *
from database import Employee
from database import EmployeeDatabase
from datetime import date



class PayReport:
	# Employee Data
	def __init__(self, e_id, data):
		self.data = data
		self.e_id = e_id

	# Get Inforation from csv and database
	def get_name (self): # Gets the name of this employee
		return self.data.get_employee(self.e_id).get_full_name()

	def get_pay_method (self): # Gets the pay method for this employee
		return self.data.get_employee_data(self.e_id, 'pay_method')

	def get_salary (self): # Gets the employee's salary
		return float(self.data.get_employee_data(self.e_id, 'salary'))

	def get_hourly_rate (self): # Gets the employee's hourly rate
		return float(self.data.get_employee_data(self.e_id, 'hourly'))

	def get_total_hours (self): # Gets the total hours the employee has worked
		total_time = 0
		for time in self.data.get_employee(self.e_id).timecard_data:
		    total_time += time
		return total_time

	def get_receipts (self): # Gets receipt associated with employee id
		return self.data.get_employee(self.e_id).receipt_data

	def get_commission_rate (self): # Gets commission rate of this employee
		return self.data.get_employee_data(self.e_id, 'comission_rate')

	# Calculate hours
	def get_overtime_hours(self): # Gets overtime hours
		return self.get_total_hours() - 40 if self.get_total_hours() > 40 else 0

	def get_regular_hours(self): # Gets regular hours
		return self.get_total_hours() if self.get_total_hours() <= 40 else 40

	# Calculate Rates
	def get_overtime_rate(self): # Gets 1.5 * hourly rate
		return self.get_hourly_rate() * 1.5

	# Calculate Hourly Pay
	def get_regular_pay(self): # Gets regular pay
		return self.get_regular_hours() * self.get_hourly_rate()

	def get_overtime_pay(self): # Gets overtime pay
		return self.get_overtime_hours() * self.get_overtime_rate()

	def get_total_hourly_pay(self): # Gets total hourly pay
		return self.get_regular_pay() + self.get_overtime_pay()

	# Non-Hourly Pay
	def get_commission_pay(self): # Gets the payment from commissions
		total = 0
		for commission in self.get_receipts():
			total += commission * (self.get_commission_rate/100)
		return total

	# Object to String conversion
	def __str__(self): # Convert PayReport object to string listing all the necessary details for the pay report.
		pay_string = ""
		if self.get_pay_method() == '1':
			pay_string = 'Hours: {0:.2f}, Pay: {1:.2f}'.format(self.get_total_hours(), self.get_total_hourly_pay())
		else:
			pay_string = 'Salary: {0:.2f}'.format(self.get_salary())
		info_string = 'ID: {0}, Name: {1}, {2}'.format(self.e_id, self.get_name(), pay_string)
		return info_string

def pay_roll(data):
	reptx = open('Resources\\PayReport.txt', 'a')
	reptx.write('\n------------Payreport of: {0}------------\n'.format(date.today()))
	for e_id in data.employees.keys():
		reptx.write(PayReport(e_id, data).__str__() + '\n')
	print("Generated payroll at: {0}".format(reptx.name))
	reptx.close()
