# Ask the user for the type of analysis and the result file
filename = input("Enter file name: ") or "example.html"
type_of_analysis = input("Extract tags or text: ") or 'text'
result_file = input("Save the result to the file: ") or 'example-tags.txt'

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
            start_index = line.find(">")
            end_index = line.find("<", start_index + 1)
            while start_index != -1 and end_index != -1:
                text = line[start_index + 1:end_index]
                if text.strip() != "":
                    output.append(text.strip())
                start_index = line.find(">", end_index + 1)
                end_index = line.find("<", start_index + 1)

with open(result_file, "w") as file:
    for item in output:
        file.write(item + "\n")

# Print a success message
print("Saved!")
