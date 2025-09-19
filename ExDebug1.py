def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : humidité

    Retour :
    - "Tout est sous contrôle!" si tout est bon
    - "Environnement non optimal" les problèmes sinon
"""

    alerte = False

# Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")


    # Vérification humidité
    if humidite < 18:
        print("Température trop basse")
        alerte = True
    elif humidite > 27:
        print("Température trop élevée")

    if poussiere != "faible":
        print("Pas assez de poussière")
        alerte = True


    # Vérification poussière
    if poussiere != "faible":
        print("Pas assez de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"

if __name__ == "__main__":
    #TODO : demander le nombre d'ordis [avec gestion d'erreur]
    #TODO : créer 3 listes (temperatures, poussiere, humidites)

    #TODO : Pour nombre d'ordis
        #TODO : Demander temperature, poussiere et humidite [avec gestion d'erreur]
        #TODO : Ajouter les 3 valeurs dans leurs listes respectives

    #TODO : Pour nombre d'ordis
        #TODO : Verifier l'environnement : utiliser la fonction et afficher le resultat

    temp = float(input("Entrez la température: "))
    poussiere = input("Entrez le niveau de poussière: ")
    humidite = float(input("Entrez l'humidité: "))
    print(environnement_optimal(25, "faible", 40))
