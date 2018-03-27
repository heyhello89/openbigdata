import sys

def greet_users(username):
    for i in username:
        print("Hello, "+i[0].upper()+i[1:]+"!")

username=sys.argv[1:]
greet_users(username)