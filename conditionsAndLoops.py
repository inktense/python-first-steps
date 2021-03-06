# You're planning a vacation, and you need to decide which city you want to visit.
# You have shortlisted four cities and identified the return flight cost, daily hotel cost, and weekly car rental cost.
# While renting a car, you need to pay for entire weeks, even if you return the car sooner.

# City 	Return Flight ($) 	Hotel per day ($) 	Weekly Car Rental ($)
# Paris 	200 	20 	200
# London 	250 	30 	120
# Dubai 	370 	15 	80
# Mumbai 	450 	10 	70

# Answer the following questions using the data above:

#     If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
#     How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?
#     If your total budget for the trip is $1000, which city should you visit to maximize the duration of your trip?
#     Which city should you visit if you want to minimize the duration?
#     How does the answer to the previous question change if your budget is $600, $2000, or $1500?

import math

# Defining cities as dictionaries


def city_data(city, flight, hotel, car):
    return {
        'name': city,
        'flight': flight,
        'hotel': hotel,
        'car': car
    }


paris = city_data("Paris", 200, 20, 200)
london = city_data("London", 250, 30, 120)
dubai = city_data("Dubai", 370, 15, 80)
mumbai = city_data("Mumbai", 450, 10, 70)

cities = [paris, london, dubai, mumbai]


def cost_of_trip(city, num_days=0):
    return city['flight'] + (city['hotel'] * num_days) + (city['car'] * math.ceil(num_days / 7))


def days_to_visit_cost(days):
    costs = []
    for city in cities:
        cost = cost_of_trip(city, days)
        costs.append((cost, city['name']))
    return min(costs)

# Responses to first set of questions
print('Responses to first set of questions')
print(days_to_visit_cost(7))
print(days_to_visit_cost(4))
print(days_to_visit_cost(10))
print(days_to_visit_cost(14))


def with_budget(budget, less_days=False):
    days = 1
    cost = 0

    while cost < budget:
        cost_before = cost
        try:
            costs_before = costs.copy()
        except:
            # if costs dictionary doesn't exist, create an empty dictionary
            costs_before = {}
        costs = {}
        for city in cities:
            cost = cost_of_trip(city, days)
            costs[cost] = city['name']

        if less_days:
            cost = max(list(costs.keys()))
            if cost >= budget:
                return days-1, costs_before[cost_before]
        else:
            cost = min(list(costs.keys()))
            if cost >= budget:
                return days-1, costs_before[cost_before]

        days += 1


# Responses to second set of questions
print('Responses to second set of questions')
print(with_budget(600))
print(with_budget(600, less_days=True))
print(with_budget(1000))
print(with_budget(1000, less_days=True))
print(with_budget(2000))
print(with_budget(2000, less_days=True))
print(with_budget(1500))
print(with_budget(1500, less_days=True))

