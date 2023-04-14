import time
import datetime as dt
from queue import PriorityQueue



def TworzeniePotomkow(scr, N, S):
    potomkowie = []
    if len(scr[1]) >= N: return potomkowie
    for i in range(N):
        potomek = scr[1][:] #kopiowanie rodzica
        potomek.append(i)
        #h1 = heurystyka1(potomek, N)
        #h2 = heurystyka2(potomek,N)
        h3 = S - heurystyka3(potomek)
        #print(h3)
        potomkowie.append((h3,potomek))
    #print(f"potomkowie {scr} = {potomkowie}")
    return potomkowie

def SprawdzenieWarunkow(el,N):
    #print(f"Długość len(el) {len(el)} || {N}")
    if(len(el[1])!=N): return False
    #print(f"priorytet {el[0]} elementu {el[1]}")
    flaga = 0
    for i in range(len(el[1])):
        for y in range(i+1,len(el[1])):
            if y >= N: break            
            w = abs(el[1][i]-el[1][y])
            k = abs(i-y)
            if(w==k): 
                flaga = 1
                break

            if(el[1][i]==el[1][y]):
                flaga = 1
                break
    if flaga==0:
        return True
    else: return False

def BestFS(N):
    s0=(0,[])
    pq=PriorityQueue()
    pq.put(s0)
    znalezione = []
    S = N/2 *(N-1) # dla heurystyki 3
    #czasy
    t0 = time.time()
    t1 = time.time()
    czasy = []
    czasy2 = []
    t3 = 0

    while not pq.empty():
        el =pq.get()
        #if(len(el[1])==N):print(el)

        if(SprawdzenieWarunkow(el, N)):
                t2 = time.time()
                czasy.append(t2-t1)
                t3 += (t2-t1)
                czasy2.append(t3)
                t1 = time.time()
                znalezione.append(el[1])
        tmp = TworzeniePotomkow(el,N, S)
        for p in tmp:
            pq.put(p)
    #print(znalezione)
    #print(czasy)
    #print(czasy2)
    return znalezione, czasy, czasy2

#Heurystyka H1 przykład:

def heurystyka1(wektor, n):
    waga = 0
    for w in wektor:
        if w < n/2:        
            waga += n-w
        else:
            waga+=w+1    
    return (n-len(wektor))*waga


#Heurystyka H2 przykład:
def heurystyka2(el,N):
    ilePol = N*N
    bitepola=set()
    for i in range(N):
        index = -1
        for e in el:
            bitepola.add((i,e))
            index +=1
            #print(f"i={i} || index= {index}")
            bitepola.add((index,i))
            if i > index:
                for y in range(N):
                    #print((i,y))
                    w = abs(e-y)
                    k = abs(i-index)
                    #print(w==k)
                    if(w==k): 
                        #print(f"wiersze: e={e} - y={y} = abs {abs(e-y)}")
                        #print(f"kolumny: i={i} - index={index} = abs {abs(i-index)}")
                        bitepola.add((i,y))
    return ilePol - len(bitepola)


#Heurystyka H3 przykład:
def heurystyka3(el):
    dh = 0
    if (len(el)>1):
        index = -1
        for e in el:
            index+=1
            for i in range(index+1, len(el)):
                if i == index: continue
                if el[i]!=e:
                    dh += 1
    return dh

#Heurystyka H4 przykła:


n=7

znalezione, czasy, czasy2 = BestFS(n)

print(znalezione)
print(czasy)
print(czasy2)

#sprawdzenie
#wektor = [0,2,1,2]
#print(heurystyka3(wektor))