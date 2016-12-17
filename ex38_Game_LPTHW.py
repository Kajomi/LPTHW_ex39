# Homework - Create your own game, try to make it as interesting and use different kinds of tricks.
# This means functions, lists, variables and modules!
# function is def name_of_function(what arguments we want to include):
# list is: my_list = []
# module is something you import to your Python script like from sys import argv

from sys import exit 

print "---------STAR WARS THE GAME----------"
print "-------------------------------------"
print "Long time ago in a galaxy far far away a war has broken"
print "\nbetween the rebels and the Empire led by Lord Sidius and his sidekick Darth Vader"
print "\nThe rebels lead by Princess Leia, the only Diney princess with a gun, with the help of rogue Han Solo"
print "and her brother the great Jedi Luke, who is planet-locked in Naboo."
#print "\nthe rebels sent Leia and han together with few droids to get Luke but run into an ambush by the Empire"
#print "\tYou run into tie figters, will you stay and fight them or get ridd of them by going to light speed?"

def millenium_falcon():
	print "\n\nYou are in Millenium Falcon with Han Solo and Princess Leia flying through the vastness of space."
	print "Suddenly you notice Emprires tie figters coming strait at you, but are not sure if they have noticed you yet?"
	print "Will you try to escape with the knowledge they may have seen you and call for backup, or will you fight them to"
	print "make sure your whereabouts will not be revealed to the Empire to send starfigters to the location?"
	
	tie_figter = raw_input(">>> ")
	
	if "escape" in tie_figter:
		print "You sneak behid a nearby planet and head your way to Naboo where Luke is waiting for you."
		print "Do you spend time in the planet you sneaked behind to or go straight to Naboo?"
		
		planet = raw_input(">>> ")
		
		if "spend" in planet or "time" in planet:
			print "You managed to stay under the radar and the tie fighters did not see you. Good job Team!"
			naboo_planet()
		else:
			print "You went too fast past the planet and straight to lightspeed which grabbed the attention of the tie fighters."
			print "Now they are after you and have called the main battle ships for help!!"
			print "\tPrepare for a Battle!!"
			star_killers()
		
	elif "fight" in tie_figter:
		print "You decide to fight the tie fighters!"
		print "Do you try to destroy them partly to escape as soon as possible?"
		print "Or will you bring down all of them regardless that there are many of them?"
		
		fight = raw_input(">>> ")
		
		if "partly" in fight or "escape" in fight:
			print "You manage to shoot few of them down and distract the others and escape."
			print "But you know your whereabouts are now known to the Empire. You will need to hide in Endor fores planet"
			print "To make sure you can distract the Empire and safely travel to Naboo later."
			endor_planet()
		elif "bring" in fight or "all" in fight or "down" in fight:
			print "Becouse it took so much time to fight all the tie fighters, the powerful and deadly Start killers are here!!"
			print "Now you must face the enormous Star Killers and avoid of being caught by the Empire as that would mean almost certain"
			print "end to the rebellion and the victory of the Empire!!!!"
			star_killers()
		else:
			death("As you spent too much time hesitating the odds turned against you, you got caught by the Empire.")
	else:
		death("You got shot down due to not making a decision soon enough - the rebellion has been defeated!")
		
def endor_planet():
	print "You have come to Endor to hide from the Empire's Star killer fleet that are looking for you."
	print "If you spent long time on the planet the Star killers will eventually leave, but this puts Luke in jeopardy as he is all alone in Naboo waiting for Leia and Han."
	print "Or will you just gather resources from the planets friendly Ewoks and leave as soon as possible - within 24 hours and face the danger of having to face the feared Star killers after all?"
	
	ewoks = raw_input(">>> ")
	
	if "spend" in ewoks or "longer" in ewoks or "long" in ewoks:
		print "As you spend more time on Endor the Empire had sent its ATA -walkers to the planet and they have found you!"
		print "The battle was fierce and many Ewoks died for the rebellions."
		death("You were taken by suprise by the Empire's land troops who caught you and executed Han and Leia - the leaders of the rebellion.")
	elif "gather" in ewoks or "resources" in ewoks or "leave" in ewoks or "soon" in ewoks:
		print "You were able to gather lots of necessary resources. As you are highly respected by Ewoks the tiny warriors supporting the rebellion"
		print "they offer to distract the Empire's fleet by staging a hoax camp, meantime you can fly out from the other side of the planet and head towards Naboo"
		naboo_planet()
	else:
		print "You were in a panic and not sure what you wanted to do - the team had differing opinions! This lead to exposure."
		print "Now you must get rid of the Empire's strong and plentiful fleet. This is a Russian rulet as the escape plan is almost as crazy as fighting the Start killers!!"
		asteroid_field()
		
def asteroid_field():
	print "You are entring the most dense asteroid field in this part of the Galaxy! It is full of asteroids from small basketball size rocks to"
	print "asteroids the size of mountains! Behind you have the Empire's fleet consisting of huge Star killers blazing their way through the asteroid field"
	print "\nWill you keep on going  even further into the asteroid field or hide somewhere, and if yes then where?"
	
	asteroid = raw_input(">>> ")
	
	if "keep" in asteroid or "going" in astroid or "further" in asteroid:
		death("You pushed your luck too much - you got hit by an asteroid.")
	elif "starkiller" in asteroid or "side" in asteroid:
		print "You got lucky by attaching Millenium Falcon to the side of an Starkiller."
		print "Good thing is Bobba Fett is not part of the game and you manage after all to escape from the Empire."
		naboo_planet()
	else:
		death("You got eaten by a space worm afterseeking refuge inside an asteroid - glorious way to go.")
		
def naboo_planet():
	print "You have found your way to Naboo where Luke Skywalker has been hiding and waiting for you to come and pick him up."
	print "\tIt is of utmost importance to get Luke to Hoth the ice planet where the rebellions have their main base."
	print "\tLuke has essential information needed to destroy the Empire and its main base the Deathstar."
	print "You find Luke and set on your way. As you leave, a local mop recognizes Han and demands him to pay hes loan back immediately. They are a big mop."
	print "Will you leave Han to them and leave, fight them and escape or offer the droids?"
	
	mop = raw_input(">>> ")
	
	if "leave" in mop or "Han" in mop or "han" in mop:
		death("You are bunch of douchbags! bad thing is Han is the one flying the Millenium Falcon, therefore you failed!")
	elif "fight" in mop or "escape" in mop:
		print "You got to choose your battles! You managed to defeat the mop but also to draw lot of attention to yourselves!"
		print "This is why you got caught by the Stormtroopers who have their subheadquarters few blocks away."
		jail()
	elif "offer" in mop or "droids" in mop:
		print "Sometimes it is good to obey knowing the bigger context. This was a good decision and you manage to leave Naboo with Luke"
		print "\nAnd head to the Rebel base in planet Hoth."
		hoth_planet()
	else:
		print "As Luke is a great Jedi - he uses his ability to use the force and does the hand thing."
		print "therefore, our team can leave the planet Naboo with the droids and Han and go to the Rebel base in planet Hoth."
		hoth_planet()
		
def jail():
	print "You have been caught by the Empires henchman - the Stromtroopers- and are in jail in planet Naboo."
	print "\nYou will be sent to the Death star which will mean the defeat of the rebellion."
	print "But there is a catch! The troopers got them becouse they were fighting the mop - they're friends."
	print "\tThey don't know they are the leaders of rebellion, at least not now but they are about to call the Head of Justice. If this happens they true identity will be revealed!"
	print "Will you stage a riot to break the prison?"
	
	riot = raw_input(">>> ")
	
	if "stage" in riot or "riot" in riot or "yes" in riot:
		print "You will fight and escape!!"
		hoth_planet()
	else:
		death("You got caught and weren't able to escape once the troops came to pick you up and sent you to the Death Star.")
		
def star_killers():
	print "You are facing the Starkillers and many other tie fighters!"
	print "\nYou don not stand a chance but you only way of surviving is to escape - but how?"
	print "Will you go to light speed or try to escape the fleet somewhere nearby?"
	
	escape = raw_input(">>> ")
		
	if "light" in escape or "speed" in escape:
		print "You are going to light speed! Will you go to light speed immediately or try to manouver first inspite the heavy laser storm coming your way?"
		
		speed = raw_input(">>> ")
		
		if "immediately" in speed:
			death("You didn't make sure the road was clear - Millenium falcon hit a planet.")
		else:
			print "You got some heavy hits from the Starkillers but managed to calculate safe route to safety."
			naboo_planet()
	elif "escape" in escape or "somewhere" in escape or "nearby" in escape:
		print "As you cannot take too many hits from starships hundred times your size, you decide to flee."
		print "You decide to flee to a friends place - a city above the clouds. Who is this mysterios friend?"
		
		lando = raw_input(">>> ")
		
		if "Lando" in lando or "lando" in lando:
			print "You got to safety (and know something from the real movies) and managed to continue your way shortly."
			hoth_planet()
		else:
			death("Watch the movies please, and you also died as you went to wrong friends place.")
	else:
		death("You hesitated with decision making and you took too many shots and the plane exploded.")
		
def hoth_planet():
	print "You have finally managed to find your way to Hoth - home of the rebels - enemies of the Empire!"
	print "The rebels are planning to attac the Death star and with Lukes information are ready!"
	print "As the time comes and X-wings are ready to take off, you are face with a decision."
	print "Will join your team on Millenium falcon and head towards the death star or stay at the base and help with the organization and surveillance?"
	
	dec = raw_input(">>> ")
	
	if "join" in dec or "head" in dec or "towards" in dec:
		print "You journey continues - get your gear on and get ready for some action!"
		deat_star()
	elif "stay" in dec or "base" in dec or "help" in dec:
		print "That is a great choise too, but your journey in this game has ended. Hope you enjoyed it!"
		exit()
	else:
		print "Not sure what your choise was, be more specific."
		hoth_planet()
		
def death_star():
	print "You, as part of the rebellion, are headed towards the Death start - headquarter of the Empire, inhabited by Lord Sidius and Darth Vader!"
	print "As soon as you all arrive, you are faced with hundreds of tie fighters and league of starkillers - the battle will be intense."
	print "Will you go with few of your friends in X-wings and go towards the main Starkiller, or will you join couple of others in X-wings who are going to the left and aiming to hit from the side?"
	
	attack = raw_input(">>> ")
	
	if "towards" in attack or "main" in attack:
		print "You got an upper hand and your success hangs on a balance! You need to be fast and aggressive. Will you aim straight at the main laser cannon in the starkiller?"
		
		cannon = raw_input(">>> ")
		
		if "yes" in cannon:
			death("You got shot by the laser cannon.")
		elif "no" in cannon:
			death("You tried to hit from the side, but gor shot by a team of tie fighters.")
		else:
			death("You were too aggressive and weren't thinking straight. You have to think fast but not be too impulsive.")
	elif "left" in attack or "side" in attack:
		print "There are less enemy planes on the left side so there is more space to move."
		print "\tWill you look around or follow the X-wings?"
		
		look = raw_input(">>> ")
		
		if "look" in look or "around" in look:
			print "While looking around you notice a secret tunnel. Will you go inside?"
			
			inside = raw_input(">>> ")
			
			if "yes" in inside:
				print "You found the weakspot of the Death star!"
				inside_star()
			elif "no" in inside:
				print "You got drifted aside and need to return back to the main rebel fleet."
				deat_star()
			else:
				death("You were sloppy and got shot by a laser cannon.")
				
def inside_star():
	print "You are close to a final victory over the Empire! You must find the reactor that is the source of energy and fuel that Death Star uses."
	print "You need to decide whether or not you will follow Luke's draft of the architecture of the star or follow your own feelings and trust them."
	print "\tWhat will you do?"
	
	reactor = raw_input(">>> ")
	
	if "luke" in reactor or "Luke" in reactor or "draft" in reactor:
		print "Luke is the legendary Jedi - trusting his plan and draft is the best thing to do."
		print "Becouse of this you managed to destroy the Death Star and secured the victory to the Rebels!!! Good JOB Team!!!"
		exit()
	elif "own" in reactor or "feelings" in reactor or "trust" in reactor:
		death("You are not a Jedi! You cannot use the force. This lead you to get lost and failing the rebellion.")
	else:
		print "You are hesitating - that can be fatal! Will you call the main rebel ship to ask for instructions?"
		
		call = raw_input(">>> ")
		
		if "yes" in call:
			death("You cannot be making calls while in a fight and inside a death star! You hit the wall and died.")
		else:
			print "You decide not to call but have to make the decision by yourself."
			inside_star()

def death(why):
	print why, "The Empire Prevails!"
	exit(0)
	
millenium_falcon()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		