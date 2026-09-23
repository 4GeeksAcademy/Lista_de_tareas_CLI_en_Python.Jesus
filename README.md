# 📦 CLI Task Manager - Herramienta de Gestión de Tareas para Logística

## 📋 Descripción General

**CLI Task Manager** es una herramienta ligera de terminal diseñada para **coordinadores operativos de logística**, que permite registrar, consultar y eliminar tareas internas de forma rápida durante el día a día operativo. Gracias a su persistencia local en un archivo `.csv`, las tareas pueden guardarse al final de un turno y recuperarse al inicio del siguiente, sin depender de bases de datos externas ni conexión a internet.

## ✨ Características Principales

- ➕ **Registro de nuevas tareas** mediante `add_one_task(title)`.
- 📃 **Listado de tareas pendientes** con numeración secuencial mediante `print_list()`.
- ❌ **Eliminación de tareas completadas** por posición mediante `delete_task(number_to_delete)`.
- 💾 **Persistencia de datos local** en `todos.csv` mediante `save_todos()` y `load_todos()`.
- 🔁 **Menú interactivo en consola** que permite ejecutar múltiples acciones dentro de la misma sesión.

## 🛠️ Requisitos y Tecnologías

- 🐍 **Python 3.x**
- 🚫 **Sin dependencias externas**: el proyecto utiliza exclusivamente la librería estándar de Python (`csv`, `os`).

## 🗂️ Estructura del Archivo `todos.csv`

Las tareas se guardan en formato CSV, con **una tarea por línea** y una sola columna que contiene el título de la tarea:

```csv
Revisar inventario del almacén A
Coordinar entrega con transportista
Actualizar hoja de rutas
```

## 🚀 Instrucciones de Uso / Ejecución

### 1. Clonar o abrir el proyecto en GitHub Codespaces

```bash
git clone https://github.com/<usuario>/Lista_de_tareas_CLI_en_Python.Jesus.git
cd Lista_de_tareas_CLI_en_Python.Jesus
```

O simplemente abre el repositorio en **GitHub Codespaces** desde el botón `Code > Open with Codespaces`.

### 2. Ejecutar la aplicación

```bash
python3 todo.py
```

### 3. Guía del menú interactivo

Al ejecutar el programa, se mostrará un menú con las siguientes opciones:

```
--- Gestión de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Eliminar tarea
4. Guardar tareas
5. Cargar tareas
6. Salir
```

- Selecciona el número de la opción deseada y presiona `Enter`.
- Puedes agregar, listar y eliminar tareas múltiples veces dentro de la misma sesión antes de salir.
- Usa la opción **4** para guardar los cambios en `todos.csv` y la opción **5** para recuperarlos en una sesión futura.

## 🧩 Estructura del Código / Funciones

| Función                        | Responsabilidad                                                                 |
|--------------------------------|----------------------------------------------------------------------------------|
| `add_one_task(title)`          | Agrega una nueva tarea a la lista en memoria.                                    |
| `print_list()`                 | Muestra todas las tareas pendientes con numeración secuencial desde el 1.        |
| `delete_task(number_to_delete)` | Elimina la tarea en la posición indicada, validando entradas inválidas.          |
| `save_todos()`                  | Guarda la lista de tareas actual en el archivo `todos.csv`.                      |
| `load_todos()`                  | Carga las tareas desde `todos.csv` (si existe) hacia la lista en memoria.        |
| `main()`                        | Ejecuta el bucle interactivo con el menú principal de la aplicación.             |
