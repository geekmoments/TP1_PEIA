import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

file_path = './data/Datos_2544003.xlsx'  
data = pd.read_excel(file_path)

# conv de la columna 'Fecha' a formato datetime
data['Fecha'] = pd.to_datetime(data['Fecha'])
data['Año'] = data['Fecha'].dt.year

# Separar  
data_2021 = data[data['Año'] == 2021]
data_2022 = data[data['Año'] == 2022]
data_2023 = data[data['Año'] == 2023]

#   generar y guardar los Graf  de dist emp y densidad
def plot_empirical_distribution_and_density(data, year):
    ventas = data['Ventas']
    
    # calculo la CDF emp
    sorted_ventas = np.sort(ventas)
    cdf = np.arange(1, len(sorted_ventas) + 1) / len(sorted_ventas)

    # estim de densidad con KDE
    kde = gaussian_kde(ventas)
    x_range = np.linspace(min(ventas), max(ventas), 1000)
    density = kde(x_range)

    # graf la CDF emp y la est de densidad
    fig, ax1 = plt.subplots(2, 1, figsize=(10, 8))

    # graf la CDF
    ax1[0].step(sorted_ventas, cdf, where='post')
    ax1[0].set_title(f'Empirical CDF for {year}')
    ax1[0].set_xlabel('Ventas')
    ax1[0].set_ylabel('Cumulative Probability')

    # graf la densidad
    ax1[1].plot(x_range, density)
    ax1[1].set_title(f'Density Estimation (KDE) for {year}')
    ax1[1].set_xlabel('Ventas')
    ax1[1].set_ylabel('Density')

    plt.tight_layout()
    plt.savefig(f'./output/distribution_{year}.png')   
    plt.close()

# Crear el directorio outout
import os
if not os.path.exists('./output'):
    os.makedirs('./output')

# Generar Graf
plot_empirical_distribution_and_density(data_2021, 2021)
plot_empirical_distribution_and_density(data_2022, 2022)
plot_empirical_distribution_and_density(data_2023, 2023)
