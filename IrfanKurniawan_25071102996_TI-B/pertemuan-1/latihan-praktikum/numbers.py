x = 1    #integer
y = 0.5  #float
z = 1j   #kompleks

#konversi dari tipe satu ke tipe lain 
a  = float(x)   #konversi dari integer ke float
b = int(y)      #konversi dari float ke integer
c = complex(x)  #konversi dari integer ke kompleks

print(a)
print(b)
print(c)

#cetak tipe data variabelnya
print(type(a))
print(type(b))
print(type(c))

#bilangan acak dengan import random
import random
print(random.randrange(1,10)) #ini akan menampilkam amgka acak dari 1 sampai 9