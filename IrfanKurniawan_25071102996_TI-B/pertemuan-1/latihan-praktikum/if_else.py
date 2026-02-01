#if mengevaluasi suatu kondisi, jika kondisinya benar, blok kode di dalam pernyataan if akan dieksekusi, jika salah, blok kode akan dilewati
number = 15
if number > 0:
  print('the number is positive')

#penggunaan elif untuk menyatakan "jika kondisi sebelumnya tidak benar, maka coba ini"
a = 33
b = 33
if b > a:
  print('b is greater than a')
elif b == a:
  print('a and b are equal')
  
#pernyataan else akan dieksekusi ketika kondisi if dan elif bernilai False 
a = 200
b = 33
if b > a:
  print('b is greater than a')
elif b == a:
  print('a and b are equal')
else:                          #pernyataan else harus berada di akhir
  print('a is greater than b')

#pernyataan if bersarang
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:          #if bagian dalam hanya akan dijalankan jika kondisi luar benar
    print("and also above 20!")
  else:
    print("but not above 20.")
    
a = 2
b = 330
print("A") if a < b else print("B") #pernyataan if else dalam satu baris

a = 60
b = 20
bigger = a if a > b else b #menetapkan nilai dengan if else
print("Bigger is", bigger)

#masukkan pernyataan pass jika ingin blok kode didalam if kosong
a = 33
b = 200
if b>a:
  pass