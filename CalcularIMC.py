import tkinter as tk 
from tkinter import ttk
from ClaseIMC  import *

def calcularIMC():
    try:
        
        peso = float(input_peso.get())
        altura = float(input_altura.get())

        persona = Persona()

        persona.valorerror(peso, altura) 

        imc = persona.calcularIndicedeMasaCorporal() 
 
        clasificacion = persona.clasificarimc() 
     
       
        etiqueta_IMC.config(text=f"Tu IMC es: {imc:.1f}")   
        # {imc:.1f} sirve para redondear la respuesta en un decimal
        etiqueta_rango.config(text=f"Tu categoría es: {clasificacion}")
        etiqueta_error_peso.config(text="")
        etiqueta_error_altura.config(text="")
    
        # Controlador para los errores.
    except ValueError as ve:
        if "peso" in str(ve):
         
            etiqueta_error_peso.config(text="Ingresa un peso válido.")

        elif "altura" in str(ve):
        
            etiqueta_error_altura.config(text="Ingresa una altura válida.")
        else:
            etiqueta_error_peso.config(text="Ingresa un peso válido.")
            etiqueta_error_altura.config(text="Ingresa una altura válida.")

ventana=tk.Tk()
ventana.title("Indice de masa corporal")
ventana.config(width=500, height=500)

etiqueta_peso=ttk.Label(text="Introduce tu peso en kilogramos")
etiqueta_peso.place (x=20,y=20)

etiqueta_altura=ttk.Label(text="Introduce tu altura en metros")
etiqueta_altura.place (x=20,y=45)

#Etiquetas de ubicacion para los errores
etiqueta_error_peso=ttk.Label()
etiqueta_error_peso.place (x=300,y=20)

etiqueta_error_altura=ttk.Label()
etiqueta_error_altura.place (x=300,y=45)

input_peso=ttk.Entry()
input_peso.place(x=200,y=20, width=80)

input_altura=ttk.Entry()
input_altura.place(x=200,y=45, width=80)

boton_calcular=ttk.Button(text="Calcular",command=calcularIMC)
boton_calcular.place(x=100,y=90)

etiqueta_IMC=ttk.Label(text="Tu indice de masa corporal es:")
etiqueta_IMC.place (x=20,y=130)

etiqueta_rango=ttk.Label(text="Tu categoria es: ")
etiqueta_rango.place (x=20, y=150)
ventana.mainloop()

