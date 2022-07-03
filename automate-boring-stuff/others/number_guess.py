import random

count = 0
number = random.randint(0, 50)
print("I am thinking of a number between 0 to 50")

while True:
    print("Take a guess")
    user_number = int(input())
    if user_number < number:
        print("Your guess is too low :P")
        count += 1

    elif user_number > number:
        print("Your guess is too high :)")
        count += 1

    elif user_number == number:
        print("Good job! you got my number in " + str(count) + " guesses!")
        break
