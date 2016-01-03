# author		: babang/DreamHunter
# date			: 3 january 2016
# desc			: program that counts any unique number in a file
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	_temp = line.split(' ', line.count(' '))
	_ret = 0
	_found = 0
	for i in range(1, 10):
		if _temp.count(str(i)) == 1 and not _found:
			_ret = _temp.index(str(i)) + 1
			_found = 1
	return _ret

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%s"%_decode(test)
    	

test_cases.close()
