# Projet_3

Aidez MacGyver � s'�chapper !

Lien GitHub: https: // github.com / Walrick / Projet_3
A utiliser avec python 3.6

installer les d�pendances:
pip install - r requirements.txt

Lancer le jeu:
main.py

Pour jouer:
Utilise les touches directionnelles pour bouger MacGyver et ramasse les trois objets pour endormir le garde et gagner !
Utilise �chap pour quitter

Pour modifier la map:
espace = tuile(d�placement normal)
X = mur infranchissable
A = arriv� sur la map
S = sortie de la map

Description:
A la ra�ine du jeu il y a main.py, README.md requirements.txt et Map.txt. J'utilise un package contenant un dossier d'objet graphique et 6 fichiers: Game.py, Graphic.py, Character.py, Item.py, Tule.py, fonction.py.
Le fichier main.py sert � lancer le jeu.
Le fichier Game.py poss�de la class Game qui s'occupe de charger la map avec Map.txt et de g�rer les �v�nements et l'ensemble de la logique du jeu.
Le fichier Graphic contient la class Graphic pour afficher le jeu.
Les fichiers Character, Item et Tule contiennent les classes Character, Item et Tule qui g�rent leurs objets.
Le fichier fonction.py regroupe les fonctions utiles du jeu.
J'ai regroup� les donn�es des tuiles dans un dictionnaire "lvl" dans game.py qui a pour cl� un tuple de coordonn�es x, y de la map. Je stocke �galement dans une liste item la liste des objets et dans une liste character une liste de personnages. La boucle principale est dans classe Main pour initier et v�rifier si le joueur gagne et, ou perd la partie
Ce projet a �t� mon premier programme d�velopp� en environnement virtuel et m'a pris du temps pour le mettre en place. N'�tant habitu� � ne programmer que pour moi, j'ai eu quelques difficult�s � rendre mon programme lisible et intelligible pour autrui (commentaires en anglais). Pour finir, le module Pygame m'�tait inconnu, mais vu que je connaissais OpenGL je n'ai pas �t� trop perdu et l'apprentissage s'est fait rapidement.


