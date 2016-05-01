from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
import threading
from reproducir import play

def main():

    #Creacion de la ventana
    interfaz=Tk()

    interfaz.title("Reproductor de Audio")

    frame1 = Frame(interfaz)
    frame1.pack(side=TOP)
    frame2 = Frame(interfaz)
    frame2.pack(side=TOP)
    frame3 = Frame(interfaz)
    frame3.pack(side=TOP)
    frame4=Frame(interfaz)
    frame4.pack(side=TOP)
    frame5=Frame(interfaz)
    frame5.pack(side=TOP)

    global file1, file2, file3, file4


    #Cargar achivo1
    def open1():

        global file1
        #Obtencion de la direccion del archivo
        file1= askopenfilename()

    #Cargar archivo2
    def open2():

        global file2

        file2= askopenfilename()

    #Cargar archivo3
    def open3():

        global file3

        file3= askopenfilename()

    def open4():

        global file4

        file4= askopenfilename()

    def reproducir():

        global file1, file2, file3, file4

        t1=threading.Thread(target=Raltiempo, args=(file1,))
        t2=threading.Thread(target=Raltiempo, args=(file2,))
        t3=threading.Thread(target=Raltiempo, args=(file3,))
        t4=threading.Thread(target=Raltiempo, args=(file4,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
    def Raltiempo(nombre):

        sonido=play(1024)
        Datos=sonido.open(nombre)
        sonido.start(Datos[0],Datos[1],Datos[2])
        sonido.play(Datos[3])
        sonido.closed()



    Archivo1=Button(frame1, padx=30, pady=2,text="Cargar archivo 1",command=open1)
    Archivo1.pack(side=LEFT)

    Archivo2=Button(frame2, padx=30, pady=2,text="Cargar archivo 2",command=open2)
    Archivo2.pack(side=LEFT)

    Archivo3=Button(frame3, padx=30, pady=2,text="Cargar archivo 3",command=open3)
    Archivo3.pack(side=LEFT)

    Archivo4=Button(frame4, padx=30, pady=2,text="Cargar archivo 4",command=open4)
    Archivo4.pack(side=LEFT)

    Reproducir=Button(frame5, padx=30, pady=2,text="Reproducir tiempo real",command=reproducir)
    Reproducir.pack(side=LEFT)

    interfaz.mainloop()

if __name__=="__main__":
    main()