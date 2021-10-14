#### `auth` library

The `auth` library has two helper functions:

* `read_auth_data(path)`
    Loads a csv file at `path`, and read in the data
    
    The csv file should have two columns, titled `id` and `pw_hash`
    * `id`: the id of the employee
    * `pw_hash`: the MD5 checksum of the password (can be calculated for a given password with `hashlib.md5(password.encode()).hexdigest()`

* `verify_password(_id, _pass)`:
    Verifies (via md5 checksum) that the given `_pass` is the password for the employee with the given `_id`
    
    Returns one of three values:
    * `0`: the password is correct
    * `1`: the password is not correct
    * `2`: the `_id` is not found in the data
