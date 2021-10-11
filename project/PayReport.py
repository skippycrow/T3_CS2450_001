from database import Employee
from database import EmployeeDatabase

def pay_report_frame(user, search):
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
		pass
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
	