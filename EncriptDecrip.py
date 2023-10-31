import tkinter as tk
from tkinter import filedialog, simpledialog
from cryptography.fernet import Fernet
import base64

def encrypt_file():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo para cifrar")
    if file_path:
        key = simpledialog.askstring("Clave de cifrado", "Ingresa la clave de cifrado:")
        if key:
            key = base64.urlsafe_b64encode(key.encode())
            cipher_suite = Fernet(key)

            with open(file_path, 'rb') as file:
                original_data = file.read()
            encrypted_data = cipher_suite.encrypt(original_data)

            save_path = filedialog.asksaveasfilename(title="Guardar archivo cifrado", defaultextension=".enc")
            if save_path:
                with open(save_path, 'wb') as file:
                    file.write(encrypted_data)
                tk.messagebox.showinfo("Cifrado completado", "El archivo se ha cifrado correctamente.")

def decrypt_file():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo para descifrar")
    if file_path:
        key = simpledialog.askstring("Clave de descifrado", "Ingresa la clave de descifrado:")
        if key:
            key = base64.urlsafe_b64encode(key.encode())
            cipher_suite = Fernet(key)

            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)

            save_path = filedialog.asksaveasfilename(title="Guardar archivo descifrado", defaultextension=".txt")
            if save_path:
                with open(save_path, 'wb') as file:
                    file.write(decrypted_data)
                tk.messagebox.showinfo("Descifrado completado", "El archivo se ha descifrado correctamente.")

# Crear ventana principal
window = tk.Tk()
window.title("Encriptador/Desencriptador")
window.geometry("300x150")

# Botones de cifrado y descifrado
encrypt_button = tk.Button(window, text="Cifrar archivo", command=encrypt_file)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window, text="Descifrar archivo", command=decrypt_file)
decrypt_button.pack(pady=10)

# Ejecutar ventana
window.mainloop()
