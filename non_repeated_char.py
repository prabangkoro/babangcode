# author		: babang/DreamHunter
# date			: 8 january 2016
# desc			: program that finds first non-repeated character
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	_found = 0
	i = 0
	_ret = ''
	while not _found:
		if i > len(line):
			break
		elif i >= 0 and i < len(line):
			if line.count(line[i]) == 1:
				_found = 1
				_ret = line[i]
		i += 1
	return _ret

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%s"%_decode(test)

test_cases.close()
