# 🚲 Seoul Bike Sharing Demand Forecasting v1.0.0
## Sistema de Machine Learning para Predicción de Demanda Horaria de Bicicletas Públicas

[![Python 3.11](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)](F_Docker/Dockerfile)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Autor](https://img.shields.io/badge/Autor-developed_by_Miguel_Benítez_(UTP)-informational.svg)](https://github.com/miguelbenitez09)

> **Firma Oficial:** **`Seoul Bike Sharing Demand v1.0.0 • developed by Miguel Benítez`**  
> **Autor Principal:** **Ing. Miguel Antonio Benítez González** (Universidad Tecnológica de Panamá - UTP)  
> **Email:** `mbenitezg01@gmail.com` | **GitHub:** [@miguelbenitez09](https://github.com/miguelbenitez09) | **LinkedIn:** [Miguel Antonio Benítez González](https://www.linkedin.com/in/miguel-antonio-ben%C3%ADtez-gonz%C3%A1lez-457816247/)  
> **Licencia:** MIT License con Atribución Obligatoria  
> **Dataset:** UCI Machine Learning Repository (8,760 registros horarios, 14 features)  

---

## 📋 Información del Dataset

**Nombre:** Seoul Bike Sharing Demand Dataset  
**Fuente:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand)  
**Autor del Dataset:** Sathishkumar V E  
**DOI:** 10.24432/C5F62R

### Descripción
Este conjunto de datos contiene información sobre el sistema de bicicletas compartidas de Seúl, incluyendo el conteo de bicicletas alquiladas por hora junto con datos meteorológicos y estacionales. El objetivo es predecir la demanda de bicicletas basándose en las condiciones ambientales y temporales.

### Características Principales
El dataset consta de **8,760 instancias** (365 días × 24 horas) y **14 variables** (features), incluyendo:
- **Datos temporales:** Fecha, hora, estación del año, días festivos
- **Datos meteorológicos:** Temperatura, humedad, velocidad del viento, visibilidad, punto de rocío
- **Condiciones climáticas:** Radiación solar, lluvia, nieve
- **Variable objetivo (Target):** Rented Bike Count - Número de bicicletas alquiladas por hora

## 📊 Descripción de Variables del Dataset

### 🎯 Variable de Respuesta (Target)

* **`Rented Bike Count`**: Número de bicicletas alquiladas en cada hora
    * **Tipo**: Numérico continuo
    * **Rango**: 0 - 3,556 bicicletas

---

### 📝 Variables Explicativas (Features)

| Variable | Descripción | Tipo de Dato | Unidades |
| :--- | :--- | :--- | :--- |
| **Date** | Fecha de la observación | Fecha | dd/MM/yyyy |
| **Hour** | Hora del día | Numérico | 0-23 |
| **Temperature(°C)** | Temperatura del aire | Numérico | °Celsius |
| **Humidity(%)** | Humedad relativa | Numérico | % |
| **Wind speed (m/s)** | Velocidad del viento | Numérico | m/s |
| **Visibility (10m)** | Visibilidad | Numérico | 10m |
| **Dew point temperature(°C)** | Temperatura del punto de rocío | Numérico | °Celsius |
| **Solar Radiation (MJ/m2)** | Radiación solar | Numérico | MJ/m² |
| **Rainfall(mm)** | Precipitación | Numérico | mm |
| **Snowfall (cm)** | Nevada | Numérico | cm |
| **Seasons** | Estación del año | Categórica | Winter, Spring, Summer, Autumn |
| **Holiday** | Indicador de día festivo | Categórica | Holiday, No Holiday |
| **Functioning Day** | Indicador de día operativo | Categórica | Yes, No |

---

## 📁 Estructura del Proyecto

```
seoul_bike_sharing_demand/
├── README.md                           # Documentación del proyecto
├── A_data/                             # Datos del proyecto
│   ├── 01_raw/                         # Datos crudos originales
│   │   └── seoul_bike_data.csv
│   └── 02_processed/                   # Datos procesados
│       └── processed_bike_data.csv
├── B_notebooks/                        # Notebooks de Jupyter
│   ├── 01_exploracion_dataset.ipynb    # Exploración inicial de datos
│   ├── 02_preprocesamiento_dataset.ipynb  # Limpieza y transformación
│   └── 03_modelado_dataset.ipynb       # Entrenamiento del modelo
├── C_src/                              # Código fuente adicional
│   └── retrain_model.py                # Script para reentrenar el modelo
├── D_models/                           # Modelos entrenados
├── E_reports/                          # Reportes y resultados
├── F_Docker/                           # Configuración de Docker
│   ├── docker-compose.yml
│   └── Dockerfile
├── G_api/                              # API REST
│   ├── main.py                         # Código principal de la API
│   ├── requirements.txt                # Dependencias de la API
│   └── test_api.py                     # Script de pruebas
└── H_webInterface/                     # Interfaz web
    ├── app.py                          # Aplicación Streamlit
    ├── requirements.txt                # Dependencias de la interfaz
    └── README.md                       # Documentación de la interfaz
```

### Flujo de Trabajo

1. **Exploración (B_notebooks/01_*)**: Análisis inicial del dataset, patrones temporales y estacionales
2. **Preprocesamiento (B_notebooks/02_*)**: Feature engineering, tratamiento de series temporales
3. **Modelado (B_notebooks/03_*)**: Entrenamiento de modelos de regresión y evaluación
4. **API (G_api/)**: Despliegue del modelo como servicio REST
5. **Interfaz Web (H_webInterface/)**: Interfaz gráfica para predicciones de demanda
6. **Docker (F_Docker/)**: Contenedorización para producción

### Casos de Uso
- **Optimización de inventario**: Predecir cuántas bicicletas se necesitan en cada estación
- **Planificación operativa**: Redistribución de bicicletas según demanda esperada
- **Análisis de patrones**: Identificar factores que influyen en el uso del sistema

---

**Firma Oficial del Proyecto:**  
`Seoul Bike Sharing Demand v1.0.0 • developed by Miguel Benítez`  
Ing. Miguel Antonio Benítez González (Universidad Tecnológica de Panamá - UTP) · 2026.
