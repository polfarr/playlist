#!/usr/bin/python3

import os
from bs4 import BeautifulSoup

# Función para mostrar el menú principal y obtener la opción elegida
def mostrar_menu_principal():
    while True:
        print("--- Menú Principal ---")
        print("1. Álbumes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Géneros")
        print("0. Salir")

        opcion = input("Elige una opción (0-4): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, introduce un número entre 0 y 4.")
        else:
            print("Error: Debes ingresar un número válido.")

# Función para mostrar el menú de canciones
def mostrar_menu_canciones():
    while True:
        print("--- Menú de Canciones ---")
        print("1. Listar todas las canciones")
        print("2. Buscar canción por título")
        print("0. Volver")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            listar_canciones()
        elif opcion == "2":
            buscar_cancion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Función para listar las canciones disponibles en la carpeta
def listar_canciones():
    carpeta_songs = "songs"
    archivos = [f for f in os.listdir(carpeta_songs) if f.startswith("song") and f.endswith(".xml")]

    if len(archivos) > 0:
        print("Canciones disponibles:")
        i = 0
        while i < len(archivos):
            print(f"{i+1}. {archivos[i]}")
            i += 1
    else:
        print("No hay canciones disponibles.")


# Función para buscar una canción por su título
def buscar_cancion():
    titulo_busqueda = input("Introduce el título de la canción: ").strip().lower()
    carpeta_songs = "songs"
    archivos = [f for f in os.listdir(carpeta_songs) if f.startswith("song") and f.endswith(".xml")]

    i = 0
    while i < len(archivos):
        archivo_cancion = open(f"{carpeta_songs}/{archivos[i]}", "r").read()
        cancion = BeautifulSoup(archivo_cancion, 'xml')

        if cancion.title.text.lower() == titulo_busqueda:
            print(f"Canción encontrada en archivo {archivos[i]}:")
            print(f"Título: {cancion.title.text}")
            print(f"Duración: {int(cancion.duration['seconds']) / 60:.2f} minutos")
            return
        i += 1

    print("Canción no encontrada.")

# Función para mostrar el menú de álbumes
def mostrar_menu_albumes():
    while True:
        print("--- Menú de Álbumes ---")
        print("1. Listar todos los álbumes")
        print("2. Buscar álbum por título")
        print("0. Volver")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            listar_albumes()
        elif opcion == "2":
            buscar_album()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Función para listar los álbumes disponibles en la carpeta
def listar_albumes():
    carpeta_albums = "albums"
    archivos = [f for f in os.listdir(carpeta_albums) if f.startswith("album") and f.endswith(".xml")]

    if len(archivos) > 0:
        print("Álbumes disponibles:")
        i = 0
        while i < len(archivos):
            print(f"{i+1}. {archivos[i]}")
            i += 1
    else:
        print("No hay álbumes disponibles.")

# Función para buscar un álbum por su título
def buscar_album():
    titulo_busqueda = input("Introduce el título del álbum: ").strip().lower()
    carpeta_albums = "albums"
    archivos = [f for f in os.listdir(carpeta_albums) if f.startswith("album") and f.endswith(".xml")]

    i = 0
    while i < len(archivos):
        archivo_album = open(f"{carpeta_albums}/{archivos[i]}", "r").read()
        album = BeautifulSoup(archivo_album, 'xml')

        if album.title.text.lower() == titulo_busqueda:
            print(f"Álbum encontrado en archivo {archivos[i]}:")
            print(f"Título: {album.title.text}")
            return
        i += 1

    print("Álbum no encontrado.")

# Función para mostrar el menú de artistas
def mostrar_menu_artistas():
    while True:
        print("--- Menú de Artistas ---")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por nombre")
        print("0. Volver")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            listar_artistas()
        elif opcion == "2":
            buscar_artista()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Función para listar los artistas disponibles en la carpeta
def listar_artistas():
    carpeta_artistas = "artists"
    archivos = [f for f in os.listdir(carpeta_artistas) if f.startswith("artist") and f.endswith(".xml")]

    if len(archivos) > 0:
        print("Artistas disponibles:")
        i = 0
        while i < len(archivos):
            print(f"{i+1}. {archivos[i]}")
            i += 1
    else:
        print("No hay artistas disponibles.")

# Función para buscar un artista por su nombre
def buscar_artista():
    nombre_busqueda = input("Introduce el nombre del artista: ").strip().lower()
    carpeta_artistas = "artists"
    archivos = [f for f in os.listdir(carpeta_artistas) if f.startswith("artist") and f.endswith(".xml")]

    i = 0
    while i < len(archivos):
        archivo_artista = open(f"{carpeta_artistas}/{archivos[i]}", "r").read()
        artista = BeautifulSoup(archivo_artista, 'xml')

        if artista.name.text.lower() == nombre_busqueda:
            print(f"Artista encontrado en archivo {archivos[i]}:")
            print(f"Nombre: {artista.name.text}")
            return
        i += 1

    print("Artista no encontrado.")

# Función para mostrar el menú de géneros
def mostrar_menu_generos():
    while True:
        print("--- Menú de Géneros ---")
        print("1. Listar todos los géneros")
        print("2. Buscar género por nombre")
        print("0. Volver")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            listar_generos()
        elif opcion == "2":
            buscar_genero()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Función para listar los géneros disponibles en la carpeta
def listar_generos():
    carpeta_generos = "genres"
    archivos = [f for f in os.listdir(carpeta_generos) if f.startswith("genre") and f.endswith(".xml")]

    if len(archivos) > 0:
        print("Géneros disponibles:")
        i = 0
        while i < len(archivos):
            print(f"{i+1}. {archivos[i]}")
            i += 1
    else:
        print("No hay géneros disponibles.")

# Función para buscar un género por su nombre
def buscar_genero():
    nombre_busqueda = input("Introduce el nombre del género: ").strip().lower()
    carpeta_generos = "genres"
    archivos = [f for f in os.listdir(carpeta_generos) if f.startswith("genre") and f.endswith(".xml")]

    i = 0
    while i < len(archivos):
        archivo_genero = open(f"{carpeta_generos}/{archivos[i]}", "r").read()
        genero = BeautifulSoup(archivo_genero, 'xml')

        if genero.name.text.lower() == nombre_busqueda:
            print(f"Género encontrado en archivo {archivos[i]}:")
            print(f"Nombre: {genero.name.text}")
            return
        i += 1

    print("Género no encontrado.")

# Información de la versión de la aplicación
version = 0.5
titulo_app = "Playlist v" + str(version)

print(titulo_app)
print("-" * len(titulo_app))

# Bucle principal del programa
while True:
    opcion_menu = mostrar_menu_principal()

    if opcion_menu == 1:
        mostrar_menu_albumes()
    elif opcion_menu == 2:
        mostrar_menu_artistas()
    elif opcion_menu == 3:
        mostrar_menu_canciones()
    elif opcion_menu == 4:
        mostrar_menu_generos()
    elif opcion_menu == 0:
        print("Saliendo...")
        break