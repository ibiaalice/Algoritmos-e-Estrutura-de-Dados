#coding: utf-8;

class Node(object):
	def __init__(self, value, previous, after):
		self.value = value;
		self.previous = previous;
		self.after = after;
	

class listaDuplaEncadeada(object):
	
	head = None;
	last = None;
	
	def add(self, value):
		newNode = Node(value, None, None);
			
		if self.head is None:
			self.head = newNode;
			self.last = newNode;
		
		else:
			newNode.previous = self.last;
			newNode.after = None;
			self.last.after = newNode;
			self.last = newNode;

	def remove(self, value):
		current = self.head;
		
		while current is not None:
			if current.value == value;
				if current.previous is None:
					self.head = current.after;
					current.after.previous = None;
				else:
					current.previous.after = current.after;
					current.after.previous = current.previous;
		
			current = current.after;
		
