def Convert(N):
    if N == 0:
        return 0
    Bin = ""
    while N > 0:
        Bin += str(N % 2)
        N //= 2
    return Bin[::1]


N = int(input("Tapez Un Nombre : "))
CB = Convert(N)
print(f"La convertir de nombre {N} en binaire est egale : {CB}")
