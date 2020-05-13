
import time
def rechercheDicho(L: list, elt: int)-> int:
   L =sorted(L)
   e = 0
   tr = False
   deb = 0
   fin = len(L)-1
   t1 = time.perf_counter()
   while tr == False and deb<=fin:
       e = e+1
       mil = int(((deb+fin)/2))
       print(mil)
       if L[mil] == elt:
           tr = True
       else:
           if elt>L[mil]:
               deb = mil+1
           else:
                fin = mil-1

   duree = time.perf_counter() - t1
   if tr==True:
       return ("voila le nombre d'etape(s)"),e,("afin de trouver"),elt,('durée ='),duree
   else:
       return -1,('durée ='),duree


