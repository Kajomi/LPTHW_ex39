"""
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through the list

for number in the_count:
	print "This is count %d" % number
	
# same as above

for fruit in fruits:
	print "a fruit of type %s" % fruit
	
# also we can go through mixed lists too.
for i in change:
	print "I got %r " % i
	
# we can also build lists, first start with an empty one.
elements = []

# then use the range function to do 0 to 5 counts
for i in range(3, 6):
	print "Adding %d to the list" % i
	#append is a function that lists understand
	elements.append(i)
	
# now we can print them out too
for i in elements:
	print "Element was: %d" % i 
	
print elements 
"""
# My own version of the practical
# Going through my GIS courses to see where I am at with my studies

course_GIS = ['intro', 'sequel', 'remote_sensing', 'rasterGIS', 'bigData_GIS', 'quantum_GIS']
course_Credit = [6, 5, 3, 5, 3, 5]

for num in course_Credit:
	print "I got this many credits from my GIS course: %d\n" % num 
	
for gis in course_GIS:
	print "I have passed this GIS course: %s." % gis 
	
# building a list
# first create a new empty list - to which the values are being appended.

all_GIS = []

for x in range(0, 2):
	print "This course is dealing with the basics: %d" % x 
	all_GIS.append(x) 
	
for x in range(3, 6):
	print "This course is more advanced/ specific: %d" % x 
	all_GIS.append(x) 
	
for x in all_GIS:
	print "My finished course: %d." % x 
	
# accessing the content of lists

rasterGIS = course_Credit[3]
course_Credit[0] = 7
highest = course_GIS[0], max(course_Credit)
latest = course_GIS[-1]
course_GIS.reverse()

print "For rasterGIS course, the amount of credit is %d." % rasterGIS
print "I rememberd the credit wrong for intro course. The right amount is %d." % course_Credit[0]
print "%s course has the highest amount of credit available: %d." % highest
print "The last course I took was %s." % latest 	
print "So, when starting from the latest, my courses have been these ones: \n\t* %s" % course_GIS


























