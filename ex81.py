"""
Exercise 81: Compute the Hypotenuse
(23 Lines)
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
"""
def hyp(opp,adj):
    fr=opp**2+adj**2
    return(fr)
print('the length of the longest side is:',hyp(2,2))
