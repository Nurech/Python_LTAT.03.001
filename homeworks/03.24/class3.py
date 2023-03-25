# Get heights of boys and girls
boys_heights = input("Enter the boys' heights: ")
girls_heights = input("Enter the girls' heights: ")

# Split the inputs into lists
boys_heights = boys_heights.split()
girls_heights = girls_heights.split()

# Sort the lists in descending order
boys_heights.sort(reverse=True)
girls_heights.sort(reverse=True)

# Zip the lists together and print the pairs
dance_pairs = zip(boys_heights, girls_heights)
print("Dance pairs are: ", end="")
for pair in dance_pairs:
    print(pair, end=" ")
print()

# Check if there are boys or girls left without a partner
if len(boys_heights) > len(girls_heights):
    print("Boys with heights of", end=" ")
    for height in boys_heights[len(girls_heights):]:
        print(height, end=", ")
    print("were left without a partner.")
elif len(girls_heights) > len(boys_heights):
    print("Girls with heights of", end=" ")
    for height in girls_heights[len(boys_heights):]:
        print(height, end=", ")
    print("were left without a partner.")
