from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

fifth = raw_input("Give me another variable: ")
print "Your fifth variable is: %r" % fifth