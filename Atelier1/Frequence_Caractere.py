def Frequence_Caractere(chaine, caractere):
    count = 0
    for char in chaine:
        if char == caractere:
            count += 1
    return count


chaine = input("Veuillez Saisir Une Chaine De Caractere : ")
caractere = input("Veuillez Saisir Un Caractere QUi Veux Trouver : ")
FCaractere = Frequence_Caractere(chaine, caractere)

print(f"Le Nombre De Caractere {caractere} dans la Chaine Est : {FCaractere}")
