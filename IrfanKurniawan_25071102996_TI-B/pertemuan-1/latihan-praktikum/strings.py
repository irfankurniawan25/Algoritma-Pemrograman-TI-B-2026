#string dikelilingi oleh tanda kutip dua atau satu
print('hello') #ini string dengan tanda kutip satu
print("hello") #ini string dengan tanda kutip dua

#kutipan didalam kutip 
print("hello 'world!'")

#menetapkan string ke variabel
a = 'hello'
print(a)

#stirng adalah array
a = 'hello'
print(a[1]) #akan menampilkan 'e'

#melakukan perulangan pada sting
for x in 'hello':
    print(x)
    
#menghitung panjang string
a = 'hello, world!'
print(len(a)) #menampilkan panjang dari variabel a = 13

#memeriksa karakter tertentu dalam sebuah string
txt = 'the best things in life are free!'
print('free' in txt) #akan menampilkan True

#memeriksa karakter tertentu tidak ada dalam sebuah string
txt = 'the best things in life are free!'
print('expensive' not in txt) #akan menampilkan True