import tkinter as tk
from tkinter import messagebox
import random

# Variables globales
posiciones_con_numeros = []
posicion_vacia = None
botones = {}

# Crear la ventana principal
root = tk.Tk()
root.title("2048")
root.geometry("820x460")  # Tamaño de la ventana

# Cambiar el color de fondo de la ventana a verde
root.config(bg="green")

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido a mi 2048!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=50)

# Funciones vacías para los botones
def nuevo_juego():
    global posiciones_con_numeros, posicion_vacia, botones

    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("360x320")

    # Crear una lista de 16 posiciones (4x4)
    posiciones = [(fila, columna) for fila in range(4) for columna in range(4)]

    # Seleccionar aleatoriamente dos posiciones para mostrar el número 2
    posiciones_con_numeros = random.sample(posiciones, 2)  # Dos números "2"

    # La última posición será el espacio vacío
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

    if direccion == "Up":
        for fila in range(fila_vacia - 1, -1, -1):
            if (fila, columna_vacia) in posiciones_con_numeros:
                # Mover el número al espacio vacío
                boton_a_mover = (fila, columna_vacia)
                botones[boton_a_mover]["text"] = "2"  # Mostrar el número "2"
                botones[posicion_vacia]["text"] = ""  # El espacio vacío queda vacío
                # Actualizar las posiciones
                posiciones_con_numeros.remove(boton_a_mover)
                posicion_vacia = (fila, columna_vacia)
                break

    elif direccion == "Down":
        for fila in range(fila_vacia + 1, 4):
            if (fila, columna_vacia) in posiciones_con_numeros:
                # Mover el número al espacio vacío
                boton_a_mover = (fila, columna_vacia)
                botones[boton_a_mover]["text"] = "2"
                botones[posicion_vacia]["text"] = ""
                posiciones_con_numeros.remove(boton_a_mover)
                posicion_vacia = (fila, columna_vacia)
                break

    elif direccion == "Left":
        for columna in range(columna_vacia - 1, -1, -1):
            if (fila_vacia, columna) in posiciones_con_numeros:
                # Mover el número al espacio vacío
                boton_a_mover = (fila_vacia, columna)
                botones[boton_a_mover]["text"] = "2"
                botones[posicion_vacia]["text"] = ""
                posiciones_con_numeros.remove(boton_a_mover)
                posicion_vacia = (fila_vacia, columna)
                break

    elif direccion == "Right":
        for columna in range(columna_vacia + 1, 4):
            if (fila_vacia, columna) in posiciones_con_numeros:
                # Mover el número al espacio vacío
                boton_a_mover = (fila_vacia, columna)
                botones[boton_a_mover]["text"] = "2"
                botones[posicion_vacia]["text"] = ""
                posiciones_con_numeros.remove(boton_a_mover)
                posicion_vacia = (fila_vacia, columna)
                break


def key_press(event):
    if event.keysym in ['Up', 'Down', 'Left', 'Right']:
        mover_todos(event.keysym)

def salir():
    root.quit()

# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar", "Instrucciones del juego:\n\n1. Con las flechas del teclado combinas los mosaicos.\n2. Combina mosaicos del mismo numero para conseguir mas puntos.\n3. Combina la mayor cantidad de mosaicos para conseguir mas puntos.")

# Botón para "Nuevo juego"
boton_nuevo_juego = tk.Button(root, text="Nuevo Juego", font=("Helvetica", 14), command=nuevo_juego)
boton_nuevo_juego.pack(pady=10)

boton_como_jugar = tk.Button(root, text="Como Jugar", font=("Helvetica", 14), command=mostrar_instrucciones)
boton_como_jugar.pack(pady=10)

# Botón para "Salir"
boton_salir = tk.Button(root, text="Salir", font=("Helvetica", 14), command=salir)
boton_salir.pack(pady=10)

# Enlazar eventos de teclado
root.bind("<Key>", key_press)

# Iniciar el bucle principal de la ventana
root.mainloop()
