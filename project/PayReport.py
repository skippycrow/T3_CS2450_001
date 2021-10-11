from database import Employee
from database import EmployeeDatabase

def pay_report(user, search):
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
	"""
	# Check user information and permissions
	if(CheckPermissions()):
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
		Pay ammount
	"""
	#hours = 40 if search.hours > 40 else search.hours
	#rate = search.rate
	#return hours * rate
	pass