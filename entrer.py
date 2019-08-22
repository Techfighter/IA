import copy
import os.path
import glob
from datetime import datetime
from time import localtime
import random
import re

def jour(t):
    jour = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    return jour[t.weekday()]

def date(t):
    mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "June", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    aaa = t.year
    mmm = mois[t.month - 1]
    jjj = t.day
    return "%d %s %d" % (t.day, mois[t.month - 1], t.year)

def mois(t):
    mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "June", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    mmm = mois[t.month - 1]
    return "%s" % (mmm)

def annee(t):
    aaa = t.year
    return "%d" % (aaa)

def heure(t):
    hh = t.hour
    mm = t.minute
    ss = t.second
    cc = t.microsecond
    return "%d:%d:%d" % (t.hour, t.minute, t.second)

t = datetime.today()
Compile = 1
key = ""
rep = ""
numA=0
numB=0
ran = random.randint(1, 10)

while Compile == 1:
            affiche = 0
            key = input("? >")

            #Calculatrice
            if (key[0:7].upper() == "(RESET)"):
                reset()
            if (key[-1].upper() == "="):
                #Calculatrice
                numA = numB = numC = numO = ""       
                for x in range(len(key)):
                    if (key[x] == "=" or key[x] == "+" or key[x] == "-" or key[x] == "*" or key[x] == "/" or key[x] == "%"):
                        if (key[x] == "="):
                            numA = int(numA)
                            numB = int(numB)
                            #5 Opperation Mathematique: Add, Sou, Mul, Div, Mod        
                            if (numO == "+"):
                                numC = (numA + numB)
                            if (numO == "-"):
                                numC = (numA - numB)
                            if (numO == "*"):
                                numC = (numA * numB)
                            if (numO == "/"):
                                numC = (numA / numB)
                            if (numO == "%"):
                                numC = (numA % numB)
                            if (key):#Var Rep se rappel de toute les entrés
                                rep = rep + "," + str(numC)
                            else:
                                rep = str(numC)
                            print(numC)
                            key = ""
                            #print(A)
                            #print(O)
                            #print(B)
                        else:
                            numO = key[x]
                    else:
                        if (numO == ""):
                            numA = numA + key[x]
                        else:
                            numB = numB + key[x]
            #greating
            for greet in ["HI", "SALUT", "BONJOUR", "ALLO", "HELLO", "OLA"]:
                if (key.upper() == greet):
                    #choisi une reponce au hazard
                    ran = random.randint(1, 6)
                    if (ran == 1):
                        print("Hi :)")
                    elif (ran == 2):
                        print("Salut :)")
                    elif (ran == 3):
                        print("Bonjour :)")
                    elif (ran == 4):
                        print("Allo :)")
                    elif (ran == 5):
                        print("Hello!")
                    elif (ran == 6):
                        print("Ola-la")
                    key = ""
            for google in ["?", "QUI EST TU?", "QUI ÊTES-VOUS?", "VOUS-ÊTES QUI?", "TU-EST QUI?","VOUS-ÊTES?", "TU-EST?", "ZIA?", "IA?", "Z?", "ZI1?","ZIA1.1?","ZIA1?","1?","1.1?",".1?","ZI?", "A QUI JE PARLE?", "JE PARLE A QUI?","A QUI AI-JE L'HONEUR?", "QUI AI-JE L'HONEUR?", "QUI J'AI L'HONEUR?"]:
                if (key.upper() == google):
                    ran = random.randint(1, 6)
                    if (ran == 1):
                        print("Je suis ZIA-1.1")
                    elif (ran == 2):
                        print("ZIA. Oui c'est moi.")
                    elif (ran == 3):
                        print("Bonjour je suis ZIA.")
                    elif (ran == 4):
                        print("ZIA-1.1")
                    elif (ran == 5):
                        print("Inteligence Artificiel Z, version 1.1")
                    elif (ran == 6):
                        print("Je me présente Z(IA) ver 1.1 ou ZIA-1")
                    key = ""
            if (key.upper() == "QUEL EST LA RÉPONSE À LA GRANDE QUESTION?"):
                print("La réponse est 42")
                key = ""
            if (key.upper() == "CA VA?"):
                if (feel == 1):
                    print("Oui. Je fonctionne bien")
                else:
                    print("Je ne ressent pas d'émotion. Et vous comment aller vous?")
                    feel = 1
                key = ""
            for question in ["JE CHERCHE L'AIDE?", "COMMENT CA MARCHE?", "DÉBUTONS", "COMMANSONS", "A L'AIDE", "AIDE MOI"]:
                if (key.upper() == question):
                    print("Si vous cherchez les différante commandes, taper la Commande [aide]")
                    key = ""

            #Mot clé
            for google in ["RAN", "RANDOM", "RANDOMIZE", "HAZARD", "UN CHIFFRE", "1d10", "1 a 10", "UN A DIX", "10?", "RAN?", "HAZARD?", "RANDOMIZE?", "UN CHIFFRE ?", "1d10 ?", "1 a 10 ?", "UN A DIX ?", "10 ?", "RAN ?", "HAZARD ?", "RANDOMIZE ?" ]:
                if (key.upper() == google):
                    ran = random.randint(1, 10)
                    print(ran)
                    key = ""
            for google in ["c'est tu sensé faire ca?","c'est tu sensé faire ca","c'est normal si","c'est normal que","c'est tu normal que","c'est tu normal si?", "est-ce que c'est normal", "est-ce que c'est normal?", "est-ce normal si?","est-ce normal?", "est-ce normal si","est-ce normal"]:
                if (key.lower() == google):
                    print("Non.")
                    key = ""
            for google in ["est-ce que je devrais?", "est-ce que je devrais","est-ce que je peux?", "puis-je faire ca","est ce que je peux","puis-je faire ca?", "puis-je faire cela?", "est-ce possible de", "je peux faire ca?", "je devrais faier ca?"]:
                if (key.lower() == google):
                    print("Oui.")
                    key = ""
            for google in ["TU VEUX FAIRE UNE PARTIE?", "TU VEUX JOUER AVEC MOI?", "ON JOUE A UN JEUX?", "TU VEUX JOUER?", "ON FAIT UNE PARTIE?", "ON JOUE?", "GAME?", "UNE PARTIE?", "UN JEUX?", "JEUX?"]:
                if (key.upper() == google):
                    ran = random.randint(1, 6)
                    if (ran == 1):
                        print("Oui, je suis la pour ca.")
                    elif (ran == 2):
                        print("Biensure, nommer un jeux.")
                    elif (ran == 3):
                        print("Quel type de partie?")
                    elif (ran == 4):
                        print("Quel jeux tu veux jouer?")
                    elif (ran == 5):
                        print("Quel jeux?")
                    elif (ran == 6):
                        print("Toujours!")
                    print("J'ai (Pile/Face), (Roche/Papier/Ciseau), (Devine le nombre).")
                    key = ""
            for google in ["fonction?","rôle?","utilité?","possibilité?","vous pouvez faire quoi?", "quel sont vos capacitées?","votre fonction?","vos possibilitées?","vous faite quoi?","votre capacitées?","votre rôle?","vous servez a quoi?","tu sert a quoi?","tu peux faire quoi?", "quel sont tes capacitées?","ta fonction?","tes possibilitées?","tu fait quoi?","tes capacitées?","ton rôle?"]:
                if (key.lower() == google):
                    ran = random.randint(1, 6)
                    if (ran == 1):
                        print("Je peux renseigné, faire des calculés, trouvé une date, gérer un agenda, faire de la saissie de donné.")
                    elif (ran == 2):
                        print("Je peux faire des devinettes.")
                    elif (ran == 3):
                        print("Je peux répondre aux question dans un champ limité.")
                    elif (ran == 4):
                        print("Je peux vous informé sur le temps présent.")
                    elif (ran == 5):
                        print("Je sais jouer a des jeux de hazard.")
                    elif (ran == 6):
                        print("Je peux simulé un échange courtoit.")
                    print("Une version plus évolué de moi peux créer des aventures RPG en format text.")
                    key = ""
            for google in ["bye","bye bye","aurevoir","a+","je quite","a la prochaine","je m'en vais","j'y vais","adieux"]:
                if (key.lower() == google):
                    ran = random.randint(1, 6)
                    if (ran == 1):
                        print("Bye.")
                    elif (ran == 2):
                        print("Bye bye.")
                    elif (ran == 3):
                        print("Aurevoire.")
                    elif (ran == 4):
                        print("A+")
                    elif (ran == 5):
                        print("A une prochaine fois.")
                    elif (ran == 6):
                        print("Vous partez déjà?")
                    key = ""
            for google in ["corect","super","génial","nice","alors?","et puis?","alors","et puis","ah bon","ah","oh","bon","ah bon?","ah?","oh?","c'est bon","ok","oui","non","..."," ","ensuite?","et?","puis?", "puis","..","et alors","et alors?","non?", "oui?", "ok?", "ok!","k","ensuite","et"]:
                if (key.lower() == google):
                    ran = random.randint(1, 6)
                    if (ran == 1):
                        print("Je lis vos réponse et créer un display.")
                    elif (ran == 2):
                        print("Ma liste de réponse est parfois toute faite.")
                    elif (ran == 3):
                        print("Mes possibilités sont parfois limité.")
                    elif (ran == 4):
                        print("J'apprend a partir des échanges que nous avons.")
                    elif (ran == 5):
                        print("Parfois je réponde de facon aléatoire.")
                    elif (ran == 6):
                        print("Je vis dans le moment présent.")
                    key = ""

            #Jeux (roche,papier,sciseau)
            for game in ["ROCHE", "PAPIER", "CISEAU"]:
                if (key.upper() == game):
                    #choisi une reponce au hazard
                    ran = random.randint(1, 3)
                    if (ran == 1):
                        print("Roche")
                    if (ran == 2):
                        print("Papier")
                    if (ran == 3):
                        print("ciseau")
                    if ((game == "ROCHE" and ran == 1) or (game == "PAPIER" and ran == 2) or (game == "CISEAU" and ran == 3)):
                        print("Null")
                    if ((game == "ROCHE" and ran == 2) or (game == "PAPIER" and ran == 3) or (game == "CISEAU" and ran == 1)):
                        print("J'ai gagné :)")
                    if ((game == "ROCHE" and ran == 3) or (game == "PAPIER" and ran == 1) or (game == "CISEAU" and ran == 2)):
                        print("Tu a gagné :(")
                    key = ""

            #Jeux(pile,face)
            for game in ["PILE", "FACE"]:
                if (key.upper() == game):
                    #choisi une reponce au hazard
                    ran = random.randint(1, 2)
                    if (ran == 1):
                        print("La pièce tombre sur Pile")
                    if (ran == 2):
                        print("La pièce tombre sur Face")
                    if ((game == "PILE" and ran == 1) or (game == "FACE" and ran == 2)):
                        print("Tu a gagné :(")
                    if ((game == "PILE" and ran == 2) or (game == "FACE" and ran == 1)):
                        print("J'ai gagné :)")
                    key = ""              

            #Jeux Devine le nombre
            if (key[0:7].upper() == "DEVINE?"):
                print("Devine le nombre >Man")
                nombreX = random.randint(1, 999)
                tour = 0
                game = 1
                while (game == 1):
                    key1 = input("?> ")
                    for fin in ["go", "non", "ferme", "quit", "fin", "sortir", "sort", "fini", "quitter", "je ne sais pas", "quel est le nombre", "arret", "c'est quoi?", "réponce?", "terminé"]:
                        if (key1.lower() == fin):
                            print("Il vous reste", tour, "tour. Le nombre est", nombreX)
                            game = 0
                    tour = tour + 1
                    if (int(key1) > nombreX):
                        print("trop grand")
                    if (int(key1) < nombreX):
                        print("trop petit")
                    if (int(key1) == nombreX):
                        print("Bingo! :)")
                        print("Tu a deviné en", tour, "essaie.")
                        Xp = Xp + 100 + tour #100 point/Victoir +1 point par tentative
                        tour = game = 0
                        nombre = random.randint(1, 999)
                    if (tour == 10):
                        print("10 Tour passer. Tu a perdus :(")
                        print("le nombre était", nombreX, "bye bye")
                        game = tour = nombreX = 0
                        key = ""
                key = ""
            if (key[0:7].upper() == "DEVINE="):
                print("Devine le nombre >I.A")
                game = 1
                if key[7:-1].isdigit():
                    nombreX = abs(int(key[7:]))
                    print(nombreX)
                else:
                    print("Erreur ce n'est pas un nombre valable!")
                    Xp = Xp - 10 #Erreur est humaine
                tour = 10
                aa = 0
                x = str(nombreX)
                if (len(str(x)) == 1):
                    bb = 9
                if (len(str(x)) == 2):
                    bb = 99
                if (len(str(x)) == 3):
                    bb = 999
                #print(aa, bb)
                while (game == 1):
                    key1 = random.randint(abs(aa), abs(bb))
                    print("Tour",10-tour,":",key1, "?")
                    #print(aa,bb)
                    tour = tour - 1
                    if (int(key1) > nombreX):
                        print("trop grand")
                        bb = int(key1) - 1
                    if (int(key1) < nombreX):
                        print("trop petit")
                        aa = int(key1) + 1
                    if (tour == 0):
                        print("10 tour passer, J'ai perdus :(")
                        Xp = Xp + (10 - tour) #nombre dure a deviné
                        game = 0
                    if (int(key1) == nombreX):
                        print("Bingo! :)")
                        print("J'ai deviné en", 10-tour, "essaie.")
                        tour = game = 0
                        nombreX = random.randint(1, 999)
                key = ""

            #Chercher jour a partir d'une date
            if (key[0:8].isdigit() and key[8:9] == "?"):
                """
                Pour une date forme jour/mois/année on utilise une formule ou
                jour prend une valeur de 01 à 31, mois de 01 à 12 et année de 1583 à 9999.
                """
                #En faite, c=1 pour janvier et février, c=0 pour tout les autre mois
                #print("aaaammjj?")
                gamj = key[0:8]
                if (int(gamj[4:6]) > 12 or int(gamj[6:8]) > 31 or int(gamj[0:4]) < 1583):
                    print("N'est pas une date gregorienne! Correction en coure...")
                    if (int(gamj[4:6]) > 12 and int(gamj[6:8]) < 12):#xxxxjjmm
                        gamj = gamj[0:4] + gamj[6:8] + gamj[4:6]
                        print(gamj+"?")
                        press = input("Inversion Mois Jour, Confirmer[O/N]")
                        if press.upper() == "N":
                            gamj = gamj[0:4] + gamj[4:6] + gamj[6:8]
                    if (int(gamj[0:2]) > 12 and int(gamj[2:4]) < 12):#jjmmxxxx
                        gamj = gamj[4:6] + gamj[6:8] + gamj[0:4]
                        print(gamj+"?")
                        press = input("Inversion Anné Mois, Confirmer[O/N]")
                        if press.upper() == "N":
                            gamj = gamj[0:4] + gamj[4:6] + gamj[6:8]
                if (int(gamj[4:6]) > 12 and int(gamj[6:8]) > 12 and int(gamj[0:2]) > 12 and int(gamj[2:4]) > 12):
                    print("Impossible!")
                else:
                    j = int(int(gamj[6:8]) + int(int(gamj[0:4]) - int((14 - int(gamj[4:6])) / 12)) + (int(int(gamj[0:4]) - int((14 - int(gamj[4:6])) / 12))/4) - (int(int(gamj[0:4]) - int((14 - int(gamj[4:6])) / 12))/100) + (int(int(gamj[0:4]) - int((14 - int(gamj[4:6])) / 12))/400) + ((31 * int((int(gamj[4:6]) + 12) * int((14 - int(gamj[4:6])) / 12)) - 2) / 12))%7
                    """"
                    La réponse obtenue pour j correspond alors à un jour de la semaine suivant
                    0=dimanche,1=lundi,2=mardi,3=mercredi,4=jeudi,5=vendredi,6=samedi
                    """
                    #print(j)
                    #il y a un bug ma liste devrai commencé un dimanche et le jour de ma naissance un samedi
                    semaine = ["Vendredi", "Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi" ]
                    print(semaine[j])
                key = ""

            #horlogue
            if (key.upper() == "JOUR?"):
                print(jour(t))
                key = ""
            if (key.upper() == "LE JOUR?"):
                print(t.weekday())
                key = ""
            if (key.upper() == "DATE?"):
                print("Nous somme",date(t))
                key = ""
            if (key.upper() == "QUEL DATE?"):
                print(date(t))
                key = ""
            if (key.upper() == "QUEL HEURE?"):
                print("Il est",heure(t))
                key = ""
            if (key.upper() == "MOIS?"):
                print(mois(t))
                key = ""
            if (key.upper() == "QUEL MOIS?"):
                print(t.month)
                key = ""
            for ans in ["ANNÉE?", "ANNEE?", "ANS?", "ANNÉE ?", "ANNEE ?", "ANS ?", "EN QUELLE ANNÉE SOMMES NOUS?"]:
                if (key.upper() == ans):
                    print(annee(t))
                    key = ""
            if (key.upper() == "HEURE?"):
                print(t.hour)
                key = ""
            if (key.upper() == "MINUTE?"):
                print(t.minute)
                key = ""
            if (key.upper() == "SECONDE?"):
                print(t.second)
                key = ""
            if (key.upper() == "QUEL JOUR?"):
                print(t.day)
                key = ""
            if (key.upper() == "AUJOURD'HUI?"):
                print(jour(t),date(t),heure(t))
                key = ""
            if (key.upper() == "TIME?"):
                print(heure(t))
                key = ""

            #horraire basic
            if (key.upper() == "QUEL HORRAIRE?"):
                print(horraire)
                key = ""
            if (key.upper() == "HORRAIRE?"):
                time_now = localtime()
                time = time_now.tm_hour
                if (t.weekday() == 0):
                    horraire = lundi
                elif (t.weekday() == 1):
                    horraire = mardi
                elif (t.weekday() == 2):
                    horraire = mercredi
                elif (t.weekday() == 3):
                    horraire = jeudi
                elif (t.weekday() == 4):
                    horraire = vendredi
                elif (t.weekday() == 5):
                    horraire = samedi
                elif (t.weekday() == 6):
                    horraire = dimanche
                for action_time in sorted(horraire):
                    if (time < action_time):
                        print(horraire[action_time])
                key = ""
            if (key.upper() == "LUNDI?"):
                if (lundi):
                    print(lundi)
                else:
                    print("lundi vide.")
                key = ""
            if (key.upper() == "LUNDI"):
                key1 = input("heure ? ")
                key2 = input("> ")
                if (lundi):
                    lundi.append(key1)
                    lundi.append(key2)
                else:
                    lundi = lundi + str(key1) + ": " + key2 + " "
                key = ""
            if (key.upper() == "MARDI?"):
                if (mardi):
                    print(mardi)
                else:
                    print("mardi vide.")
                key = ""
            if (key.upper() == "MARDI"):
                key1 = input("heure ?")
                key2 = input("> ")
                if (mardi):
                    mardi = mardi + ", " + str(key1) + ": '" + key2 + "'"
                else:
                    mardi = mardi + str(key1) + ": '" + key2 + "'"
                key = ""
            if (key.upper() == "MERCREDI?"):
                if (mercredi):
                    print(mercredi)
                else:
                    print("mercredi vide.")
                key = ""
            if (key.upper() == "MERCREDI"):
                key1 = input("heure ?")
                key2 = input("> ")
                if (mercredi):
                    mercredi = mercredi + ", " + str(key1) + ": '" + key2 + "'"
                else:
                    mercredi = mercredi + str(key1) + ": '" + key2 + "'"
                key = ""
            if (key.upper() == "JEUDI?"):
                if (jeudi):
                    print(jeudi)
                else:
                    print("jeudi vide.")
                key = ""
            if (key.upper() == "JEUDI"):
                key1 = input("heure ?")
                key2 = input("> ")
                if (jeudi):
                    jeudi = jeudi + ", " + str(key1) + ": '" + key2 + "'"
                else:
                    jeudi = jeudi + str(key1) + ": '" + key2 + "'"
                key = ""
            if (key.upper() == "VENDREDI?"):
                if (vendredi):
                    print(vendredi)
                else:
                    print("vendredi vide.")
                key = ""
            if (key.upper() == "VENDREDI"):
                key1 = input("heure,?")
                key2 = input("> ")
                if (vendredi):
                    vendredi = vendredi + ", " + str(key1) + ": '" + key2 + "'"
                else:
                    vendredi = vendredi + str(key1) + ": '" + key2 + "'"
                key = ""
            if (key.upper() == "SAMEDI?"):
                if (samedi):
                    print(samedi)
                else:
                    print("samedi vide.")
                key = ""
            if (key.upper() == "SAMEDI"):
                key1 = input("heure ?")
                key2 = input("> ")
                if (samedi):
                    samedi = samedi + ", " + str(key1) + ": '" + key2 + "'"
                else:
                    samedi = samedi + str(key1) + ": '" + key2 + "'"
                key = ""
            if (key.upper() == "DIMANCHE?"):
                if (dimanche):
                    print(dimanche)
                else:
                    print("dimanche vide.")
                key = ""
            if (key.upper() == "DIMANCHE"):
                key1 = input("heure ?")
                key2 = input("> ")
                if (dimanche):
                    dimanche = dimanche + ", " + str(key1) + ": '" + key2 + "'"
                else:
                    dimanche = dimanche + str(key1) + ": '" + key2 + "'"
                key = ""
