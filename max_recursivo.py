#coding: utf-8;

def max(array, init, end):
	
	if init == end:
		return array[init];
	
	mid = int((init + end) / 2);
	previous = max(array, init, mid);
	after = max(array, mid + 1, end);
	
	if previous > after:
		return previous;
	else:
		return after;


