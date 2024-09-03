while True:
    try:
        num_1 = float(input("Please provide a number:"))
        num_2 = float(input("Please provide another number:"))
    except ValueError:
        print("Input provided is not a number. Please try again.")        
        continue # try again, go to the top of the loop
    break


def calculate(num_1, num_2, operation):
    if operation == 'sum':
        return num_1 + num_2
    elif operation == 'difference':
        return num_1 - num_2
    elif operation == 'product':
        return num_1 * num_2
    elif operation == 'quotient':
        return num_1 / num_2

def func_quotient():
    try:
        quotient = num_1 / num_2
    except ZeroDivisionError:
        return "Undefined (division by zero)"
    return quotient

        
        
print("The total is: ", calculate(num_1, num_2, 'sum'))
print("The difference is: ", calculate(num_1, num_2, 'difference'))
print("The product is: ", calculate(num_1, num_2, 'product'))
print("The quotient is: ", calculate(num_1, num_2, 'quotient'))


