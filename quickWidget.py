#!/usr/bin/python
import tkinter as tk
import os
root=tk.Tk()
frame = tk.Frame(root)
frame.pack()

tasks={
	"open firefox":"firefox&",
	"open Terminal":"exo-open --launch TerminalEmulator",
	"PDF Viewer":"qpdfview --unique&",
	"Open File Manager":"thunar $HOME&",
	"Show sensors":'xfce4-sensors&',
	"Open Coursera":'firefox coursera.org&',
	"open INFYTQ":'firefox https://infytq.infosys.com/home&',
	"Open Gmail":'firefox gmail.com&', 
	"Open Twitter":'firefox twitter.com&', 
	"Read Latest News":'firefox eenadu.net&', 
	"Open Sublime":'/opt/sublime_text/sublime_text&',
	"Kill Firefox":"killall -9 firefox&",
	"Music":"audacious",
	"Reboot":"reboot"
	}
#commands=['firefox', 'thunar $HOME','sensors','firefox coursera.org&','firefox gmail.com&','firefox twitter.com', 'firefox eenadu.net','/opt/sublime_text/sublime_text','quit']

for task,cmd in tasks.items():
	slogan = tk.Button(frame,text=task,command=lambda cmd=cmd: os.system(cmd))
	#slogan.pack(side=tk.TOP)
	slogan.grid(columnspan=4)
	#print(task,cmd)
print(os.system("figlet -f slant QuickWidget"))
print("Made with love by shanmukha vishnu")
root.mainloop()

#https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments