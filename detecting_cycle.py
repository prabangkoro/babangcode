# author		: babang/DreamHunter
# date			: 5 january 2016
# desc			: program that find any cycle
import sys
test_cases = open(sys.argv[1], 'r')

# at the beginning, im trying to use floyd 
# but i dont really understand the implementation
# so i just use my own logic, but it works :D
def _floyd(_list):
	idx = 0
	mu = 0
	lam = 0
	found = 0
	while found == 0 and idx < len(_list):
		a = _list[idx]
		for i in range(idx+1,len(_list)):
			b = _list[i]
			if a == b and found == 0:
				found = 1
				mu = idx
				lam = i - idx
		idx += 1

	return lam, mu


def _decode(line):
	_temp = line.split(' ', line.count(' '))
	lam , mu = _floyd(_temp)
	for i in range(lam):
		print "%s"%_temp[mu+i],

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	_decode(test) 
    	print ''   	

test_cases.close()
