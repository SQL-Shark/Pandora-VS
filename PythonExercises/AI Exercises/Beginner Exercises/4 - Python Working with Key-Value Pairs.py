## Key Value pairs
## 2 linked values where the key
## Real physical dictionary
## Key + definition

student = {'name':'John','age': 25, 'courses':['Math', 'CompSci']}

print(student)



print(student['name'])


## by adding get you avoid an error.
print(student.get('phone','Not Found'))

student['phone'] = '555-5555'

print(student)

student.update({'name':'Jane', 'age':26, 'phone':'555-6666'})


print(student)

## Deleting values
del student['age']

print(student)

## Popping values
name = student.pop('name')

print(student)
print(name)


student = {'name':'John','age': 25, 'courses':['Math', 'CompSci']}
## Looping through

#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())


## When looping through a dictionary don't loop through the list
## It would just loop through the keys


for key, value in student.items:
    print(key,value)
