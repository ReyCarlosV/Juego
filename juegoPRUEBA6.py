import tkinter as tk
import random
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Portada de Inicio")
root.geometry("400x300")
root.config(bg="green")

# Variables globales
posiciones_con_numeros = {}
botones = {}
marcador = 0

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido al Juego!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=30)

# Crear el marcador en la ventana principal
marcador_label = tk.Label(root, text=f"Marcador: {marcador}", font=("Helvetica", 16), bg="green", fg="white")
marcador_label.pack(pady=10)


def nuevo_juego():
    global posiciones_con_numeros, botones, marcador

    # Reiniciar marcador
    marcador = 0
    marcador_label.config(text=f"Marcador: {marcador}")

    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("400x500")

    # Crear una lista de 16 posiciones (4x4)
    posiciones = [(fila, columna) for fila in range(4) for columna in range(4)]

    # Seleccionar aleatoriamente dos posiciones para mostrar el número 2
    posiciones_iniciales = random.sample(posiciones, 2)

    # Asignar las posiciones con los valores 2
    posiciones_con_numeros = {pos: 2 for pos in posiciones_iniciales}

    # Crear un mosaico de 4x4 botones
    for fila in range(4):
        for columna in range(4):
            texto = str(posiciones_con_numeros.get((fila, columna), ""))
            boton = tk.Button(nueva_ventana, text=texto, width=10, height=4)
            boton.grid(row=fila, column=columna, padx=5, pady=5)
            botones[(fila, columna)] = boton

    # Vincular las teclas a la nueva ventana
    nueva_ventana.bind("<Key>", key_press)
    nueva_ventana.focus_set()

    # Agregar botón Salir en la ventana de juego
    boton_salir_juego = tk.Button(nueva_ventana, text="Salir", font=("Helvetica", 14), command=nueva_ventana.destroy)
    boton_salir_juego.grid(row=4, column=0, columnspan=4, pady=10)  # Usar grid para posicionarlo


def actualizar_marcador(puntos):
    global marcador
    marcador += puntos
    marcador_label.config(text=f"Marcador: {marcador}")


def mover_todos(direccion):
    global posiciones_con_numeros

    posiciones_antes = posiciones_con_numeros.copy()
    mover_numeros(direccion)

    if posiciones_con_numeros != posiciones_antes:
        agregar_numero()
    else:
        # Comprobar si no hay más movimientos posibles
        if not hay_movimientos():
            mostrar_mensaje_fin()


def mover_numeros(direccion):
    global posiciones_con_numeros

    delta_fila, delta_columna = 0, 0
    if direccion == "Up":
        delta_fila = -1
    elif direccion == "Down":
        delta_fila = 1
    elif direccion == "Left":
        delta_columna = -1
    elif direccion == "Right":
        delta_columna = 1

    nuevas_posiciones = {}
    sumado = set()

    if delta_fila > 0 or delta_columna > 0:
        posiciones_ordenadas = sorted(posiciones_con_numeros.keys(), key=lambda x: (x[0], x[1]), reverse=True)
    else:
        posiciones_ordenadas = sorted(posiciones_con_numeros.keys(), key=lambda x: (x[0], x[1]))

    for fila, columna in posiciones_ordenadas:
        if (fila, columna) in posiciones_con_numeros:
            nueva_fila, nueva_columna = fila, columna
            valor = posiciones_con_numeros[(fila, columna)]

            while True:
                siguiente_fila = nueva_fila + delta_fila
                siguiente_columna = nueva_columna + delta_columna

                if 0 <= siguiente_fila < 4 and 0 <= siguiente_columna < 4:
                    if (siguiente_fila, siguiente_columna) not in nuevas_posiciones:
                        nueva_fila, nueva_columna = siguiente_fila, siguiente_columna
                    elif nuevas_posiciones.get((siguiente_fila, siguiente_columna)) == valor and (
                    siguiente_fila, siguiente_columna) not in sumado:
                        nuevas_posiciones[(siguiente_fila, siguiente_columna)] *= 2
                        sumado.add((siguiente_fila, siguiente_columna))
                        actualizar_marcador(
                            nuevas_posiciones[(siguiente_fila, siguiente_columna)])  # Actualizar marcador
                        valor = 0  # Eliminar valor en la posición actual después de sumar
                        break
                    else:
                        break
                else:
                    break

            if valor != 0:
                nuevas_posiciones[(nueva_fila, nueva_columna)] = valor

    posiciones_con_numeros = nuevas_posiciones

    for fila in range(4):
        for columna in range(4):
            if (fila, columna) in posiciones_con_numeros:
                botones[(fila, columna)]["text"] = str(posiciones_con_numeros[(fila, columna)])
            else:
                botones[(fila, columna)]["text"] = ""


def agregar_numero():
    posiciones_vacias = [(fila, columna) for fila in range(4) for columna in range(4) if
                         (fila, columna) not in posiciones_con_numeros]

    if posiciones_vacias:
        nueva_posicion = random.choice(posiciones_vacias)
        posiciones_con_numeros[nueva_posicion] = 2
        botones[nueva_posicion]["text"] = "2"


def hay_movimientos():
    for fila in range(4):
        for columna in range(4):
            if (fila, columna) not in posiciones_con_numeros:
                return True
            valor = posiciones_con_numeros[(fila, columna)]
            for delta_fila, delta_columna in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nueva_fila, nueva_columna = fila + delta_fila, columna + delta_columna
                if 0 <= nueva_fila < 4 and 0 <= nueva_columna < 4:
                    if (nueva_fila, nueva_columna) not in posiciones_con_numeros or posiciones_con_numeros[
                        (nueva_fila, nueva_columna)] == valor:
                        return True
    return False


def mostrar_mensaje_fin():
    messagebox.showinfo("Fin del Juego", f"Juego terminado. Puntos: {marcador}")
    root.quit()  # Cerrar el juego


def key_press(event):
    if event.keysym in ['Up', 'Down', 'Left', 'Right']:
        mover_todos(event.keysym)


def salir():
    root.quit()


def mostrar_instrucciones():
    messagebox.showinfo("Cómo jugar",
                        "Instrucciones del juego:\n\n1. Usa las flechas del teclado para mover los números.\n2. Si dos números iguales colisionan, se sumarán.\n3. Cada vez que muevas, aparecerá un nuevo '2' en una posición vacía.")


boton_nuevo_juego = tk.Button(root, text="Nuevo Juego", font=("Helvetica", 14), command=nuevo_juego)
boton_nuevo_juego.pack(pady=10)

boton_como_jugar = tk.Button(root, text="Cómo Jugar", font=("Helvetica", 14), command=mostrar_instrucciones)
boton_como_jugar.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", font=("Helvetica", 14), command=salir)
boton_salir.pack(pady=10)

root.mainloop()
