with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())


lines = ["line1", "line2", "line3"]

with open("file.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")


my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

for key, value in my_dict.items():
    print(f"{key}: {value}")


import json

with open("file.json", "r") as f:
    data = json.load(f)

print(data)


import json

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

with open("file.json", "w") as f:
    json.dump(my_dict, f, indent=2)


squares = [x ** 2 for x in range(10)]
print(squares)


my_list = ["a", "b", "c", "d"]

for index, value in enumerate(my_list):
    print(f"{index}: {value}")
