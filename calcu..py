class Calculatrice:
    def afficher_menu(self):
        print("\n=== Choisissez votre opération ===")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

    def Addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def Multiplication(self, a, b):
        return a * b

    def Division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erreur : Division par zéro impossible."

calculatrice = Calculatrice()

while True:
    calculatrice.afficher_menu()
    choix = input("Entrez le numéro de votre choix : ")

    if choix in ["1", "2", "3", "4"]:
        try:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))

            if choix == "1":
                resultat = calculatrice.Addition(nombre1, nombre2)
                print(f"Résultat : {resultat}")
            elif choix == "2":
                resultat = calculatrice.soustraction(nombre1, nombre2)
                print(f"Résultat : {resultat}")
            elif choix == "3":
                resultat = calculatrice.Multiplication(nombre1, nombre2)
                print(f"Résultat : {resultat}")
            elif choix == "4":
                resultat = calculatrice.Division(nombre1, nombre2)
                print(f"Résultat : {resultat}")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")



    
