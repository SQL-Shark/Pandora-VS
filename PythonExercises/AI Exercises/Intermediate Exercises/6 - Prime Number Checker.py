while True:
    try:
        num_1 = int(input("Please provide a positive number: "))
    except ValueError:
        print("Input provided is not a number. Please try again.")
        continue  # Try again, go to the top of the loop

    if num_1 <= 0:
        print("The number is not positive, please try again!")
    elif num_1 == 1:
        print("Please provide a number greater than 1.")
    else:
        flag = False  # Reset flag for each new number

        # Check for factors
        for i in range(2, num_1):
            if (num_1 % i) == 0:
                flag = True  # If a factor is found, it's not prime
                break

        # Determine if the number is prime or not
        if flag:
            print(num_1, "is not a prime number. Please try again.")
        else:
            print(num_1, "is a prime number!")
            break  # Break the loop only if the number is prime
