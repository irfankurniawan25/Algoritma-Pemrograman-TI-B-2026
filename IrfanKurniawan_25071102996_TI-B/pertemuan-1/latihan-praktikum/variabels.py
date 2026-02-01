#legal
myvar = 'irfan'
my_var = 'irfan'
_my_var_ = 'irfan'
myVar = 'irfan'
MYVAR ='irfan'
myvar2 = 'irfan'

#nama variabel peka terhadap huruf besar dan kecil

#ilegal
# 2myvar = 'irfan'
# my-var = 'irfan'
# my var = 'irfan'

#nama variabel multi kata
myVariabelName = 'irfan'   #setiap kata, kecuali kata pertama diawali huruf besar
MyVariabelName = 'irfan'   #setiap kata diawali dengan huruf kapital
my_variabel_name = 'irfan' #setiap kata dipisahkan oleh garis bawah

#banyak nilai untuk variabel dalam satu baris
x,y,z = 'jeruk', 'pisang', 'cery'
print(x)
print(y)
print(z)

#satu nilai untuk beberapa variabel
x = y = z = 'pisang'
print(x)
print(y)
print(z)

#kumpulan nilai dalam satu variabel
buah = ['apel', 'pisang', 'cery']
x,y,z = buah
print(x)
print(y)
print(z)

x = 'hello world!'
print(x) #digunkan untuk menampilkan variabel

x = 'hello'
y = 'world!'
print(x,y) #menampilkan beberapa variabel dengan dipisahkan oleh koma

x = 'hello ' #spasi digunakan untuk memberikan jarak antar kalimat
y = 'world!'
print(x + y) #menampilkan beberapa variabel dengan tanda tambah

x = 'awesome' # x variabel global

def myfunc():
    x = 'fantastic' # x varibel lokal
    print("python is",x)
    
myfunc() #x akan menampilkan yang variabel lokal

print('python is',x) #x akan menampilakan variabel global