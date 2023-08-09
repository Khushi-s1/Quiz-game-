#quiz

questions = ("Find the invalid variable among the following:",
             "Which of the following is the correct extension of thr Python file?",
             "All keywords in Python are in:",
             "Which keyword is used for function in Python language")

options = (("A. 1st_string","B. my_string_1","C. _","D. foo"),
           ("A. .python","B. .pl","C. .py","D. .p"),
           ("A. Captialized","B. lower case","C. upper case","D. none"),
           ("A. Function","B. def","C. Fun","D. Define"))

answers = ("A","C","D","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------")
print("       RESULTS       ")
print("--------------------")

print("answers:", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses:", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")