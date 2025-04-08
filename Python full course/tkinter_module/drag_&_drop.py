from tkinter import *


def drag_start(event) -> None:
    # get the widget of the event I'm dealing with
    widget = event.widget
    # create variables for its position
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event) -> None:
    # get the widget of the event I'm dealing with
    widget = event.widget
    # get and set the new position
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


window = Tk()
window.geometry('300x300')

# Label1
label1 = Label(window, bg='red', width=10, height=5)
label1.place(x=0, y=0)
label1.bind('<Button-1>', drag_start)
label1.bind('<B1-Motion>', drag_motion)

# Label2
label2 = Label(window, bg='blue', width=10, height=5)
label2.place(x=100, y=100)
label2.bind('<Button-1>', drag_start)
label2.bind('<B1-Motion>', drag_motion)


def main() -> None:
    window.mainloop()


if __name__ == '__main__':
    main()

