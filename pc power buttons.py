import os
from tkinter import *

root = Tk()
root.title("power butttons")
root.geometry("400x200")
root.iconbitmap('pow.ico')

#create a frame
frame = Frame(root)
frame.pack(pady=40, anchor='center')


def shutdown():
    os.system("shutdown /s")


def logoff():
    os.system("shutdown -l")

def restart():
    os.system("shutdown /r")

#insert player control button images
shutdwn_btn_img = PhotoImage(file='shutdown.png')
logoff_btn_img = PhotoImage(file='log.png')
restart_btn_img = PhotoImage(file='restart.png')

#create play controls frame
controls_frame = Frame(frame)
controls_frame.grid(row=4, column=0, pady=20)

#create player controls buttons
shutdown_button = Button(controls_frame, image=shutdwn_btn_img, borderwidth=0, command=shutdown)
logoff_button = Button(controls_frame, image=logoff_btn_img, borderwidth=0, command=logoff)
restart_button = Button(controls_frame, image=restart_btn_img, borderwidth=0, command=restart)

shutdown_button.grid(row=1, column=0)
logoff_button.grid(row=1, column=1)
restart_button.grid(row=1, column=2)

root.mainloop()
