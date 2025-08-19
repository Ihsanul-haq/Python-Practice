import emoji

def main():
    while True:

        user_input = input("Input: ")
        if user_input.lower() in ["exit", "quit"]:

            break

        output = emoji.emojize(user_input, language="alias")

        print(f"Output: {output}")

    


main()
