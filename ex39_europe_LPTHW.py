# Create a dictionary of EU countries
countries_EU = {
				'Finland': 'FIN',
				'Sweden': 'SWE',
				'Norway': 'NOR',
				'France': 'FRA',
				'Germany': 'GER',
				'Holland': 'HOL'
}

print "Here is a list of some EU menber countries: ", countries_EU

# Create a dict with the capitals of some EU countries
capitals_EU = {
			'FIN': 'Helsinki',
			'SWE': 'Stockholm',
			'NOR': 'Oslo',
			'FRA': 'Paris'
}

# Add some cities
capitals_EU['GER'] = 'Berlin'
capitals_EU['HOL'] = 'Amsterdam'

print "And here's a collection of some of the capitals: ", capitals_EU

# WAIT! Norway is not part of the EU! 
print "As Norway is not part of the EU - Let's delete it from the dictionaries."
del countries_EU['Norway']
print "\nFirst from countries: ", countries_EU 
del capitals_EU['NOR']
print "\nAnd then from capitals: ", capitals_EU

# print out some countries
print '-' * 10
print "Finland's capital is ", capitals_EU['FIN']
print "France's capital is ", capitals_EU['FRA']

# print out some countries
print '-' * 10
print "Hollands abbreviation is ", countries_EU['Holland']
print "Germanys abbreviation is ", countries_EU['Germany']

# to play a bit more - use both countries and capitals
print '-' * 10
print "Sweden has " + capitals_EU[countries_EU['Sweden']] + " as its capital."
print "Germanys capital is ", capitals_EU[countries_EU['Germany']]

# print every country abbreviation
print '-' * 10
for country, abbr in countries_EU.items():
	print "%s is abbreviated from %s." %(abbr, country)

# and same for capitals
print '-' * 10 
for abbr, capital in capitals_EU.items():
	print "%s is the capital of %s." %(capital, abbr)
	
# try to do both at the same time
print '-' * 10
for countries, abbr in countries_EU.items():
	print "%s is abbreviated from %s, and its capital is %s." %(countries, abbr, capitals_EU[abbr])
	
# check the keys in the dictionary 
for key in capitals_EU.keys():
	print key
	
# same for values
for val in capitals_EU.values():
	print val 

# create a new dictionary and merge it with the existing one

capitals_EU_more = {
					'ESP': 'Madrid',
					'POR': 'Lissabon',
					'EST': 'Tallin',
					'DEN': 'Copenhagen'
}

# use .update() to merge the two dicts
capitals_EU.update(capitals_EU_more)
print capitals_EU 

# remove an item by using the pop() function
print "I got Spains capital wrong - I shall remove it!"
spain = capitals_EU.pop('ESP')
print spain
print capitals_EU

# check for existence
if 'NOR' not in capitals_EU:
	print 'NOR' + ' not found' 

# check the lenght
print len(capitals_EU)









