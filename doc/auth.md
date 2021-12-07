#### `auth` library

The `auth` library has two helper functions:

* `read_auth_data(path, with_debug=False)`
    Loads a csv file at `path`, and read in the data
    
    The csv file should have two columns, titled `id` and `pw_hash`
    * `id`: the id of the employee
    * `pw_hash`: the MD5 checksum of the password (can be calculated for a given password with `hashlib.md5(password.encode()).hexdigest()`

    If `with_debug` is `True`, then the ID/password combo of 'debug'/'debug' will be added.

* `verify_password(_id, _pass)`:
    Verifies (via md5 checksum) that the given `_pass` is the password for the employee with the given `_id`
    
    Returns one of three values:
    * `0`: the password is correct
    * `1`: the password is not correct
    * `2`: the `_id` is not found in the data

* `add_password(_id, _pass)`:
    Adds hash of password `_pass` and employee id `_id` to the password data, if that id is not already present.

* `edit_password(_id, _new_pass)`:
    sets the password of employee with given `_id` to `_new_pass`, as long as that id is present

* `purge_password(_id)`:
    removes `_id` from database

* `resave_cache(path)`:
    saves password has data to a csv at `path`
    
    **Note: 'passwords_real.csv' will not be updated, as that file is for interal referencing, and would not be used in an actual deployment. If you wish to commit changes to the password database, this file must be edited manually.**
