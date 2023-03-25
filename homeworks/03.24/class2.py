# open the files for reading
f1 = open("registration_data.txt", "r")
f2 = open("running_results.txt", "r")

registration_data = f1.readlines()
running_results = f2.readlines()

f1.close()
f2.close()

registration_dict = {}
for line in registration_data:
    registration_number, name = line.split()
    registration_dict[registration_number] = name

sorted_results = sorted(running_results, key=lambda x: registration_dict.get(x.strip(), 0))
sorted_results = [int(x.strip('\n')) for x in sorted_results]


print(sorted_results)
for result in sorted_results:
    print(result)

print(registration_dict)
try:
    with open('third_file.txt', 'w') as f:
        for x in sorted_results:
            f.write(str(x)+ ". "+registration_dict.get(str(x)+ ".")+"\n")

except FileNotFoundError:
    print("err")
