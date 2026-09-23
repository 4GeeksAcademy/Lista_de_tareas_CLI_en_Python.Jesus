"""
CLI de gestión de tareas internas para una empresa de logística.
Usa únicamente la librería estándar de Python (csv, os).
"""

import csv
import os

ARCHIVO_CSV = "todos.csv"

# Lista en memoria que almacena las tareas actuales
tareas = []


def add_one_task(title):
    """Agrega una nueva tarea a la lista en memoria."""
    tareas.append(title)
    print(f"Tarea agregada: '{title}'")


def print_list():
    """Muestra todas las tareas pendientes con numeración legible desde 1."""
    if not tareas:
        print("No hay tareas pendientes.")
        return
    for indice, tarea in enumerate(tareas, start=1):
        print(f"{indice}. {tarea}")


def delete_task(number_to_delete):
    """Elimina la tarea en la posición indicada (1-indexada), con validación."""
    # Validamos que sea un número entero válido dentro del rango de la lista
    if not isinstance(number_to_delete, int):
        print("Error: debes ingresar un número entero válido.")
        return
    if number_to_delete < 1 or number_to_delete > len(tareas):
        print("Error: el número de tarea no existe.")
        return
    tarea_eliminada = tareas.pop(number_to_delete - 1)
    print(f"Tarea eliminada: '{tarea_eliminada}'")


def save_todos():
    """Guarda la lista de tareas actual en el archivo todos.csv."""
    with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for tarea in tareas:
            escritor.writerow([tarea])
    print(f"Tareas guardadas en '{ARCHIVO_CSV}'.")


def load_todos():
    """Carga las tareas desde todos.csv (si existe) hacia la lista en memoria."""
    if not os.path.exists(ARCHIVO_CSV):
        print(f"No se encontró el archivo '{ARCHIVO_CSV}'. No se cargaron tareas.")
        return

    tareas.clear()
    with open(ARCHIVO_CSV, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila:  # Evita filas vacías
                tareas.append(fila[0])
    print(f"Tareas cargadas desde '{ARCHIVO_CSV}'.")


def mostrar_menu():
    """Imprime las opciones del menú principal."""
    print("\n--- Gestión de Tareas ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Guardar tareas")
    print("5. Cargar tareas")
    print("6. Salir")


def main():
    """Bucle principal interactivo de la aplicación CLI."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            titulo = input("Ingresa el título de la tarea: ").strip()
            if titulo:
                add_one_task(titulo)
            else:
                print("Error: el título no puede estar vacío.")

        elif opcion == "2":
            print_list()

        elif opcion == "3":
            print_list()
            numero = input("Ingresa el número de la tarea a eliminar: ").strip()
            if numero.isdigit():
                delete_task(int(numero))
            else:
                print("Error: debes ingresar un número entero válido.")

        elif opcion == "4":
            save_todos()

        elif opcion == "5":
            load_todos()

        elif opcion == "6":
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
