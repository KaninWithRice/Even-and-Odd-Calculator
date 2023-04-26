# Mohammad Mishal S. Noroña | BSCPE 1-5 | Porblem 1 Even and Odd
# Add introduction
print("")
print("WELCOME TO THE EVEN & ODD CALCULATOR".center(40," ") )
print("By: Mishal Noroña".center(40," ") )

# Ask user for numbers of input
num_input = int(input("Enter how many you want to input: "))
user_input_list = open("user_input.txt","w")

# Ask user to enter numbers
numbers = []
for i in range(1, 1 + num_input):
    user_input = (input("Enter a number: \t"))
    numbers.append(user_input)

# Create a text file for user's input
with open("user_input.txt","w")as number_list:
    number_list.write("\n".join(str(user_input) for user_input in numbers))

with open("user_input.txt", "r") as user_input:
    numbers = [int(x) for x in user_input.read().split()]

# Create a Formula for Separating Even and Odd
even_numbers = []
odd_numbers = []
for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

# Add Loading Time
# Ceate a Even Text File
# Print Even List
# Ceate a Odd Text File
# Print Odd List