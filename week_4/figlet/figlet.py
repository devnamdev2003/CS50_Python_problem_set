from pyfiglet import Figlet
import sys

figlet_fonts = Figlet().getFonts()

if len(sys.argv) == 1:
    input = input("Input: ")
    print(f.renderText(input))
elif (len(sys.argv) == 3) and ((sys.argv[1] == "-f") or (sys.argv[1] == "--font")):
    if sys.argv[2] in figlet_fonts:
        input = input("Input: ")
        print(Figlet(font=sys.argv[2]).renderText(input))
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)