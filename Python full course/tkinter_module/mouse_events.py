from tkinter import *


def do_something(event) -> None:
    print(f"\nMouse coordinates: ({event.x}, {event.y})")


def enter_window(event) -> None:
    print(f"\nWindow entered at coordinates: ({event.x}, {event.y})")


def leave_window(event) -> None:
    print(f"\nWindow left at coordinates: ({event.x}, {event.y})")


def move_mouse(event) -> None:
    print(f"({event.x}, {event.y})", end=" ")


window = Tk()

starting_pos = (0, 0)

# When I press / release a button
window.bind('<Button-1>', do_something)
window.bind('<ButtonRelease>', do_something)

# when I enter / leave the window with the mouse
window.bind('<Enter>', enter_window)
window.bind('<Leave>', leave_window)

# when I move the mouse
window.bind('<Motion>', move_mouse)


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()
