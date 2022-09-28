from tkinter import *

def ventanaCreate(v):
    v.title("Adivinador de numero") 
    v.geometry("1366x700")
    v.resizable(width=False, height=False)
    v.configure(bg="#2c2638")

def atras(var1, var2):
    var1.withdraw()
    var2.deiconify()
    
def paso1():
    global v1,radioVal
    v1 = Tk()
    ventanaCreate(v1)
    
    texto = Label(v1,text="¡Bienvenido! \n\n Por favor ingrese el idioma en el que desea jugar:")
    texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))
    texto.place(x=181, y=165)

    radioVal = IntVar() 

    esp = Radiobutton(v1, text="Español",variable=radioVal, value=1, command=lambda: paso2())
    esp.config(fg="#ffa7c4", bg='#353042',font=("Verdana",30),width = 20)
    esp.place(x=412, y=370)

    ing = Radiobutton(v1, text="Inglés",variable=radioVal, value=2, command=lambda: paso2())
    ing.config(fg="#ffa7c4", bg='#353042',font=("Verdana",30),width = 20)
    ing.place(x=412, y=460)

    v1.mainloop()

def paso2():
    global v2
    v1.withdraw()
    v2 = Tk()
    ventanaCreate(v2)

    if radioVal.get() == 1:
        texto = Label(v2,text="Por favor, piensa en un número entero de\n dos cifras, que no sean iguales.\n\n ¿Listo?")
        texto.place(x=263, y=171)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        cont = Button(v2, text="Continuar", command=lambda: paso3())
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v2, text="Volver", command=lambda: atras(v2, v1))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)

    elif radioVal.get() == 2:
        texto = Label(v2,text="Think of a two-digit number (not equal). \n\n Done?")
        texto.place(x=273, y=160)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        cont = Button(v2, text="Continue", command=lambda: paso3())
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v2, text="Return", command=lambda: atras(v2, v1))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)
    
    v2.mainloop()

def paso3():

    global v3, mayorMenor
    v2.withdraw()

    v3 = Tk()
    ventanaCreate(v3)

    mayorMenor= IntVar(v3, "")

    if radioVal.get() == 1:
        texto = Label(v3,text="Bien, ahora invertí el orden de las cifras.\n\n Luego, ingrese si el numero es mayor or menor")
        texto.place(x=151, y=80)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        mayor = Radiobutton(v3, text="Mayor",variable=mayorMenor, value=1, command=lambda: paso4())
        mayor.config(fg="#ffa7c4", bg='#353042',font=("Verdana",30),width = 20)
        mayor.place(x=412, y=283)

        menor = Radiobutton(v3, text="Menor",variable=mayorMenor, value=2, command=lambda: paso4())
        menor.config(fg="#ffa7c4", bg='#353042',font=("Verdana",30),width = 20)
        menor.place(x=412, y=372)

        volver = Button(v3, text="Volver", command=lambda: atras(v3, v2))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=517, y=500)

    elif radioVal.get() == 2:
        texto = Label(v3,text="Now reverse the order of the figures. \n Then, enter if the new number is \n higher or lower than the first")
        texto.place(x=310, y=80)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        mayor = Radiobutton(v3, text="Higher",variable=mayorMenor, value=1, command=lambda: paso4())
        mayor.config(fg="#ffa7c4", bg='#353042',font=("Verdana",30),width = 20)
        mayor.place(x=412, y=283)

        menor = Radiobutton(v3, text="Lower",variable=mayorMenor, value=2,command=lambda: paso4())
        menor.config(fg="#ffa7c4", bg='#353042',font=("Verdana",30),width = 20)
        menor.place(x=412, y=372)

        volver = Button(v3, text="Return", command=lambda: atras(v3, v2))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=517, y=500)
    
    v3.mainloop()

def paso4():
    global v4, restaValue
    v3.withdraw()
    v4 = Tk()
    ventanaCreate(v4)
    restaValue = IntVar(v4, 0)

    if radioVal.get() == 1:
        texto = Label(v4,text="Ahora, al numero mayor restale el menor. \n\n Ingrese el resultado:")
        texto.place(x=261, y=80)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        resta = Entry(v4,textvariable=restaValue)
        resta.config(fg="#2c2638", bg='#ffa7c4',font=("Verdana",30))
        resta.place(x=432, y=298)

        cont = Button(v4, text="Continuar", command=lambda: paso5())
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v4, text="Volver", command=lambda: atras(v4, v3))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)
    
    if radioVal.get() == 2:
        texto = Label(v4,text="To the higher number subtract the lower one. \n\n Enter the result:")
        texto.place(x=225, y=80)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        resta = Entry(v4,textvariable=restaValue)
        resta.config(fg="#2c2638", bg='#ffa7c4',font=("Verdana",30))
        resta.place(x=432, y=298)

        cont = Button(v4, text="Continue", command=lambda: paso5())
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v4, text="Return", command=lambda: atras(v4, v3))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)

def paso5():
    global v5, sumaValue
    v4.withdraw()
    v5 = Tk()
    ventanaCreate(v5)
    sumaValue = IntVar(v5, 0)

    if radioVal.get() == 1:
        texto = Label(v5,text="Luego sumá las cifras del número \nque pensaste al principio. \n\n Ingrese el resultado:")
        texto.place(x=349, y=80)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        resta = Entry(v5,textvariable=sumaValue)
        resta.config(fg="#2c2638", bg='#ffa7c4',font=("Verdana",30))
        resta.place(x=432, y=298)

        cont = Button(v5, text="Continuar", command=lambda: paso6())
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v5, text="Volver", command=lambda: atras(v5, v4))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)
    
    if radioVal.get() == 2:
        texto = Label(v5,text="Now add the digits of the number \n you thought at the beginning. \n\n Enter the result? ")
        texto.place(x=349, y=70)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",30))

        resta = Entry(v5,textvariable=sumaValue)
        resta.config(fg="#2c2638", bg='#ffa7c4',font=("Verdana",30))
        resta.place(x=432, y=298)

        cont = Button(v5, text="Continue", command=lambda: paso6())
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v5, text="Return", command=lambda: atras(v5, v4))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)

def paso6():
    global v6
    v5.withdraw()
    v6 = Tk()
    ventanaCreate(v6)
    txt = StringVar(v6, "")

    num1 = int(restaValue.get())
    num2 = int(sumaValue.get())
    rta = calcular(num1, num2)

    if radioVal.get() == 1:
        txt.set("Pensaste en el numero: \n\n" + str(rta))
        texto = Label(v6,textvariable=txt)
        texto.place(x=349, y=120)

        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",40))
        cont = Button(v6, text="Volver a jugar", command=lambda: atras(v6, v1))
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 15, border = 0)
        cont.place(x=633, y=418)

        volver = Button(v6, text="Volver", command=lambda: atras(v6, v5))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=229, y=418)
    
    
    if radioVal.get() == 2:
        txt.set("You thought on the number: \n\n" + str(rta))
        texto = Label(v6,textvariable=txt)
        texto.place(x=303, y=120)
        texto.config(fg="#ffa7c4", bg='#2c2638',font=("Verdana",40))
    
        cont = Button(v6, text="Restart", command=lambda: atras(v6, v1))
        cont.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        cont.place(x=715, y=418)

        volver = Button(v6, text="Return", command=lambda: atras(v6, v5))
        volver.config(fg="#353042", bg='#ffa7c4',font=("Verdana",40),width = 10, border = 0)
        volver.place(x=313, y=418)


def calcular(n1, n2):

    parametro = n1 / 9

    if mayorMenor.get() == 1:
         d1 = (n2 - parametro) / 2
         d2 = (n2 + parametro) / 2
         respuesta = int(d1) * 10 + int(d2)
    
    if mayorMenor.get() == 2:
         d1 = (n2 - parametro) / 2
         d2 = (n2 + parametro) / 2
         respuesta = int(d2) * 10 + int(d1)

    return respuesta

paso1()
