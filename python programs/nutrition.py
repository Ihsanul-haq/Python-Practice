def main():
    fruits = {"Apple":130, "Banana":110, "Avocado":50, "Strawberries":50, 
"Lime":20, "Lemon":15, "Kiwifruit":90, "Cantaloupe":50,  "Grapefruit":60,
"Grapes":90, "Honeydew Melon":50, "Nectarine":60, "Orange":80, "Peach":60, 
"Pear":100, "Pineapple":50, "Plums":70, "Sweet cheries":100,"Tangerine":50, 
"Watermelon":80, 
 } 
    item = input("Item: ")
    if item in fruits:

        print(f"Calories: {fruits[item]}")


main()