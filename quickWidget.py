#!/usr/bin/python
from tkinter import *
import os
root=Tk()
root.geometry("200x500")
frame = Frame(root)
frame.pack()


leftframe = Frame(root,bd = 9, bg = "blue", cursor = "arrow")
leftframe.pack(side=TOP)

label = Label(frame, text = "A script by Shanmukha Vishnu(iam-shanmukha)")
label.pack()

tasks={
	"open firefox":"firefox&",
	"open Terminal":"exo-open --launch TerminalEmulator",
	"PDF Viewer":"qpdfview --unique&",
	"Open File Manager":"thunar $HOME&",
	"Show sensors":'xfce4-sensors&',
	"Open Coursera":'firefox coursera.org&',
	"open INFYTQ":'firefox https://infytq.infosys.com/home&',
	"Open Gmail":'firefox gmail.com&', 
	"Open twitter":'firefox twitter.com&', 
	"Read Latest News":'firefox eenadu.net&', 
	"Open Sublime":'/opt/sublime_text/sublime_text&',
	"Kill Firefox":"killall -9 firefox&",
	"Music":"audacious",
	"Reboot":"reboot"
	}
#commands=['firefox', 'thunar $HOME','sensors','firefox coursera.org&','firefox gmail.com&','firefox twitter.com', 'firefox eenadu.net','/opt/sublime_text/sublime_text','quit']

for task,cmd in tasks.items():
	buttons = Button(leftframe, text = task, command=lambda cmd=cmd: os.system(cmd))
	buttons.pack(padx =10, pady=5)
	#slogan = tk.Button(frame,text=task,command=lambda cmd=cmd: os.system(cmd))
	#slogan.pack(side="right")
	#slogan.pack(expand=1)
	#slogan.grid(columnspan=4)
	#print(task,cmd)
print(os.system("figlet -f slant QuickWidget"))
print("Made with love by shanmukha vishnu")
root.mainloop()

#https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments