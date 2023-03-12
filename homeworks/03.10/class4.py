# 4. Longest word
# (1/2) Here, you can find a list of English words. Download either the full list or the alphabetic list.
#
# Write a program that finds the longest word among the words in the file, all letters of which are different.
#
# Hint. For example, you can define a function that checks whether all letters in a given word are different. One way to do this is to
# check that each letter in a word occurs exactly once.


# https://en.wikipedia.org/w/index.php?title=Seven-segment_display&oldformat=true#Letters
# Defining a function to check if a given word consists of only characters that can be displayed on a 7-segment digital display
def check7Segment(word):
    validLetters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'N', 'P', 'U', 'b', 'c',
                    'd', 'h', 'i', 'l', 'n', 'o', 'Q', 'r', 'y', 'u', 'y']
    for letter in word:
        if letter not in validLetters:
            return False
    return True

def find_longest_word(file):
    # Open the file and read the contents
    with open(file, 'r') as f:
        words = f.read().splitlines()

    # Set longest word variable to an empty string
    longest_word = ""

    # Iterate through each word
    for word in words:
        # Check if all letters in the word are different
        # Update longest_word if the length of the current word is greater than the longest_word
        if len(word) > len(longest_word):
            # will create a set of distinct characters
            if len(word) == len(set(word)):
                if check7Segment(word):
                    longest_word = word
                    print(word)


    # Return the longest word
    return longest_word


# Test
print(find_longest_word('words.txt'))



