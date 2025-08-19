names = []
def main():
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")

    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")

    else:
        text = ", ".join(names[:-1]) + f"and{names[-1]}"
        print(f"Adieu, adieu, to{text}")

if __name__=="__main__":
    main()
