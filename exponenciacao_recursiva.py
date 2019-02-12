#coding: utf-8;

def exp_recursivo(b, e):
	if e == 0:
		return 1;
	else:
		return b * exp_recursivo(b, e -1);
	
