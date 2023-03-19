
file_to_open = 'films.txt'

def list_films(genre):
    films = []
    with open(file_to_open, 'r') as f:
        for line in f:
            if line:
                line = line.strip()
                parts = line.split(' - ')
                if len(parts) == 2:
                    name, film_genre = parts
                    if film_genre == genre:
                        films.append(name)
    return films



def add_film(name, genre):
    with open(file_to_open, 'a+') as f:
        f.write(name + ' - ' + genre + '\n')



def delete_film(name):
    with open(file_to_open, 'r+') as f:
        lines = f.readlines()
    with open(file_to_open, 'w') as f:
        for line in lines:
            line = line.strip()
            film_name, film_genre = line.split(' - ')
            if film_name != name:
                f.write(line + '\n')


print(list_films("music"))
