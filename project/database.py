"""Defines EmployeeDatabase and Employee classes"""
import csv


# needs some way to differentiate what fields are accessible by each access level
# might be here, might be elsewhere
DATA_FIELDS = [
    'name_first',
    'name_last',
    'contact_phone',
    'contact_email',
    'address_street',
    'address_city',
    'address_state',
    'zip_code',
    'classification',
    'pay_method',
    'salary',
    'hourly',
    'commission_rate',
    'routing_number',
    'account',
    'social_security',
    'birthday',
    'start_date',
    'permission',
    'title',
    'dept',
    'email',
    'end_date',
]

class EmployeeDatabase:
    """Employee Database class
    Holds id and info for each employee"""

    def __init__(self):
        # Dictionary of employees
        # id as key, Employee object as value
        self.employees = {}

    def save_to_file(self, path):
        """saves data to csv file at path"""
        with open(path, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ['ID'] + DATA_FIELDS)
            writer.writeheader()
            for e_id, employee in self.employees.items():
                row = {}
                row['ID'] = e_id
                for field in DATA_FIELDS:
                    row[field] = getattr(employee, field)
                writer.writerow(row)

    def load_from_file(self, path):
        """reads data from csv file at path"""
        with open(path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                new_employee = self.create_employee(row['ID'])
                for field in DATA_FIELDS:
                    if field in row:
                        setattr(new_employee, field, row[field])

    def create_employee(self, e_id, override_existing = False):
        """creates employee object, assigning the id
        will not by default create one if the id exists already
        created employee object is then returned"""

        if not isinstance(e_id, str):
            raise TypeError('ID should be a String')

        if e_id in self.employees and not override_existing:
            raise ValueError('''Specified id is already present in database
                If this is intended, pass in True for override_existing''')

        self.employees[e_id] = Employee(e_id)
        return self.employees[e_id]

    def get_employee(self, e_id):
        """returns employee with given id"""
        if e_id in self.employees:
            return self.employees[e_id]

        raise IndexError('id not found in employee database')

    def erase_employee(self, e_id):
        """removes employee fram database"""
        if e_id in self.employees:
            self.employees.pop(e_id)

    def set_employee_data(self, e_id, field, value):
        """sets field property of employee with given id"""

        if not field in DATA_FIELDS:
            raise AttributeError('specified field not found in DATA_FIELDS list')

        if not e_id in self.employees:
            raise IndexError('id not found in employee database')

        setattr(self.employees[e_id], field, value)

    def get_employee_data(self, e_id, field):
        """returns the field property of employee with given id"""

        if not field in DATA_FIELDS:
            raise AttributeError('specified field not found in DATA_FIELDS list')

        if not e_id in self.employees:
            raise IndexError('id not found in employee database')

        return getattr(self.employees[e_id], field)

    def read_timecard_data(self, path):
        with open(path, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                idstr = row[0]
                if not idstr in self.employees:
                    print(f'ERROR: id {idstr} not found in database')
                    continue

                for i in range(1, len(row)):
                    self.get_employee(idstr).timecard_data.append(float(row[i]))


    def read_receipt_data(self, path):
        with open(path, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                idstr = row[0]
                if not idstr in self.employees:
                    print(f'ERROR: id {idstr} not found in database')
                    continue

                for i in range(1, len(row)):
                    self.get_employee(idstr).receipt_data.append(float(row[i]))

class Employee:
    """class for single Employee data
    should primarily be managed via containing EmployeeDatabase"""

    def __init__(self, e_id):
        self.id = e_id # do **NOT** set this in any other place
        self.name_first = ''
        self.name_last = ''
        self.timecard_data = []
        self.receipt_data = []
        for field in DATA_FIELDS:
            setattr(self, field, '')

    def get_full_name(self):
        """returns full name in last, first format"""
        return self.name_last + ', ' + self.name_first

    def get_id(self):
        """returns the id of this employee"""
        return self.id
