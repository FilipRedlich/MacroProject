def createScript():
    f = open("customScipt.py", "w")
    f.write("import macro\n\nif __name__ == '__main__':\n\tmacro.pressKey('E',3)")
    f.close()

if __name__ == '__main__':
    createScript()