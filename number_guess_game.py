import random

Computer = random.randint(1,100)
guesses = 0
attempts = 0

print("Welcome to Rahul's  Number Guessing Game")
print("Choose any number between 1 to 100. You only have 6 guesses. Good luck!")
#Guess until player has no more returns
while guesses != Computer and attempts < 6:
    num = input("Enter your guessed Number! :\n")
    try:
        guesses = int(num)
    except:
        print("Please Choose Integer Value ")
        quit()
    if guesses < Computer:
        print ("Low Number Entered. Enter Higher Guesses")
    if guesses > Computer:
        print ("High Number Entered. Enter Lower Guesses")
    attempts = attempts + 1


if guesses == Computer:
    print (f"Congratulations! \n You Win!!! \n Total Attempts = {attempts}")
else:
    print("Sorry ! You Loose!")
    print(f"The Secret Number was: {Computer}")