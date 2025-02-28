#Importamos la libreria tkinter:
import tkinter as tk

#Importamos la parte grafica:
from ui_calc.interface import Ui

#Importamos la parte logica:
from logic.logic import Logic

class Calculator:
    def __init__(self, root):
        self.root = root
        self.logic = Logic(root)
        self.ui = Ui(root, self.logic)
    
if __name__ == "__main__":                           
    root = tk.Tk() #Definimos la ventana
    window_principal = Calculator(root) #Definimos el objeto
    root.mainloop() #Ejecutamos la ventana

