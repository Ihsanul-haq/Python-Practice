def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate[:2].isalpha():
        return False
    if not plate.isalnum():
        return False
    number_started = False
    for char in plate:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            return False
    return True
if __name__ == "__main__":

    main()
            
