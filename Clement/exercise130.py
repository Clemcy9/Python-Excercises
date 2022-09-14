"""
On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first letter on the
key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
character listed for that key.
Key Symbols
1 .,?!:
2 ABC
3 DEF
4 GHI
Exercise 130:Text Messaging 63
5 JKL
6 MNO
7 PQRS
8 TUV
9 WXYZ
0 space
"""
def words2key(test):
    keypad={
        '1':['.',',','?','!'],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
        '0':[' ']
        }
    # list for storing result of mapping
    result=[]
    final_res=''
    #iterate over the user text and search through the keypad array as well
    for i in test:
        # print(i)
        for k,v in keypad.items():
            if i in v:
                # print(f'found {i} at index of {(v.index(i)+1)*k} ')
                temp =(v.index(i)+1)*k
                result.append(temp)

    #convert array to strings
    final_res=final_res.join(map(str,result))
    # print(result)
    print(final_res)

words2key('hello world, Jesus is coming again')