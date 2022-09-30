# %-formatting
print('-------- %-formatting ------------')
name = 'Python'
instructor = 'Ammar'
years = 2

print('My favourite course is %s' % name)
# My favourite course is Python

print("%s is being taught by %s right now." % (name, instructor))
# Python is being taught by Ammar right now.

# %s is for string values and %d is for numbers and %f is for float numbers
print('It takes %d years to learn %s' % (years, name))
# It takes 2 years to learn Python

print('-------- str.format() ------------')
print('My favourite course is {}' .format(name))
# My favourite course is Python

# you can give indexing to replace variable at your choice
print("{1} is being taught by {0} right now." .format(instructor, name))
# Python is being taught by Ammar right now.

# specific names of the variables can be specified
course = {"name": "Beyond The Basic", "instructor": "Ammar"}
print("{name_here} is being taught by {instructor_here} right now." .format(name_here=course['name'], instructor_here=course['instructor']))
# Beyond The Basic is being taught by Ammar right now.

# Dictionaries can be passed on as a whole
print("{name} is being taught by {instructor} right now." .format(**course))
# Beyond The Basic is being taught by Ammar right now.
