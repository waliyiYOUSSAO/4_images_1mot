###### 4 image u  mot ######
#"C:\Users\HP\Downloads\gutenberg\gutenberg.txt"
#"C:\Users\HP\Downloads\liste_francais\liste_francais.txt"
import time
from itertools import permutations
def combinaisons_filtre(iterable,r):
    permute = permutations(iterable,r)
    list = [''.join(perm) for perm in permute]
    with open(r"C:\Users\HP\Downloads\gutenberg\gutenberg.txt", 'r') as fichier:
        mot_possible = [mot.strip().upper() for mot in fichier if len(mot.strip()) == r]
        for mot in mot_possible:
            print(".", end ="")
            if mot.strip().upper() in list:
                print(mot.strip().upper())
                
        else:
            print("Désolé aucun mot n'a pu être formé avec les données reçues")        
        
        
bvn = "Bienvenue dans la résolution de quatre image un mot"
for i in bvn:
    time.sleep(0.05)## utiliser pour un temps d'attente
    print(i,end ="")## affiche chque lettre de la variable bvn apres un temps
r = int(input("\nQuel est le nombre de case:"))
iterable = input("\nQuelles sont les lettres proposées par le jeu:").upper()
combinaisons_filtre(iterable, r)