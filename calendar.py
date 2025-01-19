from tkinter import *
from tkinter import font

import calendar

gui = Tk()
gui.geometry("600x500")
gui.title("CALENDAR")
gui.config(background="light blue")
print(font.families())
def show_calendar():
    year=int(year_entry.get())
    newgui=Tk()
    newgui.geometry("600x500")
    newgui.title("CALENDAR")
    newgui.config(background="light blue")
    content=calendar.calendar(year)
    cal_content=Label(newgui,text=content,bg = "bisque", fg = "gray0", font=("Songti TC",28,'bold'))
    cal_content.place(x=100,y=100)

title = Label(gui,text = "CALENDAR", bg = "bisque", fg = "gray0", font=("Songti TC",28,'bold'))
title.place(x= 230, y=25)

title2 = Label(gui,text = "Enter The Year", bg = "bisque", fg = "gray0", font=("Songti TC",28,'bold'))
title2.place(x= 218, y=100)

year_entry = Entry(gui,bg="bisque", fg= "gray0", font=("Songti TC",16))
year_entry.place(x=215 ,y=175)
show = Button(gui,highlightbackground="bisque",fg="gray0",text = "show",font=("Songti TC",28),command=show_calendar)
show.place(x=265 ,y=220)
exit = Button(gui,highlightbackground="bisque",fg="gray0",text = "exit",font=("Songti TC",28))
exit.place(x=275,y=300)
gui.mainloop()
