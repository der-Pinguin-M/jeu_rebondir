from tkinter import * 
import random
import time
x = 0
#Il faut remettre le texte de 1 en arrière, je viens d'enlever la fonction jeu
scorez = 0

class Balle:
    def __init__ (self, canvas, raquette, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.id = canvas.create_oval(10, 10, 25, 25,  fill="red")
        self.canvas.move(self.id, 245, 100)
        departs = [-3, -2, -1, 1, 2, 3]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()
        self.touche_bas = False

    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                return True
            return  False
    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        vitesse = [-6, -5, -4, -3, -2, -1]
        random.shuffle(vitesse)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.hauteur_canevas:
            self.touche_bas = True
            canvas.create_text(200, 200, text='GAME OVER', fill='green', font=('Helvetica', 40))
            canvas.create_text(200, 300, text='Pour rejouer, reactiver le programme', fill='red', font=('Times', 15))
            canvas.itemconfig(text='time :%s' % x)
        if self.heurter_raquette(pos) == True:
            self.y = vitesse[0]
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.largeur_canevas:
            self.x = -3
            
class Raquette:
    def __init__ (self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=couleur)
        self.canvas.move(self.id, 200, 300)
        self.xi = 0
        self.largeur_canevas = self.canvas.winfo_width()
        canvas.bind_all('<KeyPress-Left>', self.vers_gauche)
        canvas.bind_all('<KeyPress-Right>', self.vers_droite)

    def vers_gauche(self, evt):
        self.xi = -2

    def vers_droite(self, evt):
        self.xi = 2

    def dessiner (self):
        self.canvas.move(self.id, self.xi, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xi = 3
        if pos[2] >= self.largeur_canevas:
            self.xi = -3
            
tk = Tk()
tk.title('Rebondir (par CodiNaruto)')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
#fond_ = PhotoImage(file='f:\\fond-rebondir.gif')
#canvas.create_image(0, 0, image=fond_, anchor='nw')
raquette = Raquette(canvas, 'blue')
balle = Balle(canvas, raquette, 'red')
zoubi = canvas.create_text(100, 100, text='time :%s' % x, fill='orange', font=('Helvetica', 20))


def se(evt):
    c = 0
    if c == 0:
        c = 1
        x = 1
        while 1:
            if balle.touche_bas == False:
                raquette.dessiner()
                balle.dessiner()
            x += 1
            canvas.itemconfig(zoubi, text='time :%s' % x)
            tk.update()
            time.sleep(0.01)
        
canvas.bind_all("<Button-1>", se)
tk.mainloop()

