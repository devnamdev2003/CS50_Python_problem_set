user = input("Expression: ").strip()

if ("/" in user):
    temp = user.index("/")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) / float(seccond))
elif ("*" in user):
    temp = user.index("*")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) * float(seccond))
elif ("+" in user):
    temp = user.index("+")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) + float(seccond))
elif ("-" in user):
    temp = user.index("-")
    first = user[:temp]
    seccond = user[temp+1:]
    print(int(first) - float(seccond))
