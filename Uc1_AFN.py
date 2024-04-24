#13GIIN – Teoría de Autómatas y Lenguajes Formales
#Universidad Internacional de Valencia
#Profesor: Cuauhtémoc Ocampo
#Alumno: Joaquin Serra Prialis
#Fecha: Abril/2024

#Actividad numero 1 
#Implementación de un AFN para el Reconocimiento de Patrones. 

#Validación de direcciones de correo electrónico.
class AFN:
    def __init__(self):                                                     #Implementacion de diccionarios para representar los
        self.trancisiones = {                                               #estados y transiciones del AFN.
            "q0": {"char": ["q1"]},                                         #Estado inicial q0 a q1, donde se identificara con un caracter.
            "q1": {"char": ["q1"], "@": ["q2"]},                            #Estado q1 a q2, donde se identificará el limite con un @.
            "q2": {"char": ["q2"], ".": ["q3"]}                             #Estado q2 a q3, donde se identificará el limite con un punto.
        }
        self.estado_aceptado="q3"                                           #Estado de aceptación del AFN.

    def proceso_input(self, input_usuario):                                 #Funcion para procesar la entrada del usuario.
        estado_actual = "q0"                                                #Estado actual del AFN.
        for char in input_usuario:                                          #Bucle for de la entrada del usuario.
            estados = []                                                    #Lista para almacenar estados alcanzados.
            if char in self.trancisiones[estado_actual]:
                estados += self.trancisiones[estado_actual][char]           #Agrega los estados alcanzados a la lista estados.
                #print(estados)
            if "char" in self.trancisiones[estado_actual]:
                estados += self.trancisiones[estado_actual]["char"]         #Agrega los estados alcanzados a la lista estados.
                #print(estados)
            estado_actual = estados[0] if estados else None                 #Actualiza el estado actual.
            #print(estado_actual)
            if estado_actual is None:
                return False                                                #Retorna False si no se alcanza un estado.
        return estado_actual == self.estado_aceptado                        #Retorna el estado actual si es el estado aceptado.
    
afn = AFN()                                                                 #Instancia de la clase AFN.

strings_aceptados = ["usuario@ejemplo.com", "nombre.apellido@ejemplo.es"]   #Realizamos una lista de strings que deberian ser aceptados.
for strings in strings_aceptados:
    if afn.proceso_input(strings):                                          #Si el string es aceptado, se notifica al usuario con un mensaje.
        print(f"'{strings}' es una direccion de correo válida!!")
    else:                                                                  #Si el string no es aceptado, se notifica al usuario con un mensaje.
        print(f"'{strings}' no es una direccion de correo válida!!")
        print("Por favor, intenta ingresar un correo válido.")
        