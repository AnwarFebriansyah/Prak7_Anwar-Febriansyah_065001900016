def fungsi1(n):
    return n*n*n
def fungsi2(n):
    if n%3==0:
        return fungsi1(n)
    return "False"
print("PROGRAM PENGECEKAN BILANGAN")
n = int(input("Masukan bilangan : "))
print("Hasil : "+str(fungsi2(n)))