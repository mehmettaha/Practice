def guess(high, low):
    return int((high+low)/2)

def game():
    low = 0
    high = 100
    answer = ""
    prev = []  

    while True:
        x = guess(low, high)
       
        if x in prev:
            print("Cheater!")
            break
       
        answer = input("Is the number %d? Answer with 'Go higher', 'Go lower', 'Correct'" % x)  
       
        if answer == "Go higher":
            low = x
        if answer == "Go lower":
            high = x
        if answer == "Correct":
            break
       
        prev.append(x)
    print("Computer wins")

game()