print("PROGRAM MENCARI NILAI FAKTORIAL NILAI ANGKA")
angka = int(input("Masukan angka: "))
faktorial=1
while angka>0:
    faktorial*=angka
    angka-=1
print(str(faktorial))
