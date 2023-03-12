import queue
import time 
import matplotlib.pyplot as plt

N = 5


#koszmarna funkcja tworzaca potomkow hetmanow

def TworzeniePotomkow2(scr):
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

def SprawdzenieWarunku(el):
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



def BFS2():
    #s0 = [-1,-1,-1,-1]
    s0 = [-1]*N
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
        if(SprawdzenieWarunku(el) and -1 not in el):
            t2 = time.time()
            #print(f"czas potrzebny na odnalezienie stanu {el} : {(t2-t1)}")
            czasy.append(t2-t1)
            t3 += (t2-t1)
            czasy2.append(t3)
            t1 = time.time()
            znalezione.append(el)
        else:
            if el != [N-1]*N:
                tmp = TworzeniePotomkow2(el)
                for p in tmp: fifo2.put(p)
    czascalkowity = (time.time() - t0)
    return znalezione, czasy, czasy2, czascalkowity


znalezione, czasy, czasy2, czascalkowity = BFS2()
j = 1
for stan in znalezione:
    print(f"{j}: {stan}")
    j+=1

print(len(znalezione))
print(czasy)

plt.plot(czasy,'o')
plt.plot(czasy,'r')
plt.show()

plt.plot(czasy2,'o')
plt.plot(czasy2,'b')
plt.show()