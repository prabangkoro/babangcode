# author		: babang/DreamHunter
# date			: 6 january 2016
# desc			: program that detect any intersection
import sys
test_cases = open(sys.argv[1], 'r')

def _decode(line):
	_temp = line.split(';', line.count(';'))
	_temps1 = _temp[0].split(',', _temp[0].count(','))
	_temps2 = _temp[1].split(',', _temp[1].count(','))

	_found = 0
	idx = -1
	idy = -1
	for i in range(len(_temps1)):
		for j in range(len(_temps2)):
			if _temps1[i] == _temps2[j] and _found == 0:
				_found = 1
				idx = i
				idy = j
	res = ''
	if idx != -1:
		num = len(_temps1)
		for i in range(idx, num):
			if idy != len(_temps2):
				if _temps1[i] == _temps2[idy]:
					if idy == len(_temps2)-1 or i == len(_temps1)-1:
						# the case is end of list
						res += _temps1[i]
					elif _temps1[i+1] != _temps2[idy+1]:
						# if the next element is not the same
						res += _temps1[i]
					else:
						# print with comma
						res += (_temps1[i]+',')

				idy += 1
		print '%s'%res
	else :
		print ''

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	_decode(test)

test_cases.close()
