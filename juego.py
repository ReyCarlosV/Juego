import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Portada de Inicio")
root.geometry("820x460")  # Tamaño de la ventana

# Cambiar el color de fondo de la ventana a verde
root.config(bg="green")

# Etiqueta de título
titulo = tk.Label(root, text="¡Bienvenido a mi 2048!", font=("Helvetica", 20), bg="green", fg="white")
titulo.pack(pady=50)

# Funciones vacías para los botones
def nuevo_juego():
    # Crear una nueva ventana para el juego
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nuevo Juego - Mosaico 4x4")
    nueva_ventana.geometry("400x400")

    # Crear un mosaico de 4x4 botones
    for fila in range(4):
        for columna in range(4):
            boton = tk.Button(nueva_ventana, text=f"({fila + 1},{columna + 1})", width=10, height=4)
            boton.grid(row=fila, column=columna, padx=5, pady=5)

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

# Iniciar el bucle principal de la ventana
root.mainloop()
