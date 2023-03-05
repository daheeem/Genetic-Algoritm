import random
import math

intervalX = [-5, 5]
intervalY = [-5, 5]

def function(x,y):
    fungsi = ((math.cos(x) + math.sin(y))**2 / ((x)**2 + (y)**2))
    return fungsi

#Membuat individu/kromosom baru
def individu(length):
    indiv = [random.randint(0,9) for x in range(length)]
    return indiv

#Membuat populasi dari individu/kromosom yang telah dibuat
def populasi(pop,length):
    pops = [individu(length) for x in range(pop)]
    return pops

def split(krom):
    spl = (krom[:len(krom)//2],krom[len(krom)//2:])
    return spl

#Fungsi decode integer
def decode(krom, interval):
    sigma = 0
    g = 0
#rumus integer
    for i in range(len(krom)) :
        n = krom[i]
        g += (n * (10**-(i+1)))
        sigma += (9 * (10**-(i+1)))
    hasil = interval[0] + (((interval[1]-interval[0]) / sigma) * g)  
    return hasil

def fit_value(x,y):
    return 1/(0.01 + function(x,y))
#Menhitung nilai fitness dari masing masind individu/kromosom pada populasi
def hitungfitness(populasi):
    fitness_populasi=[]
    for i in range(len(populasi)):
        x,y = split(populasi[i])
        kromX = decode(x,intervalX)
        kromY = decode(y,intervalY)
        fit_value(kromX,kromY)
        fitness_populasi.append(fit_value(kromX,kromY))

    return fitness_populasi

#Seleksi 10 individu yang ada pada populasi sehingga menjadi 2 parent
def seleksi_orangtua(populasi):
    fitness_cand = []
    cand = []
    for i in range(4):
        n = random.randint(0,len(populasi)-1)
        cand.append(populasi[n])
    fitness_cand = hitungfitness(cand)

    parent1 = fitness_cand[0]
    for j in range(len(fitness_cand)):
        if (fitness_cand[j] >= parent1):
            parent1 = fitness_cand[j]
            idx_parent1 = fitness_cand.index(parent1)
    
    parent2 = fitness_cand[0]
    if (parent2 == parent1):
        parent2 = fitness_cand[1]

    idx_parent2 = 0
    for k in range(len(fitness_cand)):
        if(fitness_cand[k] != parent1 and fitness_cand[k] >= parent2):
            parent2 = fitness_cand[k]
            idx_parent2 = fitness_cand.index(parent2)
            
    return (cand[idx_parent1], cand[idx_parent2])

#Menyilangkan kedua parent tersebut dan menghasilkan child yang baru
def cross_over(parent1,parent2,peluang):
    c1 = []
    c2 = []
    #n adalah titik silang
    n = (len(parent1) // 2)
    if random.random() >= peluang:
        c1 = parent1
        c2 = parent2

    else:
        c1[:n]=parent1[:n]
        c1[n:]=parent2[n:]
        c2[:n]=parent2[:n]
        c2[n:]=parent1[n:]
    return (c1,c2)       

#Mutasi child tersebut sehingga menghasilkan child yang baru
def mutasi(child,peluang):
    if random.random()>=peluang:
        #posisi mutasi
        x = random.randint(1,len(child)-1)
        y = random.randint(1,len(child)-1)
        while (y == x):
           y = random.randint(1,len(child)-1)
        
        #nilai mutasi
        m = random.randint(0,9)
        n = random.randint(0,9)
        child[x] = m
        child[y] = n
    return child

#Seleksi_Survivor dengan regenerasi yaitu mengganti individu/kromosom terburuk dengan child baru hasil mutasi
def regenerasi(populasi,c1,c2):
    fit = hitungfitness(populasi)
    fitness1 = hitungfitness(populasi)
    fitness2 = fitness1
    fitness2.sort()

    a = fitness2[0]
    b = fitness2[1]

    #Mencari individu terburuk pertama
    for i in range(len(populasi)) :
        if fit[i] == a :
            x = i
            #print("idx i : ",i)
            #print("Ini x : ",x)
    populasi.pop(x)
    populasi.append(c1)
    
    #Mencari individu terburuk kedua
    for j in range(len(populasi)) :
        if fit[j] == b :
            y = j
            #print("idx j : ",j)
            #print("Ini y : ",y)
    populasi.pop(y)
    populasi.append(c2)

    return populasi

def bestkrom(populasi):
    fitAfter = hitungfitness(populasi)
    fitMax = fitAfter
    fitMax.sort(reverse=True)
    fitMax_value = fitMax[0]

    fitPopDefault = hitungfitness(populasi)
    for i in range(len(fitPopDefault)):
        if fitPopDefault[i] == fitMax_value:
            idx_best = i

    best_krom = populasi[idx_best]
    return best_krom, fitMax_value

#MAIN PROGRAM
pops = int(input("Jumlah Populasi: "))
kromosom = int(input("Panjang kromosom: "))
pop = populasi(pops, kromosom)
generasi = int(input("Jumlah Generasi: "))

i = 0
while i < generasi :
    print()
    print("GENERASI KE-",i+1)
    print(pop)

    #Seleksi 10 individu yang ada pada populasi sehingga menjadi 2 parent
    a,b = (seleksi_orangtua(pop))

    #Menyilangkan kedua parent tersebut dan menghasilkan child yang baru
    c,d = cross_over(a,b,0.7)

    #Mutasi child tersebut sehingga menghasilkan child yang baru
    p = mutasi(c,0.7)
    q = mutasi(d,0.7)

    #Seleksi_Survivor dengan regenerasi yaitu mengganti individu/kromosom terburuk dengan child baru hasil mutasi
    regenerasi(pop,p,q)
    i = i + 1

best_krom, best_value = bestkrom(pop)
print()
print("Best Kromosom    : ",best_krom)
print("Best Fitness     : ",best_value)

for i in range(len(best_krom)):
    X, Y = split(best_krom)
    valueX = decode(X, intervalX)
    valueY = decode(Y, intervalY)

print("X = ",valueX)
print("Y = ",valueY)


nilaiServis = [['Buruk', 0],['Cukup', 0], ['Baik', 0], ['Sangat Baik', 0]]
nilaiServis[0][1] = 1
print(nilaiservis[0])