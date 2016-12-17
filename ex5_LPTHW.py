name = 'Mira Kajo'
age = 28
height = 171.5 # cm 
weight = 59 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Red'

subject = 'GIS'
major = 'Geography'
code = 'Python'
comedy = 'Monthy'

print "Lets talk about that girl %s whose like only %d" % (name, age)
print "She's about %d centimeters tall." % round(height)
print "and something like %d kilos heavy which is something like %d in pounds." % (weight, weight * 2.2)
print "Actually that is not that heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending whether or not she bothered to wash her teeth." % teeth

print "Her major is %s and she likes this thing called %r.\n" % (major, subject)
print "\nAlso, she knows some " + code + " coding as well."
print "\tShe chose that language becouse shes a fan of black english humor, her favorate being: " + comedy + ' ' + code 

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "Also if I convert height to integer, multiply age by 2 and loose some weight, my final value looks like this: \n\t%d" % ((age * 2) + int(height) + (weight - 3))

