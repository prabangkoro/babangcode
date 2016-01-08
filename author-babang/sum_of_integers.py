# author		: babang/DreamHunter
# date			: 8 january 2016
# desc			: program that calculates the maximum sum of integers in an array
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	temp = line.split(',', line.count(','))
	_sum = 0
	# initial value
	for i in temp:
		_sum += int(i)
	# check another sub array sums
	_sumk = 0
	for i in range(len(temp)):
		for j in range(i+1, len(temp)+1):
			for k in range(i,j):
				_sumk += int(temp[k])
			if _sumk > _sum:
				_sum = _sumk
			_sumk = 0
	return _sum

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%d"%_decode(test)

test_cases.close()
