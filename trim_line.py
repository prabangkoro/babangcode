# author		: babang/DreamHunter
# date			: 2 january 2016
# desc			: program that limits any long line
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	if len(line) <= 55 :
		print "%s"%line
	else :
		line = line[:39]
		if line[len(line)-1] == ' ':
			line = line[:len(line)-1]
		elif line[len(line)-2] == ' ':
			line = line[:len(line)-2]
		elif line[len(line)-3] == ' ':
			line = line[:len(line)-3]
		print "%s"%(line+"... <Read More>")

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]
    	_decode(test)
    	

test_cases.close()
