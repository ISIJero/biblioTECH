# Sistema de Gestión de Bibliotecas

Este proyecto es un **Sistema de Gestión de Bibliotecas** con una arquitectura dividida en un backend (API RESTful) y un frontend (Aplicación de Escritorio).

## Arquitectura del Proyecto

El proyecto está compuesto por dos partes principales:

### 1. Backend (FastAPI + SQLite)
Ubicado en la carpeta `backend`, es una API RESTful desarrollada con **FastAPI** y **Python**.
- **Base de Datos**: Utiliza SQLite (`biblioteca_db.db`). La inicialización y creación de tablas está centralizada en `config/init_db.py`.
- **Esquema de Base de Datos**:
  - `libros`: id, nombre, autor, materia, isbn, cod, estado.
  - `personas`: id, nombre, curso, rol.
  - `prestamos`: idLibro, idPersona, fecha_retiro, fecha_entrega, estado.
- **Rutas (Endpoints)**: Cuenta con un CRUD completo para la gestión de libros bajo la ruta `/books`.
- **Estructura de Directorios**:
  - `routers/`: Define los endpoints de la API.
  - `services/`: Contiene la lógica de negocio y las consultas directas a la base de datos mediante la clase `DataBaseManagment`.
  - `schemas/`: Modelos de datos utilizando **Pydantic** para la validación de la información de entrada y salida (`Book`, `BookIn`).
  - `config/`: Configuración de la conexión y gestión de la base de datos.
- **Gestor de Dependencias**: El backend está empaquetado usando `uv` (evidenciado por `uv.lock` y `pyproject.toml`).

### 2. Frontend (Electron + React)
Ubicado en la carpeta `frontend`, es una aplicación de escritorio multiplataforma construida con **Electron**, **React** y empaquetada con **Webpack**.
- **Interfaz de Usuario**: Desarrollada con React y estructurada mediante `react-router-dom`.
- **Estilos**: Utiliza Bootstrap y CSS puro (`app.css`, `index.css`).
- **Integración con Backend**: En el archivo `main.js` (proceso principal de Electron), se lanza automáticamente el servidor de FastAPI (`uvicorn main:app`) como un subproceso. Esto permite que el usuario inicie la aplicación de manera autocontenida sin levantar el backend por separado.
- **Pantalla Principal**: La vista principal (`src/screens/mainScreen.jsx`) está en desarrollo, preparando el terreno para listar y gestionar la información obtenida desde la API.

## Requisitos Previos

- **Python** (>=3.14) y el entorno virtual / gestor `uv`.
- **Node.js** y `npm`.

## Instalación y Ejecución

### Backend
Para trabajar únicamente en la API:
1. Navega a la carpeta `backend`:
   ```bash
   cd backend
   ```
2. Instala las dependencias y activa el entorno:
   ```bash
   uv sync
   ```
3. Ejecuta el servidor en modo desarrollo:
   ```bash
   uv run uvicorn main:app --reload
   ```
   *(También puedes usar el entorno virtual creado en `.venv/bin/python`)*

### Frontend
Para ejecutar la aplicación de escritorio completa (que levantará el backend automáticamente):
1. Navega a la carpeta `frontend`:
   ```bash
   cd frontend
   ```
2. Instala las dependencias de Node:
   ```bash
   npm install
   ```
3. Inicia la aplicación de Electron:
   ```bash
   npm start
   ```

> **Nota:** Al ejecutar el frontend, Electron ejecuta el comando `python3 -m uvicorn main:app ...` en el directorio del backend. Asegúrate de que las dependencias de Python estén instaladas globalmente o ajusta el `main.js` para usar el ejecutable dentro de `.venv/bin/python` (o ejecuta el comando desde un entorno virtual activado, el error `No module named uvicorn` suele ocurrir si uvicorn no está en el `python3` global).

## Estado Actual de Desarrollo
- [x] Arquitectura base del backend con FastAPI.
- [x] Conexión y estructuración de la Base de Datos SQLite.
- [x] Endpoints y CRUD de Libros funcionales.
- [x] Arquitectura base del frontend (Electron + React).
- [x] Lanzamiento automático del servidor backend desde Electron.
- [ ] Desarrollo de la UI/UX en React (Dashboard principal, listado de libros).
- [ ] Consumo de la API desde React para mostrar la información real de libros.
- [ ] Implementación de lógica y rutas para Personas y Préstamos.
