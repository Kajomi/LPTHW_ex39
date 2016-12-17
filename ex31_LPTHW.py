print "You enter a dark room with two doors. Do you go through door #1 or door #2 or possibly door #3 or even door #4?"

# first print sets a question for the game. The raw_input is where the player/ user writes the answer/ preferred choise.
door = raw_input("> ")   

# the if -statement goes through the answer given and finds a matching partner and prints out the following instructions for that
# specific option.
if door == '1':
	print "There's a giant bear hear eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	# there is a if inside an if - statement - this is why we have another raw_input. This answer leads the player to that embedded if-statement.
	bear = raw_input("> ") 
	
	if bear == '1':
		print "The bear eats your face off. Good job!"
	elif bear == '2':
		print "The bear eats your legs off. Good job!"
	else:
		print "Well doing %s is propably better. Bear runs away." % bear

# there are 5 options for the player - thats why there is if, 3 elif's and one else statement.
# these all have (apart from the final else) embedded if - statements inside them.		
elif door == '2':
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == '1' or insanity == '2':
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
elif door == '4':
	print "This is a boring door (just to be honest with you...)"
	print "Who are you going to vote for in the presidential elections?"
	print "1. Crooced Hillary - the Wall St. sellout and representative of Status Quo."
	print "2. Narsicistic Trump - Misogynist, pathological liar who acts like an baby and propably has escaped the kindergarden (and should be sent back!)."
	
	door = raw_input("> ")
	
	if door == '1' or door == '2':
		print "You are skrewed either way.... Sorry! You'll all will have interesting four years coming up!"
	else:
		print "Not voting is okay... You do not have a real choise anyways. I'll buy you a virtual teddy bear my friend :/"
		
elif door == '3':
	print "The lord our savior at the heavens gates asks - do you believe in Intelligent Design?"
	print "A) I believe there is a designer behind the Universe and our planet."
	print "B) I believe there is lot we do not know - I cannot possibly answer that!!!"
	print "C) There is no evidence of ID - it is an endless regression - Who made the Designer!!!!"
	
	designer = raw_input("> ")
	
	if designer == 'A':
		print "You are an small minded religious person!"
	elif designer == 'B':
		print "At some point you just have to make a decision! Nothing is absolute, but what is the most plausible answer?"
	elif designer == 'C':
		print "Go to Hell!!"
	else:
		print "ERROR ERROR - invalid answer! Check your answer and try again Stupid! (Hint read the options!!)"
	
elif door > 4 > door > 15:
	print "You have found the secret door - the door of all doors!"
	print "?. You are super curios and want to know what secrets lie behind the confined boundaries."
	print "$. You have hard times following the rules and are stupid!"
	
	door = raw_input("> ")
	
	if door == '?':
		print "I salute you for your curiosity and wonderous mind!"
	elif door == '$':
		print "Aaaargg!!"
	else:
		print "I and this game are done with you! Good night!"

If the players answer in the first raw_input does not fall under any of the main if or elif's options it falls to this category.		
else:
	print "You stuble around and fall on a knife and die. Good job!"
	
# This game end immediately as the questions have been answered. If you answer wrong you have to load and run the file again in terminal.
# It does not allowe one to go back and change the answer in situation of accidentally writing a wrong answer, etc. 