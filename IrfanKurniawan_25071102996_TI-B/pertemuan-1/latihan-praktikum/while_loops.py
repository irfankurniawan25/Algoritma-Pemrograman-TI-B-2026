#cetak i selama i kurang dari 6
i = 1
while i < 6:
  print(i)
  i += 1

#keluar dari loop ketika 1 sama dengan 3 
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#     break
#     i += 1
  
#lanjutkan ke iterasi berikutnya ketika 1 sama dengan 3 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
