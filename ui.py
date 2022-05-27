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

def loadScript():
    global size
    for i in range(0,size):
        loadLine(i)

def loadLine(i):
    try:
        #read file
        f = open("customScript.pyw", "r")
        #load saved script (clear window then load from file)
        text[i].delete('1.0','end')
        temp = f.read().splitlines()
        str = temp[i+2]
        badAction = 1
        if str.find('pressKey') == 0:
            list[i].set('pressKey')
            str = str.replace('pressKey','')
            badAction = 0
        if str.find('testFunc') == 0:
            list[i].set('testFunc')
            str = str.replace('testFunc','')
            badAction = 0
        if badAction == 1:
            list[i].set('')
        text[i].insert(1.0,str)
        f.close()
    except:
        text[i].insert('1.0',"('key',numberOfPresses,interval)")

def createScript():
    #create custom script and add macro import
    f = open("customScript.pyw", "w")
    f.write("from macro import *\n\n")
    global size
    for i in range(0,size):
        getAction = str(list[i].get())
        getText = str(text[i].get('1.0','end'))
        ff = getText.find('(')
        getText = getText[ff:]
        if getText!="('key',numberOfPresses,interval)\n" and ff!=-1:
            f.write(getAction+getText)
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
    list[size-2].unbind('<<ComboboxSelected>>')
    list[size-1].bind('<<ComboboxSelected>>', addRow)

if __name__ == '__main__':
    #bind main window to root
    root = tk.Tk('Macro')
    try:
        with open("customScript.pyw", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        size = count
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