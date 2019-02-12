#coding: utf-8;

def MinMaxArray(array):
	min_element = array[0];
	max_element = array[0];
	
	for i in xrange(1, len(vetor)):
		if array[i] < min_element:
			min_element = array[i];
		elif array[i] > max_element:
			max_element = array[i];
		
	
	result = [min_element, max_element];
	
	return result;
