import time
import random

maxVal =10
nVal = 5
listeNombres = random.choices(range(maxVal),k=nVal)
def triSelection(L: list)-> list:
    """
    A compléter
    """
    return # A compléter

def triInsertion(L: list)-> list:
	t1 = time.time()
	compteur = 0
	print(L)
	n = len(L)
	for i in range(1,n):
		VT = L[i]
		j = i-1
		while j>=0 and VT < L[j]:
			L[j+1] = L[j]
			compteur+=1
			j = j-1
		L[j+1] = VT
	t2 = time.time()-t1
	print(t2)
	print(compteur)
	return L