import math
import random


class Hamurabiv2(object):
    def play_game(self):
        Hamurabiv2.introduction()
        print("Let's play!")

        # Player Stats
        population = 100
        bushels = 2800
        acresOfLand = 1000
        landValue = 19  # bushels per acres
        year = 0

        # Player Decisions
        acres_planted = 0
        bushels_fed = 0

        # EOY Counter
        peopleDied = 0
        harvested_bushels = 0
        totalLand = 0
        starved_folk = 0
        immigrant = 0
        cropyield = 0
        rat_damage = 0
        bushels_in_storage = 0  # bushels_in_storage should equal player bushels. may be redundant

        # EOG Counter
        starved_folk_total = 0

        gameON = True
        while gameON == True:
            year += 1
            while True:
                print("Are you looking to buy or sell land?")
                print(f"(You have {acresOfLand} acres of land available)")
                print("(1) to buy, (2) to sell")
                try:
                    choice = int(input(">> "))
                    if choice == 1:
                        acreBought = Hamurabiv2.askHowManyAcresToBuy()
                        while True:
                            if acreBought * landValue > bushels:
                                print("O Hammurabi, I admire your enthusiasm, but we sadly don't have enough grain!")
                                acreBought = Hamurabiv2.askHowManyAcresToSell()
                            else:
                                break
                        acresOfLand += acreBought
                        bushels -= (acreBought * landValue)
                        print(f"you have {acresOfLand} acres of land and {bushels} bushels\n")
                        break
                    elif choice == 2:
                        acresToSell = Hamurabiv2.askHowManyAcresToSell()
                        while True:
                            if acresToSell > acresOfLand:
                                print("O Hammurabi, you would sell our entire kingdom and some of our neighbor's?\n"
                                    "It would be impossible to sell more than we have.")
                                acresToSell = Hamurabiv2.askHowManyAcresToSell()
                            else:
                                break
                        acresOfLand -= acresToSell
                        bushels += (acresToSell * landValue)
                        print(f"you have {acresOfLand} acres of land now\n")
                        break
                    else:
                        print("That's not an option\n")
                except ValueError:
                    print("numbers only please\n")

            while True:
                print(f"(You have {bushels} bushels available. Our population is {population}.)")
                bushels_fed = Hamurabiv2.askHowMuchGrainToFeedPeople()
                if bushels_fed <= bushels:
                    bushels -= bushels_fed
                    print(f"(You have {bushels} left)\n")
                    break
                else:
                    print("You don't have enough bushels\n")
            while True:
                print(f"(You have {acresOfLand} acres, {bushels} bushels, and {population} people)")
                acres_planted = Hamurabiv2.askHowManyAcresToPlant(population, acresOfLand, bushels)
                print(f"planting {acres_planted} acres")
                bushels -= (acres_planted * 2)  # this may be where we're getting a negative number.
                print(f"You have {bushels} left after planting.\n")
                break

            # Tallying EOY results
            peopleDied = Hamurabiv2.plague_chance(population)
            starved_folk = Hamurabiv2.starvation_deaths(population, bushels_fed)
            starved_folk_total += starved_folk
            peopleDied += starved_folk
            if starved_folk > 0 and Hamurabiv2.uprising_flag(population, starved_folk):
                gameON = False
                print("\nToo many of your people have gone hungry, Hammurabi!\n"
                      "You are no longer ruler.")
                break
            if starved_folk == 0:
                immigrant = Hamurabiv2.immigrants(population, acresOfLand, bushels_in_storage)
            harvest_and_yield = Hamurabiv2.harvest(acres_planted)
            harvested_bushels = harvest_and_yield[0]
            cropyield = harvest_and_yield[1]
            if bushels > 0:
                rat_damage = Hamurabiv2.grain_eaten_by_rats(bushels)
            landValue = Hamurabiv2.new_cost_of_land()

            # Updating Player Stats with EOY results
            population -= peopleDied
            population += immigrant
            bushels -= rat_damage
            bushels += harvest_and_yield[0]
            rat_damage = 0
            immigrant = 0

            # EOY Result Screen / EOG Grade
            Hamurabiv2.summary(year, starved_folk, immigrant, population, harvested_bushels,
                     cropyield, bushels, rat_damage, acresOfLand, landValue)

            if year == 10:
                Hamurabiv2.final_result(starved_folk_total, acresOfLand, population)
                gameON = False
        Hamurabiv2.play_again()



    def introduction():
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

    def askHowManyAcresToBuy():  # needs a check against bushels, could push us negative
        while True:
            print("How many acres of land would you like to buy?")
            try:
                acresToBuy = int(input(">> "))
                if acresToBuy < 0:
                    print("only positive numbers please\n")
                    Hamurabiv2.askHowManyAcresToBuy()
                return acresToBuy
            except ValueError:
                print("numbers only please\n")

    def askHowManyAcresToSell():
        while True:
            print("How many acres of land would you like to sell?")
            try:
                acresToSell = int(input(">> "))
                if acresToSell < 0:
                    print("only positive numbers please\n")
                    Hamurabiv2.askHowManyAcresToSell()
                return acresToSell
            except ValueError:
                print("numbers only please\n")

    def askHowMuchGrainToFeedPeople():
        while True:
            print("How much grains would you like to feed your people?")
            try:
                bushels_fed = int(input(">> "))
                if bushels_fed < 0:
                    print("only positive numbers please\n")
                    Hamurabiv2.askHowMuchGrainToFeedPeople()
                return bushels_fed
            except ValueError:
                print("numbers only please\n")

    def askHowManyAcresToPlant(current_population, acres_owned, bushels_owned):
        max_acres_per_manpower = current_population * 10
        max_acres_with_owned_grain = bushels_owned / 2
        while True:
            print("How many acres to plant with your available grains?")
            print("(You must have enough acres, enough grain, and enough people to do the planting)")
            try:
                acres = input(">> ")
                if int(acres) < 0:
                    print("Only positive numbers please\n Our harvest will come in time!\n")
                    continue
                elif int(acres) > max_acres_per_manpower:
                    print("Wise Hammurabi, surely our kingdom will have the manpower"
                      "for that in time, but we currently do not!")
                    continue
                elif int(acres) > max_acres_with_owned_grain:
                    print("O Hammurabi, were you to provide more grain we would happily "
                      "oblige!")
                    continue
                return int(acres)
            except ValueError:
                print("numbers only please\n")
                continue

    def plague_chance(population):
        chance = random.randint(1, 100)
        plague_deaths = 0
        if chance <= 15:
            plague_deaths = population // 2
            print("O Hammurabi! A horrible plague has killed so many citizens!")
            return plague_deaths
        else:
            return plague_deaths

    def starvation_deaths(population, bushels):
        peopleFed = bushels // 20
        starved_folk = population - peopleFed
        if starved_folk <= 0:
            return 0
        else:
            return int(starved_folk)

    def uprising_flag(population, starved_folk):
        return float(starved_folk / population) > 0.45

    def immigrants(population, acresOfLand, bushels_in_storage):
        immigrant_total = int((20 * acresOfLand + bushels_in_storage) / (100 * population))
        return immigrant_total

    def grain_eaten_by_rats(stored_bushels):
        if stored_bushels == 0:
            return 0
        chance = random.randint(1, 100)
        if chance < 40:
            percent_eaten = random.randint(10, 30)
            return int(stored_bushels * (percent_eaten // 100))
        else:
            return 0

    def harvest(planted_acres):
        crop_yield = random.randint(1, 6)
        return planted_acres * crop_yield, crop_yield

    def new_cost_of_land():
        landValue = random.randint(17, 23)
        return landValue


    def summary(year, starved_people, immigrant_arrivals, population, harvest_bushels,
                 bushels_per_acre, bushels_stored, rat_damage, acres_owned, land_value):
        # figure out the strings to keep this code for the last year & just plug in the alternate strings?
        # Would also be nice to be able to change time period / setting of the game.
        # string_changes = (("You are in year", "This was year ten"),
        #                   ("In the previous year", "Over the years"),
        #                   ("The population is now", "Our great kingdom has grown from 100 proud citizens to"),
        #                   ("Over your rule we harvested"
        print("O great Hammurabi!")
        print(f"These are the results of year {year} of your ten year rule")
        print(f"In the previous year {starved_people} starved to death.")
        if starved_people == 0:
            print(f"In the previous year {immigrant_arrivals} immigrant(s) added to our population.")
        print(f"The population is now {population}.")
        print(f"We harvested {harvest_bushels} bushels at {bushels_per_acre} bushels per acre.")
        print(f"Rats destroyed {rat_damage} bushels, leaving {bushels_stored} bushels in storage.")
        print(f"The city owns {acres_owned} acres of land.")
        print(f"Land is currently worth {land_value} per acre.")


    def final_result(total_people_starved, acres, end_population):
        # started w/ 10 acres per person
        acres_per_person = acres / end_population
        if total_people_starved < 30 and acres_per_person >= 12:
            print("O Hammurabi! Our kingdom has never flourished so!"
                  "The people clamor for your continued rule!")
        elif total_people_starved < 50 and acres_per_person >= 11:
            print("Hammurabi, your reign was as we expected. Our kingdom continues on.")
        else:
            print("Your reign has ended, may your next endeavors be more to your abilities.")

    def play_again():
        print("Would you like to play again? Enter Y or N")
        response = input(">> ")
        if response == 'Y' or 'y':
            Hamurabiv2().play_game()
        else:
            print("Thanks for playing!")

if __name__ == '__main__':
    Hamurabiv2().play_game()
