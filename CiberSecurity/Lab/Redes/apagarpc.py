import tkinter as tk
from tkinter import messagebox
import time
import os
import threading

# Variable para controlar el estado del temporizador
cancelar_temporizador = False

# Función para convertir el tiempo ingresado en segundos
def convertir_a_segundos(unidad, valor):
    if unidad == 'Segundos':
        return valor
    elif unidad == 'Minutos':
        return valor * 60
    elif unidad == 'Horas':
        return valor * 3600

# Función para mostrar la cuenta regresiva en formato horas, minutos, segundos
def formatear_tiempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# Función que inicia la cuenta regresiva y apaga la computadora
def iniciar_cuenta_regresiva():
    global cancelar_temporizador
    cancelar_temporizador = False  # Resetear la variable de cancelación

    try:
        valor_tiempo = int(entrada_tiempo.get())
        unidad = unidad_tiempo.get()
        total_segundos = convertir_a_segundos(unidad, valor_tiempo)

        # Deshabilitar los botones mientras corre la cuenta regresiva
        boton_iniciar.config(state=tk.DISABLED)
        boton_cancelar.config(state=tk.NORMAL)

        for i in range(total_segundos, 0, -1):
            if cancelar_temporizador:  # Verificar si se ha cancelado el temporizador
                return  # Salir de la función si se cancela
            cuenta_regresiva.config(text=f"Tiempo restante: {formatear_tiempo(i)}")
            time.sleep(1)

        # Apagar el computador solo si no se canceló
        os.system("shutdown /s /t 1")  # Para Windows
        # os.system("shutdown -h now")  # Para Linux
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, introduce un número válido.")
    finally:
        # Restablecer estado de los botones
        boton_iniciar.config(state=tk.NORMAL)
        boton_cancelar.config(state=tk.DISABLED)

# Función para cancelar el temporizador y el apagado
def cancelar_apagado():
    global cancelar_temporizador
    cancelar_temporizador = True  # Indicar que se ha cancelado

    try:
        os.system("shutdown /a")  # Intentar cancelar el apagado en Windows
    except Exception:
        pass  # Ignorar si no hay apagado en curso

    cuenta_regresiva.config(text="Apagado cancelado.")
    entrada_tiempo.delete(0, tk.END)  # Limpiar el campo de entrada
    unidad_tiempo.set('Segundos')  # Restablecer a segundos
    boton_cancelar.config(state=tk.DISABLED)
    boton_iniciar.config(state=tk.NORMAL)

# Función para salir de la aplicación
def salir_aplicacion():
    root.quit()

# Crear ventana
root = tk.Tk()
root.title("Temporizador de Apagado")

# Dropdown para elegir la unidad de tiempo
unidad_tiempo = tk.StringVar()
unidad_tiempo.set('Segundos')  # Valor por defecto

dropdown = tk.OptionMenu(root, unidad_tiempo, 'Segundos', 'Minutos', 'Horas')
dropdown.grid(row=0, column=1)

# Entrada para ingresar el tiempo
entrada_tiempo = tk.Entry(root)
entrada_tiempo.grid(row=0, column=0)

# Botón para iniciar la cuenta regresiva
boton_iniciar = tk.Button(root, text="Iniciar", command=lambda: threading.Thread(target=iniciar_cuenta_regresiva).start())
boton_iniciar.grid(row=1, column=0)

# Botón para cancelar el apagado
boton_cancelar = tk.Button(root, text="Cancelar", command=cancelar_apagado, state=tk.DISABLED)
boton_cancelar.grid(row=1, column=1)

# Botón para salir de la aplicación
boton_salir = tk.Button(root, text="Salir", command=salir_aplicacion)
boton_salir.grid(row=1, column=2)

# Etiqueta para mostrar la cuenta regresiva
cuenta_regresiva = tk.Label(root, text="")
cuenta_regresiva.grid(row=2, column=0, columnspan=3)

root.mainloop()
