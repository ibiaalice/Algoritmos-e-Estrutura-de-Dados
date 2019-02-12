#coding: utf-8

def exp(b, e):
	result = b;
	for i in xrange(0, e -1 ):
		result *= b;
	
	return result;
