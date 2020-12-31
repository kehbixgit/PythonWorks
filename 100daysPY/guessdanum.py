import random as randomlib
random = randomlib.randint(1,23)
print ("Guess a number between 1 and 20")
while True:
    guess = int(input ())
    if guess < random:
        print ("Too low now")
    elif guess > random:
        print ("Oh Oh, too high")
    else:
        print ("That's right now!")
        break