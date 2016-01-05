# author		: babang/DreamHunter
# date			: 5 january 2016
# desc			: program that shows Mth to the last element
import sys
test_cases = open(sys.argv[1], 'r')


def _decode(line):
	_temp = line.split(' ', line.count(' '))
	num = int(_temp[len(_temp)-1])
	if num > len(_temp)-1:
		return ''
	else:
		return _temp[len(_temp)-1-num]

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%s"%_decode(test)
    	

test_cases.close()
