import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
from mutagen.mp3 import MP3

class ReproductorMP3:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor MP3")
        self.master.geometry("400x500")

        self.lista_canciones = []
        self.cancion_actual = 0
        self.tiempo_transcurrido = tk.StringVar()

        # Configurar Pygame
        pygame.init()

        # Crear widgets
        self.label = tk.Label(self.master, text="Reproductor MP3")
        self.label.pack(pady=10)

        self.lista_box = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.lista_box.pack(pady=10)

        self.btn_agregar = tk.Button(self.master, text="Agregar Canciones", command=self.agregar_canciones)
        self.btn_agregar.pack(pady=5)

        self.btn_reproducir = tk.Button(self.master, text="Reproducir", command=self.reproducir)
        self.btn_reproducir.pack(pady=5)

        self.btn_detener = tk.Button(self.master, text="Detener", command=self.detener)
        self.btn_detener.pack(pady=5)

        self.btn_siguiente = tk.Button(self.master, text="Siguiente", command=self.siguiente)
        self.btn_siguiente.pack(pady=5)

        self.barra_progreso = ttk.Progressbar(self.master, orient='horizontal', length=300, mode='determinate')
        self.barra_progreso.pack(pady=10)

        self.label_tiempo = tk.Label(self.master, textvariable=self.tiempo_transcurrido)
        self.label_tiempo.pack()

        # Actualizar la barra de progreso
        self.actualizar_barra_progreso()

    def agregar_canciones(self):
        canciones = filedialog.askopenfilenames(filetypes=[("Archivos MP3", "*.mp3")])
        for cancion in canciones:
            self.lista_canciones.append(cancion)
            self.lista_box.insert(tk.END, os.path.basename(cancion))

    def reproducir(self):
        if self.lista_canciones:
            pygame.mixer.music.load(self.lista_canciones[self.cancion_actual])
            pygame.mixer.music.play()
            self.actualizar_barra_progreso()
            self.mostrar_tiempo()

    def detener(self):
        pygame.mixer.music.stop()
        self.barra_progreso.stop()
        self.barra_progreso["value"] = 0

    def siguiente(self):
        self.cancion_actual = (self.cancion_actual + 1) % len(self.lista_canciones)
        self.reproducir()

    def actualizar_barra_progreso(self):
        if self.lista_canciones:
            duracion_total = self.obtener_duracion_cancion_actual()
            self.barra_progreso['maximum'] = duracion_total
            self.barra_progreso['value'] = 0
            self.barra_progreso.start(1000)  # Inicia la barra de progreso actualizando cada segundo
            self.master.after(1000, self.actualizar_barra_progreso)

    def mostrar_tiempo(self):
        if self.lista_canciones:
            tiempo_actual = pygame.mixer.music.get_pos() // 1000
            self.tiempo_transcurrido.set(f'Tiempo transcurrido: {tiempo_actual} s')
            self.master.after(1000, self.mostrar_tiempo)

    def obtener_duracion_cancion_actual(self):
        if self.lista_canciones:
            archivo_cancion = MP3(self.lista_canciones[self.cancion_actual])
            return archivo_cancion.info.length
        return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ReproductorMP3(root)
    root.mainloop()
