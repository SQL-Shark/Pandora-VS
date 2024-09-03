## Functions
## you can write a function and leave it completely blank by adding the pass keyword
def hello_func():
    return 'Hello Function!'

n = 0

for i in range(1,5):
    print(hello_func().upper())

### Useful thing about function is that you can re-use code
### Focus on the input and what's returned
### Functions have input and a return


## The greeting variable is only private to the function. 
## it cannot be accessed outside of the function.
def hello_func(greeting):
    return '{} Function'.format(greeting)

print(hello_func('Hi'))


def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting,name)

print(hello_func('Hi','Yovcho'))
########################################################################################


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Math', 'Art')
info = {'name':'John', 'age':22}


student_info(*courses, **info)

########################################################################################

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    ## The string is called a doc string. It's a good practice every time you write a function to write
    ## an explanation of what that function is supposed to do
    """Return True for leap years, False for non-leap years.""" 

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]



print(days_in_month(2023,12))