#fungsi dengan satu argumen
def my_function(fname):       #fname adalh parameter
    print(fname + ' refsnes')
    
my_function('email')          #email adalah argumen

#fungsi dengan 2 argumen
def my_function(fname, lname):       
    print(fname + ' ' + lname) 
    
my_function('email', 'refsnes') #jumlah argumen yang dipanggil harus sama dengan jumlah pameter

#nilai parameter default
def my_function(name = 'friend'):
    print('hello', name)
    
my_function('email')
my_function()  #ini akan mencetak secara default 'friend'

#kata kunci argumen
def my_function(animal, name):
    print('i have a', animal)
    print('my', animal + "'s name is", name)
    
my_function(animal = 'dog', name = 'buddy') #memasukkan kata kunci animal dan name yang sesuai

#argumen posisional
def my_function(animal, name):
    print('i have a', animal)
    print('my', animal + "'s name is", name)
    
my_function('dog','buddy') #argumen posisional harus berada dalam urutan yang benar

#mengembalikan nilai
def my_function(x,y):
    return x+y

result = my_function(5,3)
print(result) #akan menampilkan nilai dari x+y = 8

#mengembalikan tipe data yang berbeda
def my_function():
    return ['apel', 'pisang', 'cery']

buah = my_function()
print(buah[1]) #fungsi yang mengembalikan sebuah daftar

#argumen khusus kata kunci 
def my_function(*, name):
    print('hello', name)
    
my_function(name = 'email') #tanpa kata kunci name, kode akan eror