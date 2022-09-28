# Escribir una aplicación GUI (llamada ContDecreciente) como la que se
# ve en la figura. Cada ves que se haga clic en el botón "-", al valor de
# contador se le resta 1.

from asyncio.windows_events import NULL
from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter.font import Font

class Juego(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Adivinador")
        self.resizable(False, False)
        self.geometry("550x300")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.txt = StringVar()
        self.img = PhotoImage(file="emoji.png", width=100, height=83)
        self.btnFont = Font(family="Roboto Cn", size=10) 
        self.txtFont = Font(family="Roboto Cn", size=14) 
        self.cont = 0
        self.mayMen = ''
        
        self.texto = Label()
        self.resta = Label()
        self.suma = Label()
        self.btnReset = Label()
        self.btnAtras = Label()
        self.btnSig = Label()
        self.mayor = Label()
        self.menor = Label()
        self.Idioma()
        
    def changeEspañol(self):
        print(self.cont)
        self.cont += 1
        if self.cont == 1:

            self.txt.set("¡Bienvenido al juego! \n\n Por favor, piensa en un número de dos cifras \n que no sean iguales.")
            self.texto.place(x=76, y=76)
            self.btnSig.destroy()
            self.btnSig = Button(self, text="Siguiente",command=lambda: self.changeEspañol())
            self.btnSig.config(font=self.btnFont, fg="black", bg="white", border= 1)
            self.btnSig.place(x=280, y=200)
            self.btnAtras.destroy()
            self.btnAtras = Button(self, text="Anterior",command=lambda: self.Idioma())
            self.btnAtras.config(font=self.btnFont, fg="black", bg="white", border= 1)
            self.btnAtras.place(x=205, y=200)
            self.mayor.destroy()
            self.menor.destroy()
            self.ing.destroy()
            self.esp.destroy()
            self.btnReset.destroy()

            
        if self.cont == 2:
            self.radioValue = tk.IntVar() 

            self.txt.set("\n\n Bien, ahora invertí el orden de las cifras. \n Luego, ingrese si el numero es mayor or menor")
            self.texto.place(x=77, y=26)

            self.mayor = Radiobutton(self, text="Mayor",variable=self.radioValue, value=1)
            self.mayor.config(font=self.btnFont, fg="black", border= 1)
            self.mayor.place(x=247, y=130)

            self.menor = Radiobutton(self, text="Menor",variable=self.radioValue, value=2)
            self.menor.config(font=self.btnFont, fg="black", border= 1)
            self.menor.place(x=247, y=160)
            
            self.btnAtras.destroy()
            self.btnAtras = Button(self, text="Anterior",command=lambda: self.atras())
            self.btnAtras.config(font=self.btnFont, fg="black", bg="white", border= 1)
            self.btnAtras.place(x=205, y=200)
            self.btnSig.place(x=280, y=200)
            
            self.resta.destroy()

        if self.cont == 3:
            self.restaValue = tk.IntVar() 

            self.txt.set("\n\n Ahora, al numero mayor de los dos restale el menor. \n Ingrese el resultado:")
            self.texto.place(x=55, y=26)
            self.mayor.destroy()
            self.menor.destroy()
            self.resta = Entry(self,textvariable=self.restaValue)
            self.resta.place(x=213, y=150)

            self.suma.destroy()

        if self.cont == 4:
            self.sumaValue = tk.IntVar() 

            self.txt.set("\n\n Luego sumá las cifras del número \nque pensaste al principio. \n Ingrese el resultado:")
            self.texto.place(x=135, y=13)
            self.resta.destroy()
            self.suma = Entry(self,textvariable=self.sumaValue)
            self.suma.place(x=213, y=150)
            self.btnReset.destroy()

        if self.cont == 5:
            n = self.radioValue.get()
            self.btnSig.destroy()

            if n == 1:

                self.btnReset = Button(self, text="Empezar de nuevo",command=lambda: self.reset())
                self.texto.place(x=176, y=80)
                self.btnReset.config(font=self.btnFont, fg="black", bg="white", border= 1)
                self.btnReset.place(x=252, y=180)
                self.btnAtras.place(x=178, y=180)

                
                num1 = int(self.restaValue.get())
                num2 = int(self.suma.get())
                rta = self.calcular(num1, num2)
                self.txt.set("Pensaste en el numero: \n\n" + str(rta))
                self.suma.destroy()

                
    def calcular(self, n1, n2):

        parametro = n1 / 9

        d1 = (n2 - parametro) / 2
        d2 = (n2 + parametro) / 2

        respuesta = int(d1) * 10 + int(d2)

        return respuesta

   
    def atras(self):
        self.cont -= 2
        self.changeEspañol()

    def reset(self):
        self.cont = 0
        self.changeEspañol()

    
    def changeIngles(self):

        self.cont += 1
        if self.cont == 1:

            self.txt.set("¡Welcome to the game! \n\n Please think on a two digit number,  \n each one has to be different.")
            self.texto.place(x=76, y=76)
            self.btnSig = Button(self, text="Continue",command=lambda: self.changeIngles())
            self.btnSig.config(font=self.btnFont, fg="black", bg="white", border= 1)
            self.btnSig.place(x=280, y=200)
            self.btnAtras.destroy()
            self.btnAtras = Button(self, text="Previous",command=lambda: self.Idioma())
            self.btnAtras.config(font=self.btnFont, fg="black", bg="white", border= 1)
            self.btnAtras.place(x=205, y=200)
            self.mayor.destroy()
            self.menor.destroy()
            self.ing.destroy()
            self.esp.destroy()
            self.btnReset.destroy()
            
        if self.cont == 2:
            self.radioValue = tk.IntVar() 

            self.txt.set("\n\n Now revert the oder of the digits. \n Then, enter if the number is bigger or smaller.")
            self.texto.place(x=77, y=26)

            self.mayor = Radiobutton(self, text="Bigger",variable=self.radioValue, value=1)
            self.mayor.config(font=self.btnFont, fg="black", border= 1)
            self.mayor.place(x=247, y=130)

            self.menor = Radiobutton(self, text="Smaller",variable=self.radioValue, value=2)
            self.menor.config(font=self.btnFont, fg="black", border= 1)
            self.menor.place(x=247, y=160)
            
            self.btnAtras.destroy()
            self.btnAtras = Button(self, text="Previous",command=lambda: self.atrasIngles())
            self.btnAtras.config(font=self.btnFont, fg="black", bg="white", border= 1)
            self.btnAtras.place(x=205, y=200)
            self.btnSig.place(x=280, y=200)
            
            self.resta.destroy()

        if self.cont == 3:
            self.restaValue = tk.IntVar() 

            self.txt.set("\n\n To the biggest number subtract the smallest. \n Enter the result:")
            self.texto.place(x=55, y=26)
            self.mayor.destroy()
            self.menor.destroy()
            self.resta = Entry(self,textvariable=self.restaValue)
            self.resta.place(x=213, y=150)

            self.suma.destroy()

        if self.cont == 4:
            self.sumaValue = tk.IntVar() 

            self.txt.set("\n\n Now sum the digits of the \n first number you thought. \n Enter the result:")
            self.texto.place(x=135, y=13)
            self.resta.destroy()
            self.suma = Entry(self,textvariable=self.sumaValue)
            self.suma.place(x=213, y=150)
            self.btnReset.destroy()

        if self.cont == 5:
            n = self.radioValue.get()
            self.btnSig.destroy()

            if n == 1:

                self.btnReset = Button(self, text="Start again",command=lambda: self.resetIngles())
                self.texto.place(x=176, y=80)
                self.btnReset.config(font=self.btnFont, fg="black", bg="white", border= 1)
                self.btnReset.place(x=252, y=180)
                self.btnAtras.place(x=178, y=180)

                
                num1 = int(self.restaValue.get())
                num2 = int(self.suma.get())
                rta = self.calcular(num1, num2)
                self.txt.set("The number you thought is: \n\n" + str(rta))
                self.suma.destroy() 

    def atrasIngles(self):
        self.cont -= 1
        self.changeIngles()

    def resetIngles(self):
        self.cont = 0
        self.changeIngles()

    def Idioma(self):
        
        self.radioVal = tk.IntVar() 

        self.txt.set("\n\n Bienvenido! Por favor ingrese el idioma \n en el que desea jugar:")
        self.texto.destroy()
        self.texto = Label(self)
        self.texto.config(font =self.txtFont,textvariable=self.txt)
        self.texto.place(x=110, y=20)

        self.esp = Radiobutton(self, text="Español",variable=self.radioVal, value=1,command=lambda: self.changeEspañol())
        self.esp.config(font=self.btnFont, fg="black", border= 1)
        self.esp.place(x=247, y=130)

        self.ing = Radiobutton(self, text="Inglés",variable=self.radioVal, value=2,command=lambda: self.changeIngles())
        self.ing.config(font=self.btnFont, fg="black", border= 1)
        self.ing.place(x=247, y=160)

        self.btnAtras.destroy()
        self.btnSig.destroy()
        
root = Juego()
root.mainloop()