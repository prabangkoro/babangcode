# author		: babang/DreamHunter
# date			: 12 january 2016
# desc			: program that calculates number of lucky number
import sys
test_cases = open(sys.argv[1], 'r')

def _luck(_dig, _sum):
	if _dig == 1:
		return 1
	elif _dig > 1:
		tmp = 0
		for i in range(10):
			if (_sum-i) >= 0 and (_sum-i) <= (_dig-1)*9:
				tmp += _luck(_dig-1, _sum-i)
		return tmp
	elif _dig < 0:
		return 0

def _decode(line):
	digit = int(line)
	_sum = 0
	for sums in range(0, digit/2*9+1):
		_sum += _luck(digit/2, sums)*_luck(digit/2, sums)
	return _sum

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%d"%_decode(test)

test_cases.close()
