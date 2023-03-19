# Write a function removezeros that does the following.
#
# The function has one parameter – list of integers.
# The function finds all sublists (i.e. ranges of consecutive elements), which have zero as the sum of their elements,
# and removes such sublists from the list. The sublists may overlap with each other.
# The function doesn't return anything, it only changes the given list.
# Example 1
# >>> a = [10, 5, -3, -3, 1, 4, -4]
# >>> removezeros(a)
# >>> a
# [10]
#
# Explanation. The sum of elements in the sublist [5, -3, -3, 1] is zero, so this sublist is removed. Also the sum of elements in the
# sublist [4, -4] is zero, therefore this sublist is removed as well. Only the integer 10 remains in the list.
#
# Example 2
# >>> b = [7, 2, 2, -1, -3, 1, 2, 1, 5]
# >>> removezeros(b)
# >>> b
# [7, 5]
#
# Explanation. The list contains two sublists with the sum zero: [2, 2, -1, -3] and [-1, -3, 1, 2, 1].
# Both are removed and only the numbers 7 and 5 remain.
#
# To check your program with the autotester, submit it with the name removezeros.py.

input_list = [1, 2, 3, -1, 3, -2, -5, 3]


def removezeros(input_list):

    all_subsets = []

    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)+1):
            all_subsets.append(input_list[i:j])

    print(all_subsets)

    for set in all_subsets:
        if sum(set) == 0:
            for x in set:
                if x in input_list:
                    input_list.remove(x)


    print(input_list)
    return input_list


removezeros(input_list)
