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

def createScript():
    #create custom script and add macro import
    f = open("customScript.py", "w")
    f.write("import macro\n\n")

    #add custom commands to script
    #f.write("\tmacro.pressKey('E',10,0.2)\n")
    

    #close file
    f.close()
    #TEMP - add line
    addLine()

def addLine(action="press",key="E"):
    f = open("customScript.py", "a")
    if(action=="press"):
        f.write("macro.pressKey('"+key+"',20,0.2)")
    f.write("\n")
    f.close()

if __name__ == '__main__':
    #bind main window to root
    root = tk.Tk()

    #create main window and add background to it
    canvas = tk.Canvas(root, height=600, width=600, bg="lightblue")
    canvas.pack()

    #add frame inside main window
    frame = tk.Frame(root, bg="black")
    frame.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)

    #add button on bottom side of the window that run functions
    runFile = tk.Button(frame, text="Run Script", fg="black", bg="white", padx=7, pady=3, command=runcript)
    runFile.pack(fill="both",side='bottom')

    openFile = tk.Button(frame, text="Load Script", fg="black", bg="white", padx=7, pady=3, command=loadScript)
    openFile.pack(fill="both",side='bottom')

    saveFile = tk.Button(frame, text="Create Script", fg="black", bg="white", padx=7, pady=3, command=createScript)
    saveFile.pack(fill="both",side='bottom')

    scriptFrame = tk.Frame(frame, bg='white')
    scriptFrame.place(relwidth=1,relheight=0.83)

    #loop and refresh window 
    root.mainloop()