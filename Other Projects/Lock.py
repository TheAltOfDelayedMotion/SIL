import psutil
from tkinter import *
import tkinter.messagebox as box
import os
import datetime
import subprocess
import win32gui, win32con

#Discord.exe
f = open("attemptlogs.txt","a")
now = datetime.datetime.now()
filepath = r"C:\Users\delay\AppData\Local\Discord\app-1.0.9003\Discord.exe"

pythonprogram = win32gui.GetForegroundWindow()
win32gui.ShowWindow(pythonprogram , win32con.SW_HIDE)

def ifDiscordRunning():
    while True:
        program = "Discord.exe"
        if program in (p.name() for p in psutil.process_iter()):
            #print("Running")
            break


def main():
    ifDiscordRunning()

    def dialog1():
        username = entry1.get()
        password = entry2.get()
        if (username == 'admin' and password == 'wetmoplovesdelayed'):
            box.showinfo('Login successful', 'Welcome back, DelayedMotion, please proceed')
            window.destroy()
            f.write("Successful login on: " + (now.strftime("%Y-%m-%d %H:%M:%S")) + "\n")
            f.close()
            subprocess.Popen([filepath])
            win32gui.ShowWindow(pythonprogram, win32con.SW_SHOW)


        else:
            box.showinfo('Login unsuccessful', 'Password or User is incorrect, successfully logged.')
            os.system("taskkill /f /im  Discord.exe")
            f.write("Unsuccessful login on: " + (now.strftime("%Y-%m-%d %H:%M:%S")) + "\n")


    window = Tk()
    window.title('Discord Verification')

    frame = Frame(window)

    Label1 = Label(window, text='Username:')
    Label1.pack(padx=15, pady=5)

    entry1 = Entry(window, bd=5)
    entry1.pack(padx=15, pady=5)

    Label2 = Label(window, text='Password: ')
    Label2.pack(padx=15, pady=6)

    entry2 = Entry(window, bd=5)
    entry2.pack(padx=15, pady=7)

    btn = Button(frame, text='Check Login', command=dialog1)

    btn.pack(side=RIGHT, padx=5)
    frame.pack(padx=100, pady=19)
    window.attributes('-fullscreen', True)
    window.overrideredirect(1)
    window.attributes('-topmost', True)
    window.mainloop()


main()