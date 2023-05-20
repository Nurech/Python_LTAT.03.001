import re

def is_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

# Test the function
print(is_strong("k4A8cd82B")) #true
print(is_strong("Bdy5Cez"))
print(is_strong("password"))
