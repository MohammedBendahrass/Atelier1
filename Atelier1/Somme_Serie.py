import math


def Somme_Serie(n):
    somme = 0
    for i in range(1, n + 1):
        terme = math.factorial(i) / i
        somme += terme
    return somme


n = int(input("Entrer Un nombre : "))
resultat = Somme_Serie(n)
print(f"la somme de serie est : {resultat}")
