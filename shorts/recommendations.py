def main():
    difficulty = input("Difficult or Casual: ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
         print("Enter a valid difficulty")
         return
    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
         print("Enter a valid number of players")
         return
    if difficulty == "Difficult" and players == "Multiplayer":
            recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
            recommend("Klondie")
    elif difficulty == "Casual" and players == "Multiplayer":
            recommend("Hearts")
    else:
        recommend("Clock")    
 

def recommend(game):
    print("you might like", game)

main()