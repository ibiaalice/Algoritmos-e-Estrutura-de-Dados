#coding: utf-8;

class Node:
	
	def __init__(self, value, newNode = None):
		self.__value = value;
		self.newNode = newNode;
	
	@property
	def value(self):
		return self.__value;
	

class LinkedList:
	
	def __init__(self):
		self.__root = None;
	
	def append(self, value):
		if self.__root is None:
			self.__root = Node(value);
			return;
		
		current = self.__root;
		while current.newNode is not None:
			current = current.newNode;
		current.newNode = Node(value);
	
	def remove(self, value):
		if self.__root is None:
			return;
		
		left = None
		current = self.__root;
		
		if current.value == value:
			self.__root == current.newNode;
		
		while True:
			left = current;
			current = current.newNode;
			
			if current is None:
				break;
				
			if current.value == value:
				left.newNode = current.newNode;
	
	def show(self):
		values = [];
		current = self.__root;
		while current is not None:
			values.append(current.value);
			current = current.newNode;
		
		print("Lista Encadeada: {}".format(values));


