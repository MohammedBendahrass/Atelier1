def Puissance(X, n):
    resultat = 1
    for N in range(n):
        resultat *= X
    return resultat


X = int(input("Saisir Votre Nombre : "))
n = int(input("Saisir le puissance : "))
P = Puissance(X, n)
print(f"La puissance {X} de nombre {n} est : {P}")
