nombre = int(input("Entrez votre nombre : "))
limite = int(input("Jusqu'à quel nombre souhaitez-vous multiplier ? "))
print("Table de multiplication de", nombre)
for multiplicateur in range(1, limite + 1):
    resultat = multiplicateur * nombre
    print(multiplicateur, "*", nombre, "=", resultat)