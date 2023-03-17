import queue
import time 
import matplotlib.pyplot as plt

#Rozmiar szachownicy NxN:



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
        potomek[glebokosc] = i
        potomkowie.append(potomek)
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



def BFS2(N):
    s0 = [-1]*N
    ostatniPotomek = [N-1]*N #warunek stopu
    fifo2 =  queue.Queue()
    fifo2.put(s0)
    tmp = []
    tmp2 = []
    znalezione = []
    t0 = time.time()
    t1 = time.time()
    czasy = []
    czasy2 = []
    t3 = 0
    while not fifo2.empty():
        el = fifo2.get()
        tmp2 += el
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
                for p in tmp: fifo2.put(p)
    czascalkowity = (time.time() - t0)
    return znalezione, czasy, czasy2, czascalkowity

#N = 5
'''
#############################################################
Program będzie zapisywał wyniki do pliku o.txt
'''
import sys
original_stdout = sys.stdout
with open('o.txt', 'w') as f:
    sys.stdout = f
    for n in range(4,9):
        start = time.time()
        znalezione, czasy, czasy2, czascalkowity = BFS2(n)
        koniec = time.time()
        print(f"koniec obliczen BFS dla {n}-hetmanow, obliczenia zajely {koniec - start} sekund")
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
        #print(f"koniec obliczen BFS, obliczenia zajely {koniec - start} sekund")

    sys.stdout = original_stdout