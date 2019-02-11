#coding: utf-8;

class Arvore:
	
	#construtor do método:
	def __init__(self, key):
		self.key = key;
		self.left = None;
		self.right = None;
	
	# Método de busca recursiva 
	def buscaRecursiva(node, key):
		if node is None:
			return None;
		if node.key == key:
			return node;
		if key > node.key:
			buscaRecursiva(node.right , key);
		else:
			buscaRecursiva(node.left, key);
	
	# Método de busca Linear
	def buscaLinear(node, key):
		while no is not None:
			if node.key == key:
				return node;
			elif key > node.key:
				node = node.right;
			else:
				node = node.left;
		
		return None;
	
	# Método de inserção 
	def insere(node, key):
		if node is None:
			node = Arvore(key);
		else:
			if key < node.key:
				node.left = insere(node.left, key);
			else:
				node.right = insere(node.right, key);
		
		return node;
	
	
	# Método de Apresentação dos valores de nós
	
	nodes_tree = "";
	
	# Método de apresentação preOrder
	def preOrdem(node):
		global nodes_tree
		if node is None:
			return;
		
		nodes_tree += str(node.key) + ", ";
		preOrdem(node.left);
		preOrdem(node.right);
	
	# Método de apresentação InOrder
	def emOrdem(node):
		global nodes_tree;
		if no is None:
			return;
		emOrdem(node.left);
		nodes_tree += str(node.key) + ", ";
		emOrdem(node.right);
		
	# Método de apresentação PosOrder
	def posOrdem(node):
		global nodes_tree;
		if no is None:
			return;
		posOrdem(node.left);
		posOrdem(node.right);
		nodes_tree += str(node.key) + ", ";
	
	
	#método de procura do elemento maximo
	def maximo(x, y):
		if x > y:
			return x;
		return y;
	
	#método de cálculo de altura
	def altura(node):
		if node is None:
			return 0;
		return 1 + maximo( altura(node.left), altura(node.right));
		
	#método de exclusão
	def buscaNoPai(node, key):
		parent = node;
		while node is not None:
			if node.key == key:
				return parent
			parent = node;
			if node.key < key:
				node = node.right;
			else:
				node = node.left;
		return parent;
	
	#método de procura do maior a esquerda
	def maiorEsquerda(node):
		node = node.left;
		while node.right is not None:
			node = node.right;
		return node;
	
	#método de excluir no na arvore
	def excluir(node, key):
		atual = buscaLinear(node, key);
		if atual is None:
			return False;
		parent = buscaNoPai(node, key);
		
		if atual.left is None or atual.right is None:
			if atual.left is None:
				aux = atual.right;
			else:
				aux = atual.left;
			if parent is None:
				node = aux;
			elif key > parent.key:
				parent.right = aux;
			else:
				parent.left = aux;
			
		else:
			aux = maiorEsquerda(atual);
			atual.key = aux.key;
			if aux.left is not None:
				atual.left = aux.left;
			else:
				atual.left = None;
			
		return True;
