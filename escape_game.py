from tkinter import*

def presser(evt):
    global reponse
    
    if reponse.get() == "énigme 1_1":
        enigme1_1=Label(fenetre, text="Il faut compléter l’énigme sur le mur pour ouvrir la porte.")
        enigme1_1.pack()  
        fenetre.mainloop() 
    
    elif reponse.get() == "énigme 1_2":
        enigme1_2=Label(fenetre, text="La moitié basse de l’énigme est inutile.")
        enigme1_2.pack()
        fenetre.mainloop()
    
    elif reponse.get() == "énigme 1_3":
        enigme1_3=Label(fenetre, text="Le code est 1235")
        enigme1_3.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 2_1":
        enigme2_1=Label(fenetre, text="Il faut faire un lien entre la carte et l’histoire.")
        enigme2_1.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 2_2":
        enigme2_2=Label(fenetre, text="Les câbles forment des numéros, à vous de trouver lesquelles.")
        enigme2_2.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 2_3":
        enigme2_3=Label(fenetre, text="Le code est 7129")
        enigme2_3.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 3_1":
        enigme3_1=Label(fenetre, text="Le catalogue de pièce électronique pourrait être utile")
        enigme3_1.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 3_2":
        enigme3_2=Label(fenetre, text="Il faudrait peut etre regarder sur l'ordinateur.")
        enigme3_2.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 3_3":
        enigme3_3=Label(fenetre, text="Le code est 224391")
        enigme3_3.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 4_1":
        enigme4_1=Label(fenetre, text="La page et le code sont liés")
        enigme4_1.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 4_2":
        enigme4_2=Label(fenetre, text="Des indices devraient ce trouver dans le code de la page")
        enigme4_2.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 4_3":
        enigme4_3=Label(fenetre, text="Le code est 32428")
        enigme4_3.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 5_1":
        enigme5_1=Label(fenetre, text="Des numéros devraient êtres indiquer sur les coins de la salle")
        enigme5_1.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 5_2":
        enigme5_2=Label(fenetre, text="Je pense que c’est du binaire")
        enigme5_2.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 5_3":
        enigme5_3=Label(fenetre, text="Le code est 3195")
        enigme5_3.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 6_1":
        enigme6_1=Label(fenetre, text="Le message est codé")
        enigme6_1.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 6_2":
        enigme6_2=Label(fenetre, text="cherchez partout")
        enigme6_2.pack()
        fenetre.mainloop()
        
    elif reponse.get() == "énigme 6_3":
        enigme6_3=Label(fenetre, text="L’argent est souvent la solution à tous nos problèmes")
        enigme6_3.pack()
        fenetre.mainloop()
    
    else:
        nul=Label(fenetre, text="Il n'y a pas d'indice pour cette énigme")
        nul.pack()
        fenetre.mainloop()
        

 

fenetre = Tk()

fenetre.geometry("1000x1000")

exemple1 = Label(fenetre, text="Vous devez écrire  'énigme'  +  'le numéro de l'énigme'  +  '_le numéro de l'indice de l'énigme ")
exemple1.pack()

exemple2 = Label(fenetre, text="Par exemple : Pour le premier indice de la première énigme, tapez énigme 1_1")
exemple2.pack()

exemple3 = Label(fenetre, text="Par exemple : Pour le deuxième indice de la troisième énigme, tapez énigme 3_2")
exemple3.pack()

exemple4 = Label(fenetre, text="Il y a à chaque fois deux indices puis le troisième indice est la réponse, celle ci vous fera perdre du temps")
exemple4.pack()


reponse = StringVar()


reponse = Entry(fenetre, textvariable=reponse, width=20)
reponse.pack()

bouton_confirmer = Button(fenetre, text="Valider")
bouton_confirmer.pack()
bouton_confirmer.bind('<ButtonRelease-1>', presser)       



fenetre.mainloop()