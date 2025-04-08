from tkinter import *


def drag_start(event) -> None:
    """ Get the coordinates of where I clicked in the widget """

    # get the widget of the event I'm dealing with
    widget = event.widget
    # create attributes for its coordinates
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event) -> None:
    """ Move the widget """

    # get the widget of the event I'm dealing with
    widget = event.widget
    # get and set its new position
    x_pos = widget.winfo_x() - widget.startX + event.x
    y_pos = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x_pos, y=y_pos)


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

