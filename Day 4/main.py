import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]
user_choice = int(input('Enter 0 for rock, 2 for paper or 3 for scissors: '))
computer_choice = random.randint(0, 2)
computer_input = choice_list[computer_choice]
print("Computer Choice: " + computer_input)
user_choice_value = choice_list[user_choice]
print("User Choice:" + user_choice_value)

if user_choice > 4 or user_choice < 0:
    print("Incorrect value. Please choose again")
elif user_choice == 0 and computer_choice == 3:
    print("User Wins!")
elif user_choice == 3 and computer_choice == 2:
    print("User Wins!")
elif user_choice == 2 and computer_choice == 0:
    print("User Wins")
elif computer_choice == 0 and user_choice == 3:
    print("Computer Wins")
elif computer_choice == 3 and user_choice == 2:
    print("Computer Wins")
elif computer_choice == 2 and user_choice == 0:
    print("Computer Wins")
elif computer_choice == user_choice:
    print("It is a draw!")
