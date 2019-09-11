
import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import messagebox


def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

class Demo1:
    def __init__(self, master):
        self.master = master.geometry("300x100+600+300")

        self.frame = tk.Frame(self.master)

        self.texto = tk.Label(master, text="Digite un numero hexadecimal: ")
        textBox = tk.Text(master, height=2, width=20)

        self.buttonCommit = tk.Button(master, height=1, width=10, text="Convertir", command=lambda: self.validate_input(textBox.get("1.0","end-1c")))
        self.texto.pack()
        textBox.pack()
        self.buttonCommit.pack()

        self.frame.pack()

    def validate_input(self, numero):
        if is_hex(numero) and (len(numero) == 3):
            self.new_window(numero)
        else:
            messagebox.showerror("Error", "Entrada no valida.")


    def new_window(self, numero):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow,int(numero, 16))



class Demo2:
    def __init__(self, master, numero):
        print(numero)

        binario = binarizar(numero)

        while len(binario)!= 12:
            binario = "0" + binario

        print(binario)
        self.master = master
        self.master.geometry("1500x500+10+100")



        canvas = Canvas(self.master)
        diferencial = 105
        x = 120

        canvas.create_line(15, 30, 15, 450)  # linea horizontal x
        canvas.create_line(15, 250, 1400, 250) # linea horizontal y

        alto_bit_x1 = 15
        alto_bit_x2 = 120
        alto_bit_y1 = 130
        alto_bit_y2 = 130

        bajo_bit_x1 = 15
        bajo_bit_x2 = 120
        bajo_bit_y1 = 370
        bajo_bit_y2 = 370

        canvas.create_line(x, 100, x, 400, dash=(4, 2))
        canvas.create_line(x + 1*diferencial, 100, x + 1*diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 2 * diferencial, 100, x + 2 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 3 * diferencial, 100, x + 3 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 4 * diferencial, 100, x + 4 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 5 * diferencial, 100, x + 5 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 6 * diferencial, 100, x + 6 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 7 * diferencial, 100, x + 7 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 8 * diferencial, 100, x + 8 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 9 * diferencial, 100, x + 9 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 10 * diferencial, 100, x + 10 * diferencial, 400, dash=(4, 2))
        canvas.create_line(x + 11* diferencial, 100, x + 11 * diferencial, 400, dash=(4, 2))



        estado_actual = "alto"
        bit_actual = 0
        for num in binario:
            if estado_actual == "alto":
                if num == "1":
                    estado_actual = "bajo"
                    print("Cambia de estado a bajo")
                elif num == "0":
                    estado_actual = "alto"
                    print("El numero se queda en alto")

            elif estado_actual == "bajo":
                if num == "1":
                    estado_actual = "alto"
                    print("Cambia de estado a alto")
                elif num == "0":
                    estado_actual = "bajo"
                    print("El numero se queda en bajo")

            if estado_actual == "alto":
                canvas.create_line(alto_bit_x1 + bit_actual*diferencial, alto_bit_y1, alto_bit_x2+ bit_actual*diferencial, alto_bit_y2, fill="red")
                bit_actual = bit_actual + 1
            if estado_actual == "bajo":
                canvas.create_line(bajo_bit_x1 + bit_actual*diferencial, bajo_bit_y1, bajo_bit_x2 + bit_actual*diferencial, bajo_bit_y2, fill="red")
                bit_actual = bit_actual + 1

            print(num)




        canvas.pack(fill=BOTH, expand=1)




    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Bienvenido!")
    root.resizable(False, False)
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()