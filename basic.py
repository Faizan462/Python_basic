# print("Hello World")

# A = 4 
# B = 5
# C = A + B

# print (C)

# # comment

# if A + B > 10:
#     print("C is greater than 10")
# else:
#     print("C is less than or equal to 10")


# D = 0
# D = int(input("Enter a number: "))

# if D == C:
#     print("You guessed it right!")
# else:
#     print("Sorry, try again.")


# D -= 1
# D = D-1 
# # both are same

# print (D)


# #for math operations we can use math module
# import math 
# print(math.sqrt(D))


# E = 0
# E = int(input("Enter your age: "))

# if E > 18 and E < 65:
#     print("You are eligible to work")
# elif E < 18:
#     print("You are too young to work")
# else:
#     print("You are too old to work")


# F = 0
# F = int(input("Enter your age: "))

# while F < 0:
#     print("Age can't be negative")
#     F = int(input("Enter your age: "))

# print("Your age is:", F)


# G = 0
# G = int(input("Enter a number: "))

# for g in range(1, 10):
#     if  g == G:
#         print("You guessed it right!")
#         break
# else:
#     print("Sorry, try again.")

# import time

# timer = int(input("Enter the timer value: "))
# for i in range(timer, 0, -1):
#     seconds = i % 60
#     minutes = int(i / 60) % 60
#     hours = int(i / 3600) % 24
#     print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
#     time.sleep(1)

# print("Time's up!")


# H = 0
# H = int(input("Enter the number of rows: "))

# for i in range(H):
#     print(" " * (H - i - 1) + "* " * (i + 1))


# for i in range(H - 2, -1, -1):
#     print(" " * (H  - i - 1) + "* " * (i + 1))





# #list
# games = ["Chess", "Football", "Basketball", "Tennis", "Cricket"]
# print(games)  
# print(dir(games))  # This will show the available attributes and methods for the list object


# # Set
# games = {"Chess", "Football", "Basketball", "Tennis", "Cricket", "Cricket"}
# print(games)


#  #Tuple
# games = ("Chess", "Football", "Basketball", "Tennis", "Cricket")
# print(games)


# # Python MCQ Quiz Game

# questions = (
#     "1. Which keyword is used to define a function in Python?",
#     "2. Which data type stores multiple values?",
#     "3. Which loop is used to repeat a block of code?",
#     "4. What is the output of 10 // 3?",
#     "5. Which symbol is used for comments in Python?"
# )

# options = (
#     ("A. func", "B. define", "C. def", "D. function"),
#     ("A. int", "B. list", "C. float", "D. bool"),
#     ("A. if", "B. while", "C. switch", "D. for"),
#     ("A. 3", "B. 3.33", "C. 4", "D. 1"),
#     ("A. //", "B. #", "C. /*", "D. <!--")
# )

# answers = ("C", "B", "D", "A", "B")

# score = 0

# for i in range(len(questions)):
#     print(questions[i])

#     for option in options[i]:
#         print(option)

#     user = input("Enter your answer (A/B/C/D): ").upper()

#     if user == answers[i]:
#         print("✅ Correct!\n")
#         score += 1
#     else:
#         print("❌ Wrong!")
#         print("Correct Answer:", answers[i], "\n")

# print("Quiz Finished!")
# print("Your Score:", score, "/", len(questions))


# #dictionary

# country_capitals = {
#     "USA": "Washington, D.C.",
#     "Canada": "Ottawa",
#     "Germany": "Berlin",
#     "France": "Paris",
#     "Japan": "Tokyo"
# }

# print(country_capitals.get("Germany"))  


# print("Country Capitals Dictionary:")
# for country, capital in country_capitals.items():
#     print(f"{country}: {capital}")


# import random

# options = ["rock", "paper", "scissors"]
# computer = random.choice(options)

# my_choice = input("Enter your choice (rock/paper/scissors): ").lower()

# if my_choice not in options:
#     print("Invalid choice! Please choose rock, paper, or scissors.")
# else:
#     print(f"Computer chose: {computer}")

#     if my_choice == computer:
#         print("It's a tie!")
#     elif (my_choice == "rock" and computer == "scissors") or \
#          (my_choice == "paper" and computer == "rock") or \
#          (my_choice == "scissors" and computer == "paper"):
#         print("You win!")
#     else:
#         print("Computer wins!")



#Functions

def sum(A , B):
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))

    return A + B

sum_result = sum(0, 0)
print("The sum is:", sum_result)

