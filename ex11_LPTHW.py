#print "How old are you?"
#age = raw_input()
#print "How tall are you?"
#height = raw_input()
#print "How much do you weight?"
#weight = raw_input()

#print "So you are %r old, %r tall and %r heavy." % (age, height, weight)

# creating my own version of the exercise and adding some other elements there as well.

print "What is your Major in school?"
major = raw_input()
print "How much longer you will be in school for?"
length = raw_input()
print "How many student credits do you have?"
credit = int(raw_input())

if credit < 180:
	credit = 'You still have ways to go Buddy...'
else: 
	credit = 'You are almost a graduate! Woot Woot!'


print "So you only have %s left as a %s student. Conserning your credit score, %s" % (length, major, credit)