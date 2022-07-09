import random
# random.randint(0,5) --> will return a number from 1 to 5 (integer)
# random.random() --> 0.0 to less than 1.0


def plague_chance(population):
    chance = random.randint(1, 100)
    plague_deaths = 0
    if chance <= 15:
        plague_deaths = population / 2
        return plague_deaths
    else:
        return plague_deaths


def starvation_deaths(population, bushels_fed_to_people):
    people_we_can_feed = bushels_fed_to_people // 20
    starved_folk = population - people_we_can_feed
    if starved_folk < 0:
        return 0
    else:
        return starved_folk


def uprising_flag(population, how_many_people_starved):
    return float(how_many_people_starved/population) > 0.45        # check this one that it returns a boolean


# how to flag this based on starvation? can do in nested function or in main app when how_many_people_starved > 0
def immigrants(population, acres_owned, grain_in_storage):
    immigrant_total = int((20 * acres_owned + grain_in_storage) / (100 * population))
    return immigrant_total


def harvest(acres, bushels_used_as_seed): #double check bbbyyyy
    crop_yield = random.randint(1, 6)
    # plantable_acres = bushels // 2
    # max_acres_harvestable = population * 10 // bushels_used_as_seed
    # plantable_acres = bushels_used_as_seed
    result = [acres * crop_yield, crop_yield]
    return result


def grain_eaten_by_rats(bushels):
    chance = random.randint(1, 100)
    if chance < 40:
        percent_eaten = random.randint(10, 30)
        return bushels // (percent_eaten / 100)
    else:
        return 0


def new_cost_of_land():
    return random.randint(17,23)


def print_result(year, starved_people, immigrant_arrivals, population, harvest_bushels,
                 bushels_per_acre, bushels_stored, rat_damage, acres_owned, land_value):
    # figure out the strings to keep this code for the last year & just plug in the alternate strings?
    # Would also be nice to be able to change time period / setting of the game.
    # string_changes = (("You are in year", "This was year ten"),
    #                   ("In the previous year", "Over the years"),
    #                   ("The population is now", "Our great kingdom has grown from 100 proud citizens to"),
    #                   ("Over your rule we harvested"
    print("O great Hammurabi!")
    print(f"You are in year {year} of your ten year rule")
    print(f"In the previous year {starved_people} starved to death.")
    print(f"In the previous year {immigrant_arrivals} entered the kingdom.")
    print(f"The population is now {population}.")
    print(f"We harvested {harvest_bushels} bushels at {bushels_per_acre}." )
    print(f"Rats destroyed{rat_damage} bushels, leaving {bushels_stored} bushels in storage.")
    print(f"The city owns {acres_owned} acres of land.")
    print(f"Land is currently worth {land_value} per acre.")


def final_result(total_people_starved, acres, end_population):
    # started w/ 10 acres per person
    acres_per_person = acres / end_population
    if total_people_starved < 20 and acres_per_person > 12:
        print("O Hammurabi! Our kingdom has never flourished so!")
    elif total_people_starved < 50 and acres_per_person > 11:
        print("Hammurabi, your reign was as we expected. Our kingdom continues on.")
    else:
        print("Your reign has ended, may your next endeavors be more to your abilities.")
    print("Your reign has ended.")


