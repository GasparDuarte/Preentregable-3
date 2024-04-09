# imagen de Python más reciente como base
FROM python:3.12.1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el script y los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias del script
RUN pip install -r requirements.txt

# Comando para ejecutar el script
CMD ["python", "Preentrega3.py"]
