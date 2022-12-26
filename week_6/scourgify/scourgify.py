import sys
import csv


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    try:
        with open(sys.argv[1], newline='') as csvfile:
            students = csv.DictReader(csvfile, delimiter=',')
            with open(sys.argv[2], "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["first", "last", "house"])
                for student in students:
                    writer.writerow([student["name"].split(", ")[1], student["name"].split(", ")[0], student["house"]])
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)