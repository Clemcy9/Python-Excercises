"""
Exercise 83: Shipping Calculator
(23 Lines)
An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item, and $2.95 for each subsequent item. Write a function that takes the
number of items in the order as its only parameter. Return the shipping charge for
the order as the function’s result. Include a main program that reads the number of
items purchased from the user and displays the shipping charge
"""

import re


def shipping(numberOFitems):
    rate_for_1 = 10.95
    if numberOFitems ==1 or numberOFitems== 0:
        return rate_for_1
    multi_rate = ((numberOFitems-1) * 2.95) + 10.95
    return multi_rate

print('you purchased 5 items and your shipping fee is:',shipping(5))

print('you purchased 1 items and your shipping fee is:',shipping(1))