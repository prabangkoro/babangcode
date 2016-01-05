# author		: babang/DreamHunter
# date			: 5 january 2016
# desc			: program that counts minimum number of coins
import sys
test_cases = open(sys.argv[1], 'r')

# number of coin 3:
# 1, 3, 5
def _count(num):
	counts = 0
	while num != 0:
		if num >= 5:
			num -= 5
			counts += 1
		elif num < 5 and num >= 3:
			num -= 3
			counts += 1
		else :
			num -= 1
			counts += 1
	return counts

def _decode(line):
	return _count(int(line))

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%s"%_decode(test)
    	

test_cases.close()
