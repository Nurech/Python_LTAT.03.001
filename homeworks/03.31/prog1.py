#results = #input("Enter the name of the data file:" or "grades.txt")
grade = 4#input("Enter grade:" or 4)
classes = 12#int(input("Enter the number of classes:"))
#grades = open("grades.txt", "r")

name = ""
grade1 = 0
classes_taken = 0
students = []

lines = open("grades.txt").read().splitlines()

i = 0
for line in lines:
    i = i + 1
    
    if i % 1 == 0 and name == "":
        name = line
        #print(name)
        
        
    if i % 2 == 0:
        grade1 = round(float(line))
        #print(grade1)
        
    if i % 3 == 0:
        classes_taken = int(line)
        #print(classes_taken)
        students.append(f"{name} {grade1} {classes_taken}")
        print(students)
        #print(name + " " + str(grade))
        i = 0
        name = ""
        #grade1 = 0
        #classes_taken = 0
             
       
    
for student in students:
    name = student.split(" ")[0]
    grade = student.split(" ")[1]
    classes2 = student.split(" ")[2]
    if int(classes2) >= int(classes):
        print("Students with a grade of" + grade + "who attended at least "+classes2+" classes:")
    print(student)
    
with open("students.txt", "w") as file:
    num = 0
    avg = 0
    for student in students:
        name = student.split(" ")[0]
        grade = student.split(" ")[1]
        classes2 = student.split(" ")[2]
        avg = avg + float(grade) / 2
        num += 1
        
        
    file.write("There are "+ str(num) +" students in the class, their average grade is " + str(avg) +".")
    if int(num) > 0:
        file.write("\n")
        file.write(str(num)+" students were found.")
    elif int(num) == 0:
        file.write("\n")
        file.write("No students were found.")