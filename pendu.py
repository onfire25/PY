from random import *

faute = 0
mot = ""
motCacher = ""
lettre = ""


#choix du mot aléatoirement
def choixMot():
    global mot, motCacher
    lignes = open("words.txt", "r").readlines()
    counter = 0
    nbAlea = 0
    listMot = []

    for ligne in lignes:
        counter += 1
        listMot.append(ligne)

    nbAlea = uniform(1, counter)
    mot = listMot[int(nbAlea)]
    motCacher = mot
    cacherMot()


#on cache le mot precedement choisis
def cacherMot():
    global motCacher
    caracteres = list(motCacher)
    for i in range (0, len(caracteres)-1):
        caracteres[i] = "_"
    motCacher = "".join(caracteres)


#on verrifie si la lettre du joueur correspond à une lettre du mot
def verifLettre():
    global mot, motCacher, lettre, faute
    lettreExiste = 0
    for i in range (0, len(mot)):
        if mot[i] == lettre:
            caracteres = list(motCacher)
            caracteres[i] = lettre
            motCacher = "".join(caracteres)
            lettreExiste = 1
    if lettreExiste == 0:
        faute += 1
        print("Vous avez fait ",faute," / 6")


#on verifie si il y a victoire ou defaite
def verifVictoire():
    global motCacher,mot, faute
    if mot == motCacher :
        print("VICTOIRE")
        faute = 7
    elif faute >= 6:
        print("PERDU")


#choix de la lettre par le joueur + verification sur son choix
def choixJoueur():
    global lettre
    choixValable = 0
    lettreValide = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lettre = input("Choisissez une lettre :").upper()
    if len(lettre) > 1 :
        print ("Veuillez entrer une seul et unique lettre.")
        choixJoueur()
    for i in range(0,len(lettreValide)):
        if lettre == lettreValide[i]:
            choixValable = 1
    if choixValable == 0:
        print("Veuillez choisir une lettre.")
        choixJoueur()



#déroulement de la partie
def jeux():
    global faute, lettre, motCacher, mot
    choixMot()
    print(mot)
    print(motCacher)
    while faute <= 5 :
        choixJoueur()
        verifLettre()
        print(motCacher)
        verifVictoire()


#lancement du jeux
jeux()
