import statistics


def Moyenne(Liste):
    if len(Liste) == 0:
        return 0
    else:
        return sum(Liste) / len(Liste)


def Min_Max(Liste, Choix):
    if Choix == "min" or Choix == "Min":
        return min(Liste)
    elif Choix == "max" or Choix == "Max":
        return max(Liste)
    else:
        return "Erreur De Saisie!"


def Mediane(Liste):
    return statistics.median(Liste)


def Mode(Liste):
    try:
        return statistics.mode(Liste)
    except statistics.StatisticsError:
        return None


def Variance(Liste):
    return statistics.variance(Liste)


def Saisie_List():
    Liste = []
    n = int(input("denner la taille de la liste : "))
    for i in range(n):
        ele = float(input(f"Entrer l'element {i+1} : "))
        Liste.append(ele)
    return Liste


Liste = Saisie_List()

Choix = input(
    "\n1_'Moyenne'\n2_'Min_Max'\n3_'Mediane'\n4_'Mode'\n5_'Variance'\nChoisissez l'operation : "
)

if Choix == "Moyenne":
    print("La Moyenne de Votre Liste est : ", Moyenne(Liste))
elif Choix == "Min_Max":
    choix_min_max = input("Voulez-vous le 'min' Ou 'max' de la liste : ")
    print(f"Le {choix_min_max} est : ", Min_Max(Liste, choix_min_max))
elif Choix == "Mediane":
    print("Le Mediane De Votre Liste Est : ",Mediane(Liste))
elif Choix == "Mode":
    print("Le Mode De Votre Liste Est : ",Mode(Liste))
elif Choix == "Variance":
    print("Le Variance De Votre Liste Est : ", Variance(Liste))
else:
    print("Choix Invalide.")
