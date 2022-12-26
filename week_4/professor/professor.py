import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        summand_1 = generate_integer(level)
        summand_2 = generate_integer(level)
        counter = 0
        while counter < 3:
            sum_user = input(f"{summand_1} + {summand_2} = ")
            try:
                if int(sum_user) == (summand_1 + summand_2):
                    score += 1
                    break
                elif int(sum_user) != (summand_1 + summand_2):
                    counter += 1
                    print("EEE")
            except ValueError:
                counter += 1
                print("EEE")
            if counter == 3:
                print(f"{summand_1} + {summand_2} = {summand_1 + summand_2}")
                counter = 0
                break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()