# Sistema-Teleferico
# SIMTELE-RISK 🚡

**Sistema de Simulación y Análisis de Riesgos en el Transporte por Cable**

Proyecto académico desarrollado para la asignatura de **Métodos Numéricos**.

## 📌 Descripción del proyecto

SIMTELE-RISK es una aplicación web educativa que permite modelar, simular y analizar escenarios hipotéticos relacionados con un sistema de transporte por cable, mediante la aplicación de métodos numéricos.

El sistema contempla cuatro módulos de estudio:

1. **Detención de emergencia de cabinas:** análisis de situaciones hipotéticas de detención.
2. **Deterioro mecánico y mantenimiento:** modelado del desgaste de componentes.
3. **Oscilaciones por viento:** simulación del comportamiento de las cabinas ante condiciones de viento.
4. **Reconstrucción de señales de sensores:** análisis y reconstrucción de datos mediante técnicas numéricas.

Cada módulo contempla escenarios NORMAL, ESTRÉS y MAL CONDICIONADO, permitiendo comparar resultados y estudiar el comportamiento de los métodos numéricos.

> **Nota:** Los datos y escenarios utilizados son sintéticos e hipotéticos. El proyecto tiene fines exclusivamente académicos y no representa fallas verificadas ni está conectado a equipos reales de transporte por cable.

---

## 🛠️ Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **Flask:** framework para el desarrollo web.
- **HTML5:** estructura de las páginas.
- **CSS3:** diseño y estilos de la interfaz.
- **JavaScript:** funcionalidades e interactividad.
- **Chart.js:** visualización de gráficos.
- **PostgreSQL:** base de datos prevista para la persistencia de información.
- **Git y GitHub:** control de versiones y trabajo colaborativo.

---

# 🚀 Instalación y ejecución del proyecto

Sigue estos pasos para ejecutar SIMTELE-RISK en tu computadora.

## 1. Requisitos previos

Antes de comenzar, asegúrate de tener instalados:

- Python 3.10 o superior.
- Git.
- Visual Studio Code (recomendado).

## 2. Descargar el proyecto

Abre una terminal y ejecuta:

```bash
git clone https://github.com/Jazmin-lm/Sistema-Teleferico.git
```

Ingresa a la carpeta:

```bash
cd Sistema-Teleferico
```

También puedes abrir la carpeta desde Visual Studio Code:

```bash
code .
```

## 3. Crear el entorno virtual

El entorno virtual permite instalar las dependencias del proyecto de manera aislada.

Ejecuta:

```bash
python -m venv venv
```

## 4. Activar el entorno virtual

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts, ejecuta primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después vuelve a activar el entorno:

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
venv\Scripts\activate.bat
```

Cuando esté activado, aparecerá `(venv)` al inicio de la terminal.

## 5. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará las bibliotecas necesarias para ejecutar el proyecto.

Si todavía no existe el archivo `requirements.txt` actualizado, instala Flask manualmente:

```bash
pip install flask
```

## 6. Ejecutar la aplicación

Desde la carpeta principal del proyecto, ejecuta:

```bash
python app.py
```

Si todo está correctamente configurado, Flask mostrará una dirección similar a:

```text
http://127.0.0.1:5000/
```

Abre esa dirección en tu navegador para visualizar SIMTELE-RISK.

Para detener el servidor, presiona:

```text
Ctrl + C
```

---

# 📂 Estructura del proyecto

```text
SIMTELE-RISK/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── backend/
│   ├── metodos/
│   │   ├── sistemas_lineales.py
│   │   ├── interpolacion.py
│   │   ├── raices.py
│   │   ├── integracion.py
│   │   └── edo.py
│   │
│   ├── modulos/
│   │   ├── detencion.py
│   │   ├── deterioro.py
│   │   ├── oscilaciones.py
│   │   └── sensores.py
│   │
│   └── errores.py
│
├── templates/
│   ├── index.html
│   ├── detencion.html
│   ├── deterioro.html
│   ├── oscilaciones.html
│   ├── sensores.html
│   └── historial.html
│
├── static/
│   ├── css/
│   │   └── estilos.css
│   └── js/
│       ├── principal.js
│       └── graficos.js
│
└── database/
    └── schema.sql
```

---

# 👥 Guía de trabajo colaborativo

Para mantener el proyecto organizado, cada integrante debe trabajar en su propia rama y evitar modificar directamente la rama principal (`main`).

## 1. Actualizar el proyecto

Antes de comenzar a trabajar, ejecutar:

```bash
git checkout main
git pull origin main
```

## 2. Crear una rama personal

Cada integrante debe crear una rama para desarrollar sus funcionalidades.

Ejemplo:

```bash
git checkout -b nombre-de-tu-rama
```

Algunos ejemplos:

- `rama-detencion`
- `rama-deterioro`
- `rama-oscilaciones`
- `rama-sensores`

## 3. Guardar los cambios

Después de realizar modificaciones:

```bash
git add .
git commit -m "Descripcion de los cambios realizados"
```

## 4. Subir los cambios a GitHub

```bash
git push -u origin nombre-de-tu-rama
```

Si ya habías publicado esa rama anteriormente:

```bash
git push
```

## 5. Integrar los cambios

Cuando el trabajo esté listo:

1. Entrar al repositorio en GitHub.
2. Seleccionar la opción **Compare & pull request**.
3. Crear un Pull Request dirigido a `main`.
4. Esperar la revisión del equipo.
5. Integrar los cambios mediante **Merge pull request** cuando sean aprobados.

**Importante:** Antes de comenzar una nueva tarea, actualiza tu rama con los últimos cambios de `main` para evitar conflictos.

---

## ⚠️ Recomendaciones

- No subir la carpeta `venv/` a GitHub.
- No compartir contraseñas ni archivos `.env`.
- Mantener actualizado el archivo `requirements.txt` cuando se agreguen dependencias.
- Realizar commits descriptivos y frecuentes.
- No modificar directamente `main`.
- Probar los cambios antes de crear un Pull Request.

---

## 🎯 Objetivo académico

Aplicar métodos numéricos para resolver modelos matemáticos, analizar errores, comparar resultados y estudiar el comportamiento de diferentes escenarios hipotéticos relacionados con el transporte por cable.

**SIMTELE-RISK — Métodos Numéricos.**