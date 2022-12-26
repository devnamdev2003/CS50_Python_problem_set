import sys


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif sys.argv[1][-2:] != "py":
    print("Not a Python file")
    sys.exit(1)
else:
    try:
        count = 0
        with open(sys.argv[1], newline='') as pythonfile:
            lines = pythonfile.readlines()
            for line in lines:
                if len(line.lstrip()) > 0:
                    if line.lstrip()[0] == "#":
                        pass
                    else:
                        count += 1
        print(count)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)