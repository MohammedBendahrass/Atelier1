def Somme(n):
    resultat = 0
    for N in range(1, n + 1):
        resultat += N
    return resultat


N = int(input("Entrer le nombre qui veux de calculer votre somme : "))
S = Somme(N)
print(f"la somme de 1 a {N} est : {S}")
