def main():

    groceries={}

    try:
        while True:
            item = input().strip().upper()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item]=1
            #if item:
                #groceries[item]=groceries.get(item,0)+1


    except EOFError:
        print()
        pass
    for item in sorted(groceries):
        print(f"{groceries[item]} {item}")

if __name__ == "__main__":

    main()

