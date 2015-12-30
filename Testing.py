#this program code created to answer the Testing challenge
import sys
test_cases = open(sys.argv[1], 'r')

def _check(line):
    test = line.split(' | ', 1)

    test1 = test[1]
    obj = test[0]
    count = 0

    for i in range(len(obj)):
        if obj[i] != test1[i]:
            count += 1
    return count


for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	
    	num = _check(test)
        if num == 0:
            print "Done"
        elif num <= 2 :
            print "Low"
        elif num > 2 and num <= 4:
            print "Medium"
        elif num > 4 and num <= 6:
            print "High"
        elif num > 6:
            print "Critical"

test_cases.close()
