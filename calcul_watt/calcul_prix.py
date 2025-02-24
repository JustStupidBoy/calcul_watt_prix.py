# gestion d'erreur
def demander_float(message):
    while True:  # redémarre si l'input n'est pas bon
        try:
            user_input = input(message).strip()  # Retirer les espaces avant et après la saisie
            return float(user_input)  # Convertir en float après avoir retiré les espaces
        except ValueError:  # si ya une erreur, affiche le message
            print("Erreur : veuillez entrer un nombre valide.")

# fonction principale
def main(): 
    #pose une question puis récupère le résultat
    print("Consommation en kW/h : ", end='')
    kw = demander_float("")
    print("prix du kw/h en euros : ", end='')
    prix = demander_float("")
    calcul(kw, prix)

# kw et prix sont des paramètres transmis à la fonction calcul()
def calcul(kw, prix):
    # Durées et leurs multiplicateurs
    durees = {
        "1h": 1,
        "24h": 24,
        "7 jours": 24 * 7,
        "30 jours": 24 * 30,
        "Par an": 24 * 365
    }

    for periode, facteur in durees.items():
        cout = kw * prix * facteur
        print(f"{periode} : {cout:.2f} euros")

# éxecute main (il faut le faire de cette manière pour éviter des problèmes)
if __name__ == "__main__": 
    main()
