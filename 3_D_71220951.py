angkanya = int(input("Masukkan Angka: "))

for bea in range(angkanya):
    print(' '*(angkanya-bea-1) + '* '*(bea+1))
for bea in range(angkanya):
    print(' '*(bea+1) + '* '*(angkanya-bea-1))
