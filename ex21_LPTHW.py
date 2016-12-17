# Getting familiar with return that allows one to do more while creating own functions. 

def add(a, b): # I created a function called add and have assigned two arguments called a and b.
    print "ADDING %d + %d" % (a, b)
    return a + b # with return, the function will return the result of values assigned to arguments a and b.
	
def substract(a, b):
    print "SUSTRACTING %d - %d" % (a, b)
    return a - b 
	
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b 
	
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
	
print "Let's do some math with just functions!"
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d." % (age, height, weight, iq)

# a puzzle for extra credit, type it in anyways
print "Here is a puzzle!"

what = add(age, substract(height, multiply(weight, divide(iq, 2)))) 
print "That becomes: ", what, "Can you do it by hand?"

# My own variation to practice more functions and return.
def LPTHW(x, z):
	print "%d total amount of exercises, %d already done." % (x, z)
	return x - z

done_ex = LPTHW(52, 21)
print "I have %d of the practicals left to do." % (done_ex)


def my_dog(breed):
	german_shephard = breed / 3
	corgi = german_shephard * 2
	jack_russel = corgi / 3 
	return german_shephard, corgi, jack_russel
	
mutt_madeof = 50
german, corgi, jack = my_dog(mutt_madeof)

print "My dog is a mutt and is believed to be %d percent Australian Cattle dog." % mutt_madeof
print "Other breeds are believed to be the following:\n\t* German Shephard about %d prc,\n\t* corgi something like %d prc,\n\t* and Jack Russel the remaining %d prc. " %(german, corgi, jack)
print "No wonder he looks slightly weird..."

mutt_madeof = mutt_madeof / 2

print "\nI might be wrong on this though, the breerer said it can also be closer to this:"
print "\t* %d German Shephard,\n\t* %d Corgi,\n\t* and %d of Jack russel terrier." % my_dog(mutt_madeof)
print "\n\n\t--> and rest being Aussie (%d)." % mutt_madeof
print "\nStill my Doggo looks weird but he makes it up with good personality!"


















