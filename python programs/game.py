import random

def main():
    level = get_level()
    number = random.randint(1, level)
    guess_number(number)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            continue
def guess_number(answer):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            elif guess < answer:
                print("Too Small!")
            elif guess > answer:
                print("Too Large!")
            else:
                print("Just right")
                break
        except ValueError:
            pass
            
main()



