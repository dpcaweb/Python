import secrets
import string
import tkinter as tk

def generar_contrasena(longitud):
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(alfabeto) for i in range(longitud))
    return contrasena

def guardar_contrasena():
    contrasena = label_contrasena.cget("text")
    with open("contrasenas.txt", "a") as archivo:
        archivo.write(contrasena + "\n")

def generar_contrasena_grafica():
    longitud = int(entry_longitud.get())
    contrasena = generar_contrasena(longitud)
    label_contrasena.config(text=contrasena)

root = tk.Tk()
root.title("Generador de contraseñas seguras")
root.geometry("400x250")

label_longitud = tk.Label(root, text="Longitud de la contraseña:")
label_longitud.pack()

entry_longitud = tk.Entry(root)
entry_longitud.pack()

button_generar = tk.Button(root, text="Generar contraseña", command=generar_contrasena_grafica)
button_generar.pack()

label_contrasena = tk.Label(root, text="")
label_contrasena.pack()

button_guardar = tk.Button(root, text="Guardar contraseña", command=guardar_contrasena)
button_guardar.pack()

root.mainloop()
