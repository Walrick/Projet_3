# Projet_3

Aidez MacGyver � s'�chapper !

Lien GitHub : https://github.com/Walrick/Projet_3
A utiliser avec python 3.6
installer les d�pendances : 

pip install -r requirements.txt

Lancer le jeu :

main.py

Description : 
J'ai choisi de s�parer le programme en trois fichiers principaux : main, game et graphic. J'utilise un package contenant un dossier d'objet graphique et 4 fichiers : character, item, tule et fonction. 
Le fichier main.py sert � lancer le jeu. 
Le fichier game.py poss�de la class Main qui s'occupe de charger la map avec map.txt et de g�rer les �v�nements et l'ensemble de la logique du jeu. 
Le fichier graphic contient la class Graphic pour afficher le jeu. 
Les fichiers character, item et tule contiennent les classes Character, Item et Tule qui g�rent leurs objets. 
Le fichier fonction.py regroupe les fonctions utiles du jeu. 
J'ai regroup� les donn�es des tuiles dans un dictionnaire "lvl" dans game.py qui a pour cl� un tuple de coordonn�es x, y de la map. Je stocke �galement dans une liste item la liste des objets et dans une liste caract�re une liste de personnages. La boucle principale est dans classe Main pour initier et v�rifier si le joueur gagne et, ou perd la partie
Ce projet a �t� mon premier programme d�velopp� en environnement virtuel et m'a pris du temps pour le mettre en place. N'�tant habitu� � ne programmer que pour moi, j'ai eu quelques difficult�s � rendre mon programme lisible et intelligible pour autrui (commentaires en anglais). Pour finir, le module Pygame m'�tait inconnu, mais vu que je connaissais OpenGL je n'ai pas �t� trop perdu et l'apprentissage s'est fait rapidement.


