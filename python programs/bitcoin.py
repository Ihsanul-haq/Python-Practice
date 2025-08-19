import requests
import sys
def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")


    try:
        bitcoins = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=your_key")
        response.raise_for_status()
        data = response.json()
        #print(data)
        price = float(data["data"]["priceUsd"])
        total = bitcoins * price
        print(f"${total:,.4f}")

    except requests.RequestException:
        sys.exit("Error fetchinf bitcoin price")
if __name__ == "__main__":
    main()
