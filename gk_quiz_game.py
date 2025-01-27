print("Welcome to my gk quiz!")
name = input("Enter you name : ")
print(name)


playing = input("Do you want to play ? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay! let's play :) ")
    
    
score = 0
answer = input("What is the opposite of tall ? ")
if answer.lower() == "short":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the correct past tense of go ? ")
if answer.lower() == "went":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What do we call a baby cat ? ")
if answer.lower() == "kitten":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What sound does a dog make ? ")
if answer.lower() == "bark":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the opposite of happy ? ")
if answer.lower() == "sad":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which part of the plant is usually green ? ")
if answer.lower() == "leaf":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of our galaxy ? ")
if answer.lower() == " milky way ":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What do we call animals that eat only plants ? ")
if answer.lower() == "herbivores":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got "+str(score)+" correct answers out of 8.")
print("You got "+str(score/8 * 100)+"%")
