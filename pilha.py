#coding: utf-8

import random;

class pilha:
	
	def __init__(self):
		self.__stack = [];
	
	def push(self, value):
		self.__stack.append(value);
	
	def pop(self):
		return self.__stack.pop();
	
	def show(self):
		return "Stack: {}".format(self.__stack);
	
	
