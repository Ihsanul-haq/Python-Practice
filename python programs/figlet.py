from pyfiglet import Figlet
import sys
import random
def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        text = input ("Input: ")
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(text))

    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font_name = sys.argv[2]
        if font_name not in fonts:
            sys.exit ("Invalid usage")
        text = input ("Input: ")
        figlet.setFont(font=font_name)
        print(figlet.renderText(text))

    else:
        sys.exit("Invalid usage")
if __name__=="__main__":
    main()