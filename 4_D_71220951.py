print("------Nilai Ke 1------")
harian1 = int(input("Nilai Harian :"))
uts1 = int(input("Nilai UTS :"))
uas1 = int(input("Nilai UAS :"))

print("------Nilai Ke 2------")
harian2 = int(input("Nilai Harian :"))
uts2 = int(input("Nilai UTS :"))
uas2 = int(input("Nilai UAS :"))

totalharian = harian1*30/100 + harian2*30/100
totaluts = uts1*30/100 + uts2*30/100
totaluas = uas1*40/100 + uas2*40/100

totalnilai = totalharian+totaluts+totaluas
total = totalnilai/2


def totalnilaiangka():
    print("Total nilai yang didapat :", total)
totalnilaiangka()

def totalnilaihuruf():
    if (100 >= total >= 80):
        print("Total Nilai Dalam Huruf: A")
    elif (80 > total >= 60):
        print("Total Nilai Dalam Huruf: B")
    elif (60 > total >= 40):
        print("Total Nilai Dalam Huruf: C")
    elif (40 > total >= 20):
        print("Total Nilai Dalam Huruf: D")
    else:
        print("Total Nilai Dalam Huruf: E")
totalnilaihuruf()