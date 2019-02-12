#coding: utf-8;

def heap_sort(array):
	
	length = len(array);
	index = len(array) / 2;
	parent = 0;
	child = 0;
	aux = 0;
	
	while True:
		if index > 0:
			index -= 1;
			aux = array[index];
		
		else:
			length -= 1;
			
			if length == 0:
				return;
			
			aux = array[length];
			array[length] = array[0];
		
		parent = index;
		child = index * 2 + 1;
	
	while child < length:
		if(child + 1) < length and array[child + 1] > array[child]:
			child += 1;
		if array[child] > aux:
			array[parent] = array[child];
			parent = child;
			child = parent * 2 + 1;
		else:
			break;
		
	array[parent] = aux;
