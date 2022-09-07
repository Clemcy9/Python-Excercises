'''
Exercise 82: Taxi Fare
(22 Lines)
In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters traveled. Write a function that takes the distance traveled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function
'''


def fare(distance):
    base_fare = 4.00
    added_fare =0.25
    distance_in_meters = distance * 1000
    multiplication_factor = distance_in_meters//140
    return ((multiplication_factor*added_fare)+base_fare)

print(fare(12))






