import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator")
number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbol = int(input("How many symbol would you like? "))
number_of_digits = int(input("How many numbers would you like? "))

random_letter = random.sample(letters, number_of_letters)
random_number = random.sample(numbers, number_of_digits)
random_symbol = random.sample(symbols, number_of_symbol)


password_list = random_letter + random_symbol + random_number
randomized_list = random.sample(password_list, len(password_list))

final_password = ''.join(randomized_list)
print(final_password)