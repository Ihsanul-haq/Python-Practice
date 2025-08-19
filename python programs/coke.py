def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Inser Coin: "))
            
            if coin in [5, 10, 25]:
                amount_due -= coin
        except:
            pass
    print(f"Change Owed: {abs(amount_due)}")
main()
