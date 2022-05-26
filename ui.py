import tkinter as tk
from os import system

def runcript():
    #hide window
    root.iconify()
    #run custon script

    system('python customScript.py')

    #bring back window after script end
    root.deiconify()

def loadScript():
    f = open("customScript.py", "r")
    text.delete('1.0','end')
    text.insert(1.0,f.read())

def createScript():
    #create custom script and add macro import
    f = open("customScript.py", "w")
    #f.write("from macro import *\n\n")
    getText = text.get('1.0','end')
    f.write(getText)

    #close file
    f.close()

    #TEMP - add line
    #addLine()

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
    bgCanvas = tk.Canvas(root, height=600, width=600, bg="lightblue")
    bgCanvas.pack()

    #add canvas inside main window
    mainCanvas = tk.Canvas(root, bg="black")
    mainCanvas.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)

    #add button on bottom side of the window that run functions
    runFile = tk.Button(mainCanvas, text="Run Script", fg="black", bg="white", padx=7, pady=3, command=runcript)
    runFile.pack(fill="both",side='bottom')

    openFile = tk.Button(mainCanvas, text="Load Script", fg="black", bg="white", padx=7, pady=3, command=loadScript)
    openFile.pack(fill="both",side='bottom')

    saveFile = tk.Button(mainCanvas, text="Create Script", fg="black", bg="white", padx=7, pady=3, command=createScript)
    saveFile.pack(fill="both",side='bottom')


    scriptSpace = tk.Canvas(mainCanvas, bg='white')
    scriptSpace.place(relwidth=1,relheight=0.83)

    text = tk.Text(scriptSpace, width=200, height=200)
    try:
        loadScript()
    except:
        text.insert('1.0','from macro import *\n\n')
    text.pack()

    #loop and refresh window 
    root.mainloop()