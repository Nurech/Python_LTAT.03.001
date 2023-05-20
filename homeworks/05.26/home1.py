import re

with open('addresses.txt', 'r') as file:
    data = file.read().splitlines()

username_pattern = re.compile(r'http[s]?://www\.ut\.ee/~(\w+)/')

for line in data:
    match = username_pattern.search(line)
    if match:
        print(match.group(1))
