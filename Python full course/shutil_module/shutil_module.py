# Using the shutil module, there are three ways to copy a file:
#   - copyfile() copies the contents of a file
#   - copy() is copyfile() + permission mode + destination can be a directory
#   - copy2() is copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', 'other.txt')
