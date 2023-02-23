score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Score must be in the range of 0-100")

else:
    grading_type = input("Is the grading differentiated or non-differentiated (d/n)? ")
    try:
        if grading_type == "d":
            if score >= 90:
                print("A")
            elif score >= 80:
                print("B")
            elif score >= 70:
                print("C")
            elif score >= 60:
                print("D")
            elif score >= 50:
                print("E")
            else:
                print("F")
        elif grading_type == "n":
            if score >= 50:
                print("PASSED")
            else:
                print("FAILED")
        else:
            print("Grading type not recognized")
    except ValueError:
        print("Grading type not recognized")
