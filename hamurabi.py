import random
# random.randint(0,5) --> will return a number from 1 to 5 (integer)
# random.random() --> 0.0 to less than 1.0

    def plague_chance(population):
        chance = random.random()
        plague_deaths = 0
        if chance <= 0.15:
            plague_deaths = population / 2
            return plague_deaths
        else:
            return plague_deaths


    def starvation_deaths(population, bushels_fed_to_people):
        people_we_can_feed = bushels_fed_to_people // 20
        starved_folk = population - people_we_can_feed
        if starved_folk < 0:
            return 0.0
        else:
            return starved_folk


    def uprising_flag(population, how_many_people_starved):
            return float(how_many_people_starved/population) > 0.45        #check this one that it returns a boolean


    # how to flag this based on starvation?
    def immigrants(population, acres_owned, grain_in_storage):
        immigrant_total = int((20 * acres_owned + grain_in_storage) / (100 * population))
        return immigrant_total


    def harvest(acres, bushels_used_as_seed):
        acres_planted = bushels_used_as_seed // 2
        crop_yield = random.randint(0,3)
        return acres_planted * crop_yield


    def grain_eaten_by_rats(bushels):
        chance = random.random()
        if chance < 0.40:
            percent_eaten = random.randint(10, 30)
            return bushels // (percent_eaten / 100)
        else:
            return 0


    def new_cost_of_land():
        return random.randint(17,23)