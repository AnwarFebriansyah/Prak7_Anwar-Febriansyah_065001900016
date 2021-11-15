vokal = ["A","I","U","E","O"]
jumlah_vokal = 0
jumlah_konsonan = 0
print("PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT")
kalimat = input("Masukkan kalimat : ")
for huruf in kalimat:
    if huruf.upper() in vokal :
        jumlah_vokal+=1
    elif not huruf == " ":
        jumlah_konsonan+=1
print("Jumlah huruf vokal adalah "+str(jumlah_vokal))
print("jumlah huruf konsonan adalah "+str(jumlah_konsonan))
