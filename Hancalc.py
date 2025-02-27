#Importamos la libreria tkinter
import tkinter as tk

#Definimos la clase calculadora
class Calculator:
    
    #Creamos el metodo init
    def __init__(self,parent):
        
        #parent = ventana abierta
        self.parent = parent
        
        #Le damos un titulo a la calculadora
        self.parent.title("Hancalc")
        
        #Le damos un tamaño
        self.parent.geometry("245x270")
        
        #Le damos un tono gris al fondo
        self.parent.configure(bg = "#2c2f2d")
        
        #Mantenemos la pantalla en un tamaño fijo, que no sea reescalable
        self.parent.resizable(False, False)
        
        #Creamos una etiqueta en la que se muestra el resultado y los numeros que vamos poniendo
        self.ShowResult = tk.Label( parent,
                                   
                                   #Le damos un texto de muestra
                                    text = "0",
                                    
                                    #Ubicamos el texto en "e" ("Este")
                                    anchor = "e",
                                    
                                    #Le damos un ancho
                                    width = 20,
                                    
                                    #Le damos un alto
                                    height = 2,
                                    
                                    #Definimos el tamaño del borde
                                    bd = 2,
                                    
                                    #Definimos que tenga un "surcado"
                                    relief = "sunken",
                                    
                                    #Le damos un color verde de display de calculadora
                                    bg = "#a9dfbf",
                                    
                                    #Le damos una fuente y un tamaño
                                    font = ("Courier", 13)
                                )

        #Usamos grid para ubicar el display
        self.ShowResult.grid(
                                #Lo colocamos en la fila 0
                                row=0,
                                
                                #Y en la columna 0
                                column=0,
                                
                                #Indicamos que ocupe 5 columnas
                                columnspan=5,
                                
                                #Que tenga un pad de 10 en el eje X
                                padx=10,
                                
                                #Que tenga un pad de 10 en el eje Y
                                pady=10,
                                
                                #Hacemos que el widget se expanda y ocupe todo el ancho de la pantalla
                                sticky = "ew"
                            )
        #Diccionario para almacenar los botones y usarlos como variables para asignarles una funcion a cada uno:
        self.buttons = {}
        
        #Definimos: Texto,Fila y columna de cada boton, almacenamos la informacion en tuplas
        buttons_info = [
                                                    ("C",1,4),
                     ("7",2,1), ("8",2,2),("9",2,3), ("*",2,4),
                     ("4",3,1), ("5",3,2),("6",3,3), ("/",3,4),
                     ("1",4,1), ("2",4,2),("3",4,3), ("-",4,4),
                     ("0",5,1), (".",5,2),("=",5,3), ("+",5,4)
                    ]  
        
        #Iteramos cada boton 
        for button in buttons_info:
            
            #El indice 0 es el texto
            text = button[0]
            
            #EL indice 1 es la fila
            row = button[1]
            
            #El indice 2 es la columna
            column = button[2]     
            
            #Creamos el boton
            button = tk.Button(     #Indicamos donde queremos que se muestre el widget
                                    self.parent,
                               
                                    #Definimos el texto:
                                    text = text,
                                    
                                    #Le damos una fuente y un tamaño
                                    font = ("arial", 10),
                                    
                                    #Le damos un ancho
                                    width = 3,
                                    
                                    #Le damos un alto
                                    height = 1,
                                    
                                    #Le damos tamaño a los bordes
                                    bd = 2,
                                    
                                    #Le damos una textura de hundido
                                    relief = "raised",
                                    
                                    
                                    #Le damos un color gris mas claro que el fondo de la calculadora
                                    bg = "#444745",
                                    
                                    #Le damos color oscuro al texto
                                    fg = "#ffffff",
                                                                      
                               )    
                      
            #Ubicamos los botones
            button.grid(    #Definimos la fila segun lo que hayamos puesto en la tupla:
                            row = row,
                            
                            #Definimos la columna segun lo que hayamos puesto en la tupla
                            column = column,
                            
                            #Le damos un padding 5 en el eje X
                            padx = 5,
                            
                            #Le damos un padding 5 en el eje Y
                            pady = 5
                        
                        )
            
            #A los botones C y = le damos un color verde y una fuente blanca
            if text == "C" or text == "=":
                button.config(bg="#2ecc71", fg="white") 
                
            #Asignamos que cada vez que le demos click a un boton llame al metodo Calculo  
            #button.config(command = lambda val = text : self.Calculation(val)) 
            
            #Llamamos al metodo que valida si se ingresa
            button.config(command = lambda val = text : self.HandleInput(val))
   
                
    #Creamos un metodo que hace los calculos
    def Calculation(self,value):
        
        #Obtenemos el valor actual
        v_actual = self.ShowResult["text"]
        
        #Si se ingresa = hacemos el calculo
        if value == "=":
            
            try:
                 
                #Calculamos los datos ingresados por el usuario y lo convertimos en un string
                result = str(eval(v_actual))
                
                #Mostramos el resultado en pantalla:
                self.ShowResult.config(text = result)
            
            #Si se intenta dividir por 0 mostramos un mensaje:
            except ZeroDivisionError:
                self.ShowResult.config(text = "Cannot divide by 0")  
            
            #Si ocurre otro error, ej: 02213123 +++++ 123123
            except:
                self.ShowResult.config(text = "ERROR")  
                
        #Si ingresa el boton C        
        elif value == "C":
            
            #Se limpia el display
            self.ShowResult.config(text = "0")   
            
        #Si ingresa otro valor    
        else: 
            
            #Lo sumamos al valor que se encuentre en el display  
            self.ShowResult.config(text = v_actual + value)      
            
    #Metodo para refrescar la pantalla:        
    def RefreshScreen(self,value):
        
        #Consultamos el valor actual
        v_actual = self.ShowResult["text"]
        
        #Si es 0 entonces cambiamos el 0 por el valor que ingresemos
        if v_actual == "0":
            self.ShowResult.config(text = value)   
            
        #Si no es 0 lo concatenamos con el otro valor    
        else:
            
            self.ShowResult.config(text = v_actual + value) 
            
    #Validando si se ingresa un numero o un punto se refresca el display        
    def HandleInput(self,value):
        
        #Si es asi se quita el 0
        if value.isdigit() or value == ".":
            self.RefreshScreen(value)
            
        #Si ingresan +,-,/,* etc entonces se hacen los calculos    
        else:
            self.Calculation(value)                    
        
#Definimos la ventana
root = tk.Tk()

#Definimos el objeto 
WindowPrincipal = Calculator(root)

#Ejecutamos la ventana:
root.mainloop()

