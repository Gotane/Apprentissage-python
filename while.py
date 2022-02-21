"""n = 0
while n < 10:
    print("valeur de n : "+str(n))
    n = n + 1

print("fin de la boucle") """

mot_de_passe = ""
while not mot_de_passe == "YOANN":
    print("mot de passe incorrect")
    mot_de_passe = input("Quel est le mot de passe")

print("Mot de passe correct")
