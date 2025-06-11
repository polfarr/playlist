#!/usr/bin/python3

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

# Función para listar las canciones desde un archivo XML
def listar_canciones():
    archivo_cancion = open("songs/song_1.xml", "r").read()
    cancion = BeautifulSoup(archivo_cancion, 'xml')

    print(f"Título: {cancion.title.text}")
    print(f"Duración: {int(cancion.duration['seconds']) / 60} minutos")

    print("Artistas:")
    for artista in cancion.artists.find_all("artist"):
        print(f" - {artista.text}")

# Función para buscar una canción por su título
def buscar_cancion():
    titulo_busqueda = input("Introduce el título de la canción: ").strip().lower()
    archivo_cancion = open("songs/song_1.xml", "r").read()
    cancion = BeautifulSoup(archivo_cancion, 'xml')

    if cancion.title.text.lower() == titulo_busqueda:
        print(f"Canción encontrada: {cancion.title.text}")
        print(f"Duración: {int(cancion.duration['seconds']) / 60} minutos")
    else:
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

def listar_albumes():
    print("Listando todos los álbumes... (Funcionalidad pendiente)")

def buscar_album():
    print("Buscando álbum... (Funcionalidad pendiente)")

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

def listar_artistas():
    print("Listando todos los artistas... (Funcionalidad pendiente)")

def buscar_artista():
    print("Buscando artista... (Funcionalidad pendiente)")

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

def listar_generos():
    print("Listando todos los géneros... (Funcionalidad pendiente)")

def buscar_genero():
    print("Buscando género... (Funcionalidad pendiente)")

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