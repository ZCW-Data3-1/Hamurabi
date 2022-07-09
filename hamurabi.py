import math
import random

# print(random.randint(0, 5))
# #This will output either 1, 2, 3, 4 or 5.
# print(math.ceil(random.random() * 100.0))

print("Congratulations, you are the newest ruler of ancient Sumer, elected for a ten year term of office.\n"
      "Your duties are to dispense food, direct farming, and buy and sell land as needed to support your people.\n"
      "Watch out for rat infestations and the plague! Grain is the general currency, measured in bushels.\n\n"
      "The following will help you in your decisions:\n"
      "- Each person needs at least 20 bushels of grain per year to survive\n"
      "- Each person can farm at most 10 acres of land\n"
      "- It takes 2 bushels of grain to farm an acre of land\n"
      "- The market price for land fluctuates yearly\n"
      "\n"
      "Rule wisely and you will be showered with appreciation at the end of your term.\n"
      "Rule poorly and you will be kicked out of office!\n")

class Hamurabi(object):
    def play_game(self):
        print("Let's play!")
        print("Here is what you start the game with:\n\n"
              "- 100 people\n"
              "- 2800 bushels of grain in storage\n"
              "- 1000 acres of land\n"
              "- Land value is 19 bushels/acre\n")

        #Counter
        peopleCount = 100
        bushels = 2800
        acresOfLand = 1000
        landValue= 19


        gameOn = True
        while gameOn == True:
            while True:
                print("Are you looking to buy land or sell?")
                print("(1) to buy, (2) to sell")
                choice = int(input(">> "))
                if choice == 1:
                    print("How many acres of land would you like to buy?")
                    print(f"(You have {acresOfLand} acres  and {bushels} bushels available)")
                    print(f"(Price of acres is {landValue} bushels/ acre this year)")
                    try:
                        acresToBuy = int(input(">> "))
                    except ValueError:
                        print("numbers only please\n")
                        print("How many acres of land would you like to buy?")
                        acresToBuy = int(input(">> "))
                    if acresToBuy < acresOfLand:
                        acresOfLand = acresOfLand + acresToBuy
                        bushels = bushels - (acresToBuy*landValue)
                        print(f"you have {acresOfLand} acres of land and {bushels} bushels\n")
                        break
                    else:
                        print("You don't have enough land")
                elif choice == 2:
                    print("How many acres of land would you like to sell?")
                    print(f"(You have {acresOfLand} acres of land available)")
                    try:
                        acresToSell = int(input(">> "))
                    except ValueError:
                        print("numbers only please")
                        print("How many acres of land would you like to sell?")
                        acresToSell = int(input(">> "))
                        continue
                    if acresToSell < acresOfLand:
                        acresOfLand = acresOfLand - acresToSell
                        bushels = bushels + (acresToSell*landValue)
                        print(f"you have {acresOfLand} acres of land now\n")
                        break
                    else:
                        print("You don't have enough land")
                else:
                    print("That's not an option")

            while True:
                print("How much grain would you like to feed your people?")
                print(f"(You have {bushels} bushels available)")
                try:
                    toFeed = int(input(">> "))
                except ValueError:
                    print("numbers only please")
                    continue
                if toFeed < bushels:
                    bushels = bushels - toFeed
                    print(f"(You have {bushels} left)\n")
                    break
                else:
                    print("You don't have enough bushels for everyone")

            while True:
                print("How many acres to plant with your available grains?")
                print("(You must have enough acres, enough grain, and enough people to do the planting)")
                print(f"(You have {acresOfLand} acres, {bushels} bushels, and {peopleCount} people)")
                try:
                    choice = int(input(">> "))
                except ValueError:
                    print("numbers only please")
                    continue
                if choice > bushels//2:
                    print("You don't have enough grain")
                    continue
                elif choice > peopleCount * 10:
                    print("Your population isn't large enough to harvest that many acres")
                    continue




















if __name__ == '__main__':
    Hamurabi().play_game()
