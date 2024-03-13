import tkinter as tk
from tkinter import messagebox
import random

class JeuAllumettes(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Jeu des Allumettes")
        self.geometry("400x200")

        self.nb_allumettes = 30
        self.joueur_actuel = "Humain"
        self.dernier_choix = 2

        self.label_allumettes = tk.Label(self, text=f"Allumettes restantes : {self.nb_allumettes}")
        self.label_allumettes.pack()

        self.entry_allumettes = tk.Entry(self)
        self.entry_allumettes.pack()

        self.bouton_jouer = tk.Button(self, text="Jouer", command=self.jouer_tour)
        self.bouton_jouer.pack()

        self.bouton_recommencer = tk.Button(self, text="Recommencer", command=self.recommencer_jeu)
        self.bouton_recommencer.pack()
        self.bouton_recommencer.config(state=tk.DISABLED)

    def jouer_tour(self):
        try:
            choix = int(self.entry_allumettes.get())
            if choix < 1 or choix > min(2 * self.dernier_choix, self.nb_allumettes):
                messagebox.showerror("Erreur", "Nombre d'allumettes invalide !")
                return
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide !")
            return

        self.nb_allumettes -= choix
        self.label_allumettes.config(text=f"Allumettes restantes : {self.nb_allumettes}")
        
        if self.nb_allumettes <= 0:
            messagebox.showinfo("Fin du jeu", f"Le joueur {self.joueur_actuel} a perdu !")
            self.bouton_jouer.config(state=tk.DISABLED)
            self.bouton_recommencer.config(state=tk.NORMAL)
            return

        if self.joueur_actuel == "Humain":
            self.joueur_actuel = "Ordinateur"
            choix_ordi = self.choix_ordi()
            self.nb_allumettes -= choix_ordi
            self.label_allumettes.config(text=f"Allumettes restantes : {self.nb_allumettes}")
            if self.nb_allumettes <= 0:
                messagebox.showinfo("Fin du jeu", "L'ordinateur a perdu !")
                self.bouton_jouer.config(state=tk.DISABLED)
                self.bouton_recommencer.config(state=tk.NORMAL)
                return
            self.joueur_actuel = "Humain"
        
        self.dernier_choix = choix

    def choix_ordi(self):
        max_choix = min(2 * self.dernier_choix, self.nb_allumettes)
        return random.randint(1, max_choix)

    def recommencer_jeu(self):
        self.nb_allumettes = 30
        self.joueur_actuel = "Humain"
        self.label_allumettes.config(text=f"Allumettes restantes : {self.nb_allumettes}")
        self.bouton_jouer.config(state=tk.NORMAL)
        self.bouton_recommencer.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = JeuAllumettes()
    app.mainloop()

#MasterLipakumu