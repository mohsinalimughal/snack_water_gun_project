import random

computer_score = 0
user_score = 0
user_name = input("Enter your name !")

list1 = ["snack", "water", "gun"]

def snack(computer_input):
    global user_score, computer_score
    if computer_input == "snack":
        print("Tie............!")
    elif computer_input == "water":
        user_score += 1
        print("You Got One Score")
    else:
        computer_score += 1
        print("Oh, Computer Got one Score")

def water(computer_input):
    global user_score, computer_score
    if computer_input == "snack":
        computer_score += 1
        print("Oh, Computer Got one Score")
    elif computer_input == "water":
        print("Tie............!")
    else:
        user_score += 1
        print("You Got One Score")

def gun(computer_input):
    global user_score, computer_score
    if computer_input == "snack":
        computer_score += 1
        print("Oh, Computer Got one Score")
    elif computer_input == "water":
        user_score += 1
        print("You Got One Score")
    else:
        print("Tie............!")

def check_score():
    global user_name
    print(f"Computer Score is {computer_score}\n {user_name} Score is {user_score}")

def game():
    while True:
        user_input = int(input('''Select your choice!
                       1 For snack
                       2 For Water
                       3 For Gun
                       4 Check score
                       5 for exit the game: '''))
        computer_input = random.choice(list1)
        if user_input == 1:
            snack(computer_input)
        elif user_input == 2:
            water(computer_input)
        elif user_input == 3:
            gun(computer_input)
        elif user_input == 4:
            check_score()
        elif user_input == 5:
            break
        else:
            print("Invalid choice. Please try again.")

game()
