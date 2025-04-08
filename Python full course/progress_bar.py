# Tkinter is a Python binding to the Tk GUI toolkit.

from tkinter import *
from tkinter.ttk import *


def start(bar: Progressbar, percent: StringVar, count: int = 0, tasks: int = 100) -> None:

    if count < tasks:
        # increase items
        bar['value'] += (100 / tasks)
        count += 1
        percent.set(f"Progress: {int((count / tasks) * 100)}%")
        # after
        bar.after(100, start, bar, percent, count, tasks)


def main() -> None:

    window = Tk()

    percent = StringVar()

    progress_bar = Progressbar(
        window,
        orient=HORIZONTAL,
        length=300
    )
    progress_bar.pack(padx=20, pady=10)

    percent_label = Label(
        window,
        textvariable=percent
    )
    percent_label.pack()

    button = Button(
        window,
        text="download",
        command=lambda: start(progress_bar, percent)
    )
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()

