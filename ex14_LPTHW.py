# another way to add input so you can pass variables to script (anther way of discriping a file)

# we will write a script (file) that will accept the argument, which is the ex14.py u write in command line.

# first, import is a function u use to add features to your script from the python feature set.

#from sys import argv
# argv is "argument variable", This variable holds the arguments you pass to your python script when you run it.


#something, first, second, third = argv 
# this line "unpacks" argv so that, rather than holding all the arguments,
# it gets assigned to four variables you can work with: script, 1st, 2nd, 3rd.

#print "the script is called: ", something 
#print "your first variable is:", first
#print "your 2nd variable is:", second
#print "your final variable is:", third


from sys import argv

# assigs arguments to two variables called script and user_name.
script, user_name, skill_level = argv
prompt = '> ' # assigns value '> ' to variable prompt 

print "Hi %s, I'm the %s script." % (user_name, script)
print "I would like to ask few questions, if that is okay?"
print "You told you are %s in Python coding" % skill_level 
print "Do you find Python language to be funny?"
python = raw_input(prompt) # this part starts the actual questions. 

print "Where did you learn coding %s?" % user_name
where = raw_input(prompt)

print "As you are %r in Python, where do you work %s?" % (skill_level, user_name) 
work = raw_input(prompt) 

print "In Monthy Python - what body part crushes people?"
body_part = raw_input(prompt)

print """
Alright, so you said %r about Python being funny.
You learned Python in %s.
And you work in %s. 
%s is used to crush people in the sitcom - that is hilarious, isn't it!!!
"""% (python, where, work, body_part)


