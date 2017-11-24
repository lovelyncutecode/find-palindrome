# -*- coding: utf-8 -*-
def isPalindrome(x):#определяет является ли число палиндромом путем реверсирования числа, преобразованного в строку, возращает соответствующее булевое значение
	revx=str(x)[::-1]
	if x==int(revx):
		return True
	else: return False

def primeList(l,h):#основываясь на алгоритме решета Эратосфена, отбирает простые числа в диапазоне от l до h, возвращая список с этими числами
	import math
	a = [True] * (h-l)
	for i in range(2, int(math.sqrt(h))):
		for j in range(i * 2, h, i):
			if j<l:
				continue
			a[j-l] = False
	b = [i+l for i in range(0, h-l) if a[i]]
	return b	

def prod(l,h):#находит наибольший палиндром, возвращая найденный палиндром и сомножители  
	list=primeList(l,h)
	maxPalindrome=[0,0,0]
	for i in list:
		for j in list:
			if j<=i:
				continue	
			resMaxPal=i*j
			if isPalindrome(resMaxPal) and resMaxPal>maxPalindrome[0]: 	
				maxPalindrome=[resMaxPal,i,j]
	
	return maxPalindrome	

def main():
	res=prod(10000,99999)
	print('Got {} after multiplying {} by {} :::-)'.format( *res))

if __name__ == '__main__':
    main()	


