print("Welcome to my General Knowledge Quiz!")
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Ask if the user wants to play
playing = input("Do you want to play? (yes/no): ").strip().lower()
if playing != "yes":
    print("Alright! See you next time. Goodbye!")
    quit()

print("Okay! Let's play :)")

# List of questions and answers
questions = [
    ("What is the opposite of tall?", "short"),
    ("What is the correct past tense of go?", "went"),
    ("What do we call a baby cat?", "kitten"),
    ("What sound does a dog make?", "bark"),
    ("What is the opposite of happy?", "sad"),
    ("Which part of the plant is usually green?", "leaf"),
    ("What is the name of our galaxy?", "milky way"),
    ("What do we call animals that eat only plants?", "herbivores"),
]

score = 0

# Loop through questions
for question, correct_answer in questions:
    answer = input(question + " ").strip().lower()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is '{correct_answer}'.")

# Display final results
print(f"\nYou got {score} out of {len(questions)} questions correct.")
percentage = (score / len(questions)) * 100
print(f"Your score: {percentage:.2f}%")

# Add performance feedback
if percentage == 100:
    print("Excellent! You're a genius! 🎉")
elif percentage >= 75:
    print("Great job! You did really well! 👍")
elif percentage >= 50:
    print("Good effort! Keep learning. 😊")
else:
    print("Don't worry, try again next time! 💪")

