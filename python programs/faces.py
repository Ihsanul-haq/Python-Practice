def convert(text):

    text=text.replace(":)", "\U0001F642")
    text=text.replace(":(", "\U0001F641")
    return text
def main():
    user_input = input()
    output = convert(user_input)
    print(output)
if __name__ == "__main__":
    main()
