print(10 > 9)  # menghasilkan True
print(10 == 9) # menghasilkan False
print(10 < 9)  # menghasilkan False

a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
else:
  print("b lebih kecil dari a")
  
print(bool('hello')) #menghasilkan True
print(bool(15))      #menghasilkan True

#berikut ini yang akan menamoilkan nilai False
print(bool(False)) 
print(bool(None))
print(bool(0))
print(bool(''))
print(bool(()))
print(bool({}))
print(bool([]))

#fungsi dapat mengembalikan nilai boolean
def myfunction():
  return True
print(myfunction())