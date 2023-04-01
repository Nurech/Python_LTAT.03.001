# Open the input and output files
with open("corncob_caps.txt", "r") as input_file, open("words.txt", "w") as output_file:
    # Read each line from the input file and format as a Python string
    words = [f'"{line.strip()}"' for line in input_file]
    # Write the formatted words to the output file as a Python list
    output_file.write("[" + ", ".join(words) + "]")
