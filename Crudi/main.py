import os
import tkinter as tk
from tkinter import filedialog
import pygame

class ReproductorMP3:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor MP3")
        self.master.geometry("400x400")

        self.lista_canciones = []
        self.cancion_actual = 0

        # Configurar Pygame
        pygame.init()

        # Crear widgets
        self.label = tk.Label(self.master, text="Reproductor MP3")
        self.label.pack(pady=10)

        self.lista_box = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.lista_box.pack(pady=20)

        self.btn_agregar = tk.Button(self.master, text="Agregar Canciones", command=self.agregar_canciones)
        self.btn_agregar.pack(pady=10)

        self.btn_reproducir = tk.Button(self.master, text="Reproducir", command=self.reproducir)
        self.btn_reproducir.pack(pady=5)

        self.btn_siguiente = tk.Button(self.master, text="Siguiente", command=self.siguiente)
        self.btn_siguiente.pack(pady=5)

        self.btn_detener = tk.Button(self.master, text="Detener", command=self.detener)
        self.btn_detener.pack(pady=5)

    def agregar_canciones(self):
        canciones = filedialog.askopenfilenames(filetypes=[("Archivos MP3", "*.mp3")])
        for cancion in canciones:
            self.lista_canciones.append(cancion)
            self.lista_box.insert(tk.END, os.path.basename(cancion))

    def reproducir(self):
        if self.lista_canciones:
            pygame.mixer.music.load(self.lista_canciones[self.cancion_actual])
            pygame.mixer.music.play()

    def detener(self):
        pygame.mixer.music.stop()

    def siguiente(self):
        self.cancion_actual = (self.cancion_actual + 1) % len(self.lista_canciones)
        self.reproducir()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReproductorMP3(root)
    root.mainloop()
