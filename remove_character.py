# author		: babang/DreamHunter
# date			: 6 january 2016
# desc			: program that remove any same character
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	_temp = line.split(', ', line.count(', '))
	_ret = ''
	for i in _temp[0]:
		_rem = 0
		for j in _temp[1]:
			if j == i and _rem == 0:
				_rem = 1
		if _rem == 0:
			_ret += i
	return _ret

	

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%s"%_decode(test)   	

test_cases.close()
