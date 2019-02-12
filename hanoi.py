#coding: utf-8;

def hanoi(a, b, c, num):
	if num == 1:
		print 'Move from ' + str(a) + 'to ' + str(b);
	else:
		hanoi( a, b, c, num -1);
		hanoi( a, b, c, 1);
		hanoi( a, b, c, num -1);
		
	
