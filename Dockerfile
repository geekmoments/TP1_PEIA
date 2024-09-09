# Utilizar una imagen oficial de Python 3
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar las dependencias especificadas en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos del proyecto al directorio de trabajo
COPY . .

# Comando para ejecutar el script Python
CMD ["python", "tp1_p3.py"]
