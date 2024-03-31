# En gros faut faire un menu pour le P, F, C et le c+ c-
import os

current_user = os.getlogin()
print()
print("Bienvenue dans le menu des jeu !")
print(f"A quoi voulez-vous jouer aujourd'hui, {current_user} ?")
print()
print("Pour jouer a 'Pierre, Feuille, Ciseaux' taper 1")
print("Pour jouer a 'C'est plus, C'est moins' taper 2")
print("Pour quitter tapez 3")
print()

def demander_nombre(prompt='> ', min_val=1, max_val=3):
    try:
        # Tentez de convertir l'entrée en un nombre entier
        entree_utilisateur = int(input("Votre choix : "))
        return entree_utilisateur
        # Si la conversion est réussie, la boucle se termine
    
    except ValueError:
        # Si une exception ValueError est levée, cela signifie que l'entrée n'est pas un nombre
            print("Ce n'est pas un nombre valide. Veuillez réessayer.")
            return demander_nombre()

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier1 = "Pierre.py"
chemin_fichier1 = os.path.join(repertoire_script, nom_fichier1)

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier2 = "import_random.py"
chemin_fichier2 = os.path.join(repertoire_script, nom_fichier2)



while True:
    entree_utilisateur = demander_nombre()

    if entree_utilisateur == 1:
        os.system(f"python \"{chemin_fichier1}\"")
    
    elif entree_utilisateur == 2:
        os.system(f"python \"{chemin_fichier2}\"")
    
    elif entree_utilisateur == 3:
         os.system(f"python \"{chemin_fichier1}\"")