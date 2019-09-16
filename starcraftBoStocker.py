from os import path, listdir, makedirs, remove, system

version = "1.1"

# TODO : Générer les titres avec des ASCII-ART
# ==> https://github.com/sepandhaghighi/art
# ==> https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text


# Afin de gérer tout nouveau contributeur sans changer le coeur du programme.
createurs = ("Eliot Hermabessiere", "Cyprien Rousselot")

# TODO : gérer les couleurs du texte
# Colors : explications sur ==> http://ozzmaker.com/add-colour-to-text-in-python/
# https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
#colors = {'erreur': '\033[1;31;47m', # Rouge gras sur fond blanc
#          'normal': '\033[0;30;47m', # Noir normal sur fond blanc
#          }

repertoires = { 'zerg': path.join('BO', 'zerg'),
                'terran': path.join('BO', 'terran'),
                'protoss': path.join('BO', 'protoss'),
                }

filename_extension = '.txt'



def create():
    # Dictionnaire sur les différentes commandes du menu
    create_commandes_menu_saisie = {
        '/finish': {'description': 'pour terminer la saisie du BO'},
        '/cancel': {'description': 'pour annuler la creation de BO'},
        }
    
    # Dictionnaire sur les différents affichages du menu
    affichage = {
        'titre': """

                                            ______        __              
                                           / ____/_____ _/_/  ___   _____ 
                                          / /    / ___// _ \ / _ \ / ___/ 
                                         / /___ / /   /  __//  __// / 
                                         \____//_/    \___/ \___//_/ 

""",
        'menu_race': """
                                              Choisissez une race:

                                            Zerg / Protoss / Terran

""",
        'menu_saisie': f"""
                               Listez les differentes etapes de vore BO puis
{texte_commandes(35, create_commandes_menu_saisie)}

""",
}
    print(f"{affichage['titre']}{affichage['menu_race']}")
    commande = input().lower()
    if commande != "back":
        if commande in repertoires:
            repertoire = repertoires[commande]
        else:
            erreur("Commande inconnue")
            return # Sortie du menu "create"

        print(f"{affichage['titre']}{affichage['menu_saisie']}")
        texte_build_order = ''
        fin_saisie_build_ordre = False
        while not fin_saisie_build_ordre:
            saisie = input("Saisissez l'étape : ")
            if saisie in create_commandes_menu_saisie:
                fin_saisie_build_ordre = True
            else:
                texte_build_order = texte_build_order + '\r\n' + saisie
        if saisie in create_commandes_menu_saisie:
            if 'fonction' in create_commandes_menu_saisie[saisie]:
                create_commandes_menu_saisie[saisie]['fonction']()
            elif saisie == '/finish':
                print(f"{affichage['titre']}")
                nom_fichier = input('Nommez votre Build-Order : ') + filename_extension
                # Sauvegarder le fichier BO dans le repertoire
                sauvegarder_fichier(path.join(repertoire, nom_fichier), texte_build_order)
                print(f'Sauvegarde le build-order "{nom_fichier[:-len(filename_extension)]}" dans le fichier "{path.join(repertoire, nom_fichier)}"')
            



def info():
    # Dictionnaire sur les différentes commandes du menu
    info_commandes_menu_liste_bo = {
        '/back': {'description': 'pour revenir en arriere'},
        }
    
    info_commandes_menu_affiche_bo = {
        '/back': {'description': 'pour revenir en arriere'},
        '/remove': {'description': 'pour supprimer ce BO'},
        '/modify': {'description': 'pour le modifier'},
        }
    
    # Dictionnaire sur les différents affichages du menu
    affichage = {
        'titre': """
                                           ____        ____      
                                          /  _/____   / __/____  
                                          / / / __ \ / /_ / __ \ 
                                         / / / / / // __// /_/ / 
                                       /___//_/ /_//_/   \____/  

""",
        'menu_race': """
                                              Choisissez une race:

                                            Zerg / Protoss / Terran

""",
        'menu_liste_bo': f"""
                             ecrivez le numero du BO a afficher
{texte_commandes(35, info_commandes_menu_liste_bo)}

                                      Voici les BO Enregistres:

""",
        'menu_affiche_bo': f"""
{texte_commandes(35, info_commandes_menu_affiche_bo)}

""",
        'menu_remove': """
                                            BO supprime

""",
    }
    print(f"{affichage['titre']}{affichage['menu_race']}")
    commande = input().lower()
    if commande not in info_commandes_menu_liste_bo:
        if commande in repertoires:
            repertoire = repertoires[commande]
        else:
            erreur("Commande inconnue")
            return # Sortie du menu "info"

        print(f"{affichage['titre']}{affichage['menu_liste_bo']}")
        liste_fichiers_bo = [f for f in listdir(repertoire) if (path.isfile(path.join(repertoire, f))) and (filename_extension in f)]
        # Numéroter les BO pour les choisir par leur index
        for index, bo in enumerate(liste_fichiers_bo):
            print(f"{index} - {bo[0:-len(filename_extension)]}")
        numero_bo = int(input("Saisissez le numéro du BO : "))
        nom_bo = liste_fichiers_bo[numero_bo][0:-len(filename_extension)]
        nom_fichier = liste_fichiers_bo[numero_bo]

        print(f"{affichage['titre']}{affichage['menu_affiche_bo']}")
        print(40*" " + nom_bo)
        texte_build_order = lire_fichier(path.join(repertoire, nom_fichier))
        print(texte_build_order)

        commande = input("Saisissez votre commande : ").lower()
        if commande in info_commandes_menu_affiche_bo:
            if 'fonction' in info_commandes_menu_affiche_bo[commande]:
                info_commandes_menu_affiche_bo[commande]['fonction']()
            elif commande == '/remove':
                print(f"{affichage['titre']}{affichage['menu_remove']}")
                remove(path.join(repertoire, nom_fichier))
                print(f'Le build-order "{nom_bo}" est effacé.')
            elif commande == '/modify':
                print(f"{affichage['titre']}{affichage['menu_remove']}")
                system(f"notepad {path.join(repertoire, nom_fichier)}")
                print(f"""Modifiez le build-order "{nom_bo}" dans la fenêtre qui s'ouvre ...""")


def erreur(description = ""):
    print(f"""
                                      ______                              
                                     / ____/_____ _____ ___   __  __ _____
                                    / __/  / ___// ___// _ \ / / / // ___/
                                   / /___ / /   / /   /  __// /_/ // /    
                                  /_____//_/   /_/    \___/ \__,_//_/   

                                  {description}
                                  oops il ya un probleme dans la matrice

""")
    input("press 'RETURN' key ...")


def accueil():
    accueil_commandes = {
        'info': {'description': 'pour voir les BO', 'fonction': info},
        'create': {'description': 'pour ajouter un BO', 'fonction': create},
        'exit': {'description': 'pour quitter'},
        }
    
    print(f"""Starcraft Build-order stocker version {version}
Cree par {texte_createurs()} :)
Porté en Python par GuiGeek

                               _______________________________________________________ 
                                _____ __             ______           ______    __  __ 
                               / ___// /_____ ______/ ____/________ _/ __/ /_  / / / / 
                               \__ \/ __/ __ `/ ___/ /   / ___/ __ `/ /_/ __/ / / / / 
                              ___/ / /_/ /_/ / /  / /___/ /  / /_/ / __/ /_  / / / / 
                             /____/\__/\__,_/_/   \____/_/   \__,_/_/  \__/ /_/ /_/ 
                              ________________________________________________________ 

                                    Bienvenue dans le stocker de BO starcraft

                                    Ecrivez :
{texte_commandes(40, accueil_commandes)}

""")
    commande = input().lower()
    if commande in accueil_commandes:
        if 'fonction' in accueil_commandes[commande]:
            accueil_commandes[commande]['fonction']()
        elif commande == "exit":
            return False
    else:
        erreur("Commande inconnue")
    return True


# Fonctions partagées
def sauvegarder_fichier(fichier, texte):
    # Crée l'arborescence si elle est absente
    chemin = path.dirname(fichier)
    if not path.exists(chemin):
        makedirs(chemin)
    # Enregistre le fichier
    with open(fichier, "w") as f:
        f.write(texte)

def lire_fichier(fichier):
    with open(fichier) as f:
        texte = f.read()
    return texte

def texte_createurs():
    """Retourne la liste des createur sous forme de texte avec les séparateurs appropriés (',' et 'et' selon la position)."""
    texte = ""
    for i, createur in enumerate(createurs):
        if i == 0:
            texte = texte + createur # Premier de la liste
        elif (i+1) == len(createurs):
            texte = texte + " et " + createur # Dernier de la liste
        else:
            texte = texte + ", " + createur # Tous les autres
    return texte
    
def texte_commandes(espaces, commandes):
    """Retourne la liste des commandes/descriptions sous forme de texte."""
    texte = ""
    for commande, caracteristiques in commandes.items():
        if 'description' in caracteristiques:
            texte = texte + espaces*" " + f"*{commande}* : {caracteristiques['description']}\r\n"
    return texte
    

if __name__ == "__main__":
    while accueil():
        pass
