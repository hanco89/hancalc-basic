#Importamos la librería tkinter
import tkinter as tk

#Importamos la parte grafica:
#from ui_calc.ui import Ui

class Button:
    def __init__(self, ui):
        self.ui = ui
        self.parent = ui.parent
        
        #Definimos: Texto,Fila y columna de cada boton, almacenamos la informacion en tuplas
        buttons_info = [
            ("(",1,1), (")",1,2),("%",1,3), ("C",1,4),
            ("7",2,1), ("8",2,2),("9",2,3), ("*",2,4),
            ("4",3,1), ("5",3,2),("6",3,3), ("/",3,4),
            ("1",4,1), ("2",4,2),("3",4,3), ("-",4,4),
            ("0",5,1), (".",5,2),("=",5,3), ("+",5,4)
        ]
        for text, row, column in buttons_info: #Iteramos cada boton 
            #Creamos los botones
            button = tk.Button(                           
                self.parent, #Indicamos donde queremos que se muestre el widget                                                             
                text = text, #Definimos el texto:                                                      
                font = ("arial", 10), #Le damos una fuente y un tamaño                                                                      
                width = 3, #Le damos un ancho                                                                      
                height = 1, #Le damos un alto                                                                      
                bd = 2,  #Le damos tamaño a los bordes                                                                      
                relief = "raised", #Le damos una textura de hundido                                                                                          
                bg = "#444745",  #Le damos un color gris mas claro que el fondo de la calculadora                                                                      
                fg = "#ffffff", #Le damos color oscuro al texto                                                                     
            )    
            #Ubicamos los botones usando grid
            button.grid(                        
                row = row, #Definimos la fila segun lo que hayamos puesto en la tupla:                                                   
                column = column,  #Definimos la columna segun lo que hayamos puesto en la tupla                                                   
                padx = 5, #Le damos un padding 5 en los ejes X Y                                             
                pady = 5                        
            )
            #A los botones C y = le damos un color verde y una fuente blanca
            if text == "C" or text == "=": 
                button.config(bg="#2ecc71", fg="white")
    
            #Llamamos al metodo que genera un resultado si presionamos un boton
            button.config(command = lambda val=text: self.ui.handle_input(val))