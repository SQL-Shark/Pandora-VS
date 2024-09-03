# Comment
## By adding 3 quotes (both single and double) we can create a string over multiple lines
### String
message = "Bobby's World"
greeting = 'Hello'
name = 'Nadia'


print(message)

# len for length
print(len(message))

#to access specific characters from the length use the following code
# First character is included but the last one is not
print(message[8:13])
#if you don't put anything it will just start from the beginning
print(message[:7])
#You can do the same with the ending
print(message[8:])

## Methods and Functions are essentially the same thing. 
##A method is just a function that belongs to an object.

print(message.lower())
print(message.upper())


print(message.lower().count('b'))

## if it doesn't find a character it returns a -1

## Replace method takes 2 arguments

new_message = message.replace('World','Universe')

print(new_message)



##message1 = '{}, {}. Welcome!'.format(greeting,name)

## Python version > 3.6  
message1 = f'{greeting}, {name.upper()}. Welcome!'

print(dir(name))
### dir + variable name you can see all the available methods

## Use help function + name of the method
#print(help(str))
print(help(str.lower))




