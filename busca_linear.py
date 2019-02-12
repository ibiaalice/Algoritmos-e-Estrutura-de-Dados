#coding: utf-8;

#método de busca linear
def buscaLinear(value, array):
	for i in xrange(0, len(array)):
		if array[i] == value:
			return i;
	
	return -1; 
