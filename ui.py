def createScript():
    f = open("customScript.py", "w")
    f.write("""import macro
if __name__ == '__main__':
    macro.pressKey('E',3)\n""")
    f.close()

if __name__ == '__main__':
    createScript()