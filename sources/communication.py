# Créé par lilo bardy, le 28/03/2024 en Python 3.7
import socket



def envoieMessage(msg_a_envoyer):
    connexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hote="192.168.1.27"               #<------------------------------------------------- ip locale de l'adversaire -------------------------------------------------------------------
    port = 12800
    connexion.connect((hote, port))
    msg_a_envoyer = str(msg_a_envoyer)
    msg_a_envoyer = msg_a_envoyer.encode() #transformation en UTF8
    connexion.send(msg_a_envoyer)
    connexion.close()


def recoitmessage():
    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                             #Attente de recevoir un message par l'autre joueur
    hote = '192.168.1.15'            #<------------------------------------------------- ip locale personnelle -------------------------------------------------------------------
    port = 12800
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    connexion, infos_connexion = connexion_principale.accept()
    msg_recu = ""
    while msg_recu == "":
        chno = connexion.recv(1024)

        msg_recu = chno.decode()
    connexion.close()
    return msg_recu