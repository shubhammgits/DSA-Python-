# prime numbers between a range:

def printPrimeNum(a,b):
    for i in range(a,b+1):
        if i%i == 0:
            print(i)

printPrimeNum(1,10)
