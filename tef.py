import os

class TEF:
    def __init__(self,etat_initial,etats):
        self.etat_initial=etat_initial
        self.etats=etats #dictionnaire associant état avec les transitions possibles depuis cet état

    def __repr__(self): #on indique avec __repr__ quelle chaîne de car on souhaite en retour d'un appel à la classe TEF
        affichage=f"etat_initial={self.etat_initial} et etats=" #notamment pour la lisibilité de notre fonction tracer
        for el in self.etats:
            affichage+=f"\n{el} : {self.etats[el]}"
        return affichage


    def traceFonc(fonction):
        def decore(*args,**kwargs): #on récupère les arguments données en entrée par la fonction décorée
            print(f"--- Fonction tracée : {fonction.__name__} ---")
            print(f"Arguments : {args}, \n{kwargs}")
            resultat=fonction(*args,**kwargs)
            print(f"Résultat : {resultat}") #affichage de la sortie de la fonction
            print("--- Fin de la fonction ---\n")
            return resultat
        return decore #la fonction "tracer" retourne le résultat de notre fct "decore"


    def __len__(self):
        """
        Retourne le nombre d'états du transducteur
        """
        return len(self.etats)


    def read(self,fichier):
        """
        Lit un fichier donné en entrée et retourne son contenu
        """
        try:
            with open(fichier,"r",encoding="utf-8") as f:
                contenu=f.read()
            return contenu
        except FileNotFoundError:
            print(f"Fichier '{fichier}' introuvable.")
            return ""
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier : {e}")
            return ""


    def ajout_transition(self,etat_depart:str,entree:str,sortie:str,etat_suivant:str):
        """
        Ajouter une transition dans un dictionnaire au transducteur avec, en entrée :
        - l'état de départ (où le transducteur se trouve avant que la transition ait eu lieu)
        - l'entrée (chaîne d'entrée)
        - la sortie (chaine de sortie après la transition)
        - l'état suivant (où le transducteur se trouvera après la transition)
        """

        #si l'état de départ n'est pas dans le dict états, on l'ajoute
        if etat_depart not in self.etats:
            self.etats[etat_depart]=[]

        #et même si état de départ déjà dans états, possibilité de plusieurs transitions
        #on associe l'état de départ à une entrée, une sortie, et l'état qui suit
        self.etats[etat_depart].append((entree,sortie,etat_suivant))

        #process=print(f"Transition ajoutée : (depuis {etat_depart}) {entree} -> {sortie} (vers {etat_suivant})")
        #return process


    def __add__(self,transition:tuple):
        """
        Ajoute une transition au transducteur sous forme d'un tuple : etat_depart, entree, sortie, etat_suivant
        """
        #on vérifiei si l'élément ajouté est bien un tuple de 4 éléments
        if len(transition)==4:
            etat_depart,entree,sortie,etat_suivant=transition
            self.ajout_transition(etat_depart,entree,sortie,etat_suivant) #appel de la fct ajout_transition
            return self
        else:
            print("L'entrée prend en compte 4 éléments")


    def __sub__(self,transition):
        """
        Retire une transition au transducteur sous forme d'un tuple : etat_depart, entree, sortie, etat_suivant
        """
        if len(transition)==4:
            etat_depart,entree,sortie,etat_suivant=transition

            #si l'état de départ correspond à un état de départ du dictionnaire, alors :
            if etat_depart in self.etats:
                #on crée une nouvelle liste de transitions pour cette état, sans la transition indésirable
                self.etats[etat_depart]=[
                    t for t in self.etats[etat_depart]
                    if not (t[0]==entree and t[1]==sortie and t[2]==etat_suivant) #on conserve toutes les transitions t sauf celle à supprimer
                ]

                #si l'état de départ n'a plus aucune transition, on peut le supprimer du dictionnaire
                if not self.etats[etat_depart]:
                    del self.etats[etat_depart]

                #print(f"Transition supprimée : (depuis {etat_depart}) {entree} -> {sortie} (vers {etat_suivant})")
                return self
            else:
                print(f"L'état de départ '{etat_depart}' n'existe pas")  #si l'état n'existe pas
        else:
            print("L'entrée prend en compte 4 éléments")


    @traceFonc
    def analyse(self,chaine_dentree:str):
        """
        Prend en entrée une chaîne de caractères (ou un doc) et renvoie la chaîne de sortie du transducteur après voir appliqué toutes les transitions
        """
        #si on a un fichier en entrée, on appelle à la fonction read puis execute suite du script
        if os.path.isfile(chaine_dentree):
            chaine_dentree=self.read(chaine_dentree)

        #si on a une string en entrée, on execute:
        chaine_sortie="" #chaîne de sortie est une str
        etat_courant=self.etat_initial

        #on parcourt chaque caractère de notre chaîne d'entrée
        for car in chaine_dentree:
            if etat_courant in self.etats: #si la clé état courant existe dans états,
                #dans notre état correspondant,
                for entree,sortie,etat_suivant in self.etats[etat_courant]:
                     if car==entree: #si car de la chaîne correspond à entrée de l'état,

                          #print("Transition appliquée : ")
                          #print(etat_courant,car,sortie,etat_suivant)

                          chaine_sortie+=sortie  #on écrit la sortie
                          etat_courant=etat_suivant #on applique la transition

            else:
                print("Etat non reconnu")
                chaine_sortie+=car
                pass

        return chaine_sortie
