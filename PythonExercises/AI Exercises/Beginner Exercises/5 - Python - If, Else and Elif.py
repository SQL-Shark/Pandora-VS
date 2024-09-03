# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


### if -> elif -> elif -> else signifies SWITCH statement

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')




user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


### IS compares their IDs
a = [1, 2, 3]
b = [1, 2, 3]


print(id(a))
print(id(b))
print(a is b)




# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

