#!/usr/bin/python
import tkinter as tk
import os
root=tk.Tk()
frame = tk.Frame(root)
frame.pack()

tasks={
	"open firefox":"firefox&",
	"Open File Manager":'thunar $HOME&',
	"Show sensors":'xfce4-sensors&',
	"Open Coursera":'firefox coursera.org&',
	"Open Gmail":'firefox gmail.com&', 
	"Open Twitter":'firefox twitter.com&', 
	"Read Latest News":'firefox eenadu.net&', 
	"Open Sublime":'/opt/sublime_text/sublime_text&',
	"Kill Firefox":"killall -9 firefox&"
	}
#commands=['firefox', 'thunar $HOME','sensors','firefox coursera.org&','firefox gmail.com&','firefox twitter.com', 'firefox eenadu.net','/opt/sublime_text/sublime_text','quit']

for task,cmd in tasks.items():
	slogan = tk.Button(frame,text=task,command=lambda cmd=cmd: os.system(cmd))
	#slogan.pack(side=tk.TOP)
	slogan.grid(columnspan=4)
	print(task,cmd)
root.mainloop()

#https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments