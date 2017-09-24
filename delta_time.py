#author: babang/Dreamhunter
import sys
test_cases = open(sys.argv[1], 'r')

def _stotm(_str):
	temp = _str.split(':', _str.count(':'))
	return int(temp[0])*3600+int(temp[1])*60+int(temp[2])

def _tmtos(_tm):
	hh = _tm/3600
	mm = (_tm%3600)/60
	ss = _tm%60
	# formatting
	if hh < 10:
		hh = '0'+str(hh)
	if mm < 10:
		mm = '0'+str(mm)
	if ss < 10:
		ss = '0'+str(ss)
	print "%2s:%2s:%2s"%(hh,mm,ss)

def _diff(time1, time2):
	diff = 0
	diff = _stotm(time1) - _stotm(time2)
	if diff < 0:
		diff = -diff
	return diff

def _decode(line):
	temp = line.split(' ', line.count(' '))
	_tmtos(_diff(temp[0], temp[1]))

for test in test_cases:

    if test != '\n':
    	# remove any newline
    	if test[len(test)-1] == '\n':
    		test = test[:len(test)-1]
    	_decode(test)

test_cases.close()
