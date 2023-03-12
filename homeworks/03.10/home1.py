username = input("Enter username: ") or 'jooseptoots'


def validate():
    password1 = input("Enter password: ") or 'kentuk123'
    password2 = input("Enter password again: ") or '123kentuk'
    if password1.strip() != password2.strip():
        print("The passwords do not coincide!")
        validate()
    if len(password1) < 8:
        print("The password must be at least 8 characters!")
        validate()
    if not any(char.isdigit() for char in password1):
        print("The password must contain both letters and numbers!")
        validate()
    if not any(char.isalpha() for char in password1):
        print("The password must contain both letters and numbers!")
        validate()
    else:
        reversed_password = password1[::-1]
        print("The password is " + reversed_password)


validate()
