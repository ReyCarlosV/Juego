import tkinter as tk
from tkinter import messagebox
import random

# Crear la ventana principal
root = tk.Tk()
root.title("Portada de Inicio")
root.geometry("400x300")  # Tamaño de la ventana
root.config(bg="green")  # Cambiar el color de fondo de la ventana a verde

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido al Juego!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=30)


# Funciones para los botones
def nuevo_juego():
    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("400x400")

    # Crear una lista de todas las posiciones en el mosaico (16 posiciones para 4x4)
    posiciones = [(fila, columna) for fila in range(4) for columna in range(4)]

    # Seleccionar dos posiciones al azar para poner el número "2"
    posiciones_con_2 = random.sample(posiciones, 2)

    # Crear el mosaico de botones de 4x4
    for fila in range(4):
        for columna in range(4):
            # Si la posición actual está entre las posiciones seleccionadas, muestra "2"
            if (fila, columna) in posiciones_con_2:
                boton = tk.Button(nueva_ventana, text="2", width=10, height=4)
            else:
                boton = tk.Button(nueva_ventana, text="0", width=10, height=4)
            boton.grid(row=fila, column=columna, padx=5, pady=5)


def salir():
    root.quit()


# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar",
                        "Instrucciones del juego:\n\n1. Hacer esto.\n2. Luego hacer aquello.\n3. ¡Gana el juego!")


# Botón para "Nuevo juego"
boton_nuevo_juego = tk.Button(root, text="Nuevo Juego", font=("Helvetica", 14), command=nuevo_juego)
boton_nuevo_juego.pack(pady=10)

# Botón para "Cómo jugar"
boton_como_jugar = tk.Button(root, text="Cómo Jugar", font=("Helvetica", 14), command=mostrar_instrucciones)
boton_como_jugar.pack(pady=10)

# Botón para "Salir"
boton_salir = tk.Button(root, text="Salir", font=("Helvetica", 14), command=salir)
boton_salir.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
