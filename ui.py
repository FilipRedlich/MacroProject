import tkinter as tk
from tkinter import ttk
import macro

def runcript():
    #hide window
    root.iconify()
    #save current script before running
    createScript()
    
    #execute action with args
    global size
    loop = 0
    nrLoop = 0
    i = 0
    while i < size:
        #get the arguments from text
        args = str(text[i].get('1.0','end'))
        space = args.find(' ')
        arg1 = args[:space]
        args = args[space+1:]
        space2 = args.find(' ')
        arg2 = args[:space2]
        arg3 = args[space2+1:]
        try:
            #run function depending on the number of args
            if list[i].get() == 'pressKey':
                if(space == -1):
                    macro.pressKey(str(arg1))
                elif(space2 == -1):
                    macro.pressKey(str(arg1),int(arg2))
                else:
                    macro.pressKey(str(arg1),int(arg2),float(arg3))
            if list[i].get() == 'loop':
                loop = i
                nrLoop = int(arg1)
            if list[i].get() == 'endloop':
                if nrLoop > 0:
                    i = loop
                    nrLoop -= 1
                if nrLoop == -1:
                    i = loop
            if list[i].get() == 'click':
                if int(arg1) == 1:
                    arg1 = 'PRIMARY'
                elif int(arg1) == 2:
                    arg1 = 'SECONDARY'
                elif int(arg1) == 3:
                    arg1 = 'MIDDLE'
                else:
                    arg1 = 'PRIMARY'
                if(space == -1):
                    macro.click(str(arg1))
                elif(space2 == -1):
                    macro.click(str(arg1),int(arg2))
                else:
                    macro.click(str(arg1),int(arg2),float(arg3))
            if list[i].get() == 'clickPlace':
                if int(arg3) == 1:
                    arg3 = 'PRIMARY'
                elif int(arg3) == 2:
                    arg3 = 'SECONDARY'
                elif int(arg3) == 3:
                    arg3 = 'MIDDLE'
                else:
                    arg3 = 'PRIMARY'
                if(space == -1):
                    macro.clickPlace(int(arg1))
                elif(space2 == -1):
                    macro.clickPlace(int(arg1),int(arg2))
                else:
                    macro.clickPlace(int(arg1),int(arg2),str(arg3))
            if list[i].get() == 'wait':
                macro.wait(float(arg1))
            i += 1
        except:
            i += 1

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
        str = temp[i]
        #load action to list depending on action in script
        badAction = 1
        if str.find('pressKey') == 0:
            list[i].set('pressKey')
            str = str.replace('pressKey ','')
            text[i].insert(1.0,str)
            #text[i]['state'] = 'normal'
            badAction = 0
        if str.find('loop') == 0:
            list[i].set('loop')
            str = str.replace('loop ','')
            text[i].insert(1.0,str)
            #text[i]['state'] = 'normal'
            badAction = 0
        if str.find('endloop') == 0:
            list[i].set('endloop')
            str = str.replace('endloop ','')
            #text[i]['state'] = 'disabled'
            badAction = 0
        if str.find('click') == 0:
            list[i].set('click')
            str = str.replace('click ','')
            text[i].insert(1.0,str)
            #text[i]['state'] = 'enabled'
            badAction = 0
        if str.find('clickPlace') == 0:
            list[i].set('clickPlace')
            str = str.replace('clickPlace ','')
            text[i].insert(1.0,str)
            #text[i]['state'] = 'enabled'
            badAction = 0
        if str.find('wait') == 0:
            list[i].set('wait')
            str = str.replace('wait ','')
            text[i].insert(1.0,str)
            #text[i]['state'] = 'enabled'
            badAction = 0
        if badAction == 1:
            list[i].set('')
        #load args for action
        f.close()
    except:
        #template for empty
        0


def createScript():
    #create custom script and add macro import
    f = open("customScript.txt", "w")
    #f.write("from macro import *\n\n")
    global size
    for i in range(0,size):
        getAction = str(list[i].get())
        getText = str(text[i].get('1.0','end'))
        if getText.find('keyToPress') == -1 and getText.find('numberOfLoops') == -1 and getText.find('mouseButton') == -1 and getText.find('seconds') == -1:
            if str(list[i].get()) != "":
                f.write(getAction+' '+getText)
    #close file
    f.close()

def addRow(event):
    global size
    if str(list[size-1].get()) != "":
        for i in range(size,size+1):
            #combobox for choosing options
            list.append(ttk.Combobox(scriptSpace, textvariable=tk.StringVar()))
            list[i]['values'] = ("","pressKey","click","clickPlace","wait","loop","endloop")
            list[i].state(["readonly"])
            #list[i].set("pressKey")
            list[i].grid(column=0,row=i+1)
            #textbox that loads script or sets up textbox
            text.append(tk.Text(scriptSpace, height=1))
            #set template text
            if str(list[i-1].get()) == "pressKey":
                text[i-1].insert('1.0',"keyToPress numberOfPresses intervalBetween")
                #text[i-1]['state'] = 'normal'
            elif str(list[i-1].get()) == "loop":
                text[i-1].insert('1.0',"numberOfLoops")
                #text[i-1]['state'] = 'normal'
            elif str(list[i-1].get()) == "click":
                text[i-1].insert('1.0',"mouseButton(1/2/3) numberOfClicks interval")
            elif str(list[i-1].get()) == "clickPlace":
                root.iconify()
                x,y = macro.getPlace()
                text[i-1].insert('1.0',str(x)+" "+str(y)+" mouseButton(1/2/3)")
                root.deiconify()
            #else:
                #text[i-1]['state'] = 'disabled'
            text[i].grid(column=1,row=i+1)
            size+=1
        #unbind old list and bind new
        list[size-2].unbind('<<ComboboxSelected>>')
        list[size-1].bind('<<ComboboxSelected>>', addRow)
        #overwrite scrollbar everytime new row is added to check if needed
        vsb = tk.Scrollbar(mainCanvas, orient="vertical", command=scrollSpace.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        scrollSpace.configure(yscrollcommand=vsb.set)
        scriptSpace.update_idletasks()

if __name__ == '__main__':
    #bind main window to root
    root = tk.Tk()
    root.title('Macro')
    #try to get size from file if exist if not size=1
    try:
        with open("customScript.txt", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        size = count+2
    except:
        size=1

    #create main window and add background to it
    bgCanvas = tk.Canvas(root, height=600, width=600)
    bgCanvas.pack()

    #add canvas inside main window
    mainCanvas = tk.Frame(root, bg="white")
    mainCanvas.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)
    mainCanvas.grid_rowconfigure(0, weight=1)
    mainCanvas.grid_columnconfigure(0, weight=1)

    #add button on bottom side of the window that run functions
    runFile = tk.Button(mainCanvas, text="Run Script", fg="black", bg="white", padx=7, pady=3, command=runcript)
    runFile.grid(row=1,column=0,columnspan=2,sticky="news")

    openFile = tk.Button(mainCanvas, text="Load Script", fg="black", bg="white", padx=7, pady=3, command=loadScript)
    openFile.grid(row=2,column=0,columnspan=2,sticky="news")

    saveFile = tk.Button(mainCanvas, text="Create Script", fg="black", bg="white", padx=7, pady=3, command=createScript)
    saveFile.grid(row=3,column=0,columnspan=2,sticky="news")

    #add interactive space to modify custom script
    scrollSpace = tk.Canvas(mainCanvas, bg='white')
    scrollSpace.grid(row=0,column=0, sticky="news")
    #weight value columns of the grid
    scrollSpace.columnconfigure(0,weight=1)
    scrollSpace.columnconfigure(1,weight=6)
    #scrollbar to scroll through script rows
    vsb = tk.Scrollbar(mainCanvas, orient="vertical", command=scrollSpace.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    scrollSpace.configure(yscrollcommand=vsb.set)
    #frame that contains all script lines
    scriptSpace = tk.Frame(scrollSpace, bg="white")
    scrollSpace.create_window((0, 0), window=scriptSpace, anchor='nw')

    #description to rows
    descText1 = tk.Text(scriptSpace, height=1, width=15)
    descText1.insert('1.0','Action')
    descText1['state'] = 'disabled'
    descText1.grid(column=0,row=0)
    #descText1.pack()
    descText2 = tk.Text(scriptSpace, height=1)
    descText2.insert('1.0','Args')
    descText2['state'] = 'disabled'
    descText2.grid(column=1,row=0)
    #descText2.pack()

    text=[]
    list=[]
    for i in range(0,size):
        #combobox for choosing options
        list.append(ttk.Combobox(scriptSpace, textvariable=tk.StringVar()))
        list[i]['values'] = ("","pressKey","click","clickPlace","wait","loop","endloop")
        list[i].state(["readonly"])
        #list[i].set("pressKey")
        list[i].grid(column=0,row=i+1)
        #textbox that loads script or sets up textbox
        text.append(tk.Text(scriptSpace, height=1))
        loadLine(i)
        text[i].grid(column=1,row=i+1)
    
    #updater that lets tk calculate sizes
    scriptSpace.update_idletasks()
    #listener for select
    list[size-1].bind('<<ComboboxSelected>>', addRow)
    #set the canvas scrolling region
    scrollSpace.config(scrollregion=scrollSpace.bbox("all"))
    #launch the GUI
    root.mainloop()