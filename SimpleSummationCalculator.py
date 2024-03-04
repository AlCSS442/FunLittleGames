first_number = input("Type a number")
if first_number.isdigit():
    print(first_number)
else:
    print("Please type in a number.")
    quit()
second_number = input("Please type the second number.")
if second_number.isdigit():
    sum = float(first_number) + float(second_number)
    #need to use the float function because the number could have a decimal
    print("The sum is " + str(sum) + ".")
    quit()