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
Para ejecutar Support2YouAPI como contenedor existen las siguientes opciones:
- Obtener la imagen del API con cualquiera de las siguientes opciones:
    - Realizar el build de la imagen en local: `docker build -t brventura/support2you-api:1.0.0 .`
    - Descargar la imagen desde DockerHub: `docker pull brventura/support2you-api:1.0.0`
- Ejecutar el contenedor: `docker run --rm -d --name support2you-api --env-file ./.env  -p 8080:8080 brventura/support2you-api:1.0.0` o `docker run -d --name support2you-api --env-file ./.env  -p 8080:8080 brventura/support2you-api:1.0.0` en caso que se quiera preservar el contenedor despues de detenido.