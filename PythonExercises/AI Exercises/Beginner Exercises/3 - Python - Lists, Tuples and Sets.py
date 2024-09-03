## Lists

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)


print(len(courses))


print(courses[3])

### THis is more useful to grab the last item. Especially for long lists
print(courses[-1])

### first index is inclusive but the second index is not
print(courses[0:2])

print(courses[2:])

## This is called slicing


## Add an item at the end of the list

courses.append('Art')


print(courses)

### First value is position where you want to insert
courses.insert(0,'Swimming')

print(courses)




courses_2 = ['Art','Education']
## This adds the entire list to the list making it nested
courses.insert(0,courses_2)
## Instead to add the list use the EXTEND
courses.extend(courses_2)

print(courses)


### Remove specific method
courses.remove('Math')

print(courses)


## You can use the pop() method to drop the last value off the list

courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

popped = courses.pop()

print(popped)
print(courses)




## To reverse 

courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

courses.reverse()

print(courses)



## Sort alphabetically

courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

courses.sort()

print(courses)



### Sort ASC
courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

nums = [1,5,2,4,3,6]

courses.sort()
nums.sort()

print(courses)
print(nums)



### Sort DESC
courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

nums = [1,5,2,4,3,6]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)




### Sort DESC
courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

nums = [1,5,2,4,3,6]

## use a sorted function (to get a sorted version of the list without altering the original)
sorted_list = sorted(courses)

print(sorted_list)




## This will be extremely useful later on when we discuss loops

## Finding Values by using IN
courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

## print('Art' in courses)


for course in courses:
    print(course)



### Find the index


for index, course in enumerate(courses):
    print(index,course)


## Turn our list of courses into a string value separated by commas
courses = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']

## Using a join function
course_str = ', '.join(courses)

## to do the reverse
new_list = course_str.split(', ')

print(course_str)
print(new_list)






###############################################################################################
## Tuples
## Very similar to lists
## We can't modify tuples
## in programming; - mutable and immutable


## Mutable - Lists
list_1 = ['Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)



## Immutable - Tuples

tuple_1 = ('Swimming', 'History', 'Math', 'Physics', 'CompSci', 'Art')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)


tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

#######################################################################################################
## Sets
## Sets doesn't really care about order
## Sets throws away duplicates


cs_courses = {'Swimming', 'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'Art','History', 'Math'}
#Membership test (to check if a value exists within). Sets does it more efficiently than the other 2.
print('Math' in cs_courses)

print(cs_courses)

## To compare Sets to see which values map
print(cs_courses.intersection(art_courses))
## To see which values are different
print(cs_courses.difference(art_courses))
## To combine them use Union
print(cs_courses.union(art_courses))


# Empty List
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {} # This isn't riht ! it's a dictionary
empty_set = set() ## This is the correct value