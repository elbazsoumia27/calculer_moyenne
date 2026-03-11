"""#-------Exemple 1--------

def calculer_moyenne (note1, note2, note3):
    moyenne = (note1 + note2 + note3) / 3
    return moyenne

# Appel de la fonction
resultat = calculer_moyenne(12, 15, 14)
print("La moyenne est", resultat)

#-------Exemple 2--------
def calculer_moyenne (notel, note2, note3):

    moyenne = (notel + note2 + note3) / 3
    return moyenne

def decision(moyenne):
    if moyenne >= 18:
        return "Admis"
    else:
        return "Ajourné"

#Programme principal
m = calculer_moyenne (12, 8, 9)
etat = decision(m)
print("Moyenne:", m)
print("Résultat:", etat)"""

#-------Exemple 3--------
def calculer_moyenne (n1, n2, n3):

    return (n1 + n2 + n3)/3

def decision(moyenne):
    if moyenne > 10:
        return "Admis"
    else:
        return "Ajourné"

if __name__ == "__main__":
    #Saisie des notes
    note1 = float(input("Entrez la première note: "))
    note2 = float(input("Entrez la deuxième note: "))
    note3 = float(input("Entrez la troisième note: "))

    moy = calculer_moyenne (note1, note2, note3)
    etat = decision(moy)

    print("La moyenne est", moy)
    print("Résultat:", etat)