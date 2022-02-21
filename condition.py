# == égal
# < inférieur
# <= inférieur ou égal
# > supérieur
# >= supérieur ou égal
#true /false --> boolean
#12<= age <18
#elif age == 1 or age ==2



def afficher_informations_personne(nom, age):
    print("je m'appelle " + nom + " et j'ai " + str(age) + " ans.")
    print("l'an prochain j'aurais " + str(age + 1) + " ans")

    if age == 17:
        print("vous êtes presque majeur")
    elif 12<= age <18:
        print("vous êtes ado")
    elif age == 1 or age == 2:
        print("vous êtes un bébé")
    elif age == 18:
        print("tout juste majeur")
    elif age > 60:
        print("vous êtes sénior")
    elif age < 10:
        print("vous êtes un enfant")
    elif age >= 18:
        print("vous êtes majeur")
    else:
        print("vous êtes mineur")

        """ en booléan
        condition = age >=18
        print(condition)
        if condition:
            print("vous êtes majeur")
        else:
            print("vous êtes mineur")
        elif sinon si
        """


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne +"quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except:
            print("errur : vous devez rentrer un nombre pour l'age")
    return age_int


def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("quel est ton nom ? ")
    return nom_str
#demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

#demander l'âge
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#afficher les résulats

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
