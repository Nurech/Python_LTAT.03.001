# (1/3) Write a function that takes a filename as its argument and returns file size in bytes if the file exists in the system,
# or 0 if it doesn't or it is actually a folder.
#
# Hint: use Python module os.path.
#
# >>> file_size("horrorstory.txt")
# 37065
# >>> file_size("mypasswords.lst")
# 0

import os.path


def file(filename):
    if os.path.isfile(filename):
        return os.path.getsize(filename) / 1024
    else:
        return 0


dir = 'class2.py'
print('Your file size is ', file(dir), ' Kb')
