import tkinter as tk
from tkinter import ttk
import subprocess

def runcript():
    #hide window
    root.iconify()
    #save current script
    createScript()
    #run custon script
    p = subprocess.Popen('python customScript.pyw', creationflags = subprocess.CREATE_NO_WINDOW)
    #p = os.popen('python customScript.pyw')
    #wait for end of script
    p.communicate()
    #subprocess.Popen('del macro.py', creationflags = subprocess.CREATE_NO_WINDOW)
    #bring back window after script end
    root.deiconify()

def loadScript(i):
    #read file
    f = open("customScript.pyw", "r")
    #load saved script (clear window then load from file)
    text[i].delete('1.0','end')
    temp = f.read().splitlines()
    text[i].insert(1.0,temp[i])
    f.close()

def createScript():
    #create custom script and add macro import
    f = open("customScript.pyw", "w")
    #f.write("from macro import *\n\n")
    for i in range(0,5):
        getText = str(text[i].get('1.0','end'))
        f.write(getText)

    #close file
    f.close()

    #TEMP - add line
    #addLine()

#add line to file depending on action type
def addLine(action="press",key="E"):
    f = open("customScript.pyw", "a")
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

    #add interactive space to modify custom script
    scriptSpace = tk.Canvas(mainCanvas, bg='white')
    scriptSpace.place(relwidth=1,relheight=0.83)

    scriptSpace1 = tk.Canvas(scriptSpace, bg='white')
    scriptSpace1.place(relwidth=0.2)
    scriptSpace2 = tk.Canvas(scriptSpace, bg='white')
    scriptSpace2.place(relwidth=0.8,relx=0.2)
    
    scriptSpace1.grid(column=0,row=0)
    scriptSpace2.grid(column=1,row=0,columnspan=3)

    text=[]
    list=[]
    for i in range(0,5):
        #combobox for choosing options
        list.append(ttk.Combobox(scriptSpace1, textvariable=tk.StringVar()))
        list[i]['values'] = ("Press Key","Test Func",'a','b','c','g')
        list[i].set("Press Key")
        list[i].pack()
        #textbox that loads script or sets up textbox
        text.append(tk.Text(scriptSpace2, height=1))
        try:
            loadScript(i)
        except:
            text[i].insert('1.0','key presses interval')
        text[i].pack()

    #listener for select
    #list[0].bind('<<ComboboxSelected>>', text[0].insert('end',str(list[0].get())))

    #loop and refresh window 
    root.mainloop()