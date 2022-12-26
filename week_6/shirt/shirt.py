import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif sys.argv[1][-3:] not in ["jpg", "jpeg", "png"] or sys.argv[2][-3:] not in ["jpg", "jpeg", "png"]:
    print("Invalid input")
    sys.exit(1)
elif sys.argv[1][-3:] != sys.argv[2][-3:]:
    print("Input and output have different extensions")
    sys.exit(1)
else:
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = Image.open(sys.argv[1])
        photo_resized = ImageOps.fit(photo, size)
        photo_resized.paste(shirt, mask=shirt)
        photo_resized.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)