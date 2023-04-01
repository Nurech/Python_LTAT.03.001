init_pos = [[1, 2, 3, 4], [5, 6, 7, 8]]
pos = [[6, 8, 4, 5], [2, 7, 3, 1]]


def A():
    temp1 = [pos[0][3], pos[0][0], pos[0][1], pos[0][2]]
    temp2 = [pos[1][3], pos[1][0], pos[1][1], pos[1][2]]
    pos[0] = temp1
    pos[1] = temp2


def B():
    temp1 = [pos[1][0], pos[1][1], pos[1][2], pos[1][3]]
    temp2 = [pos[0][0], pos[0][1], pos[0][2], pos[0][3]]
    pos[0] = temp1
    pos[1] = temp2


def C():
    temp1 = [pos[0][0], pos[0][2], pos[1][2], pos[0][3]]
    temp2 = [pos[1][0], pos[0][1], pos[1][1], pos[1][3]]
    pos[0] = temp1
    pos[1] = temp2


# C()
# print(pos)

# print("The position is")


while init_pos != pos:
    for i in pos:
        print(f"     {i[0]} {i[1]} {i[2]} {i[3]}")
    choice = str(input("Your move:"))
    if choice == "A":
        A()
    elif choice == "B":
        B()
    elif choice == "C":
        C()
print("Puzzle is solved!")
