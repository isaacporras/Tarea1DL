from tkinter import *

from tkinter import messagebox

def error(cadena):
    p5 = int(str(cadena[4]+"0"+"0"+"0"),2)
    p4 = int(str(cadena[3]+"0"+"0"+"0"),2)
    p3 = int(str(cadena[2]+"0"+"0"),2)
    p2 = int(str(cadena[1]+"0"),2)
    p1 = int(str(cadena[0]),2)

    result = p5+p4+p3+p2+p1
    return str(result)

def codigoHamming(cadena):
    p1 = [cadena[0],cadena[1],cadena[3],cadena[4],cadena[6],cadena[8],cadena[10],cadena[11]]
    p2 = [cadena[0],cadena[2],cadena[3],cadena[5],cadena[6],cadena[9],cadena[10]]
    p3 = [cadena[1],cadena[2],cadena[3],cadena[7],cadena[8],cadena[9],cadena[10]]
    p4 = [cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10]]
    p5 = [cadena[11]]

    palabraDatosSinParidad = ["_","_",cadena[0],"_",cadena[1],cadena[2],cadena[3],"_",cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10],"_",cadena[11]]

    fp1=[paridadPar(p1),"_",cadena[0],"_",cadena[1],"_",cadena[3],"_",cadena[4],"_",cadena[6],"_",cadena[8],"_",cadena[10],"_",cadena[11]]
    fp2=["_",paridadPar(p2),cadena[0],"_","_",cadena[2],cadena[3],"_","_",cadena[5],cadena[6],"_","_",cadena[9],cadena[10],"_","_"]
    fp3=["_","_","_",paridadPar(p3),cadena[1],cadena[2],cadena[3],"_","_","_","_",cadena[7],cadena[8],cadena[9],cadena[10],"_","_"]
    fp4=["_","_","_","_","_","_","_",paridadPar(p4),cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10],"_","_"]
    fp5=["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",paridadPar(p5),cadena[11]]

    palabraDatosParidad = [paridadPar(p1),paridadPar(p2),cadena[0],paridadPar(p3),cadena[1],cadena[2],cadena[3],paridadPar(p4),cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10], paridadPar(p5),cadena[11]]

    resultado = [palabraDatosSinParidad,fp1,fp2,fp3,fp4,fp5,palabraDatosParidad]

    return resultado

def codigoHammingImpar(cadena):
    p1 = [cadena[0],cadena[1],cadena[3],cadena[4],cadena[6],cadena[8],cadena[10],cadena[11]]
    p2 = [cadena[0],cadena[2],cadena[3],cadena[5],cadena[6],cadena[9],cadena[10]]
    p3 = [cadena[1],cadena[2],cadena[3],cadena[7],cadena[8],cadena[9],cadena[10]]
    p4 = [cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10]]
    p5 = [cadena[11]]

    palabraDatosSinParidad = ["_","_",cadena[0],"_",cadena[1],cadena[2],cadena[3],"_",cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10],"_",cadena[11]]

    fp1=[paridadImpar(p1),"_",cadena[0],"_",cadena[1],"_",cadena[3],"_",cadena[4],"_",cadena[6],"_",cadena[8],"_",cadena[10],"_",cadena[11]]
    fp2=["_",paridadImpar(p2),cadena[0],"_","_",cadena[2],cadena[3],"_","_",cadena[5],cadena[6],"_","_",cadena[9],cadena[10],"_","_"]
    fp3=["_","_","_",paridadImpar(p3),cadena[1],cadena[2],cadena[3],"_","_","_","_",cadena[7],cadena[8],cadena[9],cadena[10],"_","_"]
    fp4=["_","_","_","_","_","_","_",paridadImpar(p4),cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10],"_","_"]
    fp5=["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",paridadImpar(p5),cadena[11]]

    palabraDatosParidad = [paridadImpar(p1),paridadImpar(p2),cadena[0],paridadImpar(p3),cadena[1],cadena[2],cadena[3],paridadImpar(p4),cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10], paridadImpar(p5),cadena[11]]

    resultado = [palabraDatosSinParidad,fp1,fp2,fp3,fp4,fp5,palabraDatosParidad]

    return resultado

def comprobacion(cadena,pruebaParidad):

    sinParidad = [cadena[2],cadena[4],cadena[5],cadena[6],cadena[8],cadena[9],cadena[10],cadena[11],cadena[12],cadena[13],cadena[14],cadena[16]]

    p1 = [sinParidad[0],sinParidad[1],sinParidad[3],sinParidad[4],sinParidad[6],sinParidad[8],sinParidad[10],sinParidad[11]]
    p2 = [sinParidad[0],sinParidad[2],sinParidad[3],sinParidad[5],sinParidad[6],sinParidad[9],sinParidad[10]]
    p3 = [sinParidad[1],sinParidad[2],sinParidad[3],sinParidad[7],sinParidad[8],sinParidad[9],sinParidad[10]]
    p4 = [sinParidad[4],sinParidad[5],sinParidad[6],sinParidad[7],sinParidad[8],sinParidad[9],sinParidad[10]]
    p5 = [sinParidad[11]]

    datosRecibidos = list(cadena) + [str(pruebaParidad)]+["_"]
    fp1=[paridadPar(p1),"_",cadena[0],"_",cadena[1],"_",cadena[3],"_",cadena[4],"_",cadena[6],"_",cadena[8],"_",cadena[10],"_",cadena[11]]+ aux_comprobacion(cadena[0],p1)
    fp2=["_",paridadPar(p2),cadena[0],"_","_",cadena[2],cadena[3],"_","_",cadena[5],cadena[6],"_","_",cadena[9],cadena[10],"_","_"]+ aux_comprobacion(cadena[1],p2)
    fp3=["_","_","_",paridadPar(p3),cadena[1],cadena[2],cadena[3],"_","_","_","_",cadena[7],cadena[8],cadena[9],cadena[10],"_","_"]+ aux_comprobacion(cadena[3],p3)
    fp4=["_","_","_","_","_","_","_",paridadPar(p4),cadena[4],cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10],"_","_"]+ aux_comprobacion(cadena[7],p4)
    fp5=["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",paridadPar(p5),cadena[11]]+ aux_comprobacion(cadena[15],p5)

    result = [datosRecibidos,fp1,fp2,fp3,fp4,fp5]

    return result

def aux_comprobacion(result,paridad):
    if result != paridadPar(paridad):
        return ["Error","1"]
    else:
        return ["Correcto","0"]

def comprobacionSimplificada(cadena):
    sinParidad = [cadena[2],cadena[4],cadena[5],cadena[6],cadena[8],cadena[9],cadena[10],cadena[11],cadena[12],cadena[13],cadena[14],cadena[16]]

    p1 = [sinParidad[0],sinParidad[1],sinParidad[3],sinParidad[4],sinParidad[6],sinParidad[8],sinParidad[10],sinParidad[11]]
    p2 = [sinParidad[0],sinParidad[2],sinParidad[3],sinParidad[5],sinParidad[6],sinParidad[9],sinParidad[10]]
    p3 = [sinParidad[1],sinParidad[2],sinParidad[3],sinParidad[7],sinParidad[8],sinParidad[9],sinParidad[10]]
    p4 = [sinParidad[4],sinParidad[5],sinParidad[6],sinParidad[7],sinParidad[8],sinParidad[9],sinParidad[10]]
    p5 = [sinParidad[11]]

    if aux_comprobacionSimplificada(cadena[0],p1)== "Error":
        return "Error"
    if aux_comprobacionSimplificada(cadena[1],p2)== "Error":
        return "Error"
    if aux_comprobacionSimplificada(cadena[3],p3)== "Error":
        return "Error"
    if aux_comprobacionSimplificada(cadena[7],p4)== "Error":
        return "Error"
    if aux_comprobacionSimplificada(cadena[15],p5)== "Error":
        return "Error"
    else:
        return "Correcto"

def aux_comprobacionSimplificada(result,paridad):
    if result != paridadPar(paridad):
        return "Error"
    else:
        return "Correcto"

def paridadPar(cadena):
    contador= 0

    for x in cadena:
        if (x == "1"):
            contador+=1

    if (contador%2 != 0):
        return "0"
    else:
        return "1"

def paridadImpar(cadena):
    contador= 0

    for x in cadena:
        if (x == "1"):
            contador+=1

    if (contador%2 != 0):
        return "1"
    else:
        return "0"

def ventana1(hilera):
    root = Tk()
    root.title("Tabla No 1. Calculo de bits de paridad en el codigo Hamming")
    data = codigoHamming(hilera)
    for r in range(0, 8):
        for c in range(0, 18):
            size = 30
            if c > 0:
                size = 10
            cell = Entry(root, width=size)
            cell.grid(row=r, column=c)
            if c == 0 and r == 7:
                cell.insert(0, "Palabra de datos(con paridad):")
            if r == 0 and c > 0:
                if c == 1:
                    cell.insert(0, "p1")
                    continue
                if c == 2:
                    cell.insert(0, "p2")
                    continue
                if c == 3:
                    cell.insert(0, "d1")
                    continue
                if c == 4:
                    cell.insert(0, "p3")
                    continue
                if c == 5:
                    cell.insert(0, "d2")
                    continue
                if c == 6:
                    cell.insert(0, "d3")
                    continue
                if c == 7:
                    cell.insert(0, "d4")
                    continue
                if c == 8:
                    cell.insert(0, "p4")
                    continue
                if c == 9:
                    cell.insert(0, "d5")
                    continue
                if c == 10:
                    cell.insert(0, "d6")
                    continue

                if c == 11:
                    cell.insert(0, "d7")
                    continue

                if c == 12:
                    cell.insert(0, "d8")
                    continue

                if c == 13:
                    cell.insert(0, "d9")
                    continue

                if c == 14:
                    cell.insert(0, "d10")
                    continue

                if c == 15:
                    cell.insert(0, "d11")
                    continue

                if c == 16:
                    cell.insert(0, "p5")
                    continue

                if c == 17:
                    cell.insert(0, "d12")
                    continue

            if c == 0 and r == 2:
                cell.insert(0, "p1")
                continue

            if c == 0 and r == 3:
                cell.insert(0, "p2")
                continue

            if c == 0 and r == 4:
                cell.insert(0, "p3")
                continue

            if c == 0 and r == 5:
                cell.insert(0, "p4")
                continue

            if c == 0 and r == 6:
                cell.insert(0, "p5")
                continue

            if c == 0 and r == 1:
                cell.insert(0, "Palabra de datos(sin paridad):")
                continue

            if r == 1 and c>0:
                cell.insert(1, data[0][c-1])
                continue

            if r == 2 and c>0:
                cell.insert(2, data[1][c-1])
                continue

            if r == 3 and c>0:
                cell.insert(3, data[2][c-1])
                continue

            if r == 4 and c>0:
                cell.insert(4, data[3][c-1])
                continue

            if r == 5 and c>0:
                cell.insert(5, data[4][c-1])
                continue

            if r == 6 and c>0:
                cell.insert(6, data[5][c-1])
                continue

            if r == 7 and c>0:
                cell.insert(7, data[6][c-1])
                continue

    completa = "".join(data[6])
    print(completa)
    ventana2(completa)
    root.mainloop()

def ventana2(hilera):
    root = Tk()
    root.title("Tabla No.2 Comprobacion de los bits de paridad (con primer bit de la derecha cambiado)")
    data = comprobacion(hilera,1)
    for r in range(0, 7):
        for c in range(0, 20):
            size = 10
            if c > 0 and c < 12:
                size = 15
            cell = Entry(root, width=size)
            cell.grid(row=r, column=c)

            if r == 0 and c > 0 and c < 18:
                if c == 1:
                    cell.insert(0, "p1")
                    continue
                if c == 2:
                    cell.insert(0, "p2")
                    continue
                if c == 3:
                    cell.insert(0, "d1")
                    continue
                if c == 4:
                    cell.insert(0, "p3")
                    continue
                if c == 5:
                    cell.insert(0, "d2")
                    continue
                if c == 6:
                    cell.insert(0, "d3")
                    continue
                if c == 7:
                    cell.insert(0, "d4")
                    continue
                if c == 8:
                    cell.insert(0, "p4")
                    continue
                if c == 9:
                    cell.insert(0, "d5")
                    continue
                if c == 10:
                    cell.insert(0, "d6")
                    continue
                if c == 11:
                    cell.insert(0, "d7")
                    continue
                if c == 12:
                    cell.insert(0, "d8")
                    continue
                if c == 13:
                    cell.insert(0, "d9")
                    continue
                if c == 14:
                    cell.insert(0, "d10")
                    continue
                if c == 15:
                    cell.insert(0, "d11")
                    continue
                if c == 16:
                    cell.insert(0, "p5")
                    continue
                if c == 17:
                    cell.insert(0, "d12")
                    continue
            if c == 18 and r == 0:
                cell.insert(0, "Prueba Paridad")

            if c == 19 and r == 0:
                cell.insert(0, "Bit Paridad")
                continue

            if c == 0 and r == 1:
                cell.insert(0, "Palabra de datos recibida:")
                continue

            if c == 0 and r == 2:
                cell.insert(0, "p1")
                continue

            if c == 0 and r == 3:
                cell.insert(0, "p2")
                continue

            if c == 0 and r == 4:
                cell.insert(0, "p3")
                continue

            if c == 0 and r == 5:
                cell.insert(0, "p4")
                continue

            if c == 0 and r == 6:
                cell.insert(0, "p5")
                continue

            if r == 1 and c>0:
                cell.insert(1, data[0][c-1])
                continue

            if r == 2 and c>0:
                cell.insert(2, data[1][c-1])
                continue

            if r == 3 and c>0:
                cell.insert(3, data[2][c-1])
                continue

            if r == 4 and c>0:
                cell.insert(4, data[3][c-1])
                continue

            if r == 5 and c>0:
                cell.insert(5, data[4][c-1])
                continue

            if r == 6 and c>0:
                cell.insert(6, data[5][c-1])
                continue


    print("-----------------------------------------------------------------------------")
    print(hilera)
    print(comprobacionSimplificada(hilera))
    if comprobacionSimplificada(hilera) == "Error":
        result = [data[1][18],data[2][18],data[3][18],data[4][18],data[5][18]]
        aux_result = "".join(result)
        print("------------------------")
        print(result)
        final = error(aux_result)
        messagebox.showinfo("El Error", "El error se encuentra en el bit: "+ final)

    ventana3()
    root.mainloop()

def ventana3():
    root = Tk()
    root.title("Prueba de fallo")
    root.geometry("800x200+600+300")
    frame = Frame(root)

    label = Label(root, text= "Desea cambiar uno de los bits de la hilera original para obligar a una falla ?", font = ("Helvetica",12)).pack(side = TOP)
    si = Button(frame,text="SI",command =lambda:{root.quit(),ventana4()
                                                       }).pack(side=LEFT)
    no = Button(frame,text="NO",command = lambda:root.destroy()).pack()

    frame.pack()
    root.mainloop()

def ventana4():
    root = Tk()
    root.title("Seleccion de bit")
    root.geometry("500x200+600+300")
    frame = Frame(root)

    label = Label(root, text= "Modifique la hilera binaria", font = ("Helvetica",14)).pack(side = TOP)

    e = Entry(root)
    e.pack()

    def get_hilera():
        x = e.get()
        return str(x)

    boton = Button(frame,text="Listo",command =lambda:{root.quit(),ventana2(get_hilera())
                                                       }).pack(side=LEFT)
    frame.pack()
    root.mainloop()

def ventana5(hilera):
    root = Tk()
    root.title("Tabla No 1. Calculo de bits de paridad en el codigo Hamming")
    data = codigoHammingImpar(hilera)
    for r in range(0, 7):
        for c in range(0, 12):
            size = 30
            if c > 0:
                size = 10
            cell = Entry(root, width=size)
            cell.grid(row=r, column=c)
            if c == 0 and r == 6:
                cell.insert(0, "Palabra de datos(con paridad):")
            if r == 0 and c > 0:
                if c == 1:
                    cell.insert(0, "p1")
                    continue
                if c == 2:
                    cell.insert(0, "p2")
                    continue
                if c == 3:
                    cell.insert(0, "d1")
                    continue
                if c == 4:
                    cell.insert(0, "p3")
                    continue
                if c == 5:
                    cell.insert(0, "d2")
                    continue
                if c == 6:
                    cell.insert(0, "d3")
                    continue
                if c == 7:
                    cell.insert(0, "d4")
                    continue
                if c == 8:
                    cell.insert(0, "p4")
                    continue
                if c == 9:
                    cell.insert(0, "d5")
                    continue
                if c == 10:
                    cell.insert(0, "d6")
                    continue
                if c == 11:
                    cell.insert(0, "d7")
                    continue
            if c == 0 and r > 1:
                cell.insert(0, "p" + str(r-1))
                continue
            if c == 0 and r == 1:
                cell.insert(0, "Palabra de datos(sin paridad):")
                continue

            if r == 1 and c>0:
                cell.insert(1, data[0][c-1])
                continue

            if r == 2 and c>0:
                cell.insert(2, data[1][c-1])
                continue

            if r == 3 and c>0:
                cell.insert(3, data[2][c-1])
                continue

            if r == 4 and c>0:
                cell.insert(4, data[3][c-1])
                continue

            if r == 5 and c>0:
                cell.insert(5, data[4][c-1])
                continue

            if r == 6 and c>0:
                cell.insert(6, data[5][c-1])
                continue
    completa = "".join(data[5])
    print(completa)
    ventana2(completa)
    root.mainloop()

def paridad_window():
    root = Tk()
    root.title("Codigo Hamming")
    frame = Frame(root)
    label1 = Label(root, text= "Aplicacion del codigo de Hamming", font = ("Helvetica",18)).pack()
    label = Label(root, text= "Introduzca hilera binaria:", font = ("Helvetica",14)).pack()

    e = Entry(root)
    e.pack()

    def get_hilera():
        x = e.get()
        return str(x)

    label = Label(root, fg="dark green", text= "Seleccione la paridad", font = ("Helvetica",14)).pack()
    root.geometry("500x300+600+300")
    impar = Button(frame,text="Paridad Par",command =lambda:{root.quit(),ventana5(get_hilera())
                                                       }).pack(side=LEFT)
    par = Button(frame,text="Paridad Impar",command = lambda:{root.quit(),ventana1(get_hilera())}).pack(side=RIGHT)

    exit = Button(frame,text="Salir",command = lambda:root.destroy()).pack()
    e.pack()
    frame.pack()
    root.mainloop()


paridad_window()
