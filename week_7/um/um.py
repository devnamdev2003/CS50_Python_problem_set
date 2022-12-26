import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall("([^a-z]|^)um", s.lower()))


if __name__ == "__main__":
    main()