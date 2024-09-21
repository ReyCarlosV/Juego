import tkinter as tk
import random
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Portada de Inicio")
root.geometry("400x300")  # Tamaño de la ventana
root.config(bg="green")  # Cambiar el color de fondo de la ventana a verde

# Variables globales
posiciones_con_numeros = []
posicion_vacia = None
botones = {}

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido al Juego!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=30)


# Funciones para los botones
def nuevo_juego():
    global posiciones_con_numeros, posicion_vacia, botones

    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("400x400")

    # Crear una lista de 16 posiciones (4x4)
    posiciones = [(fila, columna) for fila in range(4) for columna in range(4)]

    # Seleccionar aleatoriamente dos posiciones para mostrar el número 2
    posiciones_con_numeros = random.sample(posiciones, 2)  # Dos números "2"

    # Seleccionar una posición para el espacio vacío
    posicion_vacia = random.choice([pos for pos in posiciones if pos not in posiciones_con_numeros])

    # Crear un mosaico de 4x4 botones
    for fila in range(4):
        for columna in range(4):
            if (fila, columna) in posiciones_con_numeros:
                texto = "2"  # Mostrar el número "2" en las posiciones elegidas
            else:
                texto = ""  # Espacio vacío
            # Crear cada botón en la cuadrícula
            boton = tk.Button(nueva_ventana, text=texto, width=10, height=4)
            boton.grid(row=fila, column=columna, padx=5, pady=5)
            botones[(fila, columna)] = boton  # Almacenar la referencia del botón


def mover_todos(direccion):
    global posiciones_con_numeros, posicion_vacia

    fila_vacia, columna_vacia = posicion_vacia

    if direccion == "Up" and fila_vacia < 3:  # El espacio vacío debe estar por debajo
        fila_a_mover = fila_vacia + 1
        if (fila_a_mover, columna_vacia) in posiciones_con_numeros:
            mover_boton(fila_a_mover, columna_vacia)

    elif direccion == "Down" and fila_vacia > 0:  # El espacio vacío debe estar por encima
        fila_a_mover = fila_vacia - 1
        if (fila_a_mover, columna_vacia) in posiciones_con_numeros:
            mover_boton(fila_a_mover, columna_vacia)

    elif direccion == "Left" and columna_vacia < 3:  # El espacio vacío debe estar a la derecha
        columna_a_mover = columna_vacia + 1
        if (fila_vacia, columna_a_mover) in posiciones_con_numeros:
            mover_boton(fila_vacia, columna_a_mover)

    elif direccion == "Right" and columna_vacia > 0:  # El espacio vacío debe estar a la izquierda
        columna_a_mover = columna_vacia - 1
        if (fila_vacia, columna_a_mover) in posiciones_con_numeros:
            mover_boton(fila_vacia, columna_a_mover)


def mover_boton(fila_a_mover, columna_a_mover):
    global posiciones_con_numeros, posicion_vacia

    # Mover el número "2" al espacio vacío
    botones[(fila_a_mover, columna_a_mover)]["text"] = ""  # Vaciar el botón que tiene "2"
    botones[posicion_vacia]["text"] = "2"  # Poner "2" en la posición vacía

    # Actualizar las posiciones
    posiciones_con_numeros.remove((fila_a_mover, columna_a_mover))
    posiciones_con_numeros.append(posicion_vacia)

    # Actualizar la nueva posición vacía
    posicion_vacia = (fila_a_mover, columna_a_mover)


def key_press(event):
    if event.keysym in ['Up', 'Down', 'Left', 'Right']:
        mover_todos(event.keysym)


def salir():
    root.quit()


# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar",
                        "Instrucciones del juego:\n\n1. Usa las flechas del teclado para mover los números '2' hacia el espacio vacío.\n2. ¡Gana el juego!")


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
