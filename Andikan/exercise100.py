def year():
      a = int(input("Enter your year: "))
  
def month():
    b = int(input("Enter month 1-12: "))
    
    if b == 9 or b == 4 or b == 6 or b == 11:
      return print(30)
    
    elif b == 1 or b == 3 or b == 5 or b == 7 or b == 10 or b == 12:
      return print(31)
    
    elif b == 2 and a % 4 == 0:
      return print("29 because its a leap year")
    elif b == 2 and a % 4 != 0:
      return print(28)   
    
month()
year()
