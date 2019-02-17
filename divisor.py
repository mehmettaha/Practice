x = int(input("Enter a number : "))

def primetest(x):
    for i in range(2, int(x/2 +1)):
        if x%i == 0:
            return False
    return True

if primetest(x) is True:
    print("%d is a Prime number" % x)
else:
    print("%d is Not a prime number" % x )
