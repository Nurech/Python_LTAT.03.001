# Ask the user for the type of analysis and the result file
filename = input("Enter file name: ") or "example.html"
type_of_analysis = input("Extract tags or text: ") or 'text'
result_file = input("Save the result to the file: ") or 'example-tags.txt'
# filename = "example.html"
# type_of_analysis = 'text'
# result_file = 'example-tags.txt'


# Open the file in read mode
with open(filename, "r") as file:
    output = []

    for line in file:
        if type_of_analysis == "tags":
            start_index = line.find("<")
            end_index = line.find(">")
            while start_index != -1 and end_index != -1:
                tag = line[start_index:end_index + 1]
                output.append(tag)
                start_index = line.find("<", end_index + 1)
                end_index = line.find(">", start_index + 1)

        elif type_of_analysis == "text":
            while '<' in line or '>' in line:
                i = line.find('<')
                j = line.find('>') +1
                match = line[i:j]
                line = line.replace(match, '|')
            string_list = line.split("|")
            print(string_list)
            for str in string_list:
                str = str.strip()
                if str != '\n' or str != '':
                    output.append(str)

list_without_empty_strings = [x for x in output if x]

with open(result_file, "w") as file:
    for item in list_without_empty_strings:
        file.write(item + "\n")
