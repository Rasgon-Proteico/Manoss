# Manoss

con:
git clone https://github.com/Rasgon-Proteico/Manoss.git
debería jalar por si solo, si persisten problemas instalar las dependencias manualmente:

```bash
pip install mediapipe numpy opencv-python pygame
```

o ve directamente a sus páginas de guía

### **Alternativa de Ejecución con UV (Método Rápido)**

Si ya tienes `uv` instalado, puedes usar un flujo de trabajo mucho más rápido para configurar y ejecutar el proyecto. Estos comandos asumen que ya clonaste el repositorio y estás en la carpeta `Manoss`.

1.  **Sincroniza las dependencias:**
    Este comando leerá las dependencias del proyecto (desde `requirements.txt` o `pyproject.toml`) y las instalará en un entorno virtual de forma extremadamente rápida.
    ```bash
    uv sync
    ```

2.  **Ejecuta el script:**
    Usa `uv run` para ejecutar el programa. Este comando se encarga de usar el entorno virtual correcto sin que necesites activarlo manualmente (`source .venv/bin/activate`).
    ```bash
    uv run python Videos.py
    ```
