c = [0 for i in range(5)]
p = 0

for i in range(3):
    print("i ",i)
    for j in range(i):
        print(i)
        if i>=j:
            print("j ",j)
            c[p] = j*i + 2 
            p = p+1
            print(p)
            
print(c)