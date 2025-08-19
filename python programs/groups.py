import re
def main():
    locations = {"+1": "united States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}
    #pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")
    match = re.search(pattern, number)
    if match:
        #country_code = match.group(1)
        country_code = match.group("country_code")
        #print(f"Valid and the country code is {country_code}")
        print(locations[country_code])
    else:
        Print("Invalid.")
if __name__ == "__main__":
    main()
