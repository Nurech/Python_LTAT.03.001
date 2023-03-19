import film

def process_command(command, args):
    if command == 'D':
        print('Possible films are:')
        films = film.list_films(args)
        for x in films:
            print(x)
        return True

    elif command == 'A':
        # Call the add_film function from the film module
        name = args[args.index(" ")+1:len(args)]
        genre = args.split(" ")[0]
        parts = [name, genre]
        if len(parts) == 2:
            film.add_film(name, genre)
            print('Film added!')
            return True

    elif command == 'W':
        print('deleting:', args)
        film.delete_film(args)
        print('Film deleted from the database! Happy viewing!')
        return True
    else:
        print('Invalid command!')
        return True

# The main program

print('=== FILM DATABASE ===')
print('Display films: D <genre>')
print('Add film: A <genre> <film name>')
print('Watch film: W <film name>')
print('Exit: E')
print('===')

while True:
    command = input('> ')

    if command[0] in ['D', 'A', 'W'] and len(command) > 1:
        should_continue = process_command(command[0], command[2:len(command)])
        if not should_continue:
            break
    elif command[0] == 'E':
        break
    else:
        print('Invalid command!')

