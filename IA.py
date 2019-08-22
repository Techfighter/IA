"""
Ajouter des jeux a partir de la ligne 1528 :P
Il faut pouvoir questionner le système pour comprendre son utilisation.
Il faudrais lui ajouté la parole. 
"""
from turtle import *
from datetime import datetime
from time import localtime
import cmath
import random
import re

Analyse = []
langue = []
recherche = boucle = 1
sourcefile = MessageTemple = ""
nombreX = mos = mot = trouver = x = Xp = info = source = Rep = 0
reponse = 0

messageIA = "CALENDRIER!"
align = "center_"
taille = 20
police = "Courier"
effet = "bold"
xCoord = 0  #Max 715 'taille 20
yCoord = 0  #Max 647 'taille 20

a2d = b2d = c2d = d2d = e2d = f2d = g2d = h2d = i2d = a3d = b3d = c3d = d3d = e3d = f3d = g3d = h3d = i3d = aa3d = bb3d = cc3d = dd3d = ee3d = ff3d = gg3d = hh3d = ii3d = aaa3d = bbb3d = ccc3d = ddd3d = eee3d = fff3d = ggg3d = hhh3d = iii3d = " "
key = valide2d = ran = xo2d = ox2d = ia2d = ia3d = z2d = z3d = valide3d = xo3d = ox3d = coup2d = coup3d = game2d = game3d = 0

def setup():
    global writer, messageIA, align, taille, police, effet, xCoord, yCoord, xCorrection
    #hour_hand = Turtle()
    #for hand in second_hand, minute_hand, hour_hand:
        #hand.speed(0)
    ht()
    writer = Turtle()

def Morpion2d():
    import random
    ran = random.randint(1, 9)   
    game2d = 0
    print("TTTTT  III   CCC    TTTTT   AA    CCC    TTTTT   OO   TTTTT")
    print("T T T   I   C       T T T  A  A  C       T T T  O  O  T T T")
    print("  T     I   C    =    T    AAAA  C    =    T    O  O    T  ")
    print("  T     I   C         T    A  A  C         T    O  O    T  ")
    print(" TTT   III   CCC     TTT   A  A   CCC     TTT    OO    TTT ")
    print("")

    while (game2d == 0):
        joueur2d = input("Nombre de Joueur ? >")
        print("")
        a2d = b2d = c2d = d2d = e2d = f2d = g2d = h2d = i2d = " "
        xo2d = "X"
        ox2d = "O"
        coup2d = 9

        print(a2d,"|",b2d,"|",c2d,"   1|2|3") 
        print("- - - - -    - - -")
        print(d2d,"|",e2d,"|",f2d,"   4|5|6") 
        print("- - - - -    - - -")
        print(g2d,"|",h2d,"|",i2d,"   7|8|9") 
        print("")

        while (coup2d > 0):
            key = "" 
            print("Joueur", xo2d, "c'est a votre tour.")
            print("")

            if (xo2d == "X"):
                if (int(joueur2d) > 0):    
                    key = input(">")
                    if (key == "quit" or key == "sortie" or key == "fin"):
                        game3d = 1
                        break
                else:
                    #computer
                    key = ""
                    for z2d in range(0, 1):
                        if (z2d == 0):
                            ia2d = ox2d
                        else:
                            ia2d = xo2d
                        if ((b2d == ia2d and c2d == ia2d and a2d == " ") or (d2d == ia2d and g2d == ia2d and a2d == " ") or (e2d == ia2d and i2d == ia2d and a2d == " ")):
                            key = "1"
                        if ((a2d == ia2d and c2d == ia2d and b2d == " ") or (e2d == ia2d and h2d == ia2d and b2d == " ")):
                            key = "2"
                        if ((a2d == ia2d and b2d == ia2d and c2d == " ") or (g2d == ia2d and e2d == ia2d and c2d == " ") or (f2d == ia2d and i2d == ia2d and c2d == " ")):
                            key = "3"
                        if ((a2d == ia2d and g2d == ia2d and d2d == " ") or (e2d == ia2d and f2d == ia2d and d2d == " ")):
                            key = "4"
                        if ((a2d == ia2d and i2d == ia2d and e2d == " ") or (d2d == ia2d and f2d == ia2d and e2d == " ") or (g2d == ia2d and c2d == ia2d and e2d == " ") or (b2d == ia2d and h2d == ia2d and e2d == " ")):
                            key = "5"
                        if ((d2d == ia2d and e2d == ia2d and f2d == " ") or (c2d == ia2d and i2d == ia2d and f2d == " ")):
                            key = "6"
                        if ((a2d == ia2d and d2d == ia2d and g2d == " ") or (e2d == ia2d and c2d == ia2d and g2d == " ") or (h2d == ia2d and i2d == ia2d and g2d == " ")):
                            key = "7"
                        if ((g2d == ia2d and i2d == ia2d and h2d == " ") or (b2d == ia2d and e2d == ia2d and h2d == " ")):
                            key = "8"
                        if ((a2d == ia2d and e2d == ia2d and i2d == " ") or (g2d == ia2d and h2d == ia2d and i2d == " ") or (c2d == ia2d and f2d == ia2d and i2d == " ")):
                            key = "9"
                    if (a2d == " " and b2d == " " and c2d == " " and d2d == " " and e2d == " " and f2d == " " and g2d == " " and h2d == " " and i2d == " "):
                        key = str(ran)
                    if (key == ""):
                        valide2d = 0
                        while (valide2d == 0):
                            ran = random.randint(1, 9)
                            if ((ran == 1 and a2d == " ") or (ran == 2 and b2d == " ") or (ran == 3 and c2d == " ") or (ran == 4 and d2d == " ") or (ran == 5 and e2d == " ") or (ran == 6 and f2d == " ") or (ran == 7 and g2d == " ") or (ran == 8 and h2d == " ") or (ran == 9 and i2d == " ")):
                                key = str(ran)
                                valide2d = 1
                    print("> ", key)
                    #return key
            else:
                if (int(joueur2d) > 1):    
                    key = input(">")
                    if (key == "quit" or key == "sortie" or key == "fin"):
                        game3d = 1
                        break
                else:
                    #computer
                    key = ""
                    for z2d in range(0, 1):
                        if (z2d == 0):
                            ia2d = ox2d
                        else:
                            ia2d = xo2d
                        if ((b2d == ia2d and c2d == ia2d and a2d == " ") or (d2d == ia2d and g2d == ia2d and a2d == " ") or (e2d == ia2d and i2d == ia2d and a2d == " ")):
                            key = "1"
                        if ((a2d == ia2d and c2d == ia2d and b2d == " ") or (e2d == ia2d and h2d == ia2d and b2d == " ")):
                            key = "2"
                        if ((a2d == ia2d and b2d == ia2d and c2d == " ") or (g2d == ia2d and e2d == ia2d and c2d == " ") or (f2d == ia2d and i2d == ia2d and c2d == " ")):
                            key = "3"
                        if ((a2d == ia2d and g2d == ia2d and d2d == " ") or (e2d == ia2d and f2d == ia2d and d2d == " ")):
                            key = "4"
                        if ((a2d == ia2d and i2d == ia2d and e2d == " ") or (d2d == ia2d and f2d == ia2d and e2d == " ") or (g2d == ia2d and c2d == ia2d and e2d == " ") or (b2d == ia2d and h2d == ia2d and e2d == " ")):
                            key = "5"
                        if ((d2d == ia2d and e2d == ia2d and f2d == " ") or (c2d == ia2d and i2d == ia2d and f2d == " ")):
                            key = "6"
                        if ((a2d == ia2d and d2d == ia2d and g2d == " ") or (e2d == ia2d and c2d == ia2d and g2d == " ") or (h2d == ia2d and i2d == ia2d and g2d == " ")):
                            key = "7"
                        if ((g2d == ia2d and i2d == ia2d and h2d == " ") or (b2d == ia2d and e2d == ia2d and h2d == " ")):
                            key = "8"
                        if ((a2d == ia2d and e2d == ia2d and i2d == " ") or (g2d == ia2d and h2d == ia2d and i2d == " ") or (c2d == ia2d and f2d == ia2d and i2d == " ")):
                            key = "9"
                    if (a2d == " " and b2d == " " and c2d == " " and d2d == " " and e2d == " " and f2d == " " and g2d == " " and h2d == " " and i2d == " "):
                        key = str(ran)
                    if (key == ""):
                        valide2d = 0
                        while (valide2d == 0):
                            ran = random.randint(1, 9)
                            if ((ran == 1 and a2d == " ") or (ran == 2 and b2d == " ") or (ran == 3 and c2d == " ") or (ran == 4 and d2d == " ") or (ran == 5 and e2d == " ") or (ran == 6 and f2d == " ") or (ran == 7 and g2d == " ") or (ran == 8 and h2d == " ") or (ran == 9 and i2d == " ")):
                                key = str(ran)
                                valide2d = 1
                    print("> ", key)
                    #return key
                    
            if (key == "1"):
                if (a2d == " "):
                    a2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "2"):
                if (b2d == " "):
                    b2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "3"):
                if (c2d == " "):
                    c2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "4"):
                if (d2d == " "):
                    d2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "5"):
                if (e2d == " "):
                    e2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")            
            if (key == "6"):
                if (f2d == " "):
                    f2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "7"):
                if (g2d == " "):
                    g2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "8"):
                if (h2d == " "):
                    h2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "9"):
                if (i2d == " "):
                    i2d = xo2d
                    coup2d = coup2d - 1
                else:
                    print("Ce n'est pas un coup valide.")

            print("")
            print(a2d,"|",b2d,"|",c2d,"   1|2|3") 
            print("- - - - -    - - -")
            print(d2d,"|",e2d,"|",f2d,"   4|5|6") 
            print("- - - - -    - - -")
            print(g2d,"|",h2d,"|",i2d,"   7|8|9") 
            print("")
            
            if ((a2d == xo2d and b2d == xo2d and c2d == xo2d) or (a2d == xo2d and d2d == xo2d and g2d == xo2d) or (a2d == xo2d and e2d == xo2d and i2d == xo2d) or (g2d == xo2d and e2d == xo2d and c2d == xo2d) or (b2d == xo2d and e2d == xo2d and h2d == xo2d) or (c2d == xo2d and f2d == xo2d and i2d == xo2d) or (d2d == xo2d and e2d == xo2d and f2d == xo2d) or (g2d == xo2d and h2d == xo2d and i2d == xo2d)):
                print(xo2d, "a Gagné!")
                Win = 10
                Xp = Xp + Win
                print("Vous recevez",Win, "Xp")
                print("")
                coup2d = 0
            else:
                if (coup2d == 0):
                    print("Partie Null!")
                    print("")
                    
            if (coup2d == 8 or coup2d == 6 or coup2d == 4 or coup2d == 2):
                xo2d = "O"
                ox2d = "X"
            else:
                xo2d = "X"
                ox2d = "O"

        print("Jouer une partie ?")
        key = input("[oui / non] >")
        if (key.upper() == "NON"):
            print("La partie est terminé.")
            game2d = 1
            #exit()
        print("")

def Morpion3D():
    import random
    ran = random.randint(1, 27)
    #IA pourait être encore plus améliorée en retirant les coup aléatoire...
    #Par exemple, elle pourait fermé d'avance des trajectoire possible a son adversaire.
    #Ou faire des 'fourchettes' jusqu'a [5 en 1] ?
    game3d = 0

    print("TTTTTTT   AAA    SSS   SSS   EEEE  RRRR    AAA    CCC  TTTTTTT")
    print("T  T  T  A   A  S     S      E     R   R  A   A  C     T  T  T")
    print("   T     AAAAA   SSS   SSS   EE    RRRR   AAAAA  C        T   ")
    print("   T     A   A      S     S  E     R  R   A   A  C        T   ")
    print("  TTT    A   A   SSS   SSS   EEEE  R   R  A   A   CCC    TTT  ")
    print("")
    print("   M   M   OOO   RRRR   PPPP   III   OOO   N   N    333  DDD ")
    print("   MM MM  O   O  R   R  P   P   I   O   O  NN  N       3 D  D")
    print("   M M M  O   O  RRRR   PPPP    I   O   O  N N N ==  33  D  D")
    print("   M   M  O   O  R  R   P       I   O   O  N  NN       3 D  D")
    print("   M   M   OOO   R   R  P      III   OOO   N   N    333  DDD ")
    print("")
    print("JONATHAN BÉDARD 2018")
    print("")

    while (game3d == 0):
        joueur3d = input("Nombre de Joueur ? >")
        print("")
        a3d = b3d = c3d = d3d  = e3d = f3d = g3d = h3d = i3d = aa3d = bb3d = cc3d = dd3d = ee3d = ff3d = gg3d = hh3d = ii3d = aaa3d = bbb3d = ccc3d = ddd3d = eee3d = fff3d = ggg3d = hhh3d = iii3d = " "
        xo3d = "X"
        ox3d = "O"
        coup3d = 27

        print("STEP 1") 
        print(a3d,"|",b3d,"|",c3d,"   1|2|3") 
        print("- - - - -    - - -")
        print(d3d,"|",e3d,"|",f3d,"   4|5|6") 
        print("- - - - -    - - -")
        print(g3d,"|",h3d,"|",i3d,"   7|8|9") 
        print("")
        print("STEP 2")
        print(aa3d,"|",bb3d,"|",cc3d,"   11|22|33") 
        print("- - - - -    -- -- --")
        print(dd3d,"|",ee3d,"|",ff3d,"   44|55|66") 
        print("- - - - -    -- -- --")
        print(gg3d,"|",hh3d,"|",ii3d,"   77|88|99") 
        print("")    
        print("STEP 3")
        print(aaa3d,"|",bbb3d,"|",ccc3d,"   111|222|333") 
        print("- - - - -    --- --- ---")
        print(ddd3d,"|",eee3d,"|",fff3d,"   444|555|666") 
        print("- - - - -    --- --- ---")
        print(ggg3d,"|",hhh3d,"|",iii3d,"   777|888|999") 
        print("")

        while (coup3d > 0):
            key = "" 
            print("Joueur", xo3d, "c'est a votre tour.")
            print("")

            if (xo3d == "X"):
                if (int(joueur3d) > 0):    
                    key = input(">")
                    if (key == "quit" or key == "sortie" or key == "fin"):
                        game3d = 1
                        break
                else:
                    #computer 3d
                    for z3d in range(0, 1):
                        if (z3d == 0):
                            ia3d = ox3d
                        else:
                            ia3d = xo3d
                        #ia2d alterne les verrifications [Retarder adversaire, Complété une ligne] ****REMPLACER TOUTES LES VARS_3d
                        if ((b3d == ia3d and c3d == ia3d and a3d == " ") or (d3d == ia3d and g3d == ia3d and a3d == " ") or (e3d == ia3d and i3d == ia3d and a3d == " ") or (aa3d == ia3d and aaa3d == ia3d and a3d == " ") or (bb3d == ia3d and ccc3d == ia3d and a3d == " ") or (dd3d == ia3d and ggg3d == ia3d and a3d == " ") or (ee3d == ia3d and iii3d == ia3d and a3d == " ")):
                            key = "1"
                        if ((a3d == ia3d and c3d == ia3d and b3d == " ") or (e3d == ia3d and h3d == ia3d and b3d == " ") or (bb3d == ia3d and bbb3d == ia3d and b3d == " ") or (ee3d == ia3d and hhh3d == ia3d and b3d == " ")):
                            key = "2"
                        if ((a3d == ia3d and b3d == ia3d and c3d == " ") or (g3d == ia3d and e3d == ia3d and c3d == " ") or (f3d == ia3d and i3d == ia3d and c3d == " ") or (cc3d == ia3d and ccc3d == ia3d and c3d == " ") or (bb3d == ia3d and aaa3d == ia3d and c3d == " ") or (ff3d == ia3d and iii3d == ia3d and c3d == " ") or (ee3d == ia3d and ggg3d == ia3d and c3d == " ")):
                            key = "3"
                        if ((a3d == ia3d and g3d == ia3d and d3d == " ") or (e3d == ia3d and f3d == ia3d and d3d == " ") or (dd3d == ia3d and ddd3d == ia3d and d3d == " ") or (ee3d == ia3d and fff3d == ia3d and d3d == " ")):
                            key = "4"
                        if ((a3d == ia3d and i3d == ia3d and e3d == " ") or (d3d == ia3d and f3d == ia3d and e3d == " ") or (g3d == ia3d and c3d == ia3d and e3d == " ") or (b3d == ia3d and h3d == ia3d and e3d == " ") or (ee3d == ia3d and eee3d == ia3d and e3d == " ")):
                            key = "5"
                        if ((d3d == ia3d and e3d == ia3d and f3d == " ") or (c3d == ia3d and i3d == ia3d and f3d == " ") or (ff3d == ia3d and fff3d == ia3d and f3d == " ") or (ee3d == ia3d and ddd3d == ia3d and f3d == " ")):
                            key = "6"
                        if ((a3d == ia3d and d3d == ia3d and g3d == " ") or (e3d == ia3d and c3d == ia3d and g3d == " ") or (h3d == ia3d and i3d == ia3d and g3d == " ") or (gg3d == ia3d and ggg3d == ia3d and g3d == " ") or (dd3d == ia3d and aaa3d == ia3d and g3d == " ") or (hh3d == ia3d and iii3d == ia3d and g3d == " ") or (ee3d == ia3d and ccc3d == ia3d and g3d == " ")):
                            key = "7"
                        if ((g3d == ia3d and i3d == ia3d and h3d == " ") or (b3d == ia3d and e3d == ia3d and h3d == " ") or (hh3d == ia3d and hhh3d == ia3d and h3d == " ") or (ee3d == ia3d and bbb3d == ia3d and h3d == " ")):
                            key = "8"
                        if ((a3d == ia3d and e3d == ia3d and i3d == " ") or (g3d == ia3d and h3d == ia3d and i3d == " ") or (c3d == ia3d and f3d == ia3d and i3d == " ") or (ii3d == ia3d and iii3d == ia3d and i3d == " ") or (hh3d == ia3d and ggg3d == ia3d and i3d == " ") or (ff3d == ia3d and ccc3d == ia3d and i3d == " ") or (ee3d == ia3d and aaa3d == ia3d and i3d == " ")):
                            key = "9"
                        if ((bb3d == ia3d and cc3d == ia3d and aa3d == " ") or (dd3d == ia3d and gg3d == ia3d and aa3d == " ") or (ee3d == ia3d and ii3d == ia3d and aa3d == " ") or (a3d == ia3d and aaa3d == ia3d and aa3d == " ") or (b3d == ia3d and ccc3d == ia3d and aa3d == " ") or (d3d == ia3d and ggg3d == ia3d and aa3d == " ") or (e3d == ia3d and iii3d == ia3d and aa3d == " ")):
                            key = "11"
                        if ((aa3d == ia3d and cc3d == ia3d and bb3d == " ") or (ee3d == ia3d and hh3d == ia3d and bb3d == " ") or (b3d == ia3d and bbb3d == ia3d and bb3d == " ") or (e3d == ia3d and hhh3d == ia3d and bb3d == " ")):
                            key = "22"
                        if ((aa3d == ia3d and bb3d == ia3d and cc3d == " ") or (gg3d == ia3d and ee3d == ia3d and cc3d == " ") or (ff3d == ia3d and ii3d == ia3d and cc3d == " ") or (c3d == ia3d and ccc3d == ia3d and cc3d == " ") or (b3d == ia3d and aaa3d == ia3d and cc3d == " ") or (f3d == ia3d and iii3d == ia3d and cc3d == " ") or (e3d == ia3d and ggg3d == ia3d and cc3d == " ")):
                            key = "33"
                        if ((aa3d == ia3d and gg3d == ia3d and dd3d == " ") or (ee3d == ia3d and ff3d == ia3d and dd3d == " ") or (d3d == ia3d and ddd3d == ia3d and dd3d == " ") or (e3d == ia3d and fff3d == ia3d and dd3d == " ")):
                            key = "44"
                        if ((aa3d == ia3d and ii3d == ia3d and ee3d == " ") or (dd3d == ia3d and ff3d == ia3d and ee3d == " ") or (gg3d == ia3d and cc3d == ia3d and ee3d == " ") or (bb3d == ia3d and hh3d == ia3d and ee3d == " ") or (e3d == ia3d and eee3d == ia3d and ee3d == " ")):
                            key = "55"
                        if ((dd3d == ia3d and ee3d == ia3d and ff3d == " ") or (cc3d == ia3d and ii3d == ia3d and ff3d == " ") or (f3d == ia3d and fff3d == ia3d and ff3d == " ") or (e3d == ia3d and ddd3d == ia3d and ff3d == " ")):
                            key = "66"
                        if ((aa3d == ia3d and dd3d == ia3d and gg3d == " ") or (ee3d == ia3d and cc3d == ia3d and gg3d == " ") or (hh3d == ia3d and ii3d == ia3d and gg3d == " ") or (g3d == ia3d and ggg3d == ia3d and gg3d == " ") or (d3d == ia3d and aaa3d == ia3d and gg3d == " ") or (h3d == ia3d and iii3d == ia3d and gg3d == " ") or (e3d == ia3d and ccc3d == ia3d and gg3d == " ")):
                            key = "77"
                        if ((gg3d == ia3d and ii3d == ia3d and hh3d == " ") or (bb3d == ia3d and ee3d == ia3d and hh3d == " ") or (h3d == ia3d and hhh3d == ia3d and hh3d == " ") or (e3d == ia3d and bbb3d == ia3d and hh3d == " ")):
                            key = "88"
                        if ((aa3d == ia3d and ee3d == ia3d and ii3d == " ") or (gg3d == ia3d and hh3d == ia3d and ii3d == " ") or (cc3d == ia3d and ff3d == ia3d and ii3d == " ") or (i3d == ia3d and iii3d == ia3d and ii3d == " ") or (h3d == ia3d and ggg3d == ia3d and ii3d == " ") or (f3d == ia3d and ccc3d == ia3d and ii3d == " ") or (e3d == ia3d and aaa3d == ia3d and ii3d == " ")):
                            key = "99"        
                        if ((bbb3d == ia3d and ccc3d == ia3d and aaa3d == " ") or (ddd3d == ia3d and ggg3d == ia3d and aaa3d == " ") or (eee3d == ia3d and iii3d == ia3d and aaa3d == " ") or (aa3d == ia3d and a3d == ia3d and aaa3d == " ") or (bb3d == ia3d and c3d == ia3d and aaa3d == " ") or (dd3d == ia3d and g3d == ia3d and aaa3d == " ") or (ee3d == ia3d and i3d == ia3d and aaa3d == " ")):
                            key = "111"
                        if ((aaa3d == ia3d and ccc3d == ia3d and bbb3d == " ") or (eee3d == ia3d and hhh3d == ia3d and bbb3d == " ") or (bb3d == ia3d and b3d == ia3d and bbb3d == " ") or (ee3d == ia3d and h3d == ia3d and bbb3d == " ")):
                            key = "222"
                        if ((aaa3d == ia3d and bbb3d == ia3d and ccc3d == " ") or (ggg3d == ia3d and eee3d == ia3d and ccc3d == " ") or (fff3d == ia3d and iii3d == ia3d and ccc3d == " ") or (cc3d == ia3d and c3d == ia3d and ccc3d == " ") or (bb3d == ia3d and a3d == ia3d and ccc3d == " ") or (ff3d == ia3d and i3d == ia3d and ccc3d == " ") or (ee3d == ia3d and g3d == ia3d and ccc3d == " ")):
                            key = "333"
                        if ((aaa3d == ia3d and ggg3d == ia3d and ddd3d == " ") or (eee3d == ia3d and fff3d == ia3d and ddd3d == " ")or (dd3d == ia3d and d3d == ia3d and ddd3d == " ") or (ee3d == ia3d and f3d == ia3d and ddd3d == " ")):
                            key = "444"
                        if ((aaa3d == ia3d and iii3d == ia3d and eee3d == " ") or (ddd3d == ia3d and fff3d == ia3d and eee3d == " ") or (ggg3d == ia3d and ccc3d == ia3d and eee3d == " ") or (bbb3d == ia3d and hhh3d == ia3d and eee3d == " ") or (ee3d == ia3d and e3d == ia3d and eee3d == " ")):
                            key = "555"
                        if ((ddd3d == ia3d and eee3d == ia3d and fff3d == " ") or (ccc3d == ia3d and iii3d == ia3d and fff3d == " ") or (ff3d == ia3d and f3d == ia3d and fff3d == " ") or (ee3d == ia3d and d3d == ia3d and fff3d == " ")):
                            key = "666"
                        if ((aaa3d == ia3d and ddd3d == ia3d and ggg3d == " ") or (eee3d == ia3d and ccc3d == ia3d and ggg3d == " ") or (hhh3d == ia3d and iii3d == ia3d and ggg3d == " ") or (gg3d == ia3d and g3d == ia3d and ggg3d == " ") or (dd3d == ia3d and a3d == ia3d and ggg3d == " ") or (hh3d == ia3d and i3d == ia3d and ggg3d == " ") or (ee3d == ia3d and c3d == ia3d and ggg3d == " ")):
                            key = "777"
                        if ((ggg3d == ia3d and iii3d == ia3d and hhh3d == " ") or (bbb3d == ia3d and eee3d == ia3d and hhh3d == " ") or (hh3d == ia3d and h3d == ia3d and hhh3d == " ") or (ee3d == ia3d and b3d == ia3d and hhh3d == " ")):
                            key = "888"
                        if ((aaa3d == ia3d and eee3d == ia3d and iii3d == " ") or (ggg3d == ia3d and hhh3d == ia3d and iii3d == " ") or (ccc3d == ia3d and fff3d == ia3d and iii3d == " ") or (ii3d == ia3d and i3d == ia3d and iii3d == " ") or (hh3d == ia3d and g3d == ia3d and iii3d == " ") or (ff3d == ia3d and c3d == ia3d and iii3d == " ") or (ee3d == ia3d and a3d == ia3d and iii3d == " ")):
                            key = "999"
                    #Si aucune case n'est encore remplit, Joue au hazard
                    if (a3d == " " and b3d == " " and c3d == " " and d3d == " " and e3d == " " and f3d == " " and g3d == " " and h3d == " " and i3d == " " and aa3d == " " and bb3d == " " and cc3d == " " and dd3d == " " and ee3d == " " and ff3d == " " and gg3d == " " and hh3d == " " and ii3d == " " and aaa3d == " " and bbb3d == " " and ccc3d == " " and ddd3d == " " and eee3d == " " and fff3d == " " and ggg3d == " " and hhh3d == " " and iii3d == " "):
                        if (ran == 1):
                            key = "1"
                        if (ran == 2):
                            key = "2"
                        if (ran == 3):
                            key = "3"
                        if (ran == 4):
                            key = "4"
                        if (ran == 5):
                            key = "5"
                        if (ran == 6):
                            key = "6"
                        if (ran == 7):
                            key = "7"
                        if (ran == 8):
                            key = "8"
                        if (ran == 9):
                            key = "9"
                        if (ran == 10):
                            key = "11"
                        if (ran == 11):
                            key = "22"
                        if (ran == 12):
                            key = "33"
                        if (ran == 13):
                            key = "44"
                        if (ran == 14):
                            key = "55"
                        if (ran == 15):
                            key = "66"
                        if (ran == 16):
                            key = "77"
                        if (ran == 17):
                            key = "88"
                        if (ran == 18):
                            key = "99"
                        if (ran == 19):
                            key = "111"
                        if (ran == 20):
                            key = "222"
                        if (ran == 21):
                            key = "333"
                        if (ran == 22):
                            key = "444"
                        if (ran == 23):
                            key = "555"
                        if (ran == 24):
                            key = "666"
                        if (ran == 25):
                            key = "777"
                        if (ran == 26):
                            key = "888"
                        if (ran == 27):
                            key = "999"
                    #Si au moins une case est occupé et qu'il n'y a rien a faire, Joue au hazard
                    if (key == ""):
                        valide3d = 0
                        while (valide3d == 0):
                            ran = random.randint(1, 27)
                            if ((ran == 1 and a3d == " ") or (ran == 2 and b3d == " ") or (ran == 3 and c3d == " ") or (ran == 4 and d3d == " ") or (ran == 5 and e3d == " ") or (ran == 6 and f3d == " ") or (ran == 7 and g3d == " ") or (ran == 8 and h3d == " ") or (ran == 9 and i3d == " ") or (ran == 10 and aa3d == " ") or (ran == 11 and bb3d == " ") or (ran == 12 and cc3d == " ") or (ran == 13 and dd3d == " ") or (ran == 14 and ee3d == " ") or (ran == 15 and ff3d == " ") or (ran == 16 and gg3d == " ") or (ran == 17 and hh3d == " ") or (ran == 18 and ii3d == " ") or (ran == 19 and aaa3d == " ") or (ran == 20 and bbb3d == " ") or (ran == 21 and ccc3d == " ") or (ran == 22 and ddd3d == " ") or (ran == 23 and eee3d == " ") or (ran == 24 and fff3d == " ") or (ran == 25 and ggg3d == " ") or (ran == 26 and hhh3d == " ") or (ran == 27 and iii3d == " ")):
                                if (ran == 1):
                                    key = "1"
                                if (ran == 2):
                                   key = "2"
                                if (ran == 3):
                                    key = "3"
                                if (ran == 4):
                                    key = "4"
                                if (ran == 5):
                                    key = "5"
                                if (ran == 6):
                                    key = "6"
                                if (ran == 7):
                                    key = "7"
                                if (ran == 8):
                                    key = "8"
                                if (ran == 9):
                                    key = "9"
                                if (ran == 10):
                                    key = "11"
                                if (ran == 11):
                                    key = "22"
                                if (ran == 12):
                                    key = "33"
                                if (ran == 13):
                                    key = "44"
                                if (ran == 14):
                                    key = "55"
                                if (ran == 15):
                                    key = "66"
                                if (ran == 16):
                                    key = "77"
                                if (ran == 17):
                                    key = "88"
                                if (ran == 18):
                                    key = "99"
                                if (ran == 19):
                                    key = "111"
                                if (ran == 20):
                                    key = "222"
                                if (ran == 21):
                                    key = "333"
                                if (ran == 22):
                                    key = "444"
                                if (ran == 23):
                                    key = "555"
                                if (ran == 24):
                                    key = "666"
                                if (ran == 25):
                                    key = "777"
                                if (ran == 26):
                                    key = "888"
                                if (ran == 27):
                                    key = "999"
                                valide3d = 1
                    print("> ", key)
            else:
                if (int(joueur3d) > 1):    
                    key = input(">")
                    if (key == "quit" or key == "sortie" or key == "fin"):
                        game3d = 1
                        break
                else:
                    #computer 3d
                    for z3d in range(0, 1):
                        if (z3d == 0):
                            ia3d = ox3d
                        else:
                            ia3d = xo3d
                        #ia2d alterne les verrifications [Retarder adversaire, Complété une ligne] ****REMPLACER TOUTES LES VARS_3d
                        if ((b3d == ia3d and c3d == ia3d and a3d == " ") or (d3d == ia3d and g3d == ia3d and a3d == " ") or (e3d == ia3d and i3d == ia3d and a3d == " ") or (aa3d == ia3d and aaa3d == ia3d and a3d == " ") or (bb3d == ia3d and ccc3d == ia3d and a3d == " ") or (dd3d == ia3d and ggg3d == ia3d and a3d == " ") or (ee3d == ia3d and iii3d == ia3d and a3d == " ")):
                            key = "1"
                        if ((a3d == ia3d and c3d == ia3d and b3d == " ") or (e3d == ia3d and h3d == ia3d and b3d == " ") or (bb3d == ia3d and bbb3d == ia3d and b3d == " ") or (ee3d == ia3d and hhh3d == ia3d and b3d == " ")):
                            key = "2"
                        if ((a3d == ia3d and b3d == ia3d and c3d == " ") or (g3d == ia3d and e3d == ia3d and c3d == " ") or (f3d == ia3d and i3d == ia3d and c3d == " ") or (cc3d == ia3d and ccc3d == ia3d and c3d == " ") or (bb3d == ia3d and aaa3d == ia3d and c3d == " ") or (ff3d == ia3d and iii3d == ia3d and c3d == " ") or (ee3d == ia3d and ggg3d == ia3d and c3d == " ")):
                            key = "3"
                        if ((a3d == ia3d and g3d == ia3d and d3d == " ") or (e3d == ia3d and f3d == ia3d and d3d == " ") or (dd3d == ia3d and ddd3d == ia3d and d3d == " ") or (ee3d == ia3d and fff3d == ia3d and d3d == " ")):
                            key = "4"
                        if ((a3d == ia3d and i3d == ia3d and e3d == " ") or (d3d == ia3d and f3d == ia3d and e3d == " ") or (g3d == ia3d and c3d == ia3d and e3d == " ") or (b3d == ia3d and h3d == ia3d and e3d == " ") or (ee3d == ia3d and eee3d == ia3d and e3d == " ")):
                            key = "5"
                        if ((d3d == ia3d and e3d == ia3d and f3d == " ") or (c3d == ia3d and i3d == ia3d and f3d == " ") or (ff3d == ia3d and fff3d == ia3d and f3d == " ") or (ee3d == ia3d and ddd3d == ia3d and f3d == " ")):
                            key = "6"
                        if ((a3d == ia3d and d3d == ia3d and g3d == " ") or (e3d == ia3d and c3d == ia3d and g3d == " ") or (h3d == ia3d and i3d == ia3d and g3d == " ") or (gg3d == ia3d and ggg3d == ia3d and g3d == " ") or (dd3d == ia3d and aaa3d == ia3d and g3d == " ") or (hh3d == ia3d and iii3d == ia3d and g3d == " ") or (ee3d == ia3d and ccc3d == ia3d and g3d == " ")):
                            key = "7"
                        if ((g3d == ia3d and i3d == ia3d and h3d == " ") or (b3d == ia3d and e3d == ia3d and h3d == " ") or (hh3d == ia3d and hhh3d == ia3d and h3d == " ") or (ee3d == ia3d and bbb3d == ia3d and h3d == " ")):
                            key = "8"
                        if ((a3d == ia3d and e3d == ia3d and i3d == " ") or (g3d == ia3d and h3d == ia3d and i3d == " ") or (c3d == ia3d and f3d == ia3d and i3d == " ") or (ii3d == ia3d and iii3d == ia3d and i3d == " ") or (hh3d == ia3d and ggg3d == ia3d and i3d == " ") or (ff3d == ia3d and ccc3d == ia3d and i3d == " ") or (ee3d == ia3d and aaa3d == ia3d and i3d == " ")):
                            key = "9"
                        if ((bb3d == ia3d and cc3d == ia3d and aa3d == " ") or (dd3d == ia3d and gg3d == ia3d and aa3d == " ") or (ee3d == ia3d and ii3d == ia3d and aa3d == " ") or (a3d == ia3d and aaa3d == ia3d and aa3d == " ") or (b3d == ia3d and ccc3d == ia3d and aa3d == " ") or (d3d == ia3d and ggg3d == ia3d and aa3d == " ") or (e3d == ia3d and iii3d == ia3d and aa3d == " ")):
                            key = "11"
                        if ((aa3d == ia3d and cc3d == ia3d and bb3d == " ") or (ee3d == ia3d and hh3d == ia3d and bb3d == " ") or (b3d == ia3d and bbb3d == ia3d and bb3d == " ") or (e3d == ia3d and hhh3d == ia3d and bb3d == " ")):
                            key = "22"
                        if ((aa3d == ia3d and bb3d == ia3d and cc3d == " ") or (gg3d == ia3d and ee3d == ia3d and cc3d == " ") or (ff3d == ia3d and ii3d == ia3d and cc3d == " ") or (c3d == ia3d and ccc3d == ia3d and cc3d == " ") or (b3d == ia3d and aaa3d == ia3d and cc3d == " ") or (f3d == ia3d and iii3d == ia3d and cc3d == " ") or (e3d == ia3d and ggg3d == ia3d and cc3d == " ")):
                            key = "33"
                        if ((aa3d == ia3d and gg3d == ia3d and dd3d == " ") or (ee3d == ia3d and ff3d == ia3d and dd3d == " ") or (d3d == ia3d and ddd3d == ia3d and dd3d == " ") or (e3d == ia3d and fff3d == ia3d and dd3d == " ")):
                            key = "44"
                        if ((aa3d == ia3d and ii3d == ia3d and ee3d == " ") or (dd3d == ia3d and ff3d == ia3d and ee3d == " ") or (gg3d == ia3d and cc3d == ia3d and ee3d == " ") or (bb3d == ia3d and hh3d == ia3d and ee3d == " ") or (e3d == ia3d and eee3d == ia3d and ee3d == " ")):
                            key = "55"
                        if ((dd3d == ia3d and ee3d == ia3d and ff3d == " ") or (cc3d == ia3d and ii3d == ia3d and ff3d == " ") or (f3d == ia3d and fff3d == ia3d and ff3d == " ") or (e3d == ia3d and ddd3d == ia3d and ff3d == " ")):
                            key = "66"
                        if ((aa3d == ia3d and dd3d == ia3d and gg3d == " ") or (ee3d == ia3d and cc3d == ia3d and gg3d == " ") or (hh3d == ia3d and ii3d == ia3d and gg3d == " ") or (g3d == ia3d and ggg3d == ia3d and gg3d == " ") or (d3d == ia3d and aaa3d == ia3d and gg3d == " ") or (h3d == ia3d and iii3d == ia3d and gg3d == " ") or (e3d == ia3d and ccc3d == ia3d and gg3d == " ")):
                            key = "77"
                        if ((gg3d == ia3d and ii3d == ia3d and hh3d == " ") or (bb3d == ia3d and ee3d == ia3d and hh3d == " ") or (h3d == ia3d and hhh3d == ia3d and hh3d == " ") or (e3d == ia3d and bbb3d == ia3d and hh3d == " ")):
                            key = "88"
                        if ((aa3d == ia3d and ee3d == ia3d and ii3d == " ") or (gg3d == ia3d and hh3d == ia3d and ii3d == " ") or (cc3d == ia3d and ff3d == ia3d and ii3d == " ") or (i3d == ia3d and iii3d == ia3d and ii3d == " ") or (h3d == ia3d and ggg3d == ia3d and ii3d == " ") or (f3d == ia3d and ccc3d == ia3d and ii3d == " ") or (e3d == ia3d and aaa3d == ia3d and ii3d == " ")):
                            key = "99"        
                        if ((bbb3d == ia3d and ccc3d == ia3d and aaa3d == " ") or (ddd3d == ia3d and ggg3d == ia3d and aaa3d == " ") or (eee3d == ia3d and iii3d == ia3d and aaa3d == " ") or (aa3d == ia3d and a3d == ia3d and aaa3d == " ") or (bb3d == ia3d and c3d == ia3d and aaa3d == " ") or (dd3d == ia3d and g3d == ia3d and aaa3d == " ") or (ee3d == ia3d and i3d == ia3d and aaa3d == " ")):
                            key = "111"
                        if ((aaa3d == ia3d and ccc3d == ia3d and bbb3d == " ") or (eee3d == ia3d and hhh3d == ia3d and bbb3d == " ") or (bb3d == ia3d and b3d == ia3d and bbb3d == " ") or (ee3d == ia3d and h3d == ia3d and bbb3d == " ")):
                            key = "222"
                        if ((aaa3d == ia3d and bbb3d == ia3d and ccc3d == " ") or (ggg3d == ia3d and eee3d == ia3d and ccc3d == " ") or (fff3d == ia3d and iii3d == ia3d and ccc3d == " ") or (cc3d == ia3d and c3d == ia3d and ccc3d == " ") or (bb3d == ia3d and a3d == ia3d and ccc3d == " ") or (ff3d == ia3d and i3d == ia3d and ccc3d == " ") or (ee3d == ia3d and g3d == ia3d and ccc3d == " ")):
                            key = "333"
                        if ((aaa3d == ia3d and ggg3d == ia3d and ddd3d == " ") or (eee3d == ia3d and fff3d == ia3d and ddd3d == " ")or (dd3d == ia3d and d3d == ia3d and ddd3d == " ") or (ee3d == ia3d and f3d == ia3d and ddd3d == " ")):
                            key = "444"
                        if ((aaa3d == ia3d and iii3d == ia3d and eee3d == " ") or (ddd3d == ia3d and fff3d == ia3d and eee3d == " ") or (ggg3d == ia3d and ccc3d == ia3d and eee3d == " ") or (bbb3d == ia3d and hhh3d == ia3d and eee3d == " ") or (ee3d == ia3d and e3d == ia3d and eee3d == " ")):
                            key = "555"
                        if ((ddd3d == ia3d and eee3d == ia3d and fff3d == " ") or (ccc3d == ia3d and iii3d == ia3d and fff3d == " ") or (ff3d == ia3d and f3d == ia3d and fff3d == " ") or (ee3d == ia3d and d3d == ia3d and fff3d == " ")):
                            key = "666"
                        if ((aaa3d == ia3d and ddd3d == ia3d and ggg3d == " ") or (eee3d == ia3d and ccc3d == ia3d and ggg3d == " ") or (hhh3d == ia3d and iii3d == ia3d and ggg3d == " ") or (gg3d == ia3d and g3d == ia3d and ggg3d == " ") or (dd3d == ia3d and a3d == ia3d and ggg3d == " ") or (hh3d == ia3d and i3d == ia3d and ggg3d == " ") or (ee3d == ia3d and c3d == ia3d and ggg3d == " ")):
                            key = "777"
                        if ((ggg3d == ia3d and iii3d == ia3d and hhh3d == " ") or (bbb3d == ia3d and eee3d == ia3d and hhh3d == " ") or (hh3d == ia3d and h3d == ia3d and hhh3d == " ") or (ee3d == ia3d and b3d == ia3d and hhh3d == " ")):
                            key = "888"
                        if ((aaa3d == ia3d and eee3d == ia3d and iii3d == " ") or (ggg3d == ia3d and hhh3d == ia3d and iii3d == " ") or (ccc3d == ia3d and fff3d == ia3d and iii3d == " ") or (ii3d == ia3d and i3d == ia3d and iii3d == " ") or (hh3d == ia3d and g3d == ia3d and iii3d == " ") or (ff3d == ia3d and c3d == ia3d and iii3d == " ") or (ee3d == ia3d and a3d == ia3d and iii3d == " ")):
                            key = "999"
                    #Si aucune case n'est encore remplit, Joue au hazard
                    if (a3d == " " and b3d == " " and c3d == " " and d3d == " " and e3d == " " and f3d == " " and g3d == " " and h3d == " " and i3d == " " and aa3d == " " and bb3d == " " and cc3d == " " and dd3d == " " and ee3d == " " and ff3d == " " and gg3d == " " and hh3d == " " and ii3d == " " and aaa3d == " " and bbb3d == " " and ccc3d == " " and ddd3d == " " and eee3d == " " and fff3d == " " and ggg3d == " " and hhh3d == " " and iii3d == " "):
                        if (ran == 1):
                            key = "1"
                        if (ran == 2):
                            key = "2"
                        if (ran == 3):
                            key = "3"
                        if (ran == 4):
                            key = "4"
                        if (ran == 5):
                            key = "5"
                        if (ran == 6):
                            key = "6"
                        if (ran == 7):
                            key = "7"
                        if (ran == 8):
                            key = "8"
                        if (ran == 9):
                            key = "9"
                        if (ran == 10):
                            key = "11"
                        if (ran == 11):
                            key = "22"
                        if (ran == 12):
                            key = "33"
                        if (ran == 13):
                            key = "44"
                        if (ran == 14):
                            key = "55"
                        if (ran == 15):
                            key = "66"
                        if (ran == 16):
                            key = "77"
                        if (ran == 17):
                            key = "88"
                        if (ran == 18):
                            key = "99"
                        if (ran == 19):
                            key = "111"
                        if (ran == 20):
                            key = "222"
                        if (ran == 21):
                            key = "333"
                        if (ran == 22):
                            key = "444"
                        if (ran == 23):
                            key = "555"
                        if (ran == 24):
                            key = "666"
                        if (ran == 25):
                            key = "777"
                        if (ran == 26):
                            key = "888"
                        if (ran == 27):
                            key = "999"
                    #Si au moins une case est occupé et qu'il n'y a rien a faire, Joue au hazard
                    if (key == ""):
                        valide3d = 0
                        while (valide3d == 0):
                            ran = random.randint(1, 27)
                            if ((ran == 1 and a3d == " ") or (ran == 2 and b3d == " ") or (ran == 3 and c3d == " ") or (ran == 4 and d3d == " ") or (ran == 5 and e3d == " ") or (ran == 6 and f3d == " ") or (ran == 7 and g3d == " ") or (ran == 8 and h3d == " ") or (ran == 9 and i3d == " ") or (ran == 10 and aa3d == " ") or (ran == 11 and bb3d == " ") or (ran == 12 and cc3d == " ") or (ran == 13 and dd3d == " ") or (ran == 14 and ee3d == " ") or (ran == 15 and ff3d == " ") or (ran == 16 and gg3d == " ") or (ran == 17 and hh3d == " ") or (ran == 18 and ii3d == " ") or (ran == 19 and aaa3d == " ") or (ran == 20 and bbb3d == " ") or (ran == 21 and ccc3d == " ") or (ran == 22 and ddd3d == " ") or (ran == 23 and eee3d == " ") or (ran == 24 and fff3d == " ") or (ran == 25 and ggg3d == " ") or (ran == 26 and hhh3d == " ") or (ran == 27 and iii3d == " ")):
                                if (ran == 1):
                                    key = "1"
                                if (ran == 2):
                                   key = "2"
                                if (ran == 3):
                                    key = "3"
                                if (ran == 4):
                                    key = "4"
                                if (ran == 5):
                                    key = "5"
                                if (ran == 6):
                                    key = "6"
                                if (ran == 7):
                                    key = "7"
                                if (ran == 8):
                                    key = "8"
                                if (ran == 9):
                                    key = "9"
                                if (ran == 10):
                                    key = "11"
                                if (ran == 11):
                                    key = "22"
                                if (ran == 12):
                                    key = "33"
                                if (ran == 13):
                                    key = "44"
                                if (ran == 14):
                                    key = "55"
                                if (ran == 15):
                                    key = "66"
                                if (ran == 16):
                                    key = "77"
                                if (ran == 17):
                                    key = "88"
                                if (ran == 18):
                                    key = "99"
                                if (ran == 19):
                                    key = "111"
                                if (ran == 20):
                                    key = "222"
                                if (ran == 21):
                                    key = "333"
                                if (ran == 22):
                                    key = "444"
                                if (ran == 23):
                                    key = "555"
                                if (ran == 24):
                                    key = "666"
                                if (ran == 25):
                                    key = "777"
                                if (ran == 26):
                                    key = "888"
                                if (ran == 27):
                                    key = "999"
                                valide3d = 1
                    print("> ", key)
                    
            if (key == "1"):
                if (a3d == " "):
                    a3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "2"):
                if (b3d == " "):
                    b3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "3"):
                if (c3d == " "):
                    c3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "4"):
                if (d3d == " "):
                    d3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "5"):
                if (e3d == " "):
                    e3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")            
            if (key == "6"):
                if (f3d == " "):
                    f3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "7"):
                if (g3d == " "):
                    g3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "8"):
                if (h3d == " "):
                    h3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "9"):
                if (i3d == " "):
                    i3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")

            if (key == "11"):
                if (aa3d == " "):
                    aa3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "22"):
                if (bb3d == " "):
                    bb3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "33"):
                if (cc3d == " "):
                    cc3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "44"):
                if (dd3d == " "):
                    dd3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "55"):
                if (ee3d == " "):
                    ee3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")            
            if (key == "66"):
                if (ff3d == " "):
                    ff3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "77"):
                if (gg3d == " "):
                    gg3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "88"):
                if (hh3d == " "):
                    hh3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "99"):
                if (ii3d == " "):
                    ii3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "111"):
                if (aaa3d == " "):
                    aaa3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "222"):
                if (bbb3d == " "):
                    bbb3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "333"):
                if (ccc3d == " "):
                    ccc3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "444"):
                if (ddd3d == " "):
                    ddd3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "555"):
                if (eee3d == " "):
                    eee3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")            
            if (key == "666"):
                if (fff3d == " "):
                    fff3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "777"):
                if (ggg3d == " "):
                    ggg3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "888"):
                if (hhh3d == " "):
                    hhh3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            if (key == "999"):
                if (iii3d == " "):
                    iii3d = xo3d
                    coup3d = coup3d - 1
                else:
                    print("Ce n'est pas un coup valide.")
            print("")
            print("STEP 1") 
            print(a3d,"|",b3d,"|",c3d,"   1|2|3") 
            print("- - - - -    - - -")
            print(d3d,"|",e3d,"|",f3d,"   4|5|6") 
            print("- - - - -    - - -")
            print(g3d,"|",h3d,"|",i3d,"   7|8|9") 
            print("")
            print("STEP 2")
            print(aa3d,"|",bb3d,"|",cc3d,"   11|22|33") 
            print("- - - - -    -- -- --")
            print(dd3d,"|",ee3d,"|",ff3d,"   44|55|66") 
            print("- - - - -    -- -- --")
            print(gg3d,"|",hh3d,"|",ii3d,"   77|88|99") 
            print("")    
            print("STEP 3")
            print(aaa3d,"|",bbb3d,"|",ccc3d,"   111|222|333") 
            print("- - - - -    --- --- ---")
            print(ddd3d,"|",eee3d,"|",fff3d,"   444|555|666") 
            print("- - - - -    --- --- ---")
            print(ggg3d,"|",hhh3d,"|",iii3d,"   777|888|999") 
            print("")

            if ((a3d == xo3d and b3d == xo3d and c3d == xo3d) or (a3d == xo3d and d3d == xo3d and g3d == xo3d) or (a3d == xo3d and e3d == xo3d and i3d == xo3d) or (g3d == xo3d and e3d == xo3d and c3d == xo3d) or (b3d == xo3d and e3d == xo3d and h3d == xo3d) or (c3d == xo3d and f3d == xo3d and i3d == xo3d) or (d3d == xo3d and e3d == xo3d and f3d == xo3d) or (g3d == xo3d and h3d == xo3d and i3d == xo3d) or (a3d == xo3d and aa3d == xo3d and aaa3d == xo3d) or (b3d == xo3d and bb3d == xo3d and bbb3d == xo3d) or (c3d == xo3d and cc3d == xo3d and ccc3d == xo3d) or (d3d == xo3d and dd3d == xo3d and ddd3d == xo3d) or (e3d == xo3d and ee3d == xo3d and eee3d == xo3d) or (f3d == xo3d and ff3d == xo3d and  fff3d == xo3d) or (g3d == xo3d and gg3d == xo3d and ggg3d == xo3d) or (h3d == xo3d and hh3d == xo3d and hhh3d == xo3d) or (i3d == xo3d and ii3d == xo3d and iii3d == xo3d) or (aa3d == xo3d and bb3d == xo3d and cc3d == xo3d) or (aa3d == xo3d and dd3d == xo3d and gg3d == xo3d) or (aa3d == xo3d and ee3d == xo3d and ii3d == xo3d) or (gg3d == xo3d and ee3d == xo3d and cc3d == xo3d) or (bb3d == xo3d and ee3d == xo3d and hh3d == xo3d) or (cc3d == xo3d and ff3d == xo3d and ii3d == xo3d) or (dd3d == xo3d and ee3d == xo3d and ff3d == xo3d) or (gg3d == xo3d and hh3d == xo3d and ii3d == xo3d) or (aaa3d == xo3d and bbb3d == xo3d and ccc3d == xo3d) or (aaa3d == xo3d and ddd3d == xo3d and ggg3d == xo3d) or (aaa3d == xo3d and eee3d == xo3d and iii3d == xo3d) or (ggg3d == xo3d and eee3d == xo3d and ccc3d == xo3d) or (bbb3d == xo3d and eee3d == xo3d and hhh3d == xo3d) or (ccc3d == xo3d and fff3d == xo3d and iii3d == xo3d) or (ddd3d == xo3d and eee3d == xo3d and fff3d == xo3d) or (ggg3d == xo3d and hhh3d == xo3d and iii3d == xo3d) or (a3d == xo3d and ee3d == xo3d and iii3d == xo3d) or (b3d == xo3d and ee3d == xo3d and hhh3d == xo3d) or (c3d == xo3d and ee3d == xo3d and ggg3d == xo3d) or (d3d == xo3d and ee3d == xo3d and fff3d == xo3d) or (f3d == xo3d and ee3d == xo3d and ddd3d == xo3d) or (g3d == xo3d and ee3d == xo3d and ccc3d == xo3d) or (h3d == xo3d and ee3d == xo3d and bbb3d == xo3d) or (i3d == xo3d and ee3d == xo3d and aaa3d == xo3d) or (a3d == xo3d and bb3d == xo3d and ccc3d == xo3d) or (c3d == xo3d and bb3d == xo3d and aaa3d == xo3d) or (d3d == xo3d and ee3d == xo3d and fff3d == xo3d) or (f3d == xo3d and ee3d == xo3d and ddd3d == xo3d) or (g3d == xo3d and hh3d == xo3d and iii3d == xo3d) or (i3d == xo3d and hh3d == xo3d and ggg3d == xo3d) or (a3d == xo3d and dd3d == xo3d and ggg3d == xo3d) or (g3d == xo3d and dd3d == xo3d and aaa3d == xo3d) or (b3d == xo3d and ee3d == xo3d and hhh3d == xo3d) or (h3d == xo3d and ee3d == xo3d and bbb3d == xo3d) or (c3d == xo3d and ff3d == xo3d and iii3d == xo3d) or (i3d == xo3d and ff3d == xo3d and ccc3d == xo3d)):
                print(xo3d, "a Gagné!")
                Win = 30
                Xp = Xp + Win
                print("Vous recevez",Win, "Xp")
                print("")
                coup3d = 0
            else:
                if (coup3d == 0):
                    print("Partie Null!")
                    print("")
                    
            if (coup3d == 26 or coup3d == 24 or coup3d == 22 or coup3d == 20 or coup3d == 18 or coup3d == 16 or coup3d == 14 or coup3d == 12 or coup3d == 10 or coup3d == 8 or coup3d == 6 or coup3d == 4 or coup3d == 2):
                xo3d = "O"
                ox3d = "X"
            else:
                xo3d = "X"
                ox3d = "O"

        print("Jouer une partie ?")
        key = input("[oui / non] >")
        if (key.upper() == "NON"):
            print("La partie est terminé.")
            game3d = 1
            #exit()
        print("")

def window():
    global writer, CALENDRIER, messageIA, align, taille, police, effet , xCoord, yCoord, xCorrection
    tracer(False)
    setup()
    tracer(False)  # Terminator can occur here
    writer.clear()
    writer.home()

    if (align == "center"):
        if (xCoord > 250):
            align = "left"
            xCorrection = ""
            for x in range(round((xCoord - 250) / taille)):
                xCorrection = xCorrection + " "
            messageIA = xCorrection + messageIA
        else:
            align = "right"
            xCorrection = ""
            for x in range(round(250 - (xCoord / taille))):
                xCorrection = xCorrection + " "
            messageIA = messageIA + xCorrection
    else:
        if (xCoord > 250):
            align = "left"
            xCorrection = ""
            for x in range(round((xCoord - 250) / taille)):
                xCorrection = xCorrection + " "
            messageIA = messageIA + xCorrection
        else:
            align = "right"
            xCorrection = ""
            for x in range(round((250 - xCoord) / taille)):
                xCorrection = xCorrection + " "
            messageIA = xCorrection + messageIA

    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(310 - yCoord) #hauteur 'taille 20
        writer.color("black")
        writer.write(messageIA, align=align, font=(police, taille, effet))
        #writer.back(taille * 1.5) #changement de ligne

        color("white")
        writer.write(messageIA, align=align, font=(police, taille, effet))
        
    except Terminator:
        pass  # turtledemo user pressed STOP

def warp():
            global corrige1, corrige2, corrige3,corrige4,corrige5,corrige6,_distance, _durée, _warp, _warp, _simlt, desDist, lumière, degré, durée, desPres, com2, periode, présent, heur_pres, destination, distance, t1, t2, t3, t4, t5, t6, com
            print("Voulez-vous calculez la distance? [Oui/Non]")
            com2 = input(">")
            if (com2.upper() == "OUI"):
                periode = 365.25
                sdj = 86400
                sdh = 3600
                
                présent = round((float(annee(t)) * periode) + ((t.month - 1) * (periode / 12)) + t.day)
                heur_pres = float((t.hour * 3600) + (t.minute * 60) + t.second)
                destination = round((float(com[0:4]) * periode) + ((int(com[4:6])-1) * (periode / 12)) + int(com[6:8]))
                heur_des = float((int(com[8:10]) * 3600) + (int(com[10:12]) * 60) + int(com[12:14]))
                if (destination > présent):
                    distance = présent - destination
                    distance2 = heur_pres - heur_des
                else:
                    distance = destination - présent
                    distance2 = heur_des - heur_pres
                    
                #Passe d'une variable a une chène format date
                t1 = round(float(présent / periode))
                t2 = round(((float(présent / periode) - round(présent / periode)) * 12) + 1)
                t3 = round(((((float(présent / periode) - round(présent / periode)) * 12) + 1) - round(((float(présent / periode) - round(présent / periode)) * 12) + 1)) * (periode / 12))
                t4 = round(float(distance2 / 3600))
                t5 = round((float(distance2 / 3600) - round(float(distance2 / 3600))) * 60)
                t6 = round((((float(distance2 / 3600) - round(float(distance2 / 3600))) * 60) - round((float(distance2 / 3600) - round(float(distance2 / 3600))) * 60)) * 60)
                desPres = str(abs(t1)) + "-" + str(abs(t2)) + "-" + str(abs(t3)) + "/" + str(abs(t4)) + ":" + str(abs(t5)) + ":" + str(abs(t6))

                t1 = round(destination/periode)
                t2 = round((float(destination / periode) - round(destination / periode)) * 12)
                t3 = round((((float(destination / periode) - round(destination / periode)) * 12) - round((float(destination / 365.26) - round(destination / periode)) * 12)) * (periode / 12))
                t4 = round(float(heur_des / 3600))
                t5 = round((float(heur_des / 3600) - round(float(heur_des / 3600))) * 60)
                t6 = round((((float(heur_des / 3600) - round(float(heur_des / 3600))) * 60) - round((float(heur_des / 3600) - round(float(heur_des / 3600))) * 60)) * 60)
                desDate = str(abs(t1)) + "-" + str(abs(t2)) + "-" + str(abs(t3)) + str(abs(t4)) + str(abs(t5)) + str(abs(t6))

                t1 = round(distance / periode)
                t2 = round((float(distance / periode) - round(distance / periode)) * 12)
                if (t2 > 12):
                    t1 = t1 - 1
                    t2 = 12 - t2
                #else:
                    #t2 = 12 + t2
                t3 = round((((float(distance / periode) - round(distance / periode)) * 12) - round((float(distance / periode) - round(distance / periode)) * 12)) * (periode / 12))
                if (t3 < 0):
                    t3 = round(periode / 12) + t3
                if (t3 > (periode / 12)):
                    t3 = round(periode / 12) - t3
                #heurs
                t4 = round(distance2 / sdh)
                t5 = round((float(distance2 / sdh) - round(distance2 / sdh)) * 60)
                if (t5 > 60):
                    t4 = t4 - 1
                    t5 = 60 - t5
                #else:
                    #t2 = 12 + t2
                t6 = round((((float(distance2 / sdh) - round(distance2 / sdh)) * 60) - round((float(distance2 / sdj) - round(distance2 / sdh)) * 60)) * 60)
                if (t6 < 0):
                    t6 = 60 + t3
                if (t6 > 60):
                    t6 = 60 - t3
                desDist = str(abs(t1)) + " ans " + str(abs(t2)) + " mois " + str(abs(t3))+" jour(s)" + str(abs(t4)) + ":" + str(abs(t5)) + ":" + str(abs(t6))

                if (destination < présent):
                    print("Passé", desDist)
                else:
                    print("Futur", desDist)
                print("Etes-vous pres pour le saut dans le Temps?")
                print("Confirmé? [Oui/Non]")
                com2 = input(">")
                if (com2.upper() == "OUI"):
                    print("Verrifiez Date Présent",str(t.hour)+":"+str(t.minute)+":"+str(t.second)+"/"+date(t))
                    print("Confirmé? [Oui/Non]")
                    com2 = input(">")
                    if (com2.upper() == "NON"):
                        gdh = input("[aaaammjj/hhmmss]=")
                    #print("Vous devez également décidé d'une durée de voyage. Ce qui vous donnera une idée de la vitesse a atteindre pour vous déplacé dans le temps.")

                    lumière = 299792458 #km/s
                    degré = (lumière / 90) #3331027.3111111

                    durée = "" #durée = input("Durée voyage:[hhmmss]")
                    if (durée == ""):
                        durée = "010000"
                    vit = 0 #Test vitesse instantané
                    temoin = datetime.today().second
                    if (temoin == datetime.today().second):
                        vit = vit + 1
                    #estimé = (distance / periode) #Dans le compilateur
                    estimé = (distance / vit) #Dans situation reel 42 seconde faire 2018 ans en run normal, 47.7 ans /sec x4 ??
                    t4 = round(float(estimé / 3600))
                    t5 = round((float(estimé / 3600) - round(float(estimé / 3600))) * 60)
                    t6 = round((((float(estimé / 3600) - round(float(estimé / 3600))) * 60) - round((float(estimé / 3600) - round(float(estimé / 3600))) * 60)) * 60)
                    _estimé = str(abs(t4)) + ":" + str(abs(t5)) + ":" + str(abs(t6))
                    print("")
                    print("Durée du voyage basé: ",round((vit / 3600),1),"heurs/sec.",_estimé)
                    print("Calcule quantique en coure...")
                    _distance = distance #float((int(distance[0:2]) * 3600) + (int(distance[3:4]) * 60) + int(distance[5:6]))
                    _durée = float( (int(durée[0:2]) * 3600) + (int(durée[3:4]) * 60) + int(durée[5:6]) )
                    warp = float(abs(_distance) * 86400) / _durée
                    _warp = (cmath.cos(1 / warp))
                    _simlt = (cmath.sin(1 / warp))

                    if (destination < présent):
                        print(200-(_warp.real) * 100, "% vitesse de la lumière")
                        print((2 * lumière)-(_warp.real * lumière),"km/s")
                        print("Ich! Votre corp va se désintégré et se changé en onde radio a cette vitesse!")
                    else:
                        print((_warp.real) * 100, "% vitesse de la lumière")
                        print((_warp.real * lumière),"km/s")
                        print("Pas grande chance de survie sur une si courte période d'accélération!")
                    print("Paradox Simultanéité:", _simlt.real)

                    #print(annee(t),(t.month - 0), t.day)
                    com2 = input("Go")
                    #time_warp()
                    présent = round((float(annee(t)) * periode) + ((t.month - 0) * (periode / 12)) + t.day)
                    heur_pres = float((t.hour * 3600) + (t.minute * 60) + t.second)
                    destination = round((float(com[0:4]) * periode) + ((int(com[4:6])-0) * (periode / 12)) + int(com[6:8]))
                    if (destination <= présent):
                        distance = présent - destination
                    else:
                        distance = destination - présent

                    #print(distance)
                    corrige1 = 0
                    corrige2 = 0
                    corrige3 = 0
                    corrige4 = 0
                    corrige5 = 0
                    corrige6 = 0
                    for voyage in range(abs(distance)):
                        #print(voyage)
                        if (destination > présent):
                            présent = présent + 1
                            heur_pres = heur_pres + 1
                            #Passe d'une variable a une chène format date
                            t1 = round(float(présent / periode))
                            t2 = round(((float(présent / periode) - round(présent / periode)) * 12))
                            if (t2 <= 0):
                                corrige2 = 12
                            else:
                                corrige2 = 0
                            t3 = round(((((float(présent / periode) - round(présent / periode)) * 12) - 6) - round(((float(présent / periode) - round(présent / periode)) * 12) - 6)) * (periode / 12) - 15)
                            if (t3 <= 0):
                                corrige3 = 31
                                if (t2 > 0):
                                    corrige2 = -1
                            t4 = round(float(heur_pres / 3600))
                            t5 = round((float(heur_pres / 3600) - round(float(heur_pres / 3600))) * 60)
                            t6 = round((((float(heur_pres / 3600) - round(float(heur_pres / 3600))) * 60) - round((float(heur_pres / 3600) - round(float(heur_pres / 3600))) * 60)) * 60)
                            if (t2 + corrige2 == 0):
                                t2 = 1
                                corrige1 = 1
                                corrige2 = 0
                            desPres = str((t1 + corrige1)) + "-" + str(t2 + corrige2) + "-" + str(t3 + corrige3) + "/" + str(abs(t4 + corrige4)) + ":" + str(abs(t5 + corrige5)) + ":" + str(abs(t6 + corrige6))
                        else:
                            présent = présent - 1
                            heur_pres = heur_pres - 1
                            #Passe d'une variable a une chène format date
                            t1 = round(float(présent / periode))
                            t2 = round(((float(présent / periode) - round(présent / periode)) * 12))
                            if (t2 <= 0):
                                corrige2 = 12
                            else:
                                corrige2 = 0
                            t3 = round(((((float(présent / periode) - round(présent / periode)) * 12)) - round(((float(présent / periode) - round(présent / periode)) * 12))) * (periode / 12))
                            if (t3 <= 0):
                                corrige3 = 31
                                if (t2 > 0):
                                    corrige2 = -1
                            else:
                                corrige3 = 0
                            if (t2 + corrige2 == 0):
                                t2 = 12
                                corrige2 = 0
                            t4 = round(float(heur_pres / 3600))
                            if (t4 < 0):
                                heur_pres = heur_des
                            t5 = round((float(heur_pres / 3600) - round(float(heur_pres / 3600))) * 60)
                            if (t5 <= 0):
                                corrige5 = 59
                            else:
                                corrige5 = 0
                            t6 = round((((float(heur_pres / 3600) - round(float(heur_pres / 3600))) * 60) - round((float(heur_pres / 3600) - round(float(heur_pres / 3600))) * 60)) * 60)
                            if (t6 <= 0):
                                corrige6 = 59
                                if (t5 > 0):
                                    corrige5 = -1
                            else:
                                corrige6 = 0
                            if (t6 + corrige6 == 0):
                                t6 = 59
                                corrige6 = 0
                            desPres = str(t1 + corrige1) + "-" + str(t2 + corrige2) + "-" + str(t3 + corrige3) + "/" + str(t4 + corrige4) + ":" + str(t5 + corrige5) + ":" + str(t6 + corrige6)
                        print(desPres)
                        #messageIA = desPres
                        #window()
            com2 = ""        
            com = ""
            
def time_warp():
    global writer, CALENDRIER, distance, messageIA, align, taille, police, effet , xCoord, yCoord, xCorrection
    messageIA = "Boucle Temporelle"
    align = "center"
    taille = 20
    police = "Courier"
    effet = "bold"
    xCoord = 0  #Max 715 'taille 20
    yCoord = 0  #Max 647 'taille 20
    window()
    writer.back(20)
    for CALENDRIER in range(distance):
        messageIA = str(CALENDRIER)
    align = "center_"
    taille = 20
    police = "Courier"
    effet = "bold"
    xCoord = 0
    yCoord = 0 
    window()
    return ""
    
def Analyse_langue():
    #Split d'une chaine
    global Analyse, langue, recherche, source, sourcefile, mos, mot, trouver, x, info, boucle
    while(boucle):
        Analyse = []
        langue = []
        ma_chaine = input("> ?") #Entrer la phrase a analyser
        if (ma_chaine == ""):
            ma_chaine = "Par exemple: Une phrase est ajouté automatiquement, quand il n'y a rien."
            info = 1
        #if (info == 1):
            #print("info On")
        #else:
            #print("info Off")
        for x in range(len(ma_chaine)): #retourne ma chaine sans les caractères accsentué et ponctuation.
            if (ma_chaine[x] == "à" or ma_chaine[x] == "â" or ma_chaine[x] == "ä"):
                ma_chaine = ma_chaine[:x] + "a" + ma_chaine[x+1:]
            if (ma_chaine[x] == "é" or ma_chaine[x] == "è" or ma_chaine[x] == "ê" or ma_chaine[x] == "ë"):
                ma_chaine = ma_chaine[:x] + "e" + ma_chaine[x+1:]
            if (ma_chaine[x] == "î" or ma_chaine[x] == "ì" or ma_chaine[x] == "ï"):
                ma_chaine = ma_chaine[:x] + "i" + ma_chaine[x+1:]
            if (ma_chaine[x] == "ô" or ma_chaine[x] == "ò" or ma_chaine[x] == "ö"):
                ma_chaine = ma_chaine[:x] + "o" + ma_chaine[x+1:]
            if (ma_chaine[x] == "ù" or ma_chaine[x] == "û" or ma_chaine[x] == "ü"):
                ma_chaine = ma_chaine[:x] + "u" + ma_chaine[x+1:]
            if (ma_chaine[x] == "ç"):
                ma_chaine = ma_chaine[:x] + "c" + ma_chaine[x+1:]

        if (info == 1):
            print(ma_chaine)
        chaine = ma_chaine.split("'")   #retir tout les '
        ma_chaine = " ".join(chaine)
        chaine = ma_chaine.split(" ")   #retir tout les espaces
        mot = len(chaine)

        for x in range(mot):
            #print(chaine[x], chaine[x] in chaine)
            Mot = chaine[x]
            if (Mot.isdigit()):
                #print("Nombre détecté.")
                Analyse.append("Nombre")
            else:
                #print("Mot détercté.")
                Analyse.append("Mot")
                if (Mot[0] == Mot[0].upper()):
                    #print("Majuscule détectée")
                    Analyse.append("Majuscule")
                    if (x == 0):
                        #print("Début de phrase.")
                        Analyse.append("Début phrase")
                    else:
                        #print("Nom.")
                        Analyse.append("Nom")
                if (Mot[-1] == "."):
                    if (x == (mot - 1)):
                        #print("Fin de phrase.")
                        Analyse.append("Fin phrase")
                    else:
                        #print("Point détecté.")
                        Analyse.append("Point")
                if (ma_chaine[-1] == "!"):
                    Analyse.append("Phrase exclamative")
                if (ma_chaine[-1] == "?"):
                    Analyse.append("Phrase intérogative")
                #if (Mot[-1] == ","):
                    #print("Virgule détecté")
                    #Analyse.append("Virgule")
                if (len(Mot) >= 3 and Mot[:] == Mot[::-1]):
                    #print("Palindrôme détecté.")
                    Analyse.append("Palindrome")
                if (Mot[1:2] == "'"):   #l'?
                    Mot = Mot[2:]
                if (Mot[2:3] == "'"):   #qu'?
                    Mot = Mot[3:]
                if (Mot[-1] == "." or Mot[-1] == "," or Mot[-1] == ";" or Mot[-1] == ":" or Mot[-1] == "!" or Mot[-1] == "?"):    #?.
                    Mot = Mot[:-1]

            #Recherche dans 5 dictionnaire de langues
            recherche = 1
            source = 0
            while recherche == 1:
                if (source == 0):
                    sourcefile = "francais.txt"
                file = open(sourcefile.upper(), "r")
                for line in file:
                    mos = mos + 1
                    if (line[0:-1].upper() == Mot.upper()):
                        #print(line[0:-1],"trouver dans", sourcefile[:-4])
                        langue.append(sourcefile[:-4])
                        trouver = trouver + 1
                #if (recherche == 1):
                    #print("dictionaire",sourcefile[:-4], "terminer")
                source = source + 1
                mos = 0
                if (source == 1):
                    sourcefile = "anglais.txt"  #en majuscule
                if (source == 2):
                    sourcefile = "spanish.txt"
                if (source == 3):
                    sourcefile = "italian.txt"
                if (source == 4):
                    sourcefile = "german.txt"
                if (source == 5):               #print("Fin de la recherche linguistique.")
                    if (trouver > 0):
                        if (info == 1):
                            print(trouver, "'"+Mot+"'", "trouver.")
                        else:
                            print("'"+Mot+"'", "non trouver.")
                    trouver = 0
                    recherche = 0

        if (info == 1):
            print("")
            print(len(ma_chaine), "caractères")
            if (mot > len(Analyse)):
                print(mot, "élements.")
            if ("Mot" in Analyse):
                print(Analyse.count("Mot"), "Mots")
            if ("Nombre" in Analyse):
                print(Analyse.count("Nombre"), "Nombres")
            if ("Palindrome" in Analyse):
                print(Analyse.count("Palindrome"), "Palindromes")
            if (("Début phrase" in Analyse) and ("Fin phrase" in Analyse)):
                print("Phrase bien construite. Début et fin présente.")
            if (Analyse.count("Majuscule") == Analyse.count("Point")):
                print(Analyse.count("Point"), "phrase détecté dans la ligne")
            if ("Nom" in Analyse):
                print(Analyse.count("Nom"), "Noms")
            if ("Virgule" in Analyse):
                print(Analyse.count("Virgule"), "virgules dans la phrase.")
            if ("Phrase intérogative" in Analyse):
                print(Analyse.count("Phrase intérogative"), "phrase intérogative détecté.")
            if ("Phrase explamative" in Analyse):
                print(Analyse.count("Phrase exclamative"), "phrase explamative détecté.")
            if (info == 2):
                print(chaine)
                print("langue repéré:", langue)
        detecter = ""
        if ((langue.count("francais") > langue.count("anglais")) and (langue.count("francais") > langue.count("spanish")) and (langue.count("francais") > langue.count("italian")) and (langue.count("francais") > langue.count("german"))):
            detecter = "Francais"
        if ((langue.count("anglais") > langue.count("francais")) and (langue.count("anglais") > langue.count("spanish")) and (langue.count("anglais") > langue.count("italian")) and (langue.count("anglais") > langue.count("german"))):
            detecter = "Anglais"
        if ((langue.count("spanish") > langue.count("anglais")) and (langue.count("spanish") > langue.count("francais")) and (langue.count("spanish") > langue.count("italian")) and (langue.count("spanish") > langue.count("german"))):
            detecter = "Spanish"
        if ((langue.count("italian") > langue.count("anglais")) and (langue.count("italian") > langue.count("spanish")) and (langue.count("italian") > langue.count("francais")) and (langue.count("italian") > langue.count("german"))):
            detecter = "Italian"
        if ((langue.count("german") > langue.count("anglais")) and (langue.count("german") > langue.count("spanish")) and (langue.count("german") > langue.count("italian")) and (langue.count("german") > langue.count("francais"))):
            detecter = "German"
        if (detecter):
            if (detecter == "francais"):
                print("Vous êtes:", detecter)
            if (detecter == "anglais"):
                print("You are:", detecter)
            if (detecter == "spanish"):
                print("Yoso abla Espagnal:", detecter)
            if (detecter == "italian"):
                print(":", detecter)
            if (detecter == "german"):
                print(":", detecter)
                
        else:
            print("State: dictionnaire")
            print(langue.count("francais"), "francais")
            print(langue.count("anglais"), "anglais")
            print(langue.count("spanish"), "spanish")
            print(langue.count("italian"), "italian")
            print(langue.count("german"), "german")
        if (info == 1):
            print("State: dictionnaire")
            print(langue.count("francais"), "francais")
            print(langue.count("anglais"), "anglais")
            print(langue.count("spanish"), "spanish")
            print(langue.count("italian"), "italian")
            print(langue.count("german"), "german")

def jour(t):
    global jour
    jour = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    return jour[t.weekday()]

def date(t):
    global a, m ,j, mois
    mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "June", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    a = t.year
    m = mois[t.month - 1]
    j = t.day
    return "%d %s %d" % (t.day, mois[t.month - 1], t.year)

def mois(t):
    global mois, m
    mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "June", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    m = mois[t.month - 1]
    return "%s" % (m)

def annee(t):
    global a
    a = t.year
    return "%d" % (a)

def heure(t):
    global hh, mm, ss, cc
    hh = t.hour
    mm = t.minute
    ss = t.second
    cc = t.microsecond
    return "%d:%d:%d" % (t.hour, t.minute, t.second)

horraire = ""
lundi = [0, "Dormir", 5, "Reveille", 6, "Production", 8, "Sortie stock", 11, "Dinner", 12, "Declaration fin de journée", 13, "Retour stock", 14, "Sortir chien", 16, "Souper", 17, "Activité libre", 21, "Dormir"]
mardi = {0: "Dormir", 5: "Reveille", 6: "Production", 8: "Sortie stock", 11: "Dinner", 12: "Declaration fin de journée", 13: "Retour stock", 14: "Sortir chien", 16: "Souper", 17: "Activité libre", 21: "Dormir"}
mercredi = {0: "Dormir", 5: "Reveille", 6: "Production", 8: "Sortie stock", 11: "Dinner", 12: "Declaration fin de journée", 13: "Retour stock", 14: "Sortir chien", 16: "Souper", 17: "Activité libre", 21: "Dormir"}
jeudi = {0: "Dormir", 5: "Reveille", 6: "Production", 8: "Sortie stock", 11: "Dinner", 12: "Declaration fin de journée", 13: "Retour stock", 14: "Sortir chien", 16: "Souper", 17: "Activité libre", 21: "Dormir"}
vendredi = {0: "Dormir", 5: "Reveille", 6: "Production", 8: "Sortie stock", 11: "Dinner", 12: "Declaration fin de journée", 13: "Retour stock", 14: "Sortir chien", 16: "Souper", 17: "Activité libre", 21: "Dormir"}
samedi = {0: "Dormir", 8: "Reveille", 9: "déjeuné", 12: "Dinner", 14: "Sortir chien", 16: "Souper", 17: "Activité libre", 23: "Dormir"}
dimanche = {0: "Dormir", 8: "Reveille", 9: "déjeuné", 12: "Dinner", 14: "Sortir chien", 16: "Souper", 17: "Activité libre", 23: "Dormir"}

Name = Prix = Age = Quantite = Objet = List = A = B = O = sinonime = ""
feel = 0

IA = 1
while (IA == 1):
    A = ""
    B = ""
    O = ""
    reponse = 0
    com = input(">")
    t = datetime.today()
    if (com.upper() == ""):
        print("")
                
    #greating
    for greet in ["HI", "SALUT", "BONJOUR", "ALLO", "HELLO", "OLA"]:
        if (com.upper() == greet):
            reponse = 1
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
    if (com.upper() == "QUI EST TU?"):
        print("Je suis IA 1.0")
        reponse = 1
    if (com.upper() == "CA VA?"):
        reponse = 1
        if (feel == 1):
            print("Oui. Je fonctionne bien")
        else:
            print("Je ne ressent pas d'émotion. Et vous comment aller vous?")
            feel = 1
    for question in ["JE CHERCHE L'AIDE?", "COMMENT CA MARCHE?", "DÉBUTONS", "COMMANSONS", "A L'AIDE", "AIDE MOI"]:
        if (com.upper() == question):
            reponse = 1
            print("Si vous cherchez les différante commandes, taper la Commande [aide]")

    #Game
    #(pile,face)
    for game in ["PILE", "FACE"]:
        if (com.count(" ") > 0):
            for ii in range(0, com.count(" ")):
                for i in range(0, 1 + abs(len(com[ii].split(" ")) - len(game))):
                    if (com[i:i + len(game)].upper() == game):
                        reponse = 1
                        #choisi une reponce au hazard
                        ran = random.randint(1, 2)
                        if (ran == 1):
                            print("Pile")
                        if (ran == 2):
                            print("Face")
                        if ((game == "PILE" and ran == 1) or (game == "FACE" and ran == 2)):
                            print("Tu a gagné :(")
                            Win = 1
                            print("Vous recevez", Win, "Xp")
                            Xp = Xp + Win
                        if ((game == "PILE" and ran == 2) or (game == "FACE" and ran == 1)):
                            print("J'ai gagné :)")
                        game = "_"
        else: #celui-ci bug moins
            for i in range(0, len(com)):
                if (com[i:i + len(game)].upper() == game):
                    reponse = 1
                    #choisi une reponce au hazard
                    ran = random.randint(1, 2)
                    if (ran == 1):
                        print("Pile")
                    if (ran == 2):
                        print("Face")
                    if ((game == "PILE" and ran == 1) or (game == "FACE" and ran == 2)):
                        print("Tu a gagné :(")
                        Win = 1
                        print("Vous recevez", Win, "Xp")
                        Xp = Xp + Win
                    if ((game == "PILE" and ran == 2) or (game == "FACE" and ran == 1)):
                        print("J'ai gagné :)")
                    game = "_"
                    
    #(roche, papier, sciseau)
    for game in ["ROCHE", "PAPIER", "CISEAU"]:
        for ii in range(0, 1 + com.count(" ")):
            for i in range(0, 1 + abs(len(com[ii].split(" ")) - len(game))):
                if (com[i:i + len(game)].upper() == game):
                    reponse = 1
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
                        Win = 3
                        print("Vous recevez", Win, "Xp")
                        Xp = Xp + Win
                    game = "_"
    #Tic-Tac-Toc
    if (com.upper() == "MORPION" or com.upper() == "TIC-TAC-TOT" or com.upper() == "2D"):
        Morpion2d()
        reponse = 1
    #TASSERACT (Tic-Tac-Toc 3D)
    if (com.upper() == "MORPION3D" or com.upper() == "TASSERACT" or com.upper() == "3D"):
        Morpion3D()
        reponse = 1
    #Aventure RPG
    if (com.upper() == "AVENTURE" or com.upper() == "HISTOIRE" or com.upper() == "RPG"):
        reponse = 1
        print("J'ai quelque histoires en chantier qui pourait vous plaire.")
        exec(open("E:\PERSONNEL\python_2\python\histoires\Assembler.py").read())
        #On ne peux pas ouvrir un assembler dans un sous repertoir...
        break
    #Temple 2D
    if (com.upper() == "TEMPLE" or com.upper() == "DONGEON" or com.upper() == "LABYRINTHE"):
        reponse = 1
        exec(open("E:\PERSONNEL\python_2\python\histoires\Temple\Temple.py").read())
        break
    #Temple 3D
    if (com.upper() == "TEMPLE3D" or com.upper() == "DONGEON3D" or com.upper() == "LABYRINTHE3D"):
        reponse = 1
        exec(open("E:\PERSONNEL\python_2\python\histoires\Temple\TempleIso.py").read())
        break
    #Editeur Fichier
    if (com.upper() == "EDIT" or com.upper() == "EDITER" or com.upper() == "JOJ"):
        reponse = 1
        exec(open("E:\PERSONNEL\python_2\python\histoires\Jeux-Espion\editeur.py").read())
        break
    #Ligne de Commande Avence
    if (com.upper() == "CMD" or com.upper() == "DOS" or com.upper() == "PIP"):
        reponse = 1
        exec(open("E:\PERSONNEL\python_2\python\dos.py").read())
        break
        
    #style scane
    for scane in ["?", "QUI EST TU?", "QUI ÊTES-VOUS?", "VOUS-ÊTES QUI?", "TU-EST QUI?","VOUS-ÊTES?", "TU-EST?", "ZIA?", "IA?", "Z?", "ZI1?","ZIA1.1?","ZIA1?","1?","1.1?",".1?","ZI?", "A QUI JE PARLE?", "JE PARLE A QUI?","A QUI AI-JE L'HONEUR?", "QUI AI-JE L'HONEUR?", "QUI J'AI L'HONEUR?"]:
        if (com.upper() == scane):
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
            com = ""
            reponse = 1
    if (com.upper() == "QUEL EST LA RÉPONSE À LA GRANDE QUESTION?" or com.upper() == "LA RÉPONSE À LA GRANDE QUESTION?" or com.upper() == "LA RÉPONSE À LA QUESTION?" or com.upper() == "QUEL EST LA RÉPONSE?"):
        print("La réponse c'est #42")
        com = ""
        reponse = 1
    if (com.upper() == "CA VA?"):
        reponse = 1
        if (feel == 1):
            print("Oui. Je fonctionne bien")
        else:
            print("Je ne ressent pas d'émotion. Et vous comment aller vous?")
            feel = 1
        com = ""
    for question in ["JE CHERCHE L'AIDE?", "COMMENT CA MARCHE?", "DÉBUTONS", "COMMANSONS", "A L'AIDE", "AIDE MOI"]:
        if (com.upper() == question):
            reponse = 1
            print("Si vous cherchez les différante commandes, taper la Commande [aide]")
            com = ""

    #Mot clé
    for scane in ["RAN", "RANDOM", "RANDOMIZE", "HAZARD", "UN CHIFFRE", "1d10", "1 a 10", "UN A DIX", "10?", "RAN?", "HAZARD?", "RANDOMIZE?", "UN CHIFFRE ?", "1d10 ?", "1 a 10 ?", "UN A DIX ?", "10 ?", "RAN ?", "HAZARD ?", "RANDOMIZE ?" ]:
        if (com.upper() == scane):
            ran = random.randint(1, 10)
            print(ran)
            reponse = 1
            com = ""
    for scane in ["c'est tu sensé faire ca?","c'est tu sensé faire ca","c'est normal si","c'est normal que","c'est tu normal que","c'est tu normal si?", "est-ce que c'est normal", "est-ce que c'est normal?", "est-ce normal si?","est-ce normal?", "est-ce normal si","est-ce normal"]:
        if (com.lower() == scane):
            print("Non.")
            reponse = 1
            com = ""
    for scane in ["est-ce que je devrais?", "est-ce que je devrais","est-ce que je peux?", "puis-je faire ca","est ce que je peux","puis-je faire ca?", "puis-je faire cela?", "est-ce possible de", "je peux faire ca?", "je devrais faier ca?"]:
        if (com.lower() == scane):
            print("Oui.")
            reponse = 1
            com = ""
    for scane in ["TU VEUX FAIRE UNE PARTIE?", "TU VEUX JOUER AVEC MOI?", "ON JOUE A UN JEUX?", "TU VEUX JOUER?", "ON FAIT UNE PARTIE?", "ON JOUE?", "GAME?", "UNE PARTIE?", "UN JEUX?", "JEUX?"]:
        if (com.upper() == scane):
            reponse = 1
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
            print("J'ai Pile/Face, Roche/Papier/Ciseau, Devine nombre, Morpion, Aventure, Temple.")
            com = ""
    for scane in ["fonction?","rôle?","utilité?","possibilité?","vous pouvez faire quoi?", "quel sont vos capacitées?","votre fonction?","vos possibilitées?","vous faite quoi?","votre capacitées?","votre rôle?","vous servez a quoi?","tu sert a quoi?","tu peux faire quoi?", "quel sont tes capacitées?","ta fonction?","tes possibilitées?","tu fait quoi?","tes capacitées?","ton rôle?"]:
        if (com.lower() == scane):
            reponse = 1
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
            com = ""
    for scane in ["bye","bye bye","aurevoir","a+","je quite","a la prochaine","je m'en vais","j'y vais","adieux"]:
        if (com.lower() == scane):
            reponse = 1
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
            com = ""
    for scane in ["corect","super","génial","nice","alors?","et puis?","alors","et puis","ah bon","ah","oh","bon","ah bon?","ah?","oh?","c'est bon","ok","oui","non","..."," ","ensuite?","et?","puis?", "puis","..","et alors","et alors?","non?", "oui?", "ok?", "ok!","k","ensuite","et"]:
        if (com.lower() == scane):
            reponse = 1
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
            com = ""

    #Autre Outil
    if (com[0:7].upper() == "ANALYSE LANGUE" or com[0:7].upper() == "LANGUE?" or com[0:7].upper() == "ANALYSE?"):
        Analyse_langue()
        reponse = 1
    if (com.upper() == "XP?"):
        print("Xp:",Xp)
        reponse = 1
    if (com.upper() == "REPONSE?"):
        print("Reponse:",Rep)
        reponse = 1
    #Jeux Devine le nombre
    for scane in ["COMMENT MARCHE DEVINER UN NOMBRE?","COMMENT MARCHE DEVINER UN NOMBRE","DEVINER UN NOMBRE?","FAIRE DEVINER UN NOMBRE?","DEVINER UN NOMBRE","FAIRE DEVINER UN NOMBRE"]:
        if (com.upper() == scane):
            reponse = 1
            print("TAPER 'devine?' OU 'devine='")
            print("Si vous commencez une partie vous devez la finir en 10 coups, ou taper 'quiter'.")
    if (com[0:7].upper() == "DEVINE?"):
        reponse = 1
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
                Win = 100 + tour
                print("Vous recevez", Win, "Xp")
                Xp = Xp + Win #100 point/Victoir +1 point par tentative
                tour = game = 0
                nombre = random.randint(1, 999)
            if (tour == 10):
                print("10 Tour passer. Tu a perdus :(")
                print("le nombre était", nombreX, "bye bye")
                game = tour = nombreX = 0
                com = ""
        com = ""
    if (com[0:7].upper() == "DEVINE="):
        print("Devine le nombre >I.A")
        game = 1
        reponse = 1
        if com[7:-1].isdigit():
            nombreX = abs(int(com[7:]))
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
        com = ""
        
    #interaction Man/IA
    for sinonime in ["JEUX", "PARTIE", "QUEL JEUX", "QUEL PARTIE", "JEUX DISPONIBLE", "LES JEUX DISPONIBLE", "JOUER UN JEUX", "FAIRE UNE PARTIE"]:
        for ii in range(0, com.count(" ")):
            for i in range(0, 1 + abs(len(com[ii].split(" ")) - len(sinonime))):
                if (com[i:i + len(sinonime)].upper() == sinonime):
                    reponse = 1
                    print("Il y a Roche/Papier/Ciseau, Pile/Face, Devine, Morpion, Tasseract.")
                    print("Je peux créer des RPG text/choix en entrant aventure.")
                    sinonime = "_"
    #horlogue
    if (com.upper() == "JOUR?"):
        print(jour(t))
        reponse = 1
    if (com.upper() == "LE JOUR?"):
        print(t.weekday())
        reponse = 1
    if (com.upper() == "DATE?"):
        print("Nous somme",date(t))
        reponse = 1
    if (com.upper() == "QUEL DATE?"):
        print(date(t))
        reponse = 1
    if (com.upper() == "QUEL HEURE?"):
        print("Il est",heure(t))
        reponse = 1
    if (com.upper() == "MOIS?"):
        print(mois(t))
        reponse = 1
    if (com.upper() == "QUEL MOIS?"):
        print(t.month)
        reponse = 1
    if (com.upper() == "ANNEE?" or com.upper() == "ANNÉE?" or com.upper() == "ANS?"):
        print(annee(t))
        reponse = 1
    if (com.upper() == "HEURE?"):
        print(t.hour)
        reponse = 1
    if (com.upper() == "MINUTE?"):
        print(t.minute)
        reponse = 1
    if (com.upper() == "SECONDE?"):
        print(t.second)
        reponse = 1
    if (com.upper() == "QUEL JOUR?"):
        print(t.day)
        reponse = 1
    if (com.upper() == "AUJOURD'HUI?"):
        print(jour(t),date(t),heure(t))
        reponse = 1
    if (com.upper() == "TIME?"):
        print(heure(t))
        reponse = 1

    #horraire basic
    if (com.upper() == "QUEL HORRAIRE?"):
        print(horraire)
        reponse = 1
    if (com.upper() == "HORRAIRE?"):
        time_now = localtime()
        time = time_now.tm_hour
        reponse = 1
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
                break
    #memoriser list
    if (com.upper() == "NAME?"):
        reponse = 1
        if (Name):
            print(Name)
        else:
            print("Aucun name.")
    if (com.upper() == "NAME"):
        reponse = 1
        key = input(">? ")
        if (Name):
            Name = Name + ", '" + key + "'"
        else:
            Name = Name + "'" + key + "'"
    if (com.upper() == "PRIX?"):
        reponse = 1
        if (Prix):
            print(Prix)
        else:
            print("Aucun prix.")
    if (com.upper() == "PRIX"):
        reponse = 1
        key = input(">? ")
        #key = key + "$"
        if (Prix):
            Prix = Prix + ", '" + key + "'"
        else:
            Prix = Prix + "'" + key + "'"
    if (com.upper() == "AGE?"):
        reponse = 1
        if (Age):
            print(Age)
        else:
            print("Aucun age.")
    if (com.upper() == "AGE"):
        reponse = 1
        key = input(">? ")
        if (Age):
            Age = Age + ", '" + key + "'"
        else:
            Age = Age + "'" + key + "'"
    if (com.upper() == "QUANTITÉ?"):
        reponse = 1
        if (Quantite):
            print(Quantite)
        else:
            print("Aucune quantité.")
    if (com.upper() == "QUANTITÉ"):
        reponse = 1
        key = input(">? ")
        if (Quantite):
            Quantite = Quantite + ", '" + key + "'"
        else:
            Quantite = Quantite + "'" + key + "'"
    if (com.upper() == "OBJET?"):
        reponse = 1
        if (Objet):
            print(Objet)
        else:
            print("Aucun Objet.")
    if (com.upper() == "OBJET"):
        reponse = 1
        key = input(">? ")
        if (Objet):
            Objet = Objet + ", '" + key + "'"
        else:
            Objet = Objet + "'" + key + "'"
    if (com.upper() == "LISTE?"):
        reponse = 1
        if (List):
            print(List)
        else:
            print("Aucune liste.")
    if (com.upper() == "LISTE"):
        reponse = 1
        key = input(">? ")
        if (List):
            List = List + ", '" + key + "'"
        else:
            List = List + "'" + key + "'"
    if (com.upper() == "LUNDI?"):
        reponse = 1
        if (lundi):
            print(lundi)
        else:
            print("lundi vide.")
    if (com.upper() == "LUNDI"):
        reponse = 1
        key = input("heure:? ")
        key2 = input(">?")
        if (lundi):
            lundi.append(key)
            lundi.append(key2)
            #lundi.append(key+": "+key2)
            #lundi.append(key, ":", key2)
            #lundi = lundi + ", " + str(key) + ": " + key2 + " "
        else:
            lundi = lundi + str(key) + ": " + key2 + " "
    if (com.upper() == "MARDI?"):
        reponse = 1
        if (mardi):
            print(mardi)
        else:
            print("mardi vide.")
    if (com.upper() == "MARDI"):
        reponse = 1
        key = input("heure,?")
        key2 = input(">? ")
        if (mardi):
            mardi = mardi + ", " + str(key) + ": '" + key2 + "'"
        else:
            mardi = mardi + str(key) + ": '" + key2 + "'"
    if (com.upper() == "MERCREDI?"):
        reponse = 1
        if (mercredi):
            print(mercredi)
        else:
            print("mercredi vide.")
    if (com.upper() == "MERCREDI"):
        reponse = 1
        key = input("heure,?")
        key2 = input(">? ")
        if (mercredi):
            mercredi = mercredi + ", " + str(key) + ": '" + key2 + "'"
        else:
            mercredi = mercredi + str(key) + ": '" + key2 + "'"
    if (com.upper() == "JEUDI?"):
        reponse = 1
        if (jeudi):
            print(jeudi)
        else:
            print("jeudi vide.")
    if (com.upper() == "JEUDI"):
        reponse = 1
        key = input("heure,?")
        key2 = input(">? ")
        if (jeudi):
            jeudi = jeudi + ", " + str(key) + ": '" + key2 + "'"
        else:
            jeudi = jeudi + str(key) + ": '" + key2 + "'"
    if (com.upper() == "VENDREDI?"):
        reponse = 1
        if (vendredi):
            print(vendredi)
        else:
            print("vendredi vide.")
    if (com.upper() == "VENDREDI"):
        reponse = 1
        key = input("heure,?")
        key2 = input(">? ")
        if (vendredi):
            vendredi = vendredi + ", " + str(key) + ": '" + key2 + "'"
        else:
            vendredi = vendredi + str(key) + ": '" + key2 + "'"
    if (com.upper() == "SAMEDI?"):
        reponse = 1
        if (samedi):
            print(samedi)
        else:
            print("samedi vide.")
    if (com.upper() == "SAMEDI"):
        reponse = 1
        key = input("heure,?")
        key2 = input(">? ")
        if (samedi):
            samedi = samedi + ", " + str(key) + ": '" + key2 + "'"
        else:
            samedi = samedi + str(key) + ": '" + key2 + "'"
    if (com.upper() == "DIMANCHE?"):
        reponse = 1
        if (dimanche):
            print(dimanche)
        else:
            print("dimanche vide.")
    if (com.upper() == "DIMANCHE"):
        reponse = 1
        key = input("heure,?")
        key2 = input(">? ")
        if (dimanche):
            dimanche = dimanche + ", " + str(key) + ": '" + key2 + "'"
        else:
            dimanche = dimanche + str(key) + ": '" + key2 + "'"

    if (com.upper() == "QUIT" or com.upper() == "QUITTER" or com.upper() == "Q"):
        print("bye bye")
        IA = 0
        reponse = 1

    #Mathématique
    for x in range(len(com)):
        if (com[x] == "=" or com[x] == "+" or com[x] == "-" or com[x] == "*" or com[x] == "/" or com[x] == "%" ):
            if (com[x] == "="):
                reponse = 1
                A = int(A)
                B = int(B)
                #5 Opperation Mathematique        
                if (O == "+"):
                    print(A + B)
                    Rep = A + B
                if (O == "-"):
                    print(A - B)
                    Rep = A - B
                if (O == "*"):
                    print(A * B)
                    Rep = A * B
                if (O == "/"):
                    if (B == 0):
                        print("Infini!")
                        Rep = "Infini!"
                    else:
                        print(A / B)
                        Rep = A / B
                if (O == "%"):
                    print(A % B)
                    Rep = A % B
                #print(A)
                #print(O)
                #print(B)
            else:
                O = com[x]
        else:
            if (O == ""):
                A = A + com[x]
            else:
                B = B + com[x]
        
    if (com.upper() == "COMMANDE" or com.upper() == "AIDE" or com.upper() == "HELP"):
        reponse = 1
        print("Liste des commandes de base:")
        print("aujourd'hui?,horraire?,date?,time?,jour?,le jour?,salut,qui est tu?,lundi,lundi?,jour,quel jour?,heure?,minute?,seconde?,mois?,ans?")
        print("pile,face,roche,papier,ciseaux,Liste,Liste?,Name,Prix,Age,Quantite,Objet,mardi,mercredi,jeudi,vendredi,samedi,dimanche,+,-,*,/,%,=")
        print("Devine,Morpion,3D,Aventure,Dongeon,Quit,Salut,Edit,cmd")
        
    #Chercher jour a partir d'une date
    for scane in ["COMMENT CA MARCHE CHERCHER UNE DATE","COMMENT CA MARCHE CHERCHER UNE DATE?","COMMENT CA MARCHE CHERCHER UN JOUR","COMMENT CA MARCHE CHERCHER UN JOUR?","COMMENT CA MARCHE CHERCHER JOUR","COMMENT CA MARCHE CHERCHER JOUR?","COMMENT CHERCHER UNE DATE","COMMENT CHERCHER UNE DATE?","COMMENT CHERCHER UN JOUR","COMMENT CHERCHER UN JOUR?","COMMENT CHERCHER JOUR","COMMENT CHERCHER JOUR?"]:
        if (com.upper() == scane):
            reponse = 1
            print("TAPER DATE 'AAAAMMJJ?'")
    if (len(com) == 9 and com[8:9] == "?"):
        reponse = 1
        if (isinstance(int(com[0:8]), (int, float, complex))):
            _date = com[0:8]
            _année = int(_date[0:4])
            #print("année=",année)
            _mount = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
            _mois = int(_date[4:6])
            #print("mois=",mount[mois-1])
            _jour = int(_date[6:8])
            #print("jour=",jour)

            if (int(_date[4:6]) >= 3):
                j = round(((((23 * _mois) / 9) + _jour + 4 + _année + (_année / 4) - (_année / 100) + (_année / 400) - 2) % 7) - 1)
            else:
                j = round(((((23 * _mois) / 9) + _jour + 4 + _année + ((_année - 1) / 4) - ((_année - 1) / 100) + ((_année - 1) / 400)) % 7) - 1)

            #La réponse obtenue pour j correspond alors à un jour de la semaine suivant
            #0=dimanche,1=lundi,2=mardi,3=mercredi,4=jeudi,5=vendredi,6=samedi
                
            #print(j) #il y a un bug ma liste devrai commencé un dimanche et le jour de ma naissance un samedi
            semaine = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
            print("")
            print(semaine[j],_jour,_mount[_mois-1],_année)
            #print(j,jour,mount[mois-1],année)
            if (_année < 1583):
                print("Alert! Les dates grégorien on changé de format en 1583.")

    #Recherche plus Avencer SiFic
    if (len(com) == 15 and com[14:15] == "?"):
        reponse = 1
        if (isinstance(int(com[0:8]), (int, float, complex))):
            _date = com[0:8]
            _année = int(_date[0:4])
            #print("année=",année)
            _mount = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
            _mois = int(_date[4:6])
            #print("mois=",mount[mois-1])
            _jour = int(_date[6:8])
            #print("jour=",jour)

            if (int(_date[4:6]) >= 3):
                j = round(((((23 * _mois) / 9) + _jour + 4 + _année + (_année / 4) - (_année / 100) + (_année / 400) - 2) % 7) - 1)
            else:
                j = round(((((23 * _mois) / 9) + _jour + 4 + _année + ((_année - 1) / 4) - ((_année - 1) / 100) + ((_année - 1) / 400)) % 7) - 1)

            #La réponse obtenue pour j correspond alors à un jour de la semaine suivant
            #0=dimanche,1=lundi,2=mardi,3=mercredi,4=jeudi,5=vendredi,6=samedi
                
            #print(j) #il y a un bug ma liste devrai commencé un dimanche et le jour de ma naissance un samedi
            semaine = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
            print("")
            print(semaine[j],_jour,_mount[_mois-1],_année)
            #print(j,jour,mount[mois-1],année)
            if (_année < 1583):
                print("Alert! Les dates grégorien on changé de format en 1583.")
            warp()

    if (connaissance):
        for questioner in ["Vous avez appris quelque chose?", "Qu'a tu appris?", "Qu'a tu appris de neuf?", "Tu a appris quoi?", "Tu apprend quoi?", "Quoi de neuf?", "What append?", "Enything new?", "What's news?", "Nouvelle connaissance?", "Connaissance nouvelle?"]:
            if (key1.lower() == questionner):
                reponse = 1
                for i in range(connaissance):
                    if i == 0:
                        print("J'ai appris que", connaissance[i])
                    else:
                        print(connaissance[i])
    else:
        print("Rien de neuf.")

    if reponse == 0:
        print("Je ne comprend pas", com)
        new = input("Qu'est-ce que c'est?")
        connaissance.append(com+"="+new)
        
    if (com != ""):
        Analyse_langue
