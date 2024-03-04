name = input("What is your name? ")
if name.isalpha():
#always returns the input as a string, even if the user inputs a number
    print("Hello " + name)
else:
    print("Please enter a valid name.")
    quit()

birth_year = input("What year were you born?: ")
if birth_year.isdigit():
    #this line of code checks if the input is a digit
    birth_year = int(birth_year)
    #this converts the string into a digit
    if birth_year <= 0:
        print ("Please type a number larger than 0 next time")
        quit()
    if birth_year >= 2023:
        print ("Please type a valid birth year.")
        quit()
else:
    print("Please type a number next time")
    quit()
age = 2023 - birth_year
print("You are " + str(age) + " years old.")

