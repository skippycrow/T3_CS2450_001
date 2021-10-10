# import csv

PASSWORD_CORRECT = 0
PASSWORD_INCORRECT = 1
ID_NOT_FOUND = 2

passwords = {} # populate with data
                    # should passwords be stored in plaintext, or as a hash?
                    # plaintext is a terrible idea in serious applications

def read_auth_data(path):
    global passwords
    print(passwords)
    # read from csv


def verify_password(_id, _pass):
    global passwords
    if not _id in passwords:
        return ID_NOT_FOUND
    elif passwords[_id] == _pass: # todo: maybe hash the _pass
        return PASSWORD_CORRECT
    else:
        return PASSWORD_INCORRECT
