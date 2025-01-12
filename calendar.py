from tkinter import *
from tkinter import font

import calendar

gui = Tk()
gui.geometry("600x500")
gui.title("CALENDAR")
gui.config(background="light blue")
print(font.families())
title = Label(gui,text = "CALENDAR", bg = "bisque", fg = "gray0", font=("Songti TC",28,'bold'))
title.place(x= 230, y=25)

title2 = Label(gui,text = "Enter The Year", bg = "bisque", fg = "gray0", font=("Songti TC",28,'bold'))
title2.place(x= 218, y=100)

year_entry = Entry(gui,bg="bisque", fg= "gray0", font=("Songti TC",16))
year_entry.place(x=215, y=175)
gui.mainloop()