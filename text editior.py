
from tkinter import *
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad Clone")
        self.textarea = Text(self.master, undo=True)
        self.textarea.pack(expand=True, fill=BOTH)
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self.master)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.textarea.edit_undo)
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.textarea.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut_text)
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy_text)
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        self.master.config(menu=menubar)

    def new_file(self):
        self.textarea.delete("1.0", END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.textarea.delete("1.0", END)
            self.textarea.insert("1.0", content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.textarea.get("1.0", END)
            with open(file_path, "w") as file:
                file.write(content)

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.textarea.get("1.0", END)
            with open(file_path, "w") as file:
                file.write(content)

    def exit_app(self):
        self.master.destroy()

    def cut_text(self):
        self.textarea.event_generate("<<Cut>>")

    def copy_text(self):
        self.textarea.event_generate("<<Copy>>")

    def paste_text(self):
        self.textarea.event_generate("<<Paste>>")

    def select_all_text(self):
        self.textarea.tag_add("sel", "1.0", "end")

if __name__ == "__main__":
    root = Tk()
    notepad = Notepad(root)
    root.mainloop()