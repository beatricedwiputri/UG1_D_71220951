print("============ KASIR ============")

hargabarang = int(input("Harga Barang :"))
maubelibarang = input("Apakah anda membeli barang lagi? [yes/no] :")
total = 0
while True:
    if(maubelibarang == "yes"):
        total += hargabarang
        hargabarang = input("Harga Barang :")
        maubelibarang = input("Apakah anda membeli barang lagi? [yes/no] :")
    elif(maubelibarang == "no"):
        print("TOTAL BELANJA:", total)
        break
    else:
        print("INVALID")
        break

    


