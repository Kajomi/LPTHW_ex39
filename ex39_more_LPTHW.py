# make a directory of cities in the order of their size
#from collections import 
import collections

cities = {
		'Helsinki': 575487,
		'Tampere': 208252,
		'Turku': 168622,
}

# add few more cities

cities['Oulu'] = 138188
cities['Jyvaskyla'] = 115271

for a, b in cities.items():
	print "Here is a collection of biggest cities in Finland in random order: %s: %d" % (a, b)

# s one problem with dictionaries is that they do not have order, Zed Shaw (the writer),
# hinted to look into collections.OrderedDict data structure in Python 
# OrderedDict is a dict subclass that remembers the order values were added.
# - so here's my try:
# To create a Dict with ordering, you need to give it items in order. Since a standard dict can't do that, 
# you give it a list of tuples instead. Once the OrderedDict is created it is a dictionary.
# In Other Woerds - OrderedDict does not order the values given, but jusr retains the order values were added!! 

# Therefore, first I'll change the original citites to tuple and work from that.
cities_tuple =[('Helsinki', 575487),
				('Tampere', 208252),
				('Turku', 168622),
				('Oulu', 138188),
				('Jyvaskyla', 115271)]

# Next, I'll call the OrderedDict function, that will convert the tuple into a dictionary, while simultaniously retaining the order of the values. 
cities = collections.OrderedDict(cities_tuple)

for a, b in cities.items():
	print "Using OrderedDict: %s: %d" %(a, b)


print "\nAnd here is the new Dictionary where the cities are in order\nfrom biggest to smallest:\n", cities 














