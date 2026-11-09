# Laboratorio 12 · Panorama de visitantes a Guatemala

Jorge Lopez · 221038 · Universidad del Valle de Guatemala · CC3066 Data Science

Entrega final del 8 de noviembre de 2026. Se utilizó Tableau en sustitución de Power BI, con autorización del docente.

## Archivos de entrega

- [Informe final en PDF](entregables/final/Lab12_Informe_Final_Jorge_Lopez_221038.pdf).
- [Libro final de Tableau con datos incluidos](entregables/Lab12_Final_Jorge_Lopez_221038.twbx).
- [Resultados de las pruebas](entregables/final/REGISTRO_PRUEBAS.csv) y [consistencia de indicadores](entregables/final/CONSISTENCIA.csv).

El avance del 5 de noviembre se conserva en entregables/ como evidencia de versiones: PDF y libro .twbx. El historial de Git conserva los cambios del trabajo individual.

## Abrir y consultar

Abrir el libro final en **Tableau Desktop 2026.3.0**, build 20263.26.1022.1645, plataforma mac. Se utilizó una licencia de prueba; no se publicó en Tableau Cloud. El archivo .twbx incluye los Excel y permite abrirlo sin las rutas originales.

Las pestañas Panorama, Mercados y vias y Modelos y limites organizan ocho visualizaciones. Seleccionar una vía filtra la evolución; seleccionar una región en el ranking filtra evolución regional y composición. Pulsar otra vez la marca limpia la selección. Los signos + y − de la fecha permiten cambiar entre año, trimestre y mes. File → Revert recupera la versión guardada y descarta cambios de edición no guardados.

Las curvas y las métricas muestran Total visitantes, abril de 2021–junio de 2026. Las métricas son de todo el período, sin recalcularse con filtros exploratorios. El filtro Fecha se aplica a las seis hojas de exploración; en el paquete revisado no se identificó su tarjeta visible en los dashboards. Las limitaciones y el alcance de las verificaciones se documentan en el PDF.

## Datos y actualización

- entregables/datos/Datos_Lab12.xlsx: Visitantes, Observados, Predicciones y Metricas, más dimensiones auxiliares.
- entregables/final/datos/Modelos_Tableau.xlsx: Curvas, Evaluacion y MetricasReferencia. El libro usa Curvas; Evaluacion queda disponible para reproducir los errores.
- entregables/final/evidencias/: resultados funcionales automatizados de Streamlit y auditoría estructural y numérica del Tableau.
- Lab10-DataScience/: submódulo del repositorio original con código, documentación y fuentes del Lab 10.

Las fuentes se conectan por separado, sin joins de hechos. Predicciones contiene 1,323 filas, siete series y tres modelos; Metricas conserva 21 combinaciones serie–modelo. Curvas evita repetir el observado por modelo. No se entrenan modelos nuevos.

Para cambiar rutas: Data → seleccionar fuente → Edit Connection → elegir el Excel de este repositorio y conservar la hoja correspondiente. Actualizar, comprobar totales y guardar otra vez como .twbx para incluir los datos.

## Reproducir

```sh
git clone --recurse-submodules https://github.com/Jorge162017/PowerBI-DataScience.git
cd PowerBI-DataScience
python3 -m venv .venv
.venv/bin/python -m pip install -r Lab10-DataScience/requirements.txt
./iniciar_lab10.command
```

En una copia ya clonada: git submodule update --init --recursive. El README del submódulo contiene las instrucciones completas del Lab 10.

Para preparar los datos y el PDF:

```sh
python3 -m pip install -r entregables/requirements-documentacion.txt
python3 entregables/preparar_datos.py
python3 entregables/preparar_final.py
python3 entregables/final/generar_documentos.py
```

El archivo INFORME_FINAL.md es la fuente editable del PDF y se conserva para reproducirlo. Los scripts no modifican el libro Tableau ni ajustan modelos.

## Pruebas

Tres tareas: filtrar visitantes terrestres de enero–junio de 2025; pasar del año 2025 a trimestres y meses y regresar; consultar curvas y comparar MAE/RMSE de los tres modelos de Total visitantes en toda la prueba. El protocolo, los resultados y los límites se encuentran en el PDF y los CSV.

Para repetir las comprobaciones funcionales de Streamlit:

```sh
.venv/bin/python entregables/final/verificar_streamlit.py
```

Los tiempos de Tableau son estimaciones del estudiante. Las comprobaciones de Streamlit se ejecutaron con AppTest; sus tiempos son automatizados y no representan un recorrido humano ni son comparables directamente con Tableau. No se registraron horas totales de construcción. El entorno está en entregables/final/entorno_verificacion.txt.
