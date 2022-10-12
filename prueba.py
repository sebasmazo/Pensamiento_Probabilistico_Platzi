
# Sea conteo un vector de longitud 5 con los siguientes valores
conteo  = [1, 2, 2, 3, 3]  
m = 5

conteo2 = conteo 
n = len(conteo)     # Es cinco

i=1

while (i <= n):
    conteo_i = conteo2[i]
    j = 1
    while (j <= m):
        if (j == conteo_i):
            del conteo[-1]  # Elimina el primer elemento que este en el vector "conteo"
            m = m - j
            break  # Rompe el ciclo en el q se encuentra
        else: 
            j = j + 1     
    i = i + 1


resultado = len(conteo)

print(resultado)