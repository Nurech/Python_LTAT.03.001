def dictionary(filename):
    codes = {}
    with open(filename, 'r') as file:
        for line in file:
            code, country = line.strip().split(' ')
            codes[code] = country
    return codes


def name_code(filename, country):
    names = []
    with open(filename, 'r') as file:
        for l in file:
            code = l.strip()
            if code in country:
                names.append(country[code])
            else:
                names.append("Unknown")
    return names


def main():
    country_file = input("Enter country file name: ") or "countries.txt"
    crossings_file = input("Enter border crossings file name: ") or "crossings.txt"

    country_dict = dictionary(country_file)
    country_names = name_code(crossings_file, country_dict)

    for name in country_names:
        print(name)


main()
