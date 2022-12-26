import validators


def main():
    print(email_validator(input("What's your email address? ")))


def email_validator(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()