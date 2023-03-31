import math

#https://mathworld.wolfram.com/Semiprime.html
#https://mathworld.wolfram.com/PrimeCountingFunction.html

#Try to turn string to int and return True if it throws no errors
def isNumber(string): 
    try: 
        int(string)
        return True

    except ValueError:
        return False

def isInt(numb):
    #If the number minus itself rounded up doesn't equal zero then it's not an iteger
    return (numb - math.floor(numb)) == 0


def isPrime(numb):
    #If number is a decimal, it can't be a prime
    if not isInt(numb):
        return False

    #For every number that can be a multiple and isn't one or the number
    for i in range(2, int(math.sqrt(numb))+ 1):
        #If it's divisible by that number it can't be a prime
        if(numb % i == 0):
            return False

    return True


def isSemiprime(numb):
    #If the number is a prime, it can't be a semiprime
    if isPrime(numb):
        return False

    #If it's the square of a prime, it's a semiprime
    if isPrime(math.sqrt(numb)):
        return True

    #Number can only have 2 divisors
    primeFactors = 0

    for i in range(2, int(numb) - 1):
        #If it's divisible by i
        if numb % i == 0:
            #If i isn't a prime it can't be a semiprime
            if not isPrime(i):
                return False

            #If it's divisible by a prime
            else:
                #Up the prime counter by one
                primeFactors += 1
                
                #If there's more than two prime factors, then it's not a semiprime
                if(primeFactors > 2):
                    return False
    return True


def findPrimes(start, end):
    res = []

    if start < 0 or end < 0:
        print("START AND END RANGE MUST BOTH BE POSITIVE INTEGER")
        return False

    if end < start:
        print("END OF RANGE MUST BE BIGGER THAN START")
        return False

    #Do a loop and append all tested semiprimes to the list
    for numb in range(start, end):
        if isSemiprime(numb):
            res.append(numb)

    return res


print("SEMIPRIMEFINDER 9000 AWAITING INPUT...")

while True:
    #Ask and validate user input
    command = input("\nSTART OF RANGE: ")
    if not isNumber(command):
        print("NOT A NUMBER, PLEASE TRY AGAIN")
        continue

    start = int(command)

    command = input("END OF RANGE: ")
    if not isNumber(command):
        print("NOT A NUMBER, PLEASE TRY AGAIN")
        continue

    end = int(command)
    res = findPrimes(start, end)

    if res is False:
        print("SILLY HUMAN")
    
    else:
        print("FOUND " + str(len(res)) + " SEMIPRIMES")
        print(res)