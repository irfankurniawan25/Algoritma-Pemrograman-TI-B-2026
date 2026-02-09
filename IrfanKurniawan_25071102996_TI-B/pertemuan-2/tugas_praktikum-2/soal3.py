def jumlah_digit(n):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlah_digit(n // 10)
    
x = int(input('n = ')) # n = 1234
print(f'jumlah digit {x} adalah', jumlah_digit(x)) #output: 10