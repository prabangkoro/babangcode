# author		: babang/DreamHunter
# date			: 2 january 2016
# desc			: program that encode writer's name
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	temp = line.split('|', line.count('|'))
	_dec = temp[1].split(' ', temp[1].count(' '))
	_res = ''
	for i in _dec:
		if(i.isdigit()):
			_res = _res+(temp[0][int(i)-1])
	print _res

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]
    	_decode(test)
    	print ""

test_cases.close()
