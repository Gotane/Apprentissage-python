def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("quel est votre âge ? ")
        try:
            age_int = int(age_str) + 1
        except:
            print("errur : vous devez rentrer un nombre pour l'age")
    return age_int


def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("quel est ton nom ? ")
    return nom_str
#demander le nom
nom = demander_nom()


#demander l'âge
age = demander_age()

print("je m'appelle "+nom+" et j'ai "+ str(age) +" ans.")
print("l'an prochain j'aurais "+ str(age+1)+" ans")
print("je m'appelle "+nom+" et j'ai "+ str(age) +" ans.")
print("l'an prochain j'aurais "+ str(age+1)+" ans")

#  permet de mettre un commentaire

"""commentaire
sur plusieurs
lignes"""