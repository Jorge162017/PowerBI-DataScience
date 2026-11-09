# Laboratorio 12 · Panorama de visitantes a Guatemala

Jorge Lopez · 221038 · Universidad del Valle de Guatemala · CC3066 Data Science

Avance del 5 de noviembre de 2026. Se utiliza **Tableau con autorización del docente**, en sustitución de Power BI. Se conservan las preguntas, los datos y los tres modelos del Laboratorio 10.

## Preparación de la entrega final · 8 de noviembre

### Versión revisada para entrega

- [Libro final de Tableau](entregables/Lab12_Final_Jorge_Lopez_221038.twbx).
- [PDF de diseño y evaluación](entregables/final/Lab12_Informe_Final_Jorge_Lopez_221038.pdf) y [fuente editable](entregables/final/INFORME_FINAL.md).
- [Resultados funcionales de Streamlit](entregables/final/evidencias/resultados_streamlit.json) y [auditoría del libro Tableau](entregables/final/evidencias/auditoria_tableau.json).

El libro revisado contiene ocho hojas, tres dashboards, dos acciones de filtro y los dos Excel empaquetados. Tableau usa métricas de prueba completa y Total visitantes; las curvas observadas se incluyen una sola vez por mes. La navegación se hace mediante pestañas. La fecha filtra seis hojas exploratorias; en el archivo revisado no se identificó una tarjeta visible de ese filtro en el dashboard, por lo que se debe guardar de nuevo después de mostrarla. No editar directamente el XML mientras Tableau esté abierto.

Las tres tareas funcionales de Streamlit se ejecutaron con AppTest y datos reales. Sus tiempos son automatizados, sin clics humanos; no son comparables con las estimaciones de Tableau (aproximadamente 60 segundos y 8, 12 y 1 clics). La consistencia compara salidas de Streamlit con las fuentes empaquetadas de Tableau; el documento identifica ese límite. No se midieron horas de construcción. El PDF no incorpora capturas exportadas de las aplicaciones.

Para regenerar el PDF revisado:

```sh
python3 -c "import sys; sys.path.insert(0, 'entregables/final'); from generar_documentos import render; render('INFORME_FINAL.md', 'Lab12_Informe_Final_Jorge_Lopez_221038.pdf')"
```

Las secciones siguientes conservan los materiales de preparación y los enlaces del avance, que no deben confundirse con los dos archivos de entrega revisados de arriba.

La preparación está lista; la implementación final en Tableau y las pruebas de uso siguen pendientes. No confundir estos borradores con la entrega final completada.

- [Guía de construcción en Tableau](entregables/final/TU_PARTE_TABLEAU.md) y [PDF de la guía](entregables/final/Guia_Tableau_221038.pdf).
- [Documento final editable, en preparación](entregables/final/INFORME_FINAL_BORRADOR.md) y [PDF borrador](entregables/final/Lab12_Informe_Final_BORRADOR_221038.pdf).
- [Datos auxiliares de modelos](entregables/final/datos/Modelos_Tableau.xlsx): Curvas evita duplicar el observado; Evaluacion permite recalcular MAE/RMSE según filtros.
- [Registro de pruebas](entregables/final/REGISTRO_PRUEBAS.csv), [consistencia](entregables/final/CONSISTENCIA.csv) y [entorno y tiempos](entregables/final/REGISTRO_ENTORNO_Y_TIEMPOS.csv).

Se verificó la versión del avance en su XML: **Tableau 2026.3.0, build 20263.26.1022.1645, plataforma mac**. Las capturas del avance mostraban una licencia de prueba; registrar el estado vigente al terminar. El avance contiene siete tablas en su Excel, pero solo cuatro fuentes conectadas y dos gráficas; el Excel auxiliar final aún debe conectarse. Las mediciones de rendimiento y tiempos de trabajo no se infieren de Git.

Para regenerar la preparación:

```sh
python3 -m pip install -r entregables/requirements-documentacion.txt
python3 entregables/preparar_final.py
python3 entregables/final/generar_documentos.py
```

El script de preparación verifica claves únicas, concordancia de observados y las 21 combinaciones de métricas con sus fuentes. Valores de control: [controles_final.json](entregables/final/datos/controles_final.json). No sustituyen resultados leídos en las interfaces de ambas herramientas.

Para preparar el entorno local de Streamlit:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r Lab10-DataScience/requirements.txt
```

Después, ejecutar `./iniciar_lab10.command` desde la raíz del proyecto. El script abre la aplicación del Lab 10 usando ese entorno, sin modificar el submódulo. El directorio `.venv` no se sube a Git; las versiones instaladas para la revisión se guardan en `entregables/final/entorno_verificacion.txt` cuando la instalación y la comprobación terminen.

## Entrega

- [Informe de avance](entregables/Lab12_Avance_Tableau_Jorge_Lopez_221038.pdf).
- [Libro empaquetado de Tableau](entregables/Lab12_Avance_Jorge_Lopez_221038.twbx), con el Excel incluido.
- [Datos preparados](entregables/datos/Datos_Lab12.xlsx).

## Abrir el informe

Abrir el `.twbx` en Tableau Desktop. El avance se creó con una licencia de prueba que mostraba 14 días restantes; no se publicó en Tableau Cloud. La versión guardada en el libro es Tableau 2026.3.0 (20263.26.1022.1645), plataforma mac; se obtuvo revisando su XML.

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
