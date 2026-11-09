# Verificación de la preparación · 8 de noviembre de 2026

- Excel auxiliar regenerado y reabierto: 1,764 filas de Curvas y 1,323 de Evaluacion.
- Siete series, cuatro curvas por serie (observado y tres modelos), 63 meses por curva; claves únicas.
- Observado de predicciones coincide con la fuente de observados en todo el conjunto de prueba.
- Las 21 combinaciones serie–modelo reproducen MAE y RMSE de los CSV; diferencias máximas 8.74e-11 y 2.92e-11 respectivamente, atribuibles a precisión numérica.
- Siete pruebas existentes del Lab 10 ejecutadas y aprobadas: agregaciones, períodos parciales, ausencias frente a ceros, porcentajes, restablecimiento de filtros, cobertura predictiva y evaluación de intervalos.
- Comando: `.venv/bin/python -m unittest discover -s tests -v`, ejecutado desde Lab10-DataScience usando la ruta absoluta del intérprete de la raíz.
- PDFs generados y revisados visualmente por muestra, sin modificar el avance.

El entorno se registra en entorno_verificacion.txt. Estas comprobaciones automatizadas no sustituyen las tres pruebas comparativas de usuario, los tiempos y clics, ni la revisión del libro final de Tableau, que siguen pendientes.
