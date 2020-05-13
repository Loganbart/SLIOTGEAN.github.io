def triSelection(L: list)-> list:
    n = len(L)
    for j in range(0,n-1):
	    mini = j
	    for i in range(j+1,n):
		    if L[i]<L[mini]:mini = i
	    temps = L[j]
	    L[j] = L[mini]
	    L[mini] = temps
    return L