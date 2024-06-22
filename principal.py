import tkinter as tk
from cliente.vista import Frame, barrita_menu

def main():
    ventana = tk.Tk()
    fuente_negrita = ('Helvetica', 12, 'bold')
    ventana.title('Comercio')
    ventana.iconbitmap('img/storeshop.ico')
    ventana.option_add('*Font', fuente_negrita)
    ventana.resizable(0,0)

    barrita_menu(ventana)
    app = Frame(root = ventana)
    

    ventana.mainloop()

if __name__ == '__main__':
    main()