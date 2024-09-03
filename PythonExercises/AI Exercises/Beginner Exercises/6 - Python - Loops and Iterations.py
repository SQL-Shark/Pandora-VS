nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)


## the break keyword will completely break out of the loop
## the continue will continue to the next iteration

## A loop within a loop



nums = [1,2,3,4,5]

##This does a cross-join (gave us absolutely every combination of characters)
for num in nums:
    for letter in 'abc':
        print(num,letter)


## We can go through a loop a certain number of times
## Doesn't include the last value in range
for i in range(3,10):
    print(i)



## While loops will just keep going until a certain condition is met
x=0
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1

## infinite loop
x = 0
while True:
    print(x)
    x += 1