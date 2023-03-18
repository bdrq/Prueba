import random

arrays = []
v=0
n = int(input("Por favor ingrese la cantidad de numeros que necesita=> "))
x = 0
while x < n:
    r = random.randrange(99999)
    arrays.append(r)
    x+=1

for i in range(len(arrays)):
    for j in range(i+1):
        if arrays[j]>arrays[i]:
            temp=arrays[i]
            arrays[i]=arrays[j]
            arrays[j]=temp
    v+=1

for m in arrays:
    print(m)

print("El tamaño del vector es=> ",len(arrays))
print(v)
print(x)

