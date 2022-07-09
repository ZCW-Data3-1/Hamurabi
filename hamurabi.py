import math
import random

print("Congratulations, you are the newest ruler of ancient Sumer, elected for a ten year term of office.\n"
      "Your duties are to dispense food, direct farming, and buy and sell land as needed to support your people.\n"
      "Watch out for rat infestiations and the plague! Grain is the general currency, measured in bushels.\n\n"
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

        # Counter
        population = 100
        bushels = 2800
        acresOfLand = 1000
        landValue = 19
        year = 0

        # EOY Counter
        peopleDied = 0
        totalbushel = 0
        totalLand = 0
        starved_folk = 0
        immigrant = 0
        cropyield = 0
        bushels_in_storage = 0

        gameOn = True
        while gameOn == True:
            while True:
                print("Are you looking to buy or sell land?")
                print("(1) to buy, (2) to sell")
                choice = int(input(">> "))
                if choice == 1:
                    print("How many acres of land would you like to buy?")
                    print(f"(You have {acresOfLand} acres  and {bushels} bushels available)")
                    print(f"(Price of acres is {landValue} bushels/ acre this year)")
                    try:
                        acresToBuy = int(input(">> "))
                        if acresToBuy < 0:
                            print("only positive numbers please\n")
                            continue
                    except ValueError:
                        print("numbers only please\n")
                        continue
                    if acresToBuy < acresOfLand:
                        acresOfLand = acresOfLand + acresToBuy
                        bushels = bushels - (acresToBuy * landValue)
                        print(f"you have {acresOfLand} acres of land and {bushels} bushels\n")
                        break
                    else:
                        print("You don't have enough land\n")
                elif choice == 2:
                    print("How many acres of land would you like to sell?")
                    print(f"(You have {acresOfLand} acres of land available)")
                    try:
                        acresToSell = int(input(">> "))
                        if acresToSell < 0:
                            print("only positive numbers please\n")
                            continue
                    except ValueError:
                        print("numbers only please\n")
                        continue
                    if acresToSell < acresOfLand:
                        acresOfLand = acresOfLand - acresToSell
                        bushels = bushels + (acresToSell * landValue)
                        print(f"you have {acresOfLand} acres of land now\n")
                        break
                    else:
                        print("You don't have enough land\n")
                else:
                    print("That's not an option\n")
                    #alphabet catcher add in later

            while True:
                print("How much grains would you like to feed your people?")
                print(f"(You have {bushels} bushels available)")
                try:
                    toFeed = int(input(">> "))
                    if toFeed < 0:
                        print("only positive numbers please\n")
                        continue
                except ValueError:
                    print("numbers only please\n")
                    continue
                if toFeed < bushels:
                    if (toFeed/population) < 20:
                        peopleFed = math.floor(toFeed/20)
                        starving = population - peopleFed
                        print(f"{starving} people went unfed")
                    else:
                        print("everyone was fed this year")
                    bushels = bushels - toFeed
                    print(f"(You have {bushels} left)\n")
                    break
                else:
                    print("You don't have enough bushels\n")

            while True:
                print("How many acres to plant with your available grains?")
                print("(You must have enough acres, enough grain, and enough people to do the planting)")
                print(f"(You have {acresOfLand} acres, {bushels} bushels, and {population} people)")
                try:
                    acres = int(input(">> "))
                    if acres < 0:
                        print("only positive numbers please\n")

                        break
                except ValueError:
                    print("numbers only please\n")
                    continue

            print(Hamurabi.grain_eaten_by_rats(bushels))
            print(Hamurabi.plague_chance(population))
            print(Hamurabi.uprising_flag(population, starved_folk))
            print(Hamurabi.new_cost_of_land())
            print(Hamurabi.immigrants(population, acresOfLand, bushels_in_storage))


    def starvation_deaths(population, bushels):
        people_we_can_feed = math.floor(bushels/20)
        starved_folk = population - people_we_can_feed
        if starved_folk < 0:
            return 0
        else:
            return starved_folk

    def uprising_flag(population, starved_folk):
        return float(starved_folk/population) > 0.45

    def immigrants(population, acresOfLand, bushels_in_storage):
        immigrant_total = int((20 * acresOfLand + bushels_in_storage) / (100 * population))
        return immigrant_total

    def plague_chance(population):
        chance = random.randint(1, 100)
        plague_deaths = 0
        if chance <= 15:
            plague_deaths = population / 2
            return plague_deaths
        else:
            return plague_deaths

    def harvest(acres, bushels):
        acres = bushels // 2
        crop_yield = random.randint(1, 6)
        return acres_planted * crop_yield

    def harvest(acres, bushels):
        acres = bushels // 2
        crop_yield = random.randint(1, 6)
        return acres_planted * crop_yield

    def grain_eaten_by_rats(bushels):
        chance = random.randint(1, 100)
        if chance < 40:
            percent_eaten = random.randint(10, 30)
            return bushels // (percent_eaten / 100)
        else:
            return 0

    def new_cost_of_land():
        return random.randint(17,23)

    def uprising_flag(population, starved_folk):
        return float(starved_folk/population) > 0.45



if __name__ == '__main__':
    Hamurabi().play_game()
