#Try to turn string to int and return True if it throws no errors
def isInt(string): 
    try: 
        int(string)
        return True

    except ValueError:
        return False

def isLeapYear(year):
    #Is a leap year because it's divisible by 400
    if year % 400 == 0:
        return True

    #Is NOT a leap year because it's divisible by 100 and not by 400
    elif year % 100 == 0:
        return False

    #Is a leap year because it's divisible by 4 and not divisible by 100
    elif year % 4 == 0:
        return True

    #Is NOT a leap year because it's not divisible by 4 or 400
    return False

while True:
    year = input("Enter a year: ")

    if not isInt(year):
        print("enter ONLY NUMBERS please")

    else:
        year = int(year)

        #Evaluate leap year
        if isLeapYear(year):
            print(str(year) + " is leap year")
        else:
            print(str(year) + " is not leap year")
    
    print("")