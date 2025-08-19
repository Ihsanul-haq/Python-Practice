def main():
    number = value("Ihsan")
    print(f"${number}")

def value(greeting):

    text = input ("Greeting: ").strip()
    if text.lower().startswith("hello"):
        return 0
    elif text.lower().startswith("h"):
        return 20
    else:
        return 100
if __name__ == "__main__":


    main()