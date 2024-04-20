# Support2You API project

Este proyecto contiene el API de Support2You que provee acceso a través de llamadas HTTP a la API de OpenAI para la solución de problemas técnicos que los clientes de la empresa hipotética de atención al cliente tienen.

## Tecnologías
- Python 3.9.
- FastAPI.
- Dependency Injector.
- SQL Alchemy con SQLite.
- Uvicorn server.

## Ejecución del proyecto

- Creación del entorno virtual: `py -3.9 -m venv .venv` o ` python -m venv .venv`.
- Activación del entorno virtual: Ejecutar el script de activación `activate` del entorno (`.\.venv\Scripts\activate`).
- Instalación de requerimientos: Ejecutar `pip install -r .\requirements.txt`
- Creación de archivo `.env`: Crear archivo `.env` en la raíz del proyecto y copiar el contenido del archivo `.env.example` cambiando los valores de las variables al correspondiente.
- Ejecutar proyecto: Ejecutar la aplicación con `uvicorn main:app` o `uvicorn main:app --reload` para la recarga activa de cambios.

## Estructura
Próximamente...

## Docker
Próximamente...