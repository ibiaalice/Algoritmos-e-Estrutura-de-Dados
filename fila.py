#coding: utf-8;

import random;

class Fila:
	
	def __init__(self):
		self.__queue = [];
	
	def enqueue(self, value):
		self.__queue.append(value);
	
	def dequeue(self):
		return self.__queue.pop(0);
	
	def show(self):
		print("Fila: {}".format(self.__queue));
	
