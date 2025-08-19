import csv
import sys
from tabulate import tabulate

def main():
        
    if len(sys.argv)!=2:
        sys.exit("Too few command-line arguments" 
                 if len(sys.argv)<2 
                 else "Too many command-line arguments")
    filename = sys.argv[1]
        #file must end with .py
    if not filename.endswith(".csv"):
            sys.exit("Not a CSV file")
    try:
         with open(filename, "r") as file:
              reader = csv.reader(file)
              header = next(reader)
              table = list(reader)
    except FileNotFoundError:
         sys.exit("File does not exist")

    print(tabulate(table, headers = header,tablefmt="grid"))
main()