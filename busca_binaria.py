#coding: utf-8;

# método de busca binária em um array
# importante é ter o array ordenado.
def BuscaBinaria(value, array, left, right):
	mid = int((left + right) / 2);
	
	if left <= right:
		
		if value > array[mid]:
			left = mid + 1;
			return BuscaBinaria(value, array, left, right);
		elif value < array[mid]:
			right = mid - 1;
			return BuscaBinaria(value, array, left, right);
		else
			return mid;
	
	else:
		return -1; 
