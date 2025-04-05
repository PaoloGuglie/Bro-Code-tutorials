import os

try:
    os.remove('to_remove.txt')

except FileNotFoundError:
    print("The file was not found!")

except PermissionError:
    print("You do not have permission to delete this file!")

else:
    print("File was deleted!")


# To delete an empty folder:
os.rmdir('file...')
