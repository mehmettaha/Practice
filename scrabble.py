import random
words = []
with open("sowpods.txt","r") as f:
    words = list(f)

def play(target):
    current = ["-" for i in target]
    guessed_letters = []
    for turn in range(5,-1,-1):
        print("Your current word is %s" % ("".join(current)))
        while True:    
            guess, *_ = input("Guess a letter: ").lower()
            if guess in guessed_letters:
                print("You already tried that letter")
            else:
                break
        guessed_letters.append(guess)
        if guess in target:
            for i, c in enumerate(target):
                if c == guess:
                    current[i] = guess
        else:
            print("No %s" % guess)
        print("You have %d tries remaining" % turn)
        if "".join(current) == target:
            return True
    return False

target = random.choice(words).rstrip("\n")
target = target.lower()
    
if play(target):
    print("You guessed the word! It was %s" % target)
else:
    print("Sorry, it was %s" % target)

