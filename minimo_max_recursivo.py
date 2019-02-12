#coding: utf-8;


def MinMaxArray(array, min_element, max_element, i):
	if array[i] < min_element:
		min_element = array[i];
	if array[i] > max_element:
		max_element = array[i];
	if i < len(array) - 1:
		MinMaxArray(array, min_element, max_element, i + 1);
	else:
		result = [min_element, max_element];
		return result;
		
