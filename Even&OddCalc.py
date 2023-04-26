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
import time
import sys

done = 'false'

def animate():
        sys.stdout.write('\rLoading Please Wait ▒▒▒▒▒▒▒▒▒▒  0%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait █▒▒▒▒▒▒▒▒▒  10%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ██▒▒▒▒▒▒▒▒  20%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ███▒▒▒▒▒▒▒  30%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ████▒▒▒▒▒▒  40%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait █████▒▒▒▒▒  50%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ██████▒▒▒▒  60%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ███████▒▒▒  70%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ████████▒▒  80%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait █████████▒  90%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ██████████ 100%')
        time.sleep(0.3)
        sys.stdout.write('\nDone!     \n')

animate()
# Ceate a Even Text File
with open("even_list.txt", "w") as even_list:
    even_list.write(",".join(str(x) for x in even_numbers))
# Print Even List
with open("even_list.txt", "r") as even_list:
    print("\n""Even Number List: " + even_list.read())
    
# Ceate a Odd Text File
with open("odd_list.txt", "w") as odd_list:
    odd_list.write(",".join(str(x) for x in odd_numbers))
# Print Odd List
with open("odd_list.txt", "r") as odd_list:
    print("Odd Number List: " + odd_list.read())