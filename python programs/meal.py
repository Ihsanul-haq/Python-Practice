def main():
    try:
        time = input("What time is it? ").strip()
        t = convert (time)
        if 7.0<=t<=8.0:
            print("Breakfast time")
        elif 12.0<= t <= 13.0 :
            print ("Lunch time")
        elif 18.0<= t <= 19.0:
            print("Dinner time")
    except:
        pass


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60


if __name__ == "__main__":
    main()