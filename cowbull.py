import random
def cowbull(x, guess):
    cows = 0
    bulls = 0
    for i in range(0,4):
        if guess[i] == x[i]:
            cows += 1
        elif guess[i] in x:
            bulls += 1
    return cows, bulls

x = str(random.randint(1000,9999))
guess = input("Try to guess the random number: ")

while x != guess:
    cow, bull = cowbull(x, guess)
    print("You have %d cows and %d bulls" % (cow,bull))
    guess = input("Try to guess the random number: ")

print("Congratulations!")

