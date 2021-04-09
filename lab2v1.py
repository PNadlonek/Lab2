import numpy as np

#Zadanie 3

A1 = np.array([np.linspace(1,5,5),
                np.linspace(5,1,5)])
A2=np.zeros((1,3,2))
A3=np.linspace(2,2,3)
A4=np.linspace(2,2,3)
A5=np.linspace(-90,-70,3)
A6 = np.array([[10], [10], [10], [10], [10]])

A=np.block([[A3],[A4]])
A=np.block([[A],[A5]])
A=np.block([[A2,A]])
A=np.block([[A1],[A]])
A=np.block([[A,A6]])
print(A)

#Zadanie 4

B1 = np.array([5,4,3,2,1,10])
B2 = np.array([0,0,2,2,2,10]) 
B = B1+B2
print(B)


# Zadanie 5 

C=np.max(A,1)
print("C",C)



# Zadanie 6
D=np.delete(B,5)
D=np.delete(D,0)
print(D)

# Zadanie 7 

for i in np.where(D==4):
        D[i]=0
        
print(D)


# Zadanie 8

E = np.delete(C, np.where(C == np.min(C)))
E = np.delete(E, np.where(E == np.max(E)))
#E= np.delete(E,np.where(E==np.min(E)))
print(E)

# Zadanie 9


maxIndex = np.where(A == np.max(A))[0]
for minIndex in np.where(A == np.min(A))[0]:
    if minIndex in maxIndex:
        print(A[minIndex])


# Zadanie 10

print(D@E)
print(D*E)
print(E@D)
print(E*D)


# Zadanie 11

def zadanie11(n):
   y = np.random.randint(10, size=(n,n))
   print("m: \n", y, "\n s: ", sum(y.diagonal()))

zadanie11(5)


# Zadanie 12

def zadanie12(n):     
    [rows, cols] = n.shape
    if rows == cols:
        np.fill_diagonal(n, 0)     
        np.fill_diagonal(np.fliplr(n), 0)     
        print(n)

def zadanie12b(n):
    [rows, cols] = n.shape
    if rows == cols:
        index = cols - 1
        for i in range(rows):
            for j in range(cols):
                if i == j:
                    n[i,j] = 0
                if j == index:
                    n[i,j] = 0
                    index = index - 1
        print(n)
    else: 
        print("macierz musi być kwadratowa")


t = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8], 
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
zadanie12(t)
zadanie12b(t)


# Zadanie 13


def zadanie13(n):
    [rows, cols] = n.shape
    if rows == cols:
        suma = 0
        rows = n.shape[0]
        for i in range (0, rows):
            if (i + 1) % 2 == 0:
                x = sum(n[i,:])
                suma = suma + x
        print (suma)

t = np.array([[1,1,1],
              [2,2,2],
              [3,3,3]])
zadanie13(t)



