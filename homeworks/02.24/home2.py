# Emma wants to cook raspberry jam. She has two kinds of jars, with a capacity of 5 liters and 1 liter.
# Emma has a habit of using up all the biggest jars first and then going to the smaller ones. For example,
# if she needs to make 8 liters of raspberry jam, she would first take one large jar and then three small jars.
# If the planned amount of jam does not exactly fit in the jars, Emma will not cook the jam.
#
# Write a function jam that takes three integer values as arguments:
#
# number of large jars;
# number of small jars;
# amount of jam in liters.
# The function returns the number of jars that Emma uses to make jam.
# If the amount of jam does not fit exactly in the jars, the function returns -1.
#
# Example
#
# >>> jam(2, 6, 14)
# 6
# >>> jam(3, 3, 8)
# 4
# >>> jam(1, 2, 10)
# -1
# >>> jam(5, 1, 9)
# -1

nr_of_jars = -1


def jam(nr_large, nr_small, liters_jam):
    large_liter = 5
    small_liter = 1
    nr_of_jars = -1

    if liters_jam == 0:
        return 0
    for lg_jar in range(nr_large,-1,-1):
        for small_jar in range(nr_small,-1,-1):
            if (lg_jar == 0 and small_jar == 0):
                nr_of_jars = -1
                return nr_of_jars
            elif ((lg_jar * large_liter) + (small_jar * small_liter) ) == liters_jam:
                nr_of_jars = small_jar + lg_jar
                return nr_of_jars

    return nr_of_jars
