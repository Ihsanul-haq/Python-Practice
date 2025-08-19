import csv
import sys
def main():
    if len(sys.argv)!=3:
        sys.exit("Too few command-line arguments" 
                 if len(sys.argv)<3 else 
                 "Too many command-line arguments")
    before = sys.argv[1]
    after = sys.argv[2]
    try:
        with open(before, "r") as input:
            reader = csv.DictReader(input)
            with open (after,"w", newline="") as output:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    try:
                        last, first = row["name"].split(",")
                        writer.writerow({"first":first, "last":last,
                                          "house":row["house"]})
                    except ValueError:
                        sys.exit("Invalid name format in CSV")
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

if __name__ == "__main__":
    main()

