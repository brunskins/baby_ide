from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.colorchooser import askcolor
from tkinter import simpledialog
import subprocess
compiler =Tk()
compiler.title("baby boy ide")
compiler.resizable(height = True, width = True)
file_path=""
edt_height = "40"
edt_width = "24"
run_height = "7"
run_width = "24"
def set_file_path(path):
    global file_path
    file_path = path


def run():
    if file_path == "":
        save_as()
    tfilepath = "'" + file_path + "'"
    print(tfilepath)
    command = f'python {tfilepath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete("1.0", END)
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def save_as():
    path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    path=path+".py"
    with open(path, "w") as file:
        code = editor.get("1.0", END)
        file.write(code)
        set_file_path(path)
        
def save():
    path=file_path
    with open(path, "w") as file:
        code = editor.get("1.0", END)
        file.write(code)
        set_file_path(path)
        
def open_file():
    path = askopenfilename(filetypes=[("Python Files", "*.py")])

    with open(path, "r") as file:
        code = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", code)
        set_file_path(path)

def resize():
    pass


def change_color():
    colors = askcolor(title="Color Picker")
    compiler.configure(bg=colors[1])
    editor.configure(bg=colors[1])
    code_output.configure(bg=colors[1])
def change_text():
    colors = askcolor(title="Color Picker")
    editor.configure(fg=colors[1], insertbackground=colors[1])
    code_output.configure(fg=colors[1], insertbackground=colors[1])

menu_bar = Menu(compiler)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

settings_menu = Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Clean Resize", command=resize)
settings_menu.add_command(label="Change BG Color", command=change_color)
settings_menu.add_command(label="Change Text Color", command=change_text)
menu_bar.add_cascade(label="settings", menu=settings_menu)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=7)
code_output.pack()

compiler.mainloop()
