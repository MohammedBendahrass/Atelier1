def Creer_Matrice():
    lignes = int(input("Veuillez Saisir le Nombre De Ligne : "))
    colonnes = int(input("Veuillez Saisir le Nombre De Colonne : "))
    matrice = []

    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            element = int(
                input(f"Veuillez Saisir le Nombre de element ({i} , {j}): ")
            )
            ligne.append(element)
        matrice.append(ligne)
    return matrice


def Chercher_Element(matrice, element):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == element:
                return (i, j)
    return (None, None)


matrice = Creer_Matrice()

element_Chercher = int(input("Entrer Le Nombre Qui Veux Chercher : "))

position = Chercher_Element(matrice, element_Chercher)

print(matrice)

if position != (None, None):
    print(f"La Position De Votre Nombre {element_Chercher} Est : {position}")
else:
    print(f"L'element {element_Chercher} n'a pas trouver dans la matrice {matrice}")
