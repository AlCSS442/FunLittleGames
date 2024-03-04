print("Welcome to the quiz!")

playing = input("Would you like to continue? ")
if playing.lower() != "yes":
    quit()
print ("Let the games begin!")

followup = input ("Are you ready...?")
if followup.lower() != "yes":
    quit()
score=0

answer = input("what is the largest life form on earth? ")
if answer.lower() == "fungi":
    print("Correct! Can you believe that fungal mycelium can grow for miles underground in search of food!")
    score += 1
else:
    print ("Incorrect! The correct answer is fungi. Can you believe that fungal mycelium can grow for miles underground in search of food!")

answer = input("What is the scientific name for a fungi cell? ")
if answer.lower() == "eukaryote":
    print("Correct!")
    score += 3
else:
    print ("Incorrect! The correct answer is eukaryote.")

answer = input("Which type of fungi is formed by filaments called hyphae? ")
if answer.lower() == "yeast":
    print("Correct! Mold sometimes looks furry beacause its hyphae grows upwards and releases more mold spores from their tips.")
    score += 1
else:
    print ("Incorrect! The correct answer is yeast. Did you know that mold sometimes looks furry, as it is the hyphae that grows upwards and releases more mold spores from their tips!")

answer = input("What is the study of fungi called? ")
if answer.lower() == "mycology":
    print("Correct!")
    score += 1
else:
    print ("Incorrect! The correct answer is mycology.")

print("You got " + str(score) + " questions correct!"  )
print("You got " + str((score/4)*100) + "%."  )
