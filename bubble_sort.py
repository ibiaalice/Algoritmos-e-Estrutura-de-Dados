#coding: utf-8;

def bubble_sort(array):
	for i in xrange(len(array) -1):
		if array[i] > array[i -1]:
			array[i], array[i - 1] = array[i - 1], array[i];
	
	return array;


