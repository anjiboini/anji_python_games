from tkinter import *

def doNothing():
    print("ok ok i wont............")

root=Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="Open", command=doNothing)
subMenu.add_command(label="Save", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

edit = Menu(menu)
menu.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undu", command=doNothing)
edit.add_command(label="Redo", command=doNothing)
edit.add_command(label="Cut", command=doNothing)
edit.add_separator()
edit.add_command(label="Paste", command=doNothing)

view = Menu(menu)
menu.add_cascade(label="View", menu=view)
view.add_command(label="Tool Window", command=doNothing)
view.add_command(label="Appearence", command=doNothing)
view.add_command(label="Active Editor", command=doNothing)
view.add_separator()
view.add_command(label="Scientific Mode", command=doNothing)

navigate = Menu(menu)
menu.add_cascade(label="Navigate", menu=navigate)
navigate.add_command(label="File Path", command=doNothing)

code = Menu(menu)
menu.add_cascade(label="Code", menu=code)
code.add_command(label="Generate", command=doNothing)

refactor = Menu(menu)
menu.add_cascade(label="Refactor", menu=refactor)
refactor.add_command(label="Move File", command=doNothing)

run = Menu(menu)
menu.add_cascade(label="Run", menu=run)
run.add_command(label="Debug", command=doNothing)

tools = Menu(menu)
menu.add_cascade(label="Tools", menu=tools)
tools.add_command(label="XML", command=doNothing)

vcs = Menu(menu)
menu.add_cascade(label="VCS", menu=vcs)
vcs.add_command(label="Apply Patch", command=doNothing)

window = Menu(menu)
menu.add_cascade(label="Window", menu=window)
window.add_command(label="Editor Tabs", command=doNothing)

help = Menu(menu)
menu.add_cascade(label="Help", menu=help)
help.add_command(label="Getting Started", command=doNothing)

#......the Toolbar.....

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Inser Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2,pady=2)
printButt = Button(toolbar, text="Print", command=doNothing )
printButt.pack(side=LEFT, padx=2,pady=2)

toolbar.pack(side=TOP, fill=X)
root.mainloop()
