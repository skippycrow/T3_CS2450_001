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
    'routing_number',
    'account_number',
]

class EmployeeDatabase:

    def __init__(self):
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
                e = self.create_employee(row['id'])
                for field in DATA_FIELDS:
                    if field in row:
                        setattr(e, field, row[field])

    def create_employee(self, e_id, override_existing = False):
        if e_id in self.employees and not override_existing:
            print('id found in db')
        else:
            self.employees[e_id] = Employee(e_id)
            return self.employees[e_id]
    
    def get_employee(self, e_id):
        if e_id in self.employees:
            return self.employees[e_id]
        print('id not found')
    
    def erase_employee(self, e_id):
        self.employees.pop(e_id)
    
    def set_employee_data(self, e_id, field, value):
        setattr(self.employees[e_id], field, value)
    
    def get_employee_data(self, e_id, field):
        return getattr(self.employees[e_id], field)
    
    # TODO: implement searching by name

class Employee:

    def __init__(self, e_id):
        self.id = e_id # do **NOT** set this in any other place
        for field in DATA_FIELDS:
            setattr(self, field, '')

    def get_full_name(self):
        return self.name_last + ', ' + self.name_first
    
    def get_id(self):
        return self.id
