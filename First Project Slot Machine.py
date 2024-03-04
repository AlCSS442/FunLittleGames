import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What is the amount you are depositing? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 please")
        else:
            print("Enter a number please")
    
    return amount

def get_number_of_lines():
    while True: # while loop, use break to end while loop
        lines = input("Enter the number of lines to bet on please on (1-" + str(MAX_LINES) + ")? ") #creating a string
        if lines.isdigit():
            lines = int(lines) #makes sure the value entered is a whole integer
            if 1 <= lines <= MAX_LINES: #makes sure the value entered is in the parameters, in this case, if its in between 2 values
                break
            else:
                print("Enter a valid number of lines please")
        else:
            print("Enter a number please")
    
    return lines
def how_much_on_each_line():
    while True:
        amount = input("Enter how much you would like to bet on each line please? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be between ${MIN_BET} - ${MAX_BET} please")  # This is what you're saying but in a fancier way("Amount must be between 1 and 100 please")
                #in Line 40, you're imbedding values inside of your strings--> put f in front of the string and then use the squiggly brackets for the variables and it should automatically convert it into a string 
        else:
            print("Enter a number please")
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet= how_much_on_each_line ()
        total_bet = bet * lines 

        if total_bet > balance:
            print (
                f"Your balance funds are insufficient to bet that amount. Your current balance is ${balance} ")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet} ")
    print(balance, lines)
            
main()