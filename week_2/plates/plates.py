def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (len(s) > 6) or (len(s) < 2):
        return False
    numbers_counter = 0
    for i in range(len(s)):
        if (s[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
            return False
        elif (i <= 1) and (s[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            return False
        elif (numbers_counter == 0) and (s[i] == "0"):
            return False
        elif (numbers_counter > 0) and (s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            return False
        elif s[i] in "123456789":
            numbers_counter += 1
    return True
main()
