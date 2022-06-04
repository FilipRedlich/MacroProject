import tkinter as tk
from tkinter import ttk
import subprocess
import macro

def runcript():
    #hide window
    root.iconify()
    #save current script
    #createScript()
    
    #execute action with args
    global size
    for i in range(0,size):
        #get the arguments from text
        args = str(text[i].get('1.0','end'))
        space = args.find(' ')
        arg1 = args[:space]
        args = args[space+1:]
        space2 = args.find(' ')
        arg2 = args[:space2]
        arg3 = args[space2+1:]
        #run function depending on the number of args
        if list[i].get() == 'pressKey':
            if(space == -1):
                macro.pressKey(str(arg1))
            elif(space2 == -1):
                macro.pressKey(str(arg1),int(arg2))
            else:
                macro.pressKey(str(arg1),int(arg2),float(arg3))
        if list[i].get() == 'testFunc':
            0

    #bring back window after script end
    root.deiconify()

def loadScript():
    global size
    for i in range(0,size):
        loadLine(i)

def loadLine(i):
    try:
        #read file
        f = open("customScript.txt", "r")
        #load saved script (clear window then load from file)
        text[i].delete('1.0','end')
        temp = f.read().splitlines()
        #skip first 2 lines
        str = temp[i]
        #load action to list depending on action in script
        badAction = 1
        if str.find('pressKey') == 0:
            list[i].set('pressKey')
            str = str.replace('pressKey ','')
            badAction = 0
        if str.find('testFunc') == 0:
            list[i].set('testFunc')
            str = str.replace('testFunc ','')
            badAction = 0
        if badAction == 1:
            list[i].set('')
        #load args for action
        text[i].insert(1.0,str)
        f.close()
    except:
        #template for empty
        text[i].insert('1.0',"key numberOfPresses interval")

def createScript():
    #create custom script and add macro import
    f = open("customScript.txt", "w")
    #f.write("from macro import *\n\n")
    global size
    for i in range(0,size):
        getAction = str(list[i].get())
        getText = str(text[i].get('1.0','end'))
        if getText!="key numberOfPresses interval\n":
            f.write(getAction+' '+getText)
    #close file
    f.close()

def addRow(event):
    global size
    for i in range(size,size+1):
        #combobox for choosing options
        list.append(ttk.Combobox(scriptSpace1, textvariable=tk.StringVar()))
        list[i]['values'] = ("pressKey","testFunc")
        #list[i].set("pressKey")
        list[i].pack()
        #textbox that loads script or sets up textbox
        text.append(tk.Text(scriptSpace2, height=1))
        loadLine(i)
        text[i].pack()
        size+=1
    #unbind old list and bind new
    list[size-2].unbind('<<ComboboxSelected>>')
    list[size-1].bind('<<ComboboxSelected>>', addRow)

if __name__ == '__main__':
    #bind main window to root
    root = tk.Tk('Macro')
    #try to get size from file if exist if not size=1
    try:
        with open("customScript.txt", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        size = count+2
    except:
        size=1

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

    #divided main scace in 2 parts
    scriptSpace1 = tk.Canvas(scriptSpace, bg='white')
    scriptSpace1.place(relwidth=0.2)
    scriptSpace2 = tk.Canvas(scriptSpace, bg='white')
    scriptSpace2.place(relwidth=0.8,relx=0.2)
    


    #description to rows
    descText1 = tk.Text(scriptSpace1, height=1, width=15)
    descText1.insert('1.0','Action')
    descText1['state'] = 'disabled'
    descText1.pack()
    descText2 = tk.Text(scriptSpace2, height=1)
    descText2.insert('1.0','Args')
    descText2['state'] = 'disabled'
    descText2.pack()

    text=[]
    list=[]
    for i in range(0,size):
        #combobox for choosing options
        list.append(ttk.Combobox(scriptSpace1, textvariable=tk.StringVar()))
        list[i]['values'] = ("pressKey","testFunc")
        #list[i].set("pressKey")
        list[i].pack()
        #textbox that loads script or sets up textbox
        text.append(tk.Text(scriptSpace2, height=1))
        loadLine(i)
        text[i].pack()

    #listener for select
    list[size-1].bind('<<ComboboxSelected>>', addRow)
    #loop and refresh window 
    root.mainloop()