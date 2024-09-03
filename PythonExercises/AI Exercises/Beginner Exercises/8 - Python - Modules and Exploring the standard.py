
##  import my_module as mm ## you can give the module an alias


## To import a module which is not in the same folder use this method

## to import just the function we can use the following method
## it only gives us access to the specific function from the module
## We need to use commas to include specific things

import sys
from my_module import find_index, test



## to add everything we can use *
## but this is frowned upon because it makes it harder to track down problems

#from my_module import *


courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(sys.path)



###################################################################
import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)

print(random_course)



###################################################################

import datetime
import calendar

today = datetime.date.today()

print(today)

print(calendar.isleap(2020))


###################################################################
import os

print(os.getcwd())


print(os.__file__)




###### standard library
############ anti-grivaty

import antigravity
