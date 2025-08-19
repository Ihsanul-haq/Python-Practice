from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    birth_str = input("Date of birth (YYYY-MM-DD): ").strip()
    try:
        year, month, day = map(int, birth_str.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date format")
    today = date.today()
    if birth_date > today:
        sys.exit("Birth date can not be in the future")
    day_alive = (today - birth_date).days
    minuts_alive = day_alive * 24 * 60
    minuts_words = p.number_to_words(minuts_alive, andword="").capitalize()
    print(f"You have lived for {minuts_words} minutes.")
    print(f"You were born in the {season_of_birth(month)}.")
def season_of_birth(month):
    if month in (12,1,2):
        return "winter"
    elif month in (3,4,5):
        return "spring"
    elif month in (6,7,8):
        return "summer"
    else:
        return "autumn"

if __name__ == "__main__":
    main()