def penambahan(a,b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b

def modulus(a,b):
    return a % b

def fibbonacci(n):
    if n <= 1:
        return n
    else:
        deret = []
        a,b = 0, 1
        for i in range(n):
            deret.append(a)
            a, b = b, a + b
    return deret
        
        