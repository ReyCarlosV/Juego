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
botones = {}

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido al Juego!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=30)


# Funciones para los botones
def nuevo_juego():
    global posiciones_con_numeros, botones

    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("400x400")

    # Crear una lista de 16 posiciones (4x4)
    posiciones = [(fila, columna) for fila in range(4) for columna in range(4)]

    # Seleccionar aleatoriamente dos posiciones para mostrar el número 2
    posiciones_con_numeros = random.sample(posiciones, 2)  # Dos números "2"

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
    global posiciones_con_numeros

    if direccion == "Up":
        mover_numeros(-1, 0)  # Mover hacia arriba
    elif direccion == "Down":
        mover_numeros(1, 0)  # Mover hacia abajo
    elif direccion == "Left":
        mover_numeros(0, -1)  # Mover hacia la izquierda
    elif direccion == "Right":
        mover_numeros(0, 1)  # Mover hacia la derecha


def mover_numeros(delta_fila, delta_columna):
    global posiciones_con_numeros

    # Para cada número "2", intentamos moverlo en la dirección indicada
    nuevas_posiciones = []
    for fila, columna in posiciones_con_numeros:
        nueva_fila = fila
        nueva_columna = columna

        # Seguir moviendo hasta encontrar un límite o un obstáculo
        while True:
            siguiente_fila = nueva_fila + delta_fila
            siguiente_columna = nueva_columna + delta_columna

            if 0 <= siguiente_fila < 4 and 0 <= siguiente_columna < 4 and (
            siguiente_fila, siguiente_columna) not in nuevas_posiciones:
                nueva_fila = siguiente_fila
                nueva_columna = siguiente_columna
            else:
                break

        # Almacenar la nueva posición del número "2"
        nuevas_posiciones.append((nueva_fila, nueva_columna))

    # Actualizar los botones visualmente
    for fila, columna in posiciones_con_numeros:
        botones[(fila, columna)]["text"] = ""  # Vaciar las posiciones anteriores

    for nueva_fila, nueva_columna in nuevas_posiciones:
        botones[(nueva_fila, nueva_columna)]["text"] = "2"  # Actualizar nuevas posiciones

    # Actualizar la lista de posiciones con los nuevos lugares de los números
    posiciones_con_numeros = nuevas_posiciones


def key_press(event):
    if event.keysym in ['Up', 'Down', 'Left', 'Right']:
        mover_todos(event.keysym)


def salir():
    root.quit()


# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar",
                        "Instrucciones del juego:\n\n1. Usa las flechas del teclado para mover los números '2'.\n2. ¡Gana el juego moviendo los números!")


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
