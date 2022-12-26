name = input()
for i in range(len(name)):
    if(name[i] == " "):
        print("...", end="")
        continue
    print(name[i], end="")
print("")
