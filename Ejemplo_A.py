d=[]
contador=0
filas=int (input("Digite número de filas:"))
columnas=int (input("Digite número de columnas:"))
for i in range(filas):
    d.append([])
    for j in range(columnas):
        d[i].append(None)

for i in range(filas):
    for j in range(columnas):
        d[i][j]=int (input("Digite número:"))

for i in range(filas):
    for j in range(columnas):
        if(d[i][j]==5):
            contador=contador+1
                    
print(contador)      
