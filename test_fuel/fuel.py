def main():

    while True:

        try:
            fraction = input ("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError:
            continue
            

def convert(fraction):
    try:
    
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or y == 0:
            raise ValueError
        percentage = round ((x/y) * 100,2)
        return percentage
    except(ValueError, ZeroDivisionError):
        raise ValueError
def gauge(percentage):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage} %"
           
if __name__ == "__main__":
    main()