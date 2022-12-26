import sys

names = []
while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)
    except EOFError:
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}")
        elif len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
        else:
            output = ""
            for i in range(len(names)):
                if i + 1 == len(names):
                    output += "and " + names[i]
                else:
                    output += names[i] + ", "
            print(f"Adieu, adieu, to {output}")
        sys.exit()