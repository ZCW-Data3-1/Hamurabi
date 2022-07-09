import math
import random
class Hamurabiv2(object):
    def play_game(self):
        Hamurabiv2.summary()
        print("Let's play!")

        population = 100
        bushels = 2800
        acresOfLand = 1000
        landValue = 19 #bushels per ares
        year = 0
        acres_planted = 0

        # EOY Counter
        peopleDied = 0
        totalbushel = 0
        totalLand = 0
        starved_folk = 0
        immigrant = 0
        cropyield = 0
        bushels_in_storage = 0

        gameON = True
        while gameON == True:
            while True:
                print("Are you looking to buy or sell land?")
                print(f"(You have {acresOfLand} acres of land available)")
                print("(1) to buy, (2) to sell")
                choice = int(input(">> "))
                if choice == 1:
                    acreBought = Hamurabiv2.askHowManyAcresToBuy()
                    acresOfLand += acreBought
                    bushels -= (acreBought * landValue)
                    print(f"you have {acresOfLand} acres of land and {bushels} bushels\n")
                    break
                elif choice == 2:
                    acresToSell = Hamurabiv2.askHowManyAcresToSell()
                    acresOfLand -= acresToSell
                    bushels += (acresToSell * landValue)
                    print(f"you have {acresOfLand} acres of land now\n")
                    break
                else:
                    print("That's not an option\n")
            while True:
                print(f"(You have {bushels} bushels available)")
                toFeed = Hamurabiv2.askHowMuchGrainToFeedPeople()
                if toFeed < bushels:
                    bushels -= toFeed
                    print(f"(You have {bushels} left)\n")
                    break
                else:
                    print("You don't have enough bushels\n")
            while True:
                print(f"(You have {acresOfLand} acres, {bushels} bushels, and {population} people)")
                acres_planted = Hamurabiv2.askHowManyAcresToPlant()
                print(f"planting {acres_planted} acres")
                bushels -= (acres_planted*2)
                print(f"You have {bushels} left after planting")
                break

            print(Hamurabiv2.plague_chance(population))
            print(Hamurabiv2.starvation_deaths(population, bushels))
            print(Hamurabiv2.uprising_flag(population, starved_folk))
            print(Hamurabiv2.immigrants(population, acresOfLand, bushels_in_storage))
            print(Hamurabiv2.grain_eaten_by_rats(bushels))
            print(Hamurabiv2.new_cost_of_land())











    def summary():
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

    def askHowManyAcresToBuy():
        print("How many acres of land would you like to buy?")
        try:
            acresToBuy = int(input(">> "))
            if acresToBuy < 0:
                print("only positive numbers please\n")
                Hamurabiv2.askHowManyAcresToBuy()
        except ValueError:
            print("numbers only please\n")
            Hamurabiv2.askHowManyAcresToBuy()
        return acresToBuy

    def askHowManyAcresToSell():
        print("How many acres of land would you like to sell?")
        try:
            acresToSell = int(input(">> "))
            if acresToSell < 0:
                print("only positive numbers please\n")
                Hamurabiv2.askHowManyAcresToSell()
        except ValueError:
            print("numbers only please\n")
            Hamurabiv2.askHowManyAcresToSell()
        return acresToSell

    def askHowMuchGrainToFeedPeople():
        print("How much grains would you like to feed your people?")
        try:
            toFeed = int(input(">> "))
            if toFeed < 0:
                print("only positive numbers please\n")
                Hamurabiv2.askHowMuchGrainToFeedPeople()
        except ValueError:
            print("numbers only please\n")
            Hamurabiv2.askHowMuchGrainToFeedPeople()
        return toFeed

    def askHowManyAcresToPlant():
        print("How many acres to plant with your available grains?")
        print("(You must have enough acres, enough grain, and enough people to do the planting)")
        try:
            acres = int(input(">> "))
            if acres < 0:
                print("only positive numbers please\n")
                Hamurabiv2.askHowManyAcresToPlant()
        except ValueError:
            print("numbers only please\n")
            Hamurabiv2.askHowManyAcresToPlant()
        return acres

    def plague_chance(population):
        chance = random.randint(1, 100)
        plague_deaths = 0
        if chance <= 15:
            plague_deaths = population / 2
            return plague_deaths
        else:
            return plague_deaths

    def starvation_deaths(population, bushels):
        peopleFed = math.floor(bushels/20)
        starved_folk = population - peopleFed
        if starved_folk < 0:
            return 0
        else:
            return starved_folk

    def uprising_flag(population, starved_folk):
        return float(starved_folk/population) > 0.45


    def immigrants(population, acresOfLand, bushels_in_storage):
        immigrant_total = int((20 * acresOfLand + bushels_in_storage) / (100 * population))
        return immigrant_total

    def grain_eaten_by_rats(bushels):
        chance = random.randint(1, 100)
        if chance < 40:
            percent_eaten = random.randint(10, 30)
            return bushels // (percent_eaten / 100)
        else:
            return 0

    def harvest(acres, bushels):
        acres = bushels // 2
        crop_yield = random.randint(1, 6)
        return acres_planted * crop_yield

    def new_cost_of_land():
        landValue = random.randint(17, 23)
        return landValue



if __name__ == '__main__':
    Hamurabiv2().play_game()