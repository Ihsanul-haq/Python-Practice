import sys, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" 
                 if len(sys.argv)<3 else 
                 "Too many command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_ext = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()
    if input_ext not in valid_ext or output_ext not in valid_ext:
        sys.exit("Invalid input")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    try:
        input_img = Image.open(input_file)
        shirt_img = Image.open("shirt.png")
        resized_input = ImageOps.fit(input_img, shirt_img.size)

        resized_input.paste(shirt_img, (0,0), shirt_img)
        resized_input.save(output_file)
        print(f"Saved: {output_file}")
    except FileNotFoundError:
        sys.exit("File not found")

    except Exception as e:
        sys.exit(f"Error: {e}")
if __name__ == "__main__":
    main()

