eleve_liste = ["Sophie", "Amina", "Azeddine", "alfred"]
with open("eleves.txt", "a+") as file:
    for student in eleve_liste:
        file.write(student + "\n")
    file.close()

    def ordre_alphabetique(txt):
        return sorted(txt)
    txt = str(input("Entrer une liste de lettre : "))
    print(" la liste dans l'ordre alphabétique est :", ordre_alphabetique(txt) )
    print (" la liste dans l'ordre anti-alphabétique est :",sorted(txt, reverse = True) )
    