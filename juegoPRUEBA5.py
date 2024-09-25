import tkinter as tk
import random
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Portada de Inicio")
root.geometry("400x300")  # Tamaño de la ventana
root.config(bg="green")  # Cambiar el color de fondo de la ventana a verde

# Variables globales
posiciones_con_numeros = {}
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
    posiciones_iniciales = random.sample(posiciones, 2)  # Dos números "2"

    # Asignar las posiciones con los valores 2
    posiciones_con_numeros = {pos: 2 for pos in posiciones_iniciales}

    # Crear un mosaico de 4x4 botones
    for fila in range(4):
        for columna in range(4):
            texto = str(posiciones_con_numeros.get((fila, columna), ""))  # Mostrar el número o vacío
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

    agregar_numero()


def mover_numeros(delta_fila, delta_columna):
    global posiciones_con_numeros

    nuevas_posiciones = {}
    sumado = set()  # Para recordar qué posiciones ya se han sumado

    # Ordenar las posiciones según la dirección del movimiento
    posiciones_ordenadas = sorted(posiciones_con_numeros.keys(), key=lambda x: (x[0], x[1]))

    # Ajustar el orden según la dirección del movimiento
    if delta_fila > 0 or delta_columna > 0:
        posiciones_ordenadas.reverse()

    # Procesar cada posición
    for fila, columna in posiciones_ordenadas:
        if (fila, columna) in posiciones_con_numeros:
            nueva_fila = fila
            nueva_columna = columna
            valor = posiciones_con_numeros[(fila, columna)]  # El valor del número a mover

            # Mover el número en la dirección deseada hasta que no pueda avanzar más
            while True:
                siguiente_fila = nueva_fila + delta_fila
                siguiente_columna = nueva_columna + delta_columna

                if 0 <= siguiente_fila < 4 and 0 <= siguiente_columna < 4:
                    # Verificar si la celda siguiente está vacía o si tiene el mismo valor
                    if (siguiente_fila, siguiente_columna) not in nuevas_posiciones:
                        nueva_fila = siguiente_fila
                        nueva_columna = siguiente_columna
                    elif nuevas_posiciones.get((siguiente_fila, siguiente_columna)) == valor and (
                    siguiente_fila, siguiente_columna) not in sumado:
                        # Si colisionan dos números iguales, los sumamos
                        nuevas_posiciones[(siguiente_fila, siguiente_columna)] *= 2
                        sumado.add((siguiente_fila, siguiente_columna))  # Marcar como sumado
                        # Vaciar la posición original
                        posiciones_con_numeros[(fila, columna)] = ""
                        break
                    else:
                        break
                else:
                    break

            # Colocar el número en la nueva posición
            if (nueva_fila, nueva_columna) not in nuevas_posiciones:
                nuevas_posiciones[(nueva_fila, nueva_columna)] = valor

            # Asegurarnos de que la celda original se vacíe si fue movida
            if (fila, columna) != (nueva_fila, nueva_columna):
                posiciones_con_numeros[(fila, columna)] = ""

    # Actualizar el tablero visualmente
    for fila in range(4):
        for columna in range(4):
            if (fila, columna) in nuevas_posiciones:
                botones[(fila, columna)]["text"] = str(nuevas_posiciones[(fila, columna)])
            else:
                botones[(fila, columna)]["text"] = ""

    # Actualizar las posiciones de los números
    posiciones_con_numeros = nuevas_posiciones


def agregar_numero():
    """ Agrega un nuevo número '2' en una posición vacía aleatoria. """
    posiciones_vacias = [(fila, columna) for fila in range(4) for columna in range(4) if
                         (fila, columna) not in posiciones_con_numeros or posiciones_con_numeros[(fila, columna)] == ""]

    if posiciones_vacias:
        nueva_posicion = random.choice(posiciones_vacias)
        posiciones_con_numeros[nueva_posicion] = 2
        botones[nueva_posicion]["text"] = "2"


def key_press(event):
    if event.keysym in ['Up', 'Down', 'Left', 'Right']:
        mover_todos(event.keysym)


def salir():
    root.quit()


# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar",
                        "Instrucciones del juego:\n\n1. Usa las flechas del teclado para mover los números.\n2. Si dos números iguales colisionan, se sumarán.\n3. Cada vez que muevas, aparecerá un nuevo '2' en una posición vacía.")


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
