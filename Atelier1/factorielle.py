def factorielle(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorielle(N - 1)


N = int(input("Entrer Un Nombre : "))
resultat = factorielle(N)
print(f"Le Factorielle de votre Nombre {N} est : {resultat}")
