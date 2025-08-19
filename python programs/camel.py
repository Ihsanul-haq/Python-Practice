def main():

    camel = input("CamelCase: ")
    snake = camel_to_snake(camel)
    print("snake_case: ",snake)

def camel_to_snake(name):
    snake = ""
    for i, char in enumerate(name):
        if char.isupper() and i !=0:
            snake += "_"
        snake += char.lower()
    return snake
        
if __name__ == "__main__":
    main()
