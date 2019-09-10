
import tkinter as tk




class Demo1:
    def __init__(self, master):
        self.master = master.geometry("300x100+600+300")

        self.frame = tk.Frame(self.master)

        self.texto = tk.Label(master, text="Digite un numero hexadecimal: ")
        textBox = tk.Text(master, height=2, width=20)

        self.buttonCommit = tk.Button(master, height=1, width=10, text="Convertir",
                              command=lambda: print(textBox.get("1.0","end-1c")))
        self.texto.pack()
        textBox.pack()
        self.buttonCommit.pack()

        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

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