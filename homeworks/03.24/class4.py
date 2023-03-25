string = input('Enter string: ')

depth = 0

for character in string:
    if character == '(':
        depth += 1
    elif character == ')':
        depth -= 1
        if depth < 0:
            break

if depth == 0:
    print('Brackets are balanced')
else:
    print('Brackets are not balanced')
