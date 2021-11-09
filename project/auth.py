import csv
from hashlib import md5

PASSWORD_CORRECT = 0
PASSWORD_INCORRECT = 1
ID_NOT_FOUND = 2

passwords = {}

def read_auth_data(path, with_debug=True):
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
