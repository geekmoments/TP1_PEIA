
# TP1 - Proyecto de Probabilidad y Estadística

Este proyecto analiza datos de ventas de un supermercado y genera gráficos que muestran la distribución empírica y la estimación de densidad de los años 2021, 2022 y 2023. El proyecto se ejecuta utilizando **Docker** y **Python**, y los gráficos se guardan como archivos de imagen (`.png`).

## Requisitos

- Docker (instalado y funcionando en tu sistema)
- Archivo de datos en formato Excel (`.xlsx`)

## Estructura del proyecto

```
.
├── data/
│   └── Datos_2544003.xlsx      # Archivo de datos en Excel
├── Dockerfile                  # Archivo Docker para crear la imagen
├── requirements.txt            # Lista de dependencias de Python
├── tp1_p3.py                   # Script Python principal
├── output/                     # Carpeta donde se guardarán los gráficos
└── README.md                   # Este archivo
```

## Instrucciones para ejecutar el proyecto

### 1. Construir la imagen Docker

Ejecuta el siguiente comando en el directorio raíz del proyecto (donde se encuentra el archivo `Dockerfile`) para construir la imagen Docker:

```bash
docker build -t tp1_ccruz .
```

Este comando creará una imagen llamada `tp1_ccruz`.

### 2. Ejecutar el contenedor Docker

Una vez construida la imagen, puedes ejecutar el contenedor usando el siguiente comando:

```bash
docker run -v ${PWD}/data:/app/data -v ${PWD}/output:/app/output tp1_ccruz
```

Este comando hace lo siguiente:

- **`-v ${PWD}/data:/app/data`**: Monta la carpeta local `data` para que el archivo Excel esté disponible dentro del contenedor.
- **`-v ${PWD}/output:/app/output`**: Monta la carpeta local `output` para que los gráficos generados se guarden en tu máquina local.

### 3. Ver los resultados

Una vez que el contenedor termine de ejecutarse, los gráficos generados se guardarán como archivos `.png` en la carpeta `output` en tu máquina local. Verás archivos como:

```
output/
├── distribution_2021.png
├── distribution_2022.png
└── distribution_2023.png
```

Puedes abrir estos archivos para visualizar la distribución empírica y la estimación de densidad de las ventas.

## Dependencias

Las dependencias necesarias para este proyecto están listadas en el archivo `requirements.txt`:

```txt
pandas
matplotlib
seaborn
scipy
openpyxl
```

Estas dependencias se instalan automáticamente cuando se construye la imagen Docker.

## Notas adicionales

- Si el archivo Excel tiene un nombre diferente, asegúrate de actualizar el código en `tp1_p3.py` para apuntar al archivo correcto.
- Este proyecto está diseñado para ejecutarse completamente dentro de Docker, por lo que no necesitas instalar Python o las dependencias en tu máquina local.

```

