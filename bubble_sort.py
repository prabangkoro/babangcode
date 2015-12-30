#this code is created for the answer of codeeval.com
#sorting in bubble sort
import sys
test_cases = open(sys.argv[1], 'r')

def _sort(liss):
	# buble sort
	for i in range(0, len(liss)-1):
		for j in range(len(liss)-2, i-1, -1):
			if float(liss[j])>float(liss[j+1]):
				temp = liss[j]
				liss[j] = liss[j+1]
				liss[j+1] = temp
	return liss


for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	temp = test.split(' ', test.count(' '))
    	# temp = int(temp)
    	for tee in temp:
    		tee = float(tee)

    	_sort(temp)

    	for tee in temp:
    		print "%s "%tee,
    	
    	# print "%s"%temp[test.count(' ')-1]
    print ""
    	

test_cases.close()
