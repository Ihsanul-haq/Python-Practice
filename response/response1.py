from validator_collection import validators, errors
def main():
    email = input("what's your email? ")
    try:
        validators.email(email)
        print("Valid.")
    except errors.InvalidEmailError():
        print("Invalid.")
    except ValueError():
        print("Invalid")

if __name__ == "__main__":
    main()