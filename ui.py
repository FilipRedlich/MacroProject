def createScript():
    f = open("customScript.py", "w")
    f.write("""import macro
if __name__ == '__main__':\n""")
    f.write("\tmacro.pressKey('E',3)")
    f.close()

if __name__ == '__main__':
    createScript()