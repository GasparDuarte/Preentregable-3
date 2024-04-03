# Usa una imagen de Python más reciente como base
FROM python:3.12.1-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el script y los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias del script
RUN pip install --no-cache-dir requests psycopg2-binary pandas python-dotenv

# Comando para ejecutar el script
CMD ["python", "Preentrega3.py"]
