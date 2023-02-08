def carikata():
    apakalimatnya = input ("Kalimat yang ingin diteliti : ")
    katanyaapa = input(" kata yang dicari : ")
    jumlahkatanya = apakalimatnya.count(katanyaapa, 0)
    print("Jumlah kata yang dicari : ", jumlahkatanya)
carikata()