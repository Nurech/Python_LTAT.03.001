import random

def walk(matrix, position, direction):
    row, col = position
    if matrix[row][col] == 0:
        matrix[row][col] = 1
        direction = (direction - 1) % 4
    else:
        matrix[row][col] = 0
        direction = (direction + 1) % 4

    if direction == 0:
        row -= 1
    elif direction == 1:
        col += 1
    elif direction == 2:
        row += 1
    else:
        col -= 1

    return matrix, (row, col), direction

def ant(matrix_size, position, direction):
    matrix = [[0] * matrix_size for _ in range(matrix_size)]
    steps = 0

    while 0 <= position[0] < matrix_size and 0 <= position[1] < matrix_size:
        matrix, position, direction = walk(matrix, position, direction)
        steps += 1

    ones = sum(row.count(1) for row in matrix)
    return steps, (ones / (matrix_size * matrix_size)) * 100

def main(sim):
    # matrix_size = int(input("Enter dimension of the matrix: "))
    matrix_size = sim
    simulations = 1000
    total_steps = 0
    total_ones_percent = 0

    for _ in range(simulations):
        position = (random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1))
        direction = random.randint(0, 3)
        steps, ones_percent = ant(matrix_size, position, direction)
        total_steps += steps
        total_ones_percent += ones_percent

    avg_steps = total_steps / simulations
    avg_ones_percent = total_ones_percent / simulations

    print(f"Average number of steps is {avg_steps}")
    print(f"Average percent of ones at the end is {avg_ones_percent}")
    return([avg_steps,avg_ones_percent])

avg_step_final = 0
avg_percent_final = 0
for i in range(1, 50):
    res = main(i)
    avg_step_final = (avg_percent_final + res[0]) / 2
    avg_percent_final = (avg_percent_final + res[1]) / 2
    print(res)

print(avg_step_final)
print(avg_percent_final)








# (2/2) What do you think: approximately how fast does the average
# number of steps increase as the dimension of the matrix increases?
#
# Does the average percentage of ones left in the matrix at
# the end of the journey change as the dimension of the matrix
# increases, or does it always remain approximately the same?
