import csv
from hashlib import md5

PASSWORD_CORRECT = 0
PASSWORD_INCORRECT = 1
ID_NOT_FOUND = 2

passwords = {}

def read_auth_data(path, with_debug=False):
    global passwords
    if with_debug:
        passwords['debug'] = md5('debug'.encode()).hexdigest()
    if not path: return
    with open(path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            passwords[row['id']] = row['pw_hash']


def verify_password(_id, _pass):
    global passwords
    if not _id in passwords:
        return ID_NOT_FOUND

    if passwords[_id] == md5(_pass.encode()).hexdigest(): # store MD5 checksum of password
        return PASSWORD_CORRECT

    return PASSWORD_INCORRECT

# IMPORTANT: PASSWORD CHANGES WILL NOT BE REFLECTED IN PASSWORDS_REAL.CSV
# FOR TESTING, YOU WILL NEED TO MODIFY THAT FILE IF CHANGES ARE DESIRED TO PERSIST

def add_password(_id, _pass):
    if _id in passwords:
        raise IndexError("ID already present")
    
    passwords[_id] = md5(_pass.encode()).hexdigest()


def edit_password(_id, _new_pass):
    if not _id in passwords:
        raise IndexError("ID not present")
    
    passwords[_id] = md5(_new_pass.encode()).hexdigest()


def purge_password(_id):
    if not _id in passwords:
        raise IndexError("ID not present")
    
    passwords.pop(_id)


def resave_cache(path):
    with open(path, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'pw_hash'])
        writer.writeheader()
        for _id, _pw_hash in passwords.items():
            row = {
                    'id' : _id,
                    '_pw_hash' : _pw_hash,
                }
            writer.writerow(row)
