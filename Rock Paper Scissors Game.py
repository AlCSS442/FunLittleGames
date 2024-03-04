import random 

user_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissors"]
# this is a list that is stored in a variable. A list is a data structure, which is a collection of elements and strings stored in a list. The way to access the different elements in the variable is to use an index.

while True:
    user_input = ("Choose an element; Rock, Paper, Scissors or Q to quit: ") . lower()
    #make variables equal to 0 if data type is not numeric!
    if user_input == "q":
        break
    #breaks up the loop and takes it straight to the end function
    
    if user_input not in options:
    #creating a list, so that we don't have to create 3 if statements
        continue
    #if user did not choose something in the paranthesis, it will restart the loop to "Choose an element" string

    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors" : 
    #the "and" checks if boths conditions are strue in the string
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock" :
        print("You won!")
        user_wins += 1       

    elif user_input == "scissors" and computer_pick == "paper" :
        print("You won!")
        user_wins += 1
        
    else:
        print("You lost!")
        computer_wins +=1
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print ("Goodbye!")