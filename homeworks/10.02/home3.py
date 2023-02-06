name = str(input("Enter your name: "))
shoe_size = float(input("Enter your foot length (cm): "))

shoe_size = round(1.5 * shoe_size + 2)

print("Dear " + name, " your shoe size is " + str(shoe_size) + ".")
