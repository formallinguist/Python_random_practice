#2.8 Guess game
def guess_game():
    print("What is my favourite food? ")
    guess = input("Try it: ")
    while guess != "chocolate":
        print("You are wrong")
        guess = input("Try it again: ")
    return "You guessed it!!!"


print(guess_game())