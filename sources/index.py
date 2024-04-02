# Créé par bardy1, le 07/02/2024 en Python 3.7
import pygame, sys
from pygame import *

def clickpos(event):
    if event.type == MOUSEBUTTONDOWN:
        #test pur bouton jouer
        if event.button == 1 and event.pos[0]>710 and event.pos[0]<1210 and event.pos[1]>280 and event.pos[1]<380:
            return 1
        elif event.button == 1 and event.pos[0]>710 and event.pos[0]<1210 and event.pos[1]>480 and event.pos[1]<580:
            return 2
        elif event.button == 1 and event.pos[0]>710 and event.pos[0]<1210 and event.pos[1]>680 and event.pos[1]<780:
            return 3
    else:
        return -1



        




pygame.init()

LarFEN=1920
HauFEN=1020

fen=pygame.display.set_mode((LarFEN,HauFEN))
pygame.display.set_caption("Poker Game")

background=pygame.Surface((LarFEN,HauFEN))
pygame.Surface.fill(background, (61, 135, 76))

bouton=pygame.Surface((500,100))
pygame.Surface.fill(bouton, (0,0,255))


font = pygame.font.Font(None, 100)
couleur_texte = (129,150,176)

texte_jouer1 = font.render("Joueur 1", True, couleur_texte, None)
texte_joueur2 = font.render("Joueur 2", True, couleur_texte, None)
texte_quit = font.render("Quitter", True , couleur_texte, None)

run=True
while run:
    fen.blit(background, (0,0))
    fen.blit(bouton, (710,280))
    fen.blit(bouton, (710,480))
    fen.blit(bouton, (710,680))
    fen.blit(texte_jouer1, (860, 300))
    fen.blit(texte_joueur2, (840, 500))
    fen.blit(texte_quit, (820, 700))

    for evenement in pygame.event.get():
        boutonClicke=clickpos(evenement)
        if evenement.type== QUIT or boutonClicke==3:
            run = False
        elif boutonClicke == 1 :
            exec(open("jeu1.py").read())
        elif boutonClicke == 2:
            exec(open('jeu2.py').read())

    pygame.display.update()

pygame.quit()
sys.exit()