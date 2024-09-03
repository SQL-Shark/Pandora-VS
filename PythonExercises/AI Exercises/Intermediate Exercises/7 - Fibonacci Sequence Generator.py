# Initialize the first two Fibonacci numbers
f0 = 0
f1 = 1

while True:
    try:
        num_terms = int(input("Please provide a positive number: "))
    except ValueError:
        print("Input provided is not a number. Please try again.")
        continue  # Try again, go to the top of the loop

    if num_terms <= 0:
        print("The number is not positive, please try again!")
    elif num_terms == 1:
        print("Fibonacci sequence up to", num_terms, "term:")
        print(f0)
    else:
        # Initialize the list to store Fibonacci numbers
        fibonacci = []
        
        # Generate the Fibonacci sequence
        a, b = 0, 1
        for _ in range(num_terms):
            fibonacci.append(a)
            a, b = b, a + b
        
        # Print the entire sequence
        print("Fibonacci sequence up to", num_terms, "terms:")
        print(fibonacci)
    
    break
