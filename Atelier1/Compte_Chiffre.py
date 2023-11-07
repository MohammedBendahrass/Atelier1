def Compte(N):
    result = 0
    N = abs(N)
    if N == 0:
        return 1
    else:
        while N > 0:
            N //= 10
            result += 1
        return result
    return result


N = int(input("Veuillez Entrer Un Nombre : "))
NmbChiffre = Compte(N)
print(f"Le Nombre De Chiffre De Votre Nombre {N} Est : {NmbChiffre}")
