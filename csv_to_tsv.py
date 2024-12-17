import csv
import string
import os
from tef import TEF

#Création d'un objet TEF csv vers tsv
etats={}
etat_initial="q0"
csv_to_tsv=TEF(etat_initial, etats)

#Transitions pour convertir virgules en tabulations
csv_to_tsv+=("q0",",","\t","q1")  #au cas où le doc commence par une virgule
for lettre in string.ascii_letters+string.digits+"éèùôûêîà"+" "+"#%&'()*+-./:;<=>?@[\]^_`{|}~": #si on rencontre un caractère de ce type, on le réécrit
    csv_to_tsv+=("q0",lettre,lettre,"q1")
    csv_to_tsv+=("q1",lettre,lettre,"q1")

csv_to_tsv+=("q1",",","\t","q1")  #si on croise une virgule, on la change en tabulation
csv_to_tsv+=("q1","\n","\n","q0")  #si on croise un saut de ligne, on saute la ligne

#Fonction de conversion d'un fichier csv vers tsv en utilisant la classe TEF
def conversion_csv_to_tsv(input_csv_path,output_tsv_path):
    #on lit le fichier csv en tant que chaîne avec la fonction read
    contenu_csv=csv_to_tsv.read(input_csv_path)

    #Appel à la classe TEF et la méthode analyse
    contenu_tsv=csv_to_tsv.analyse(contenu_csv)

    #on écrit le contenu dans un nouveau fichier tsv
    with open(output_tsv_path,"w",encoding='utf-8') as fichiertsv:
        fichiertsv.write(contenu_tsv)

#utilisation de la fonction
in_path=os.path.join("tests","color_srgb.csv")
out_path=os.path.join("outputs","color_result.tsv")
conversion_csv_to_tsv(in_path,out_path)
