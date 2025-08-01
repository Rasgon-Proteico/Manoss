# Manoss
Este proyecto es un piano virtual que utiliza la cámara web para detectar los gestos de las manos y generar notas musicales en tiempo real.
con:
```bash
git clone https://github.com/Rasgon-Proteico/Manoss.git
```

debería jalar por si solo, si persisten problemas instalar las dependencias manualmente:

```bash
pip install mediapipe numpy opencv-python pygame
```
o ve directamente a sus páginas de guía



### **Alternativa de Ejecución con UV (Método Rápido,Recomendado)**

## Requisitos

- Python 3.9 o superior
- `uv` (para gestionar el entorno y las dependencias)

Si ya tienes `uv` instalado, puedes usar un flujo de trabajo mucho más rápido para configurar y ejecutar el proyecto. Estos comandos asumen que ya clonaste el repositorio y estás en la carpeta `Manoss`.

1. **Activa el entorno virtual:**
    - En Linux/macOS:
      ```bash
      source .venv/bin/activate
      ```
    - En Windows (PowerShell):
      ```bash
      .venv\Scripts\Activate.ps1
      ```


2.  **Sincroniza las dependencias:**
    Este comando leerá las dependencias del proyecto (desde `requirements.txt` o `pyproject.toml`) y las instalará en un entorno virtual de forma extremadamente rápida.
    ```bash
    uv sync
    ```

3.  **Ejecuta el script:**
    Usa `uv run` para ejecutar el programa. Este comando se encarga de usar el entorno virtual correcto sin que necesites activarlo manualmente (`source .venv/bin/activate`).
    ```bash
    uv run python Videos.py
    ```
6.  **Salida**
Presiona la tecla `ESC` en la ventana de la cámara para salir.
"deactivate" para salier del entorno virtual

