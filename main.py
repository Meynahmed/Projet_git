#projet SIBY et AMINA
#Creer un fichier txt

eleve_liste = ["Sophie", "Amina", "Azeddine"]
with open("eleves.txt", "a+") as file:
    for student in eleve_liste:
        file.write(student + "\n")
    file.close()