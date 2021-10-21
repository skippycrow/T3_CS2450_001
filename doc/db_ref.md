#### `EmployeeDatabase` class

* `save_to_file(path)`
    
    Saves the `employees` dictionary into a csv at the specified `path`.

* `load_from_file(path)`
    
    Loads the csv file at the specified `path` and adds Employee objects for each row.

* `create_employee(e_id, override_existing = False)`
    
    Creates a new Employee with the specified id value and returns it.
    If the id is already in the database, a new employee will not be created, and a `ValueError` will be raised, unless `override_existing` is True

* `get_employee(e_id)`
    
    Returns the Employee object with the specified id. Will raise an `IndexError` if the id is not present.

* `erase_employee(e_id)`
    
    Removes the specified Employee from the database

* `set_employee_data(e_id, field, value)`
    
    sets the `field` property on the Employee with the id `e_id` with the `value`. Will raise `AttributeError` if the field is not recognized, and an `IndexError` if the id is not present.
    
    ```
        db.set_employee_data('12-345', 'contact_email', 'person@website.tld')
    ```

* `get_employee_data(e_id, field)`
    
    returns the value of the `field` property of the specified Employee. Will raise `AttributeError` if the field is not recognized, and an `IndexError` if the id is not present.
    
    ```
        db.get_employee_data('12-345', 'contact_email') # gives 'person@website.tld'
    ```

#### `Employee` class

* `get_full_name()`

    returns the Employee's full name, in "last, first" format

Data Fields:

* `name_first`

* `name_last`

* `contact_phone`

* `contact_email`

* `address_street`

* `address_city`

* `address_state`

* `zip_code`

* `classification`

* `pay_method`

* `salary`

* `hourly`

* `commission_rate`

* `routing_number`

* `account_number`
