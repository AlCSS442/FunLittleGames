print("Welcome to the quiz!")

playing = input("Would you like to continue? ")
if playing.lower() != "yes":
    quit()
print ("Let the games begin!")

followup = input ("Are you ready...?")
if followup.lower() != "yes":
    quit()
score=0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What does Ram stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print ("Incorrect!")

print("You got " + str(score) + " questions correct!"  )
