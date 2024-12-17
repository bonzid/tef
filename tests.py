import os
from tef import TEF

etats={}
etat_initial="q0"

#machine à rires :-)
rires=TEF(etat_initial,etats)

#Appel de la fonction "ajout_transition" pour ajouter une transition
"""
rires.ajout_transition("q0","h","h","q1")
rires.ajout_transition("q1","a","a","q2")
rires.ajout_transition("q2","!","#!","qf")
rires.ajout_transition("q2","h","#h","q1")
"""

#Utilisation de la fonction __add__ pour ajouter des transitions
rires+=("q0","h","h","q1")
rires+=("q1","a","a","q2")
rires+=("q2","!","#!","qf")
rires+=("q2","h","#h","q1")

#Utilisation de la fonction __sub__ pour supprimer une transition
rires+=("q5","g","f","q9")
rires-=("q5","g","f","q9")

hilare=os.path.join("tests","hahaha.txt")
print("\nRésultat :\n",rires.analyse(hilare)) #pour une sortie "ha#ha#ha#ha#!"


import string

etats={}
etat_initial="q0"

tokenizer=TEF(etat_initial,etats)

#Transitions pour les lettres (mots) et chiffres
for lettre in string.ascii_letters+string.digits+"éèùôûêîà":
    tokenizer+=("q0",lettre,lettre,"mot")
    tokenizer+=("mot",lettre,lettre,"mot")
    tokenizer+=("sep",lettre,lettre,"q0")

#Transitions pour les séparateurs (ponctuations et espaces)
for separateur in string.punctuation + string.whitespace: #On utilise le caractère "#" pour séparer nos tokens
    tokenizer+=("q0",separateur,("#"+separateur+"#"),"sep")
    tokenizer+=("mot",separateur,("#"+separateur+"#"),"sep")
    tokenizer+=("sep",separateur,("#"+separateur+"#"),"sep")


#print("\nDictionnaire des transitions :\n",tokenizer.etats,"\n")
#print(len(etats))

lorem=os.path.join("tests","lorem.txt")
print("Résultat du tokenizer instancié :\n",tokenizer.analyse(lorem))
print()

