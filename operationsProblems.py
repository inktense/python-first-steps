# Solve the following:

# 1. The population of a town is 198568. Out of them 45312 are men and 35678 are women. Find the number of children in the town.
total_population = 198568
women = 35678
men = 45312

children = total_population - women -men
print('Number of children is', children)

# 2. A shopkeeper has 2425 boxes of 24 pencils each. How many pencils do all the boxes have in all?
total_boxes = 2425

total_pencils = total_boxes * 24
print('Number of pencils is', total_pencils)

# 3. Linda bought a coat for $2265 and a saree for $2150. 
# She gave $5000 to the shopkeeper. How much money did the shopkeeper return to her?
coat_cost = 2265
saree_cost = 2150
total_amount = 5000

rest = total_amount - coat_cost - saree_cost
print("Linda's rest is ${}".format(rest))

# 4. The cost of 21 TV sets is $95844. Find the cost of one TV set.
TV_cost = 95844 / 21
print("Cost of one TV is ${}".format(int(TV_cost)))


# 5. A factory produces 24532 bulbs in a month. What is its annual production?
annual_production = 24532 * 12
print("Annual production is", annual_production)

# 6. There are 86 rooms in a school. 4356 students study there. Equal number of students sits in each room?
rooms_number = 86
students_number = 4356

# Rounding up the number
students_in_room_number = int(students_number / rooms_number) + (students_number % rooms_number > 0)
print("Numbers of students in a room", students_in_room_number)

# 7. 1575 students of a school want to go to Agra by bus. 
# If one bus can carry 75 students, how many buses are required to carry all the students?
bus_places_number = 75
students_number = 1575

# Rounding up the number
buses_number = int(students_number / bus_places_number) + (students_number % bus_places_number > 0)
print("Numbers of buses needed", buses_number)

# 8. Maria bought 96 toys priced equally for $12960. The amount of $1015 is still left with her. 
# Find the cost of each toy and the amount she had.
toys_number = 96
total_price = 12960

total_amount = total_price + 1015
toy_price = total_price / toys_number

print("One toy costs {}$ and Maria initially had {}$".format(toy_price, total_amount))
