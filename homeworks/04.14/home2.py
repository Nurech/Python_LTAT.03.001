def children_with_parents(names_file, children_file):
    file_names = open(names_file, 'r')
    file_codes = open(children_file, 'r')
    lines_codes = file_codes.readlines()
    lines_names = file_names.readlines()

    id_to_name = {}
    child_to_parents = {}

    for line in lines_names:
        line_parts = line.strip().split(' ')
        id_to_name[line_parts[0]] = line_parts[1] + ' ' + line_parts[2]

    for line in lines_codes:
        line_parts = line.strip().split(' ')
        parent_id, child_id = line_parts

        parent_name = id_to_name[parent_id]
        child_name = id_to_name[child_id]

        if child_name in child_to_parents:
            child_to_parents[child_name].add(parent_name)
        else:
            child_to_parents[child_name] = {parent_name}

    return child_to_parents


def main():
    result = children_with_parents("names.txt", "children.txt")
    for child, parents in result.items():
        print(f"{child}: {', '.join(parents)}")


main()
