# Define the questions, options, and correct answers
questions = [
    "What type of race is the Tour de France?",
    "How many holes in a golf competition?",
    "Who is the boxer who fought Muhammad Ali?",
    "How many circles in the Olympic emblem?"
]

options = [
    ["a. bicycle", "b. ice skating", "c. running", "d. volleyball"],
    ["a. 8", "b. 12", "c. 10", "d. 11"],
    ["a. Manny Pacquiao", "b. Oscar Dela Hoya", "c. Joe Frazier", "d. Floyd Mayweather"],
    ["a. 5", "b. 4", "c. 3", "d. 6"]
]

correct_answers = ["a", "b", "c", "a"]

# Display the questions and options
for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)

    # Get the user's answer
    user_answer = input("Enter your answer (a, b, c, or d): ")

    # Check if the user's answer is correct
    if user_answer.lower() == correct_answers[i]:
        print("Correct!")
    else:
        print("Incorrect!")

    # Show the correct answer
    print("The correct answer is:", correct_answers[i])

    # Add a line break for the next question
    print()
