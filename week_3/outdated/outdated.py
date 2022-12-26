from re import match

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

while True:
    date = input("Date: ").strip().lower()

    month_d_yyyy = r"^(?P<month>[a-z]+) (?P<day>[0-9]{1,2}), (?P<year>[0-9]{4})$"
    match_re = match(month_d_yyyy, date)

    if match_re:
        day, year = [int(n) for n in match_re.group("day", "year")]

        month_name = match_re.group("month")
        month = months.index(month_name) + 1
    else:
        if len(date) not in range(8, 11):
            continue

        try:
            month, day, year = [int(n) for n in date.split("/")]
        except ValueError:
            continue

    if 1 <= month <= 12 and 1 <= day <= 31:
        break

print(f"{year}-{month:02}-{day:02}")
