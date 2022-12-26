import random

level = ""
while not isinstance(level, int):
    try:
        level = int(input("Level: "))
        if level < 1:
            level = ""
    except ValueError:
        pass

random_number = random.randint(1, level)

end = False
while not end:
    try:
        guess = int(input("Guess: "))
        if random_number == guess:
            print("Just right!")
            break
        elif random_number > guess:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        pass