## Create a function that accepts a string
def reverse_string_reverse_join(string):
  reversed_list = list(string)
  reversed_list.reverse() ## Use reverse to reverse the string
  return ''.join(reversed_list) ## use the join function + return so we can store the result of the fuction

while True:
    try:
        original_string = input("Please provide a word or a sentence: ")
    except ValueError:
        print("Input is not an acceptable string")
        continue  # Try again, go to the top of the loop

## Create a new variable for the reversed string and print results
    reversed_string = reverse_string_reverse_join(original_string)
    print("Original String:", original_string)
    print("Reversed String:", reversed_string)
    break