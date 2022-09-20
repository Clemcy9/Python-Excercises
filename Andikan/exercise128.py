
'''
Write a function named reverseLookup that finds all of the keys in a dictionary
that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program
'''
def reverseLookup(dictionary, value):
    keys = []
    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)
    return keys

myDict = {
    'name':'Andikan',
    'username':'Andikan',
    'age':19,
    'height':'177cm',
    'blood group':'o+'
}

print(reverseLookup(myDict,'Andikan'))
print(reverseLookup(myDict,19))
print(reverseLookup(myDict,18)) 
