from datetime import date
import sys
import inflect


def main():
    converted_input = convert_input(input("Date of Birth: "))
    if isinstance(converted_input, date):
        delta_minutes = minutes_calculator(converted_input)
        inflector = inflect.engine()
        print(f"{inflector.number_to_words(delta_minutes, andword='').capitalize()} minutes")
    else:
        print("Invalid date")
        sys.exit(1)


def convert_input(user_input):
    try:
        modified_input = list(map(int, user_input.split("-")))
        return date(modified_input[0], modified_input[1], modified_input[2])
    except ValueError:
        return None


def minutes_calculator(converted_input):
    delta_days = date.today() - converted_input
    return int(delta_days.total_seconds() / 60)


if __name__ == "__main__":
    main()