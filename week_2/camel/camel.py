in_put = input("camelCase: ").strip()

for char in in_put:
    if(char.isupper()):
        print("_", end="")
    print(char.lower(), end="")

print("")
