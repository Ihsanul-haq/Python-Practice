def main():
    number = value("Ihsan")
    print(f"${number}")

def value(greeting):

    #ext = input ("Greeting: ").strip()
    if greeting.strip().lower().startswith("hello"):
        return 0
    if greeting.strip().lower().startswith("h"):
        return 20
    else:
        return 100
if __name__ == "__main__":


    main()