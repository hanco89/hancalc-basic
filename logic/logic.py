class Logic:
    def __init__(self, parent):
        self.parent = parent
        self.ui = None
        
    def acces_ui(self,ui):
        """Permite que Logic acceda a la UI para actualizarla."""
        self.ui = ui
              
    #Creamos un metodo que hace los calculos
    def calculation(self, value):
        """Realiza el cálculo según el valor ingresado."""
        if not self.ui:
            return
        current_value = self.ui.show_result["text"] #Obtenemos el valor actual
        if value == "=": #Si se ingresa el boton: "=" hacemos el calculo
            try:               
                result = str(eval(current_value)) #Calculamos los datos ingresados por el usuario y lo convertimos en un string                     
                self.ui.show_result.config(text = result) #Mostramos el resultado en pantalla    
            except ZeroDivisionError: #Si se intenta dividir por 0 mostramos un mensaje:
                self.ui.show_result.config(text = "Cannot divide by 0") 
            except Exception as error : #Si ocurre otro error, ej: 02213123 +++++ 123123
                self.ui.show_result.config(text = f"¡Error! {error}")     
        elif value == "C": #Si ingresa el boton C  
            self.ui.show_result.config(text = "0") #Se limpia el display  
        else: #Si ingresa otro valor lo sumamos al valor que se encuentre en el display           
            self.ui.show_result.config(text = current_value + value)  
            
    #Metodo para refrescar la pantalla:        
    def refresh_screen(self, value):
        """Actualiza el display con el valor ingresado.""" 
        if not self.ui:
            return     
        current_value = self.ui.show_result["text"] #Consultamos el valor actual      
        if current_value == "0": #Si es 0 entonces cambiamos el 0 por el valor que ingresemos
            self.ui.show_result.config(text = value)   
        else: #Si no es 0 lo concatenamos con el otro valor  
            self.ui.show_result.config(text = current_value + value) 
            
    #Validando si se ingresa un numero o un punto se refresca el display        
    def handle_input(self, value):
        """Determina si se debe refrescar el display o realizar un cálculo"""
        if value.isdigit() or value == ".": #Si es asi se quita el 0
            self.refresh_screen(value)
        else: #Si ingresan +,-,/,* etc entonces se hacen los calculos 
            self.calculation(value)
