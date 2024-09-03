import random

# Select a random number between 1 and 10
random_number = random.randint(1, 10)

# Allow the user up to 3 attempts to guess the number
for attempt in range(3):
    try:
        num_1 = int(input("Please guess the number (between 1 and 10): "))
    except ValueError:
        print("Input provided is not a number. Please try again.")
        continue  # Ask for input again if invalid

    # Check if the guess is correct
    if num_1 == random_number:
        print(f"Congratulations! You guessed the number! The number was: {random_number}")
        break
    else:
        if attempt < 2:  # Provide feedback only if there are attempts remaining
            print("Try again!")
        else:
            print(f"Sorry, you've used all your attempts. The number was: {random_number}")
