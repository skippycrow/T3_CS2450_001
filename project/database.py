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
    'Account',
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
    # Employee Database class
    # Holds id and info for each employee

    def __init__(self):
        # Dictionary of employees
        # id as key, Employee object as value
        self.employees = {}

    def save_to_file(self, path):
        with open(path, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ['id'] + DATA_FIELDS)
            writer.writeheader()
            for e_id, e in self.employees.items():
                row = {}
                row['id'] = e_id
                for field in DATA_FIELDS:
                    row[field] = getattr(e, field)
                writer.writerow(row)

    def load_from_file(self, path):
        with open(path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                e = self.create_employee(row['ID'])
                for field in DATA_FIELDS:
                    if field in row:
                        setattr(e, field, row[field])

    def create_employee(self, e_id, override_existing = False):
        if not isinstance(e_id, str):
            raise TypeError('ID should be a String')

        if e_id in self.employees and not override_existing:
            raise ValueError('Specified id is already present in database\nIf this is intended, pass in True for override_existing')
        else:
            self.employees[e_id] = Employee(e_id)
            return self.employees[e_id]
    
    def get_employee(self, e_id):
        if e_id in self.employees:
            return self.employees[e_id]
        else:
            raise IndexError('id not found in employee database')
    
    def erase_employee(self, e_id):
        if e_id in self.employees:
            self.employees.pop(e_id)
    
    def set_employee_data(self, e_id, field, value):
        if not field in DATA_FIELDS:
            raise AttributeError('specified field not found in DATA_FIELDS list')
        elif not e_id in self.employees:
            raise IndexError('id not found in employee database')
        else:
            setattr(self.employees[e_id], field, value)
    
    def get_employee_data(self, e_id, field):
        if not field in DATA_FIELDS:
            raise AttributeError('specified field not found in DATA_FIELDS list')
        elif not e_id in self.employees:
            raise IndexError('id not found in employee database')
        else:
            return getattr(self.employees[e_id], field)
    
    # TODO: implement searching by name

class Employee:
    # class for single Employee data
    # should primarily be manmaged via containing EmployeeDatabase

    def __init__(self, e_id):
        self.id = e_id # do **NOT** set this in any other place
        for field in DATA_FIELDS:
            setattr(self, field, '')

    def get_full_name(self):
        return self.name_last + ', ' + self.name_first
    
    def get_id(self):
        return self.id

    def set_id(self, new_id):
        raise ValueError('Don\'t')
