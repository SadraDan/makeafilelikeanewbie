from sys import argv
script, filename = argv
print "OK we have %r" %filename
print "We want to add something to %r" %filename
raw_input("Are you ready?")
target = open(filename, 'w')

print "Now add your lines to your new text file:"
prompt = raw_input()
target.write(prompt)

print "Now we close the file. Enjoy!"
target.close()

