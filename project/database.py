import csv

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
    'routing_number',
    'account_number',
]

class EmployeeDatabase:

    def __init__(self):
        self.employees = {}

    def save_to_file(self, path):
        pass

    def load_from_file(self, path):
        pass

    def create_employee(self, e_id, override_existing = False):
        if e_id in self.employees and not override_existing:
            print('id found in db')
        else:
            self.employees[e_id] = Employee(e_id)

class Employee:

    def __init__(self, e_id):
        self.id = e_id # do **NOT** set this in any other place
        for field in DATA_FIELDS:
            setattr(self, field, '')

    def get_full_name(self):
        return self.name_last + ', ' + self.name_first
    
    def get_id(self):
        return self.id
