import sys

items = {}
while True:
    try:
        user_input = input()
    except EOFError:
        print("")
        for key in sorted(items.keys()):
            print(f"{items[key]} {key}")
        sys.exit()
    try:
        items[user_input.upper()] += 1
    except KeyError:
        items[user_input.upper()] = 1