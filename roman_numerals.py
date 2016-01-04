# author		: babang/DreamHunter
# date			: 4 january 2016
# desc			: program that convert decimal to romanian number
import sys
test_cases = open(sys.argv[1], 'r')

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
def _roma(num):
	if num == 0:
		return ''
	elif num < 4:
		# code here
		return 'I'+_roma(num-1)
	elif num == 4:
		return 'IV'
	elif num < 9:
		return 'V'+_roma(num-5)
	elif num == 9:
		return 'IX'
	elif num < 40:
		return 'X'+_roma(num-10)
	elif num < 50:
		return 'XL'+_roma(num-40)
	elif num < 90:
		return 'L'+_roma(num-50)
	elif num < 100:
		return 'XC'+_roma(num-90)
	elif num < 400:
		return 'C'+_roma(num-100)
	elif num < 500:
		return 'CD'+_roma(num-400)
	elif num < 900:
		return 'D'+_roma(num-500)
	elif num < 1000:
		return 'CM'+_roma(num - 900)
	elif num < 4000 :
		return 'M'+_roma(num-1000)
	elif num >= 4000:
		return ''


def _decode(line):
	_temp = int(line)
	_ret = ''
	_ret = _roma(_temp)
	return _ret

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]

    	print "%s"%_decode(test)
    	

test_cases.close()
