from tkinter import *
import sys


def greet(event):
    """ I have to set one parameter to be used with the .bind()
    method. """

    print("Hello!")


def display_key(event):
    label.config(text=f"{event.keysym}")


def program_quit(event):
    sys.exit()


# Create window
window = Tk()
window.geometry('300x300')

# Create label
label = Label(window, font=("Helvetica", 100))
label.pack(padx=100, pady=90)

# Bind functions to keyboard events
window.bind('<Return>', greet)
window.bind('<q>', program_quit)
# respond to all keys (except those already taken before)
window.bind('<Key>', display_key)


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
