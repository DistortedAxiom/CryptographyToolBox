from eSolverToolbox.strings import StringReplacer

def start():
    x = input("Enter a string")
    modified = StringReplacer(x)
    modified.replacer()


if __name__ == '__main__':
    start()