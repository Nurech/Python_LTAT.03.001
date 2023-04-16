def find_spreaders(data):
    spreaders = set(data) - {0}
    return sorted(spreaders)


def find_vectors(data):
    vectors = set()
    for i in range(len(data) - 1):
        if data[i] != 0 and data[i+1] != 0:
            vectors.add(data[i])
    return vectors


def find_origins(data, vectors):
    origins = set()
    for person in set(data) - {0}:
        if person not in vectors:
            origins.add(person)
    return sorted(origins)

# data = [6, 7, 0, 0, 6, 7, 0, 0, 2, 3]
data = [16, 51, 27, 42, 22, 0, 0, 0,
        3, 44, 0, 39, 42, 10, 25,
        38, 0, 33, 29, 0, 0, 3, 0,
        19, 24, 0, 39, 0, 33, 13, 6,
        0, 6, 0, 0, 0, 38, 31, 31,
        0, 10, 10, 0, 6, 51, 0, 0,
        0, 0, 0, 33, 0, 33, 10, 0]

spreaders = find_spreaders(data)
print(spreaders)
vectors = find_vectors(data)
print(vectors)
origins = find_origins(data, vectors)

print(f"Spreaders of infection are: {' '.join(map(str, spreaders))}")
print(f"Vectors of infection are: {' '.join(map(str, vectors))}")
print(f"Origins of infection are: {' '.join(map(str, origins))}")
