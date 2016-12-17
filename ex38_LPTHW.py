ten_megacities = "New_York Los_Angeles Tokyo Mexico_City Shanghai Beiging London"

print ten_megacities
print "Wait a minute - there is not ten cities on that list, let's fix that!"


city = ten_megacities.split(' ')
mega_city = ["Sao Paolo", "Seoul", "Delhi", "Mumbai", "Cairo", "Moscow", "Dhaka"]

while len(city) != 10:
	next_one = mega_city.pop()
	print "Taking the last city from a list + adding it: ", next_one
	city.append(next_one) # adds the city that was just popped out from mega_city and added to next_one variable.
	print "There's %d cities now on the city -list." % len(city)
	
print "And there we go: ", city

print "Let's do some things with city variable!"

print city.pop()
print city[5]
print ' '.join(city)
print '-'.join(city[0:5])

