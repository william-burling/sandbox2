"""William Burling"""

def main():
    password = get_password()
    censor_password(password)

def get_password():
    password = input("password: ")
    while len(password) < 5:
        password = input("invalid password ")
    return password

def censor_password(password):
    for char in password:
         print("*", end="")

main()