import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        answer = x + y
        tries = 0
        while tries < 3:
            try:
                user = int(input(f"{x} + {y} = "))
                if user == answer:
                    score +=1
                    break
                else:
                    print("EEE")
                    tries+=1
            except ValueError:
                print("EEE")
                tries+=1

        if tries ==3:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")




def generate_integer(level):
    if level == 1:
        return random.randint(1,9),random.randint(1,9)
    elif level == 2:
        return random.randint(10,99),random.randint(10,99)
    elif level == 3:
        return random.randint(100,999),random.randint(100,999)
    else:
        raise ValueError("Invalid level")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass
if __name__ == "__main__":
    main()