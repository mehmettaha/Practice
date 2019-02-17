import random

def game():
    no = random.randint(1,9)
    i = 0
    while True:
        guess = input("Try to guess the number:")
        if guess != "Exit":
            i += 1
            guess = int(guess)
            if guess > no:
                print("Go lower")
            elif guess < no:
                print("Go higher")
            else:
                print("Got it\nYou took %d tries\nAnother round" % i)
                break
        else:
            return 0

while True:
    
    if game() == 0:
        print("End")
        break

    

