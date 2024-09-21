import tkinter as tk
import random
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Portada de Inicio")
root.geometry("400x300")  # Tamaño de la ventana
root.config(bg="green")  # Cambiar el color de fondo de la ventana a verde

# Variables globales
posiciones_con_2 = []
posicion_actual = None
botones = {}

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido al Juego!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=30)


# Funciones para los botones
def nuevo_juego():
    global posiciones_con_2, posicion_actual, botones

    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("400x400")

    # Crear una lista de 16 posiciones (4x4)
    posiciones = [(fila, columna) for fila in range(4) for columna in range(4)]

    # Seleccionar aleatoriamente dos posiciones para mostrar el número 2
    posiciones_con_2 = random.sample(posiciones, 2)
    posicion_actual = posiciones_con_2[0]  # Guardar la posición actual del "2"

    # Crear un mosaico de 4x4 botones
    for fila in range(4):
        for columna in range(4):
            if (fila, columna) in posiciones_con_2:
                texto = "2"
            else:
                texto = "0"

            # Crear cada botón en la cuadrícula
            boton = tk.Button(nueva_ventana, text=texto, width=10, height=4)
            boton.grid(row=fila, column=columna, padx=5, pady=5)
            botones[(fila, columna)] = boton  # Almacenar la referencia del botón


def mover(fila, columna):
    global posiciones_con_2, posicion_actual

    # Verificar si la posición está adyacente a la posición actual
    if (abs(fila - posicion_actual[0]) == 1 and columna == posicion_actual[1]) or \
            (abs(columna - posicion_actual[1]) == 1 and fila == posicion_actual[0]):
        # Cambiar el número de posición
        botones[(fila, columna)]["text"] = "2"
        botones[posicion_actual]["text"] = "0"
        posicion_actual = (fila, columna)


def key_press(event):
    global posiciones_con_2, posicion_actual

    # Mover el "2" según la tecla presionada
    if event.keysym == 'Up':
        nueva_fila, nueva_columna = posicion_actual[0] - 1, posicion_actual[1]
    elif event.keysym == 'Down':
        nueva_fila, nueva_columna = posicion_actual[0] + 1, posicion_actual[1]
    elif event.keysym == 'Left':
        nueva_fila, nueva_columna = posicion_actual[0], posicion_actual[1] - 1
    elif event.keysym == 'Right':
        nueva_fila, nueva_columna = posicion_actual[0], posicion_actual[1] + 1
    else:
        return

    # Verificar si la nueva posición está dentro de los límites y mover
    if 0 <= nueva_fila < 4 and 0 <= nueva_columna < 4:
        mover(nueva_fila, nueva_columna)


def salir():
    root.quit()


# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar",
                        "Instrucciones del juego:\n\n1. Usa las flechas del teclado para mover el número '2'.\n2. Los ceros son espacios vacíos.\n3. ¡Gana el juego!")


# Botón para "Nuevo juego"
boton_nuevo_juego = tk.Button(root, text="Nuevo Juego", font=("Helvetica", 14), command=nuevo_juego)
boton_nuevo_juego.pack(pady=10)

# Botón para "Cómo jugar"
boton_como_jugar = tk.Button(root, text="Cómo Jugar", font=("Helvetica", 14), command=mostrar_instrucciones)
boton_como_jugar.pack(pady=10)

# Botón para "Salir"
boton_salir = tk.Button(root, text="Salir", font=("Helvetica", 14), command=salir)
boton_salir.pack(pady=10)

# Enlazar eventos de teclado
root.bind("<Key>", key_press)

# Iniciar el bucle principal de la ventana
root.mainloop()
