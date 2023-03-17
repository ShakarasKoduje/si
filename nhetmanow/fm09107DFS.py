
import time


def TworzeniePotomkow(scr, N):
    potomkowie = []
    glebokosc = -1
    for i in range(len(scr)):
        if(scr[i]==-1):
            glebokosc = i
            break

    if glebokosc == -1: return potomkowie
    for i in range(N):
        potomek = scr[:]
        potomek[glebokosc] = i
        potomkowie.append(potomek)
    return potomkowie


def TworzeniePotomkow2(scr, N):
    potomkowie = []
    glebokosc = -1
    for i in range(len(scr)):
        if(scr[i]==-1):
            glebokosc = i
            break

    if glebokosc == -1: return potomkowie
    for i in range(N):
        potomek = scr[:]
        if glebokosc > 0:
            w = abs((glebokosc-1)-glebokosc)
            k = abs(i-potomek[glebokosc-1])     
            #if potomek[glebokosc-1]!=i and  w != k:
            if i not in potomek and  w != k:
                potomek[glebokosc] = i      
                potomkowie.append(potomek)
        else:
            potomek[glebokosc] = i
            potomkowie.append(potomek)
        
    #print(potomkowie)
    return potomkowie



def SprawdzenieWarunku(el,N):
    flaga = 0
    for i in range(N):
        for y in range(i+1,N):            
            w = abs(el[i]-el[y])
            k = abs(i-y)
            if(w==k): 
                flaga = 1
                break

            if(el[i]==el[y]):
                flaga = 1
                break
    if flaga==0:
        return True
    else: return False


def DFS(N):
    s0 = [-1]*N
    ostatniPotomek = [N-1]*N #warunek stopu
    lifo2 =  []
    lifo2.append(s0)
    tmp = []
    #tmp2 = []
    znalezione = []
    t0 = time.time()
    t1 = time.time()
    czasy = []
    czasy2 = []
    t3 = 0
    
    while len(lifo2)>0:
        el = lifo2.pop()
        #tmp2 += el
        if(SprawdzenieWarunku(el, N) and -1 not in el):
            t2 = time.time()
            #print(f"czas potrzebny na odnalezienie stanu {el} : {(t2-t1)}")
            czasy.append(t2-t1)
            t3 += (t2-t1)
            czasy2.append(t3)
            t1 = time.time()
            znalezione.append(el)
        else:
            if el != ostatniPotomek:
                tmp = TworzeniePotomkow2(el, N)
                if len(tmp) > 0: 
                    for p in tmp:
                        lifo2.append(p)
    czascalkowity = (time.time() - t0)
    return znalezione, czasy, czasy2, czascalkowity

'''
#############################################################
Program będzie zapisywał wyniki do pliku o.txt
'''

import sys
original_stdout = sys.stdout
with open('o2.txt', 'w') as f:
    sys.stdout = f
    for n in range(4,12):
        start = time.time()
        
        znalezione, czasy, czasy2, czascalkowity = DFS(n)
        koniec = time.time()
        print(f'''koniec obliczen DFS dla {n}-hetmanow, obliczenia zajely {koniec - start} sekund
        znaleziono {len(znalezione)} rozwiazan problemu.
        ''')
    '''
        for x in znalezione:
            print(x)
            for i in x:
                for j in range(len(x)):
                    if(i==j):
                        print("H", end=" ")
                    else: print("+", end=" ")
                print()
            print()
    '''
        #print(f"koniec obliczen DFS, obliczenia zajely {koniec - start} sekund")

    sys.stdout = original_stdout

'''
for n in range(4,9):
        start = time.time()
        znalezione, czasy, czasy2, czascalkowity = DFS(n)
        koniec = time.time()
        print(f"koniec obliczen DFS dla {n}-hetmanow, obliczenia zajely {koniec - start} sekund")

        for x in znalezione:
            print(x)
            for i in x:
                for j in range(len(x)):
                    if(i==j):
                        print("H", end=" ")
                    else: print("+", end=" ")
                print()
            print()

        print(f"koniec obliczen DFS, obliczenia zajely {koniec - start} sekund")
'''

'''
n=7

start = time.time()
znalezione, czasy, czasy2, czascalkowity, dlugosclisty = DFS(n)
koniec = time.time()


for x in znalezione:
    print(x)
    for i in x:
        for j in range(len(x)):
            if(i==j):
                print("H", end=" ")
            else: print("+", end=" ")
        print()
    print()
print(len(znalezione))
print(f"koniec obliczen DFS dla {n}-hetmanow, obliczenia zajely {koniec - start} sekund")
print(dlugosclisty)
'''
