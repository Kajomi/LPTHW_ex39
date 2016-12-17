from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "Are you sure you want to erase the file?"

raw_input('Your answer here\n\t>>> ')

print "First, let's open the file."
my_file = open(filename, 'w') # opening the file in 'write' mode, the default is 'r' as in 'read'.

print "Now, we can erase that file. No objections are accepted anymore!"
my_file.truncate()

print "Next, I am going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Next step is to write these amazing lines \nto the file we just erased."

my_file.write(line1 + '\n' + line2 + '\n' + line3) 

print "Finally, we shall close the file so you can be amazed by your poetry."

my_file.close()