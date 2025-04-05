import os

path = "C:\\Users\\windows\\Desktop\\Programming projects\\Bro-Code-tutorials\\Python full course\\info.txt"

if os.path.exists(path):

    print("This path exists!")

    if os.path.isfile(path): print("That is a file!")

    elif os.path.isdir(path): print("That is a directory!")

    else: print("Idk what this is!")

else: print("No such path exists!")
