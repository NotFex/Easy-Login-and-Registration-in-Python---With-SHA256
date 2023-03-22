""" 
 ? Felix Burwitz
 ? Feel free to use this however you like.
"""

import csv
import hashlib

def hash_password(password):
    hash_object = hashlib.sha256(password.encode('utf-8'))
    return hash_object.hexdigest()

def register():
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    hashed_password = hash_password(password)

    with open("users.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([username, hashed_password])

    print("Registration successful!")

def login():
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    with open("users.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            if line[0] == username and line[1] == hash_password(password):
                print("Login successful!")
                return
    print("Incorrect username or password!")


#test
register()
print("="*10 + "Login" + "="*10)
login()
