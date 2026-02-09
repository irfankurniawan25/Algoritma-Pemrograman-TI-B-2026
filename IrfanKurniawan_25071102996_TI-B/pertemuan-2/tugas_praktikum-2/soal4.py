def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b-1)
    
a = int(input('a = ')) # a = 2
b = int(input('b = ')) # b = 5
print(f'hasil dari {a}^{b} adalah', pangkat_rekursif(a,b)) #output: 32