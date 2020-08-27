# Projet_3

Aidez MacGyver à s'échapper !

Lien GitHub: https: // github.com / Walrick / Projet_3
A utiliser avec python 3.6

installer les dépendances:
pip install - r requirements.txt

Lancer le jeu:
main.py

Pour jouer:
Utilise les touches directionnelles pour bouger MacGyver et ramasse les trois objets pour endormir le garde et gagner !
Utilise échap pour quitter

Pour modifier la map:
espace = tuile(déplacement normal)
X = mur infranchissable
A = arrivé sur la map
S = sortie de la map

Description:
A la raçine du jeu il y a main.py, README.md requirements.txt et Map.txt. J'utilise un package contenant un dossier d'objet graphique et 6 fichiers: Game.py, Graphic.py, Character.py, Item.py, Tule.py, fonction.py.
Le fichier main.py sert à lancer le jeu.
Le fichier Game.py posséde la class Game qui s'occupe de charger la map avec Map.txt et de gérer les événements et l'ensemble de la logique du jeu.
Le fichier Graphic contient la class Graphic pour afficher le jeu.
Les fichiers Character, Item et Tule contiennent les classes Character, Item et Tule qui gérent leurs objets.
Le fichier fonction.py regroupe les fonctions utiles du jeu.
J'ai regroupé les données des tuiles dans un dictionnaire "lvl" dans game.py qui a pour clé un tuple de coordonnées x, y de la map. Je stocke également dans une liste item la liste des objets et dans une liste character une liste de personnages. La boucle principale est dans classe Main pour initier et vérifier si le joueur gagne et, ou perd la partie
Ce projet a été mon premier programme développé en environnement virtuel et m'a pris du temps pour le mettre en place. N'étant habitué à ne programmer que pour moi, j'ai eu quelques difficultés à rendre mon programme lisible et intelligible pour autrui (commentaires en anglais). Pour finir, le module Pygame m'était inconnu, mais vu que je connaissais OpenGL je n'ai pas été trop perdu et l'apprentissage s'est fait rapidement.


