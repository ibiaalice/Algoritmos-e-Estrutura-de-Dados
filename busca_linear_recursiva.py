#coding: utf-8;

def buscaLinear(value, array, length):
	if length == 1:
		if vetor[0] == value:
			return 0;
		else:
			return -1;
	else:
		i = buscaLinear(value, array, length -1);
		if i < 0:
			if array[i -1] == value:
				i = length -1;
		
		return i;


