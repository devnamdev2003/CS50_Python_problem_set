import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()