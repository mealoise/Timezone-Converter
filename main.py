# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
import Application as a
import Timezone as t

root = Tk()
root.title("Timezone Adjuster")
root.geometry("900x300")

app = Frame(root)
app.grid()
lbl = Label(app, text="Select appropriate timezone: ")
lbl.grid()

LINT = t.Timezone("LINT", 14, 00)
CHADT = t.Timezone("CHADT", 13, 45)
NZDT = t.Timezone("NZDT", 13, 00)
ANAT = t.Timezone("ANAT", 12, 00)
AEDT = t.Timezone("AEDT", 11, 00)
ACDT = t.Timezone("ACDT", 10, 30)
AEST = t.Timezone("AEST", 10, 00)
ACST = t.Timezone("ACST", 9, 30)
JST = t.Timezone("JST", 9, 00)
ACWST = t.Timezone("ACWST", 8, 45)
CST = t.Timezone("CST", 8, 00)
WIB = t.Timezone("WIB", 7, 00)

MMT = t.Timezone("MMT", 6, 30)
BST = t.Timezone("BST", 6, 00)
NPT = t.Timezone("NPT", 5, 45)
IST = t.Timezone("IST", 5, 30)
UZT = t.Timezone("UZT", 5, 00)
AFT = t.Timezone("AFT", 4, 30)
GST = t.Timezone("GST", 4, 00)
IRST = t.Timezone("IRST", 3, 30)
MSK = t.Timezone("MSK", 3, 00)
EET = t.Timezone("EET", 2, 00)
CET = t.Timezone("CET", 1, 00)  # TBC


timezones = [LINT,
             CHADT,
             NZDT,
             ANAT,
             AEDT,
             ACDT,
             AEST,
             ACST,
             JST,
             ACWST,
             CST,
             WIB]

timezone_names = []


def add_to_name_list():
    for x in timezones:
        timezone_names.append(x.name)

if __name__ == '__main__':

    add_to_name_list()
    variable = StringVar(root)
    variable.set(timezone_names[0])
    timezone_drop = OptionMenu(root, variable, *timezone_names)
    timezone_drop.grid()

    app = a.Application(root)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
