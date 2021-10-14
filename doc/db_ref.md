#### `EmployeeDatabase` class

* `save_to_file(path)`
    
    Saves the `employees` dictionary into a csv at the specified `path`.

* `load_from_file(path)`
    
    Loads the csv file at the specified `path` and adds Employee objects for each row.

* `create_employee(e_id, override_existing = False)`
    
    Creates a new Employee with the specified id value and returns it.
    If the id is already in the database, a new employee will not be created, unless `override_existing` is True

* `get_employee(e_id)`
    
    Returns the Employee object with the specified id

* `erase_employee(e_id)`
    
    Removes the specified Employee from the database

* `set_employee_data(e_id, field, value)`
    
    sets the `field` property on the Employee with the id `e_id` with the `value`
    
    ```
        db.set_employee_data('12-345', 'contact_email', 'person@website.tld')
    ```

* `get_employee_data(e_id, field)`
    
    returns the value of the `field` property of the specified Employee
    
    ```
        db.get_employee_data('12-345', 'contact_email') # gives 'person@website.tld'
    ```

#### `Employee` class

* `get_full_name()`

    returns the Employee's full name, in "last, first" format
