import tkinter as tk
import os
root=tk.Tk()
frame = tk.Frame(root)
frame.pack()

tasks={"open firefox":"firefox&","Open File Manager":'thunar $HOME&',"Show sensors":'sensors&',"Open Coursera":'firefox coursera.org&',"Open Gmail":'firefox gmail.com&', "Open Twitter":'firefox twitter.com&', "Read Latest News":'firefox eenadu.net&', "Open Sublime":'/opt/sublime_text/sublime_text&',"EXIT":"exit&"}
#commands=['firefox', 'thunar $HOME','sensors','firefox coursera.org&','firefox gmail.com&','firefox twitter.com', 'firefox eenadu.net','/opt/sublime_text/sublime_text','quit']

for task,cmd in tasks.items():
	slogan = tk.Button(frame,text=task,command=lambda cmd=cmd: os.system(cmd))
	slogan.pack(side=tk.TOP)
	print(task,cmd)
root.mainloop()
