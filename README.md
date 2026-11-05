# Laboratorio 12 · Panorama de visitantes a Guatemala

Jorge Lopez · 221038 · Universidad del Valle de Guatemala · CC3066 Data Science

Avance del 5 de noviembre de 2026. Se utiliza **Tableau con autorización del docente**, en sustitución de Power BI. Se conservan las preguntas, los datos y los tres modelos del Laboratorio 10.

## Entrega

- [Informe de avance](entregables/Lab12_Avance_Tableau_Jorge_Lopez_221038.pdf).
- [Libro empaquetado de Tableau](entregables/Lab12_Avance_Jorge_Lopez_221038.twbx), con el Excel incluido.
- [Datos preparados](entregables/datos/Datos_Lab12.xlsx).

## Abrir el informe

Abrir el `.twbx` en Tableau Desktop. El avance se creó con una licencia de prueba que mostraba 14 días restantes; no se publicó en Tableau Cloud. La versión exacta de Tableau no se registró y debe completarse desde «Acerca de Tableau».

El dashboard `Dashboard 1` contiene `Evolucion Mensual` y `Visitantes por vía`. Seleccionar Terrestre en las barras filtra la línea; limpiar la selección recupera todas las vías. Las cuatro fuentes son Visitantes, Predicciones, Metricas y Observados, independientes entre sí para evitar multiplicar registros. Las hojas vacías adicionales corresponden a la incorporación de fuentes, no a visualizaciones adicionales.

El Excel empaquetado permite abrir el avance sin la ruta original del Mac. Para actualizarlo, sustituir las conexiones de cada fuente por `entregables/datos/Datos_Lab12.xlsx`, conservar los nombres de las hojas y actualizar. Guardar nuevamente como `.twbx` para incluir los datos. La carpeta de preparación anterior llamada `PowerBI_Avance` se consolidó en `datos`.

## Datos y reproducción

`Lab10-DataScience` se conserva como submódulo del repositorio original, fijado a su versión utilizada. Para obtenerlo al clonar:

```sh
git clone --recurse-submodules https://github.com/Jorge162017/PowerBI-DataScience.git
```

En una copia ya clonada: `git submodule update --init --recursive`.

Los scripts requieren Python, pandas, openpyxl y PyMuPDF:

```sh
python3 -m pip install pandas openpyxl PyMuPDF
python3 entregables/preparar_datos.py
python3 entregables/generar_avance_tableau.py
```

El primer script replica la limpieza de `src/datos.py` del Lab 10 y copia sus resultados predictivos existentes; no entrena modelos. Produce 3,946 filas exploratorias, 1,470 observados, 1,323 predicciones y 21 combinaciones serie–modelo. `verificacion_datos.json` contiene comprobaciones de las fuentes, no resultados de ejecución de las pruebas en Tableau.

## Pruebas comparativas planificadas

El PDF define pregunta, pasos y resultado esperado para tres tareas en Streamlit y Tableau: filtrar visitantes terrestres de enero–junio de 2025; pasar del año 2025 a trimestres y meses y regresar; consultar los tres modelos de Total visitantes en abril de 2021–junio de 2026. El total de control de la primera tarea es 1,043,269.4488721137; el menor MAE de la tercera es 165,372.6258489368, de suavizamiento exponencial.

La interacción del avance se comprobó mediante capturas y la acción guardada en el libro. Las mediciones de clics, tiempos, consistencia en ambas herramientas y las ocho visualizaciones completas corresponden al trabajo final. Para consultar Streamlit, seguir el README del submódulo Lab10-DataScience.
