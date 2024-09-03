def reverse_string(string):
    return string[::-1]

while True:
    original_string = input("Please provide a word or a sentence: ")
    
    # If you want to add validation for empty strings, you can do so here
    if not original_string:
        print("Input cannot be empty. Please try again.")
        continue
    
    reversed_string = reverse_string(original_string)
    print("Original String:", original_string)
    print("Reversed String:", reversed_string)
    break
