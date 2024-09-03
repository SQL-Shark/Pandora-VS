while True:
    try:
        num_1 = int(input("Please provide a number:"))
    except ValueError:
        print("Input provided is not a number. Please try again.")        
        continue # try again, go to the top of the loop
    break

if num_1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd") 