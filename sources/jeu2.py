import pygame,sys  #module libre
import communication #module créé par notre groupe

argentTable=0
argentJ1 = 1000
argentJ2=1000
miseJoueur1=0
miseJoueur2=0
Joueur1EnJeu=True
Joueur2EnJeu=True




CarteAAfficher=[]
etatjeu=-1
nbSuivre =0

def decode_message2(msg):
    msg = msg[1:len(msg)]
    msg = msg[-len(msg):-1]
    msgdecode = []
    paranthese1 = 0
    paranthese2=0
    for i in range (len(msg)) :
        if msg[i] == '(' :
            paranthese1 = i
        elif msg[i] == ')' :
            paranthese2 = i
            if i == len(msg)-1:
                valeur = msg[paranthese1:]
            else:
                valeur = msg[paranthese1:paranthese2+1]
            valeur=decode_message3(valeur)
            msgdecode.append(valeur)

    return msgdecode

def decode_message3(msg):
    msg=msg[1:len(msg)]
    msg=msg[-len(msg):-1]
    valeur=""
    valeur2=""
    for i in range (len(msg)) :
        if msg[i] == "'" :
            if msg[i+1] in '1234567890' and msg[i+2] not in '1234567890':
                valeur=msg[i+1:i+2]
                k=i+3
            else:
                valeur=msg[i+1:i+3]
                k=i+4
            break
    for j in range(k,len(msg)):
        if msg[j] == "'":
            for l in range(j+1,len(msg)):
                if msg[l]== "'":
                    valeur2=msg[j+1:l]
                    break
            break
    return (valeur,valeur2)

def decode_message(msg):       #Pour les  2
    msg = msg[1:len(msg)]
    msg = msg[-len(msg):-1]
    msgdecode = []
    ancienRang=0
    for i in range(len(msg)):
        if msg[i] == ',':
            valeur = msg[ancienRang:i]
            ancienRang = i+2
            msgdecode.append(valeur)
        if i == len(msg)-1:
            valeur = msg[ancienRang:]
            msgdecode.append(valeur)
    return msgdecode

    #fonction pour le click d'un bouton

def clickposjeu(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        #bouton suivre/check
        if event.button == 1 and event.pos[0]>715 and event.pos[0]<815 and event.pos[1]>585 and event.pos[1]<635:
            return 1
        #bouton miser
        elif event.button == 1 and event.pos[0]>840 and event.pos[0]<940 and event.pos[1]>585 and event.pos[1]<635:
            return 2
        #bouton tapis
        elif event.button == 1 and event.pos[0]>965 and event.pos[0]<1065 and event.pos[1]>585 and event.pos[1]<635:
            return 3
        #bouton se retirer
        elif event.button == 1 and event.pos[0]>1090 and event.pos[0]<1190 and event.pos[1]>585 and event.pos[1]<635:
            return 4
    else:
        return -1



def ChargeCarte1(main,carteTable):
    CarteAffiche = []
    for carte in main:
        CarteAffiche.append('IMAGES/CARTES/' + carte[0] + "_" + carte[1] + '.png')

    for carte in carteTable:
        CarteAffiche.append('IMAGES/CARTES/' + carte[0] + "_" + carte[1] + '.png')

    carteChargee=[]
    for charger in CarteAffiche:
        carteChargee.append(pygame.image.load(charger).convert())
    return carteChargee

def miser(argentjoueur):
    miseNonFini=True
    font= pygame.font.Font(None, 50)
    textemise=font.render(" ",True,(0,0,0),None)
    fen.blit(textemise, (80, 940))
    mise=''
    while miseNonFini:
            textemise=font.render(mise,True,(0,0,0),None)
            fen.blit(miserInput,(20,800))
            for evenement in pygame.event.get():
                if evenement.type == pygame.KEYDOWN:
                    if evenement.unicode == '\b':
                        mise= mise[0:(len(mise)-1)]

                    elif evenement.unicode == '\r':
                        if int(mise) > argentjoueur:
                            mise = "Pas assez d'argent"
                            pygame.time.wait(5000)
                            mise = ''
                        else :
                            miseNonFini=False
                    else:
                        if evenement.unicode in '1234567890':
                            mise=mise + evenement.unicode
                if evenement.type == pygame.MOUSEBUTTONDOWN:
                    if evenement.button == 1 and evenement.pos[0]>185 and evenement.pos[0]<300 and evenement.pos[1]>995 and evenement.pos[1]<1020:
                        if int(mise) > argentjoueur:
                            mise = "Pas assez d'argent"
                            pygame.time.wait(5000)
                            mise = ''
                        else :
                            miseNonFini=False
            fen.blit(textemise, (80, 940))
            pygame.display.update()
    return int(mise)


pygame.init()
LarFEN=1920
HauFEN=1020
fen=pygame.display.set_mode((LarFEN,HauFEN))     #initialisation de la fenêtre à la largeur larFEN et à la HauFEN
pygame.display.set_caption("Poker Game")         #nom de la fenêtre que l'on affiche
table=pygame.image.load("IMAGES/TablePoker.png").convert()    #image de fond soit la table de jeu

miserInput=pygame.image.load("IMAGES\MiseTexte.png").convert()
joueur = pygame.image.load('IMAGES\joueur1.png')

#ici tout les textes à afficher en jeu
miserbouton=pygame.image.load("IMAGES\BOUTON\Miser.png").convert()
retirer=pygame.image.load("IMAGES\BOUTON\SeRetirer.png").convert()
suivre=pygame.image.load("IMAGES\BOUTON\Suivre.png").convert()
tapis=pygame.image.load("IMAGES\BOUTON\Tapis.png").convert()

cartejoueurOK = False
carteTable3 = False
carteTable4 = False
carteTable5 = False
Argenttotal1=1000
Argenttotal2=1000




font = pygame.font.Font(None, 100)
couleur_texte = (0,0,0)

pgmFini=False
while pgmFini==False:


    texte_argTable = font.render(str(argentTable), True, couleur_texte, None)
    texte_argj1 = font.render(str(argentJ1), True, couleur_texte, None)
    texte_argj2 = font.render(str(argentJ2), True, couleur_texte, None)
 #insertion du fond dans la fenêtre
    fen.blit(table,(0,0))

 #insertion bouton
    fen.blit(suivre,(715,585))
    fen.blit(miserbouton, (840,585))
    fen.blit(tapis,(965,585))
    fen.blit(retirer,(1090,585))


    fen.blit(texte_argTable,(743,182))
    fen.blit(texte_argj1,(20,100))
    fen.blit(texte_argj2,(20,200))
 #insertion carte
    if cartejoueurOK == True :
        fen.blit(CarteAAfficher[0],(928,730))
        fen.blit(CarteAAfficher[1],(875,725))
    if carteTable3 == True :
        fen.blit(CarteAAfficher[2],(545,368))
        fen.blit(CarteAAfficher[3],(717,368))
        fen.blit(CarteAAfficher[4],(887,368))
    if carteTable4 == True :
        fen.blit(CarteAAfficher[5],(1057,368))
    if carteTable5 == True :
        fen.blit(CarteAAfficher[6],(1225,370))

    pygame.display.update()
    if etatjeu==-1:
        msg_recu=communication.recoitmessage()

        msg_recu=decode_message2(msg_recu)             #Charger  les  cartes du joueur 2
        mainj2 = []
        mainj2.append(msg_recu[0])
        mainj2.append(msg_recu[1])

        carteTable = []
        carteTable.append(msg_recu[2])
        carteTable.append(msg_recu[3])
        carteTable.append(msg_recu[4])
        carteTable.append(msg_recu[5])
        carteTable.append(msg_recu[6])

        CarteAAfficher=ChargeCarte1(mainj2,carteTable)
        cartejoueurOK=True
        etatjeu = 0


    if etatjeu==0:
        msg_recu=communication.recoitmessage()
        msg_recu = decode_message(msg_recu)
        if int(msg_recu[0])==5:
            argentJ1= int(msg_recu[1])
            argentJ2= int(msg_recu[2])
            argentTable = int(msg_recu[3])
            etatjeu = -1
            carteTable5=False
            carteTable4=False
            carteTable3=False
            MiseTotalej1=0
            MiseTotalej2=0
            miseJoueur1=0
            miseJoueur2=0
            if argentJ1 == 0 or argentJ2 == 0:
                pgmFini=True
        else :
            etatjeu=int(msg_recu[0])
            argentTable = int(msg_recu[1])
            argentJ1= int(msg_recu[2])
            miseJoueur1 = int(msg_recu[3])
            Joueur1EnJeu =bool(msg_recu[4])



        if Joueur1EnJeu == 'True':
            Joueur1EnJeu = True
        else :
            Joueur1EnJeu = False

    if etatjeu == 2:
        carteTable3= True
    if etatjeu == 3:
        carteTable4 = True
    if etatjeu == 4:
        carteTable5 = True

#communication.envoieMessage([argentTable,argentJ1,miseJoueur1,Joueur1EnJeu,etatjeu])

    for evenement in pygame.event.get():
        if evenement.type==pygame.MOUSEBUTTONDOWN:
            boutonclicke = clickposjeu(evenement)
            if boutonclicke == 1:             #Suivre
                miseJoueur2=miseJoueur1
                argentTable = argentTable+miseJoueur2
                argentJ2 = argentJ2-miseJoueur2
                communication.envoieMessage([etatjeu,argentTable,argentJ2,miseJoueur2,Joueur2EnJeu])
                etatjeu=0
            if boutonclicke == 2:             #Miser
                miseJoueur2=miser(argentJ2)
                argentTable = argentTable+miseJoueur2
                argentJ2 = argentJ2-miseJoueur2
                communication.envoieMessage([etatjeu,argentTable,argentJ2,miseJoueur2,Joueur2EnJeu])
                etatjeu=0
            if boutonclicke == 3:            #All in
                miseJoueur2=argentJ2
                argentJ2 = 0
                argentTable = miseJoueur2 + argentTable
                communication.envoieMessage([etatjeu,argentTable,argentJ2,miseJoueur2,Joueur2EnJeu])
                etatjeu=0
            if boutonclicke == 4:         #Se retirer
                argentJ1+=argentTable
                argentTable=0
                etatjeu=5
                communication.envoieMessage([etatjeu,argentJ1,argentJ2,argentTable])
                etatjeu=-1
                carteTable5=False
                carteTable4=False
                carteTable3=False
                MiseTotalej1=0
                MiseTotalej2=0
                miseJoueur1=0
                miseJoueur2=0

    if evenement.type==pygame.QUIT:
            pgmFini=True


    pygame.display.update()
pygame.quit()
sys.exit()