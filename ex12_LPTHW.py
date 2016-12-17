# The original exercise is commented out.
"""
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "so, you're %r years old, %r tall, and %r heavy." % (age, height, weight)
"""

# My own version with some extra ingredients of the exercise.

# at the US border - scene

reason = raw_input("What brings you to the United States of America? ")

crime = raw_input("Are you planning on committing any crimes during your stay? ")

if crime == 'no':
	crime = ' \nand at the time being not planning on committing any crimes'
elif crime == 'yes':
	crime = 'but stupid enough to expose your criminal intent\n'
else:
	crime = '\nAnswer \'yes\' or \'no\'!'

commie = raw_input("Are you member of the Communist Party?" )

if commie == 'yes':
	commie = '\nso you are self proclaimed Comminist svine!'
elif commie == 'no':
	commie = '\nYou do not identify yourself as a People\'s defender I see...'
else:
	commie = '\nAnswer \'yes\' or \'no\'!'

print "Well, you are here for quote %r %s %s" % (reason, crime, commie)

if 'svine' in commie and 'stupid' in crime:
	print "Becouse you are shady Comrade and want to do crime \n- You will be deported and will never be able to enter the States! Access denied - GOODBYE!"
elif 'svine' in commie and 'planning' in crime:
	print "Being a commie is not in it self a reason to stop you from entering the country.\nBUT - we'll be watching you."
elif 'defender' in commie and 'stupid' in crime:
	print "Telling us you want to commit a crime is so stupid that \nyou will be sent back to where you came from!! Access denied - GOODBYE!"
else:
	print "Welcome to the United States of America! Enjoy your stay!!"












