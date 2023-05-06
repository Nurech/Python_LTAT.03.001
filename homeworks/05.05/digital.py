DIGIT_GRIDS = {
    '0': (' -- ', '|  |', '    ', '|  |', ' -- '),
    '1': ('    ', '   |', '    ', '   |', '    '),
    '2': (' -- ', '   |', ' -- ', '|   ', ' -- '),
    '3': (' -- ', '   |', ' -- ', '   |', ' -- '),
    '4': ('    ', '|  |', ' -- ', '   |', '    '),
    '5': (' -- ', '|   ', ' -- ', '   |', ' -- '),
    '6': (' -- ', '|   ', ' -- ', '|  |', ' -- '),
    '7': (' -- ', '   |', '    ', '   |', '    '),
    '8': (' -- ', '|  |', ' -- ', '|  |', ' -- '),
    '9': (' -- ', '|  |', ' -- ', '   |', ' -- '),
}

#
# --
#   |
#   |
#  --
# |
# |
#  --
#
#
#
# -
#  |
# -
# |
#  -
#
#
def resize_grid(grid, size):
    resized_grid = []
    for row in grid:
        if ' ' in row:
            resized_grid.append(row.replace(' ', ' ' * size))
        elif '|' in row:
            resized_grid.extend([row.replace('|', '|' * size)] * size)
        else:
            resized_grid.append(row.replace('-', '-' * size))
    return resized_grid

def display_number(number, size):
    number_str = str(number)
    digit_grids = [resize_grid(DIGIT_GRIDS[digit], size) for digit in number_str]
    for row in range(len(digit_grids[0])):
        line = ''
        for digit_grid in digit_grids:
            line += digit_grid[row] + ' ' * size
        print(line[:-size])

def main():
    # number = int(input('Enter number: '))
    number = int(1234)
    # size = int(input('Enter size: '))
    size = int(2)
    display_number(number, size)

if __name__ == '__main__':
    main()
