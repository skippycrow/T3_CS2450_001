import csv
from hashlib import md5

PASSWORD_CORRECT = 0
PASSWORD_INCORRECT = 1
ID_NOT_FOUND = 2

passwords = {} 

def read_auth_data(path):
    global passwords
    with open(path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            passwords[row['id']] = row['pw_hash']


def verify_password(_id, _pass):
    global passwords
    if not _id in passwords:
        return ID_NOT_FOUND
    elif passwords[_id] == md5(_pass.encode()).hexdigest(): # store MD5 checksum of password
        return PASSWORD_CORRECT
    else:
        return PASSWORD_INCORRECT
