#PackAges Area
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import subprocess
from tkinter import messagebox
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
import tkinter as tk

    #Naming Area
window = Tk()
window.title("Python IDE")
menu = Menu(window)
window.config(menu=menu)
widget = ScrolledText(window, font=("Monokai"), wrap=None)
widget.pack(fill=BOTH, expand=1)
widget.focus()
widget.config(font="Euphemia",fg="black")
output_area = ScrolledText(window, height=10,width=1000)
output_area.config(font="Euphemia",fg="black")
file_path = ""
autosave_status = ""
widget.insert(1.0,"print('Hello, World!')")

    #Freaturs Area
#Auto Closing Bracket Freature Code:
matched_pairs = {"{": "}", "<": ">", "(": ")","'": "'", '"': '"', "[": "]"}
def maybe_insert_matching_pair(event):
    matching = matched_pairs.get(event.char, None)
    if matching:
        event.widget.insert("insert", matching)
        event.widget.mark_set("insert", "insert-1c")
window.bind('<KeyPress>', maybe_insert_matching_pair)
#Syntax Highlighting Freature Code:
cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F'}

cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#ad5187'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00'}
cdg.tagdefs['STRING'] = {'foreground': '#ba5960'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F'}

ip.Percolator(widget).insertfilter(cdg)
#Auto Indent Freature Code:
def autoindent(event):
    widget = event.widget
    line = widget.get("insert linestart", "insert lineend")
    match = re.match(r'^(\s+)', line)
    current_indent = len(match.group(0)) if match else 0
    new_indent = current_indent + 9
    widget.insert("insert", event.char + "\n" + " "*new_indent)
    return "break"
widget.bind(":" "<Return>", autoindent)
#Status Freature Code:
def change_word(event = None):
    global text_change
    if widget.edit_modified():
        text_change = True
        word = len(widget.get(1.0, "end-1c").split())
        chararcter = len(widget.get(1.0, "end-1c").replace(" ",""))
        lines = int(widget.index('end-1c').split('.')[0])
        status_bars.config(text = f"Made By Abdou \t\t\t\t\t\t characters: {chararcter} words: {word} lines: {lines}")
    widget.edit_modified(False)


# create a label for status bar
status_bars = ttk.Label(window,text = "Made By Abdou \t\t\t\t\t\t characters: 0    words: 0    lines: 0")
status_bars.pack(side = BOTTOM)


    #Functions Area
def new():
    global code,file_path, open_path, autosave_status
    #if file_path != "" and autosave_status == "off":
    reponse = messagebox.askyesno("HEY WAIT!!!","If This file has been modified, ALL OF it will be unsaved. Continue?")
    if reponse == 1:
        file_path = ""
        widget.delete(1.0, END)
        widget.insert(1.0,"print('Hello, World!')")
    if reponse ==2:
        pass
    pass


def open_file(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        widget.delete(1.0, END)
        widget.insert(1.0, code)
window.bind("<Control-o>", open_file)
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = widget.get(1.0, END)
        file.write(code) 
def save_as(event=None):
    global code, file_path
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = widget.get(1.0, END)
        file.write(code) 
def run(event=None):
    global code, file_path
    if file_path == "":
        reponse = messagebox.askokcancel("OOPS!!!","Please Save Your Code To Run it!")
        if reponse == 1:
        	save_file()
        	cmd = f"python {file_path}"
        	process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
        		stderr=subprocess.PIPE, shell=True)
        	output, error =  process.communicate()
        	output_area.delete(1.0, END)
        	output_area.insert(1.0, output)
        	output_area.insert(1.0, error)
        if reponse == 2:
        	pass
    elif file_path != "":
        cmd = f"python {file_path}"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
            	               	stderr=subprocess.PIPE, shell=True)
        output, error =  process.communicate()
        output_area.delete(1.0, END)
        output_area.insert(1.0, output)
        output_area.insert(1.0, error)
        
    return


def pop_menu(event):
    pop_up_menu.tk_popup(event.x_root, event.y_root)
    pass
def copy():
    widget.event_generate("<<Copy>>")
    pass
def cut():
    widget.event_generate("<<Cut>>")
    pass
def paste():
    widget.event_generate("<<Paste>>")
    pass
def select_all():
    widget.event_generate("<<SelectAll>>")
def one_dark_pro():
    widget.config(bg="#1e1e1e",fg="white")
    output_area.config(bg="#1e1e1e",fg="white")
    pass
def winter_coming():
    widget.config(bg="#001629",fg="white")
    output_area.config(bg="#001629",fg="white")
    pass
def solarized():
    widget.config(bg="#002b36",fg="white")
    output_area.config(bg="#002b36",fg="white")
    pass
def shades_purple():
    widget.config(bg="#2c2956",fg="white")
    output_area.config(bg="#2c2956",fg="white")
    pass
def save_run():
    save_file()
    run()
    pass
def save_as_run():
    save_as()
    run()
    pass
def autosave_enable():
    autosave_on()
    return()
def autosave_on():
    window.bind("<KeyPress>", autosave_code)
def autosave_code(self):
    global code, file_path, reponse
    if file_path != "":
        save_path = file_path
        with open(save_path, "w") as file:
            code = widget.get(1.0, END)
            file.write(code)
            autosave_status = "on"
    if file_path == "":
        reponse = messagebox.askokcancel("OOPS!!!","Unsaved File. Save To Continue Using Auto Save")
        if reponse == 1:
            save_as()

    return(self)
def autosave_disable():
    autosave_status = "off"
    pass
def console_enable():
    output_area.pack()
    pass
def console_disable():
    output_area.pack_forget()
    pass
def show_statusbar():
    status_bars.pack(side=BOTTOM)
    pass
def hide_statusbar():
    status_bars.pack_forget()
    pass
def about_menu_command():
	about_window = Tk()
	about_window.title("About")
	about_window.resizable(0,0)
	about_label = Label(about_window,text="Simple Ide Made For Fun :')", padx=5, pady=2 ,)
	about_exit_button = Button(about_window,text="Ok", width=10, pady=8 ,command=about_window.destroy)
	about_label.pack()
	about_exit_button.pack()
	#about_window.iconphoto(False, app_icon)
	about_window.mainloop()
	pass
def realease_notes():
	realease_notes_window = Tk()
	realease_notes_window.title("Release Notes")
	realease_notes_window.resizable(0,0)
	realease_label = Label(realease_notes_window,text="Release Notes:", padx=5, pady=2 ,)
	realease_label2 = Label(realease_notes_window,text="Current Version: 1.0v", padx=5, pady=2 ,)
	realease_label3 = Label(realease_notes_window,text="More Versions: No More Versions(This version Have all Whats u Need)", padx=5, pady=2 ,)
	release_exit_button = Button(realease_notes_window,text="Ok", width=10, pady=8 ,command=realease_notes_window.destroy)
	realease_label.pack()
	realease_label2.pack()
	realease_label3.pack()
	#realease_notes_window.iconphoto(False, app_icon)
	release_exit_button.pack()
	realease_notes_window.mainloop()
	pass
def exit():
	window.destroy()
	pass

        
    #binding Area
window.bind("<Control-o>", open_file)
window.bind("<Control-S>", save_as)
window.bind("<Control-s>", save_file)
window.bind("<Control-q>", exit)
window.bind("<F5>", run)
window.bind("<Control-n>", new)
window.bind("<Control-x>", cut)
window.bind("<Control-c>", copy)
window.bind("<Control-v>", paste)
widget.bind("<Button - 3>", pop_menu)
window.bind("<Control-a>", select_all)
widget.bind("<<Modified>>",change_word)

	#Images Area
autosave_image = PhotoImage(file="Images/autosave.png")
enabled_image = PhotoImage(file="Images/output-onlinepngtools (1).png")
console_image = PhotoImage(file="Images/output-onlinepngtools (2).png")
cut_image = PhotoImage(file="Images/output-onlinepngtools (3).png")
one_dark_theme_image = PhotoImage(file="Images/output-onlinepngtools (5).png")
open_image = PhotoImage(file="Images/output-onlinepngtools (6).png")
past_image = PhotoImage(file="Images/output-onlinepngtools (7).png")
quit_image = PhotoImage(file="Images/output-onlinepngtools (8).png")
run_image = PhotoImage(file="Images/output-onlinepngtools (9).png")
save_image = PhotoImage(file="Images/output-onlinepngtools (10).png")
saveas_image = PhotoImage(file="Images/output-onlinepngtools (11).png")
selectall_image = PhotoImage(file="Images/output-onlinepngtools (12).png")
status_image = PhotoImage(file="Images/output-onlinepngtools (14).png")
theme_image = PhotoImage(file="Images/output-onlinepngtools (16).png")
xmark_image = PhotoImage(file="Images/output-onlinepngtools (15).png")
new_image = PhotoImage(file="Images/output-onlinepngtools (4).png")
copy_image = PhotoImage(file="Images/output-onlinepngtools (20).png")
app_icon = PhotoImage(file="Images/icon.jpg")





    #Menu Bars Area
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
setting_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
about_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label="Settings",menu=setting_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
menu.add_cascade(label="About", menu=about_menu)
file_menu.add_command(label="New Project", accelerator="Ctrl+N", command=new, image=new_image, compound="left")
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file, image=open_image, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file, image=save_image, compound="left")
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as, image=saveas_image, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=exit, image=quit_image, compound="left")
run_menu.add_command(label="Run", accelerator="F5", command=run, image=run_image, compound="left")
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=cut, image=cut_image, compound="left")
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=copy, image=copy_image, compound="left")
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=paste, image=copy_image, compound="left")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",accelerator="Ctrl+A", command=select_all, image=selectall_image, compound="left")
run_menu.add_separator()
run_menu.add_command(label="Save And Run", accelerator="Ctrl+Shift+S", command=save_run, image=run_image, compound="left")
run_menu.add_command(label="Save As And Run", accelerator="Ctrl+Shift+A+S", command=save_as_run, image=run_image, compound="left")
theme_menu.add_radiobutton(label="One Dark Pro", command=one_dark_pro, image=theme_image, compound="left")
theme_menu.add_radiobutton(label="Solarized", command=solarized, image=theme_image, compound="left")
theme_menu.add_radiobutton(label="Shades Of Purple", command=shades_purple, image=theme_image, compound="left")
theme_menu.add_radiobutton(label="Winter Is Coming", command=winter_coming, image=theme_image, compound="left")
enable_disable_autosave = Menu(setting_menu, tearoff=0)
enable_disable_console = Menu(setting_menu, tearoff=0)
enable_dsiable_status = Menu(setting_menu, tearoff=0)
setting_menu.add_cascade(label="Auto Save", menu=enable_disable_autosave, image=autosave_image, compound="left")
setting_menu.add_cascade(label="Console", menu=enable_disable_console, image=console_image, compound="left")
setting_menu.add_cascade(label="Status Bar", menu=enable_dsiable_status, image=status_image, compound="left")
enable_disable_autosave.add_radiobutton(label="Enable",command=autosave_enable, image=enabled_image, compound="left")
enable_disable_autosave.add_radiobutton(label="Disbale",command=autosave_disable, image=xmark_image, compound="left")
enable_disable_console.add_radiobutton(label="Enable", command=console_enable, image=enabled_image, compound="left")
enable_disable_console.add_radiobutton(label="Disable", command=console_disable, image=xmark_image, compound="left")
pop_up_menu = Menu(widget, tearoff=0)
pop_up_menu.add_command(label="Copy", command=copy)
pop_up_menu.add_command(label="Cut", command=cut)
pop_up_menu.add_separator()
pop_up_menu.add_command(label="Paste", command=paste)
pop_up_menu.add_separator()
pop_up_menu.add_command(label="Select All", command=select_all)
enable_dsiable_status.add_radiobutton(label = "Enabled", command = show_statusbar, image=enabled_image, compound="left")
enable_dsiable_status.add_radiobutton(label = "Disabled", command = hide_statusbar, image=xmark_image, compound="left")
about_menu.add_command(label="Release Notes",command=realease_notes, image=status_image, compound="left")
about_menu.add_command(label="About",command=about_menu_command, image=selectall_image, compound="left")




    #final stuffs
output_area.pack(fill=BOTH, expand=1)
window.iconphoto(False, app_icon)
window.mainloop()

#        This Code Made By Abdou
#                If You are using Or Forked it. Give me Credit :3
