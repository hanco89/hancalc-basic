#Importamos la libreria tkinter
import tkinter as tk

#Importamos los botones
from ui_calc.buttons import Button

#Definimos la clase Ui
class Ui:
    """Clase calculadora, contiene : interfaz grafica y calculos"""
    #Creamos el metodo init
    def __init__(self, parent, logic):
        self.parent = parent #parent = ventana abierta
        self.logic = logic
        self.logic.acces_ui(self)
        self.parent.title("Hancalc") #Le damos un titulo a la calculadora
        self.parent.geometry("245x270") #Le damos un tamaño
        self.parent.configure(bg = "#2c2f2d") #Le damos un tono gris al fondo
        self.parent.resizable(False, False) #Mantenemos la pantalla en un tamaño fijo, que no sea reescalable
        self.handle_input = self.logic.handle_input #Enlazamos a los botones el manejo de operadores
        
        #Creamos una etiqueta en la que se muestra el resultado y los numeros que vamos poniendo
        self.show_result = tk.Label( 
            parent,             
            text = "0",  #Le damos un texto de muestra                                                                      
            anchor = "e", #Ubicamos el texto en "e" ("Este")                                                                    
            width = 20, #Le damos un ancho y alto                                  
            height = 2,
            bd = 2,  #Definimos el tamaño del borde
            relief = "sunken",  #Definimos que tenga un "surcado"
            bg = "#a9dfbf", #Le damos un color verde de display de calculadora
            font = ("Courier", 13)  #Le damos una fuente y un tamaño
        )       
        #Usamos grid para ubicar el display
        self.show_result.grid(                      
            row=0,  #Lo colocamos en la fila y columna 0                                                
            column=0,           
            columnspan=5,  #Indicamos que ocupe 5 columnas                                                          
            padx=10, #Que tenga un padding de 10 en los ejes X Y                                                     
            pady=10,
            sticky = "ew" #Hacemos que el widget se expanda y ocupe todo el ancho de la pantalla
        ) 
        
        self.buttons = Button(self)        