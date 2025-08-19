import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid time format")
    start_hr = int(match.group(1))
    start_mnt = int(match.group(2) or 0)
    start_period = (match.group(3))
    end_hr = int(match.group(4))
    end_mnt = int(match.group(5) or 0)
    end_period = match.group(6)
    if start_mnt > 59 or end_mnt > 59:
        raise ValueError("Minutes out of range")
    start_24 = to_24_hr(start_hr,start_mnt, start_period)
    end_24 = to_24_hr(end_hr, end_mnt, end_period)
    return f"{start_24} to {end_24}"
def to_24_hr(hr, mint, period):
    if period == "AM":
        if hr == 12:
            hr = 0
    else:
        if hr !=12 :
            hr += 12
    return f"{hr:02}:{mint:02}"
if __name__ == "__main__":
    main()