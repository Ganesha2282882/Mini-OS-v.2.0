# Normal

import time as t
import tkinter as tk
import os


def clear():
    os.system("clear")

print("Starting up . . .")
t.sleep(15)
clear()
print("Login")

un = input("Username: ")
pw = input("Password: ")
clear()

print("Hi,", un + "!")
apps = ["Exit", "Calc", "GUI", "Timer", "WWW"]
print("Here are your apps", un+ "!")
print("Type each app name to go to a app:", apps)

sela = input()

if sela == "Exit":
    quit()

elif sela == "Calc":
    x = input("Enter a math equation:\n")

    print(x)

elif sela == "GUI":
    blankgui = tk.Tk()

elif sela == "Timer":
    secs = int(input("How long is your timer (in secs)?\n"))

    for x in range(secs):
        print(x, "Seconds Left!")
        t.sleep(1)
        clear()
elif sela == "WWW":
    os.system("python3 Www.py")
