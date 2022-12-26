import sys

items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

total = 0
while True:
    try:
        user_input = input("Item: ")
    except EOFError:
        sys.exit()
    try:
        total += items[user_input.title()]
        total_float = "{:.2f}".format(total)
        print(f"Total: ${total_float}")
    except KeyError:
        pass