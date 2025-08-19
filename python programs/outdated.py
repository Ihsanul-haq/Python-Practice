def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Format: MM/DD/YYYY
            if "/" in date:
                parts = date.split("/")
                if len(parts) != 3:
                    raise ValueError
                month, day, year = map(int, parts)

            # Format: Month D, YYYY
            elif "," in date:
                month_day, year = date.split(",")
                month_name, day = month_day.strip().split(" ")
                month = months.index(month_name.strip().title()) + 1
                day = int(day)
                year = int(year.strip())

            else:
                raise ValueError

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
    

            # Print in ISO 8601 format
            print(f"{year:04}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()