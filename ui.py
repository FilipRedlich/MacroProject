import tkinter as tk

def loadScript():
    0

def createScript():
    f = open("customScript.py", "w")
    f.write("""import macro
if __name__ == '__main__':\n""")
    f.write("\tmacro.pressKey('E',3)")
    f.close()

if __name__ == '__main__':
    root = tk.Tk()

    canvas = tk.Canvas(root, height=600, width=600, bg="lightblue")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8,relheight=0.7,relx=0.1,rely=0.1)

    openFile = tk.Button(root, text="Load Script", fg="black", bg="white", padx=7, pady=3, command=loadScript)
    openFile.pack(fill="both")

    saveFile = tk.Button(root, text="Create Script", fg="black", bg="white", padx=7, pady=3, command=createScript)
    saveFile.pack(fill="both")

    root.mainloop()