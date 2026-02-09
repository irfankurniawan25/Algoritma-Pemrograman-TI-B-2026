def bilangan_prima(n):
    prima = []
    
    for angka in range(2, n+1):
        cekPrima = True
        
        for x in range(2, angka):
            if (angka % x) == 0:
                cekPrima = False
                break
            
        if cekPrima:
            prima.append(angka)
    return prima

n = int(input("n = ")) # n = 50
print(f'bilangan prima dari {n} adalah',bilangan_prima(n))
#output [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 