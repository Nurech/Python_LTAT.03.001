def find_length(maze):
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    queue = [(start, 0)]  # Start counting the length from 0, not 1

    maze[0][1] = '#'

    while queue:
        (x, y), length = queue.pop(0)

        # check all moves
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            # if is end
            if (nx, ny) == end:
                return length + 1
            # if valid pos
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == ' ':
                queue.append(((nx, ny), length + 1))
                # check
                maze[nx][ny] = '#'
    return -1


# I used BFS to find the shortest path
# https://favtutor.com/blogs/breadth-first-search-python

# m = [['#', 'a', '#', '#', '#', '#', '#', '#', '#'],
#      ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#      ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
#      ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
#      ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
#      ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
#      ['#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
#      ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
#      ['#', '#', '#', '#', '#', '#', '#', 'b', '#']]
#
# print(find_length(m))
