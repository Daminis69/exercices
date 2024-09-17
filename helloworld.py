from unittest import case
helloworld = "hello"

ensoleillé = False

if ensoleillé:
    print("wouhou")
else:
    print("c'est mort")



nombre_a_gauche=input("8")
nombre_a_droite=input("7")
operation = input(['+'])

resultat = 0

if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric(): 
    print("Erreur: les deux nombres doivent etre des nombres entiers")
else:
    nombre_a_gauche = int(nombre_a_gauche)
    nombre_a_droite = int(nombre_a_droite)
    
    match operation:
        case "+": 
            resultat = nombre_a_gauche + nombre_a_droite 
        case "-": 
            resultat = nombre_a_gauche - nombre_a_droite 
        case "*": 
            resultat = nombre_a_gauche * nombre_a_droite 
        case "/": 
            if nombre_a_droite == 0:
                print("Erreur: impossible de diviser par zéro."), 
            else: resultat = nombre_a_gauche / nombre_a_droite
        
        case _: print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

print(f"Le résultat de l'opération est: {resultat}")

if __name__ == "__main__":
    main()