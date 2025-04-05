import os

source = ("C:\\Users\\windows\\Desktop\\Programming projects\\"
          "Bro-Code-tutorials\\Python full course\\os_module\\test.txt")

destination = "C:\\Users\\windows\\Desktop\\moved_file.txt"

try:

    if os.path.exists(destination):
        print("There is already a file there!")

    else:
        os.replace(destination, source)
        print('File was moved.')

except FileNotFoundError:
    print('File was not found!')

# I can also move a directory
