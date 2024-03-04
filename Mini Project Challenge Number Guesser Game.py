# https://www.youtube.com/watch?v=DLn3jOsNRVE&t=1783s

import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    #this line of code checks if the input is a digit
    top_of_range = int(top_of_range)
    # 30.25 of the video, this line of code is needed to convert the string into an integer, otherwise the program wont register the input as an integer
    if top_of_range <= 0:
        print ("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
    
random_number = random.randint(0,top_of_range)
# random.randrange the last number in the paranthesis will not be included in the range 
# so to make a range of -1 to 10, need to put -1 and 11 in the paranthesis
# random.randint will include all the numbers in the interval, including the endpoints
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    #else: Can have it written like this, but a more elegant way to write it is using elif
        #if user_guess > random_number:
            #print ("Not quite. You are above the number.")
        #else:
            #print ("Not quite. You are below the number.")
    elif user_guess > random_number:
        print ("Not quite. You are above the number.")
    else: 
        print ("Not quite. You are below the number.")

print ("You got it in", guesses, "guesses")
#or can write it as print("You got it in" + str(guesses) + "guesses")
#line 38 is the simplified verson --> can write in simplified version b/c the print statement already converts the integer into a string




