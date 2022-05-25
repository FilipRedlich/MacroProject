import tkinter as tk
from os import system
#import customScript

def runcript():
    #hide window
    root.iconify()
    #run custon script

    system('python customScript.py')
    #customScript.run()

    #bring back window after script end
    root.deiconify()

def loadScript():
    0

def addLine(action="press",key="F"):
    f = open("customScript.py", "a")
    f.write("\t")
    if(action=="press"):
        f.write("macro.pressKey('"+key+"',20,0.2)")
    f.write("\n")
    f.close()

def createScript():
    #create custom script and add macro import
    f = open("customScript.py", "w")
    f.write("import macro\n\ndef run():\n")

    #add custom commands to script
    #f.write("\tmacro.pressKey('E',10,0.2)\n")
    

    #close file
    f.close()
    addLine()

if __name__ == '__main__':
    #bind main window to root
    root = tk.Tk()

    #create main window and add background to it
    canvas = tk.Canvas(root, height=600, width=600, bg="lightblue")
    canvas.pack()

    #add frame inside main window
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8,relheight=0.7,relx=0.1,rely=0.1)

    #add button on bottom side of the window that run functions
    runFile = tk.Button(root, text="Run Script", fg="black", bg="white", padx=7, pady=3, command=runcript)
    runFile.pack(fill="both")

    openFile = tk.Button(root, text="Load Script", fg="black", bg="white", padx=7, pady=3, command=loadScript)
    openFile.pack(fill="both")

    saveFile = tk.Button(root, text="Create Script", fg="black", bg="white", padx=7, pady=3, command=createScript)
    saveFile.pack(fill="both")

    #loop and refresh window 
    root.mainloop()