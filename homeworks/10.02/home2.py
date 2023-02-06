def replace_accented_letters(str):
    new_str = ''
    for i in str:
        if i == 'Õ' or i == 'õ':
            new_str += 'o'
        elif i == 'Ä' or i == 'ä':
            new_str += 'a'
        elif i == 'Ö' or i == 'ö':
            new_str += 'o'
        elif i == 'Ü' or i == 'ü':
            new_str += 'u'
        else:
            new_str += i
    return new_str


first = replace_accented_letters(str(input("Enter first name: ").lower()))

last = replace_accented_letters(str(input("Enter last name: ").lower()))

name = '.'.join([first, last])

print(name)
