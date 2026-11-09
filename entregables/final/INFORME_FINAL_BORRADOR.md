# Panorama de visitantes a Guatemala

**Laboratorio 12 · Documento de diseño y comparación de herramientas**  
Universidad del Valle de Guatemala · Facultad de Ingeniería · CC3066 Data Science  
Semestre II, 2026 · 8 de noviembre de 2026  
**Jorge Lopez · 221038**

**Versión de preparación: pendiente de implementación final, capturas y pruebas de usuario.** Este documento reúne el trabajo que puede completarse antes de finalizar Tableau. No debe entregarse como una evaluación final ya ejecutada.

## 1. Propósito, público y alcance

Se traslada a Tableau el tablero del Laboratorio 10, desarrollado en Python, Streamlit y Plotly. El estudiante comunicó autorización del docente para sustituir Power BI; se mantienen el alcance y los requisitos de interacción. La comparación relevante será Tableau frente a Streamlit, no una implementación de Power BI que no se realizó.

El público son responsables de operación, promoción y planificación de empresas turísticas sin formación estadística especializada. El tablero apoya la planificación de personal, capacidad y campañas mediante el contexto nacional de visitantes; no estima ventas u ocupación de una empresa específica.

Las preguntas se conservan: ¿cómo evoluciona la afluencia?; ¿qué meses concentran visitas?; ¿qué vías predominan?; ¿qué mercados de origen aportan más y cómo evolucionan?; ¿cómo cambia la composición por vía entre regiones?; ¿qué modelos estuvieron más cerca de los observados?

La exploración abarca enero de 2009–junio de 2026, con visitantes = Turista + Excursionista. Las entradas no equivalen a personas únicas, gasto, ingresos, impacto ambiental ni demanda por destino. El observatorio recibe contexto turístico, sin afirmar que estas variables midan sostenibilidad. No se atribuyen causas a cambios observados.

La evaluación usa siete series: total, vías aérea, terrestre y marítima, y regiones América del Centro, América del Norte y Europa. Se reutilizan suavizamiento exponencial, Holt–Winters y ARIMA/SARIMA. No se entrenan nuevos modelos. LSTM del Lab 2 no se incorpora por tener otro protocolo de evaluación.

El avance guardado incluye dos visualizaciones y las fuentes de modelos. Las seis gráficas restantes, controles y resultados de pruebas están pendientes de revisión del libro final.

---

# 2. Diseño y navegación

## Paleta y legibilidad

Se propone conservar los colores del Lab 10. El fondo #0B141B y los paneles #14251F agrupan información; #20735F distingue controles. Texto principal #E7F0EB y secundario #B6C7BE. Observado y terrestre usan turquesa #62D9C4; suavizamiento y marítima ámbar #F4B860; ARIMA/SARIMA y aérea lavanda #A9BCFF; Holt–Winters rosa #DCA7D8. Vías y modelos aparecen en contextos separados, con leyendas explícitas.

Las regiones conservarán colores entre ranking y evolución. Los colores naturales representan identidad, no una calificación de sostenibilidad. Se empleará tipografía sans serif, títulos descriptivos, ejes con unidades y detalles por cursor. Las leyendas y etiquetas permiten identificar series sin depender solo del color. El avance usa fondo blanco y azul predeterminado; el formato final debe comprobarse con capturas.

## Organización propuesta

| Vista | Contenido y controles |
|---|---|
| Panorama | Evolución temporal, volumen por vía y estacionalidad; período, región y vía. |
| Mercados y vías | Ranking, evolución regional y composición; filtros de exploración compartidos. |
| Modelos y límites | Observado/predicho y errores; serie, modelos, período de prueba y métrica. |

Las tres vistas tendrán navegación por botones y pestañas. Las barras de vía filtran la evolución; el ranking regional filtrará las vistas de mercados. Año–trimestre–mes permitirá variar el detalle y regresar. Se ofrecerá limpieza de selecciones y retorno a la vista guardada con instrucciones visibles.

Se conservarán las preguntas, las secciones y la intención de las ocho gráficas. El cambio principal será pasar del estado de sesión y controles programados de Streamlit a hojas, dashboards y acciones de Tableau. No se contabilizan tarjetas, filtros o botones como gráficas.

Las vistas señalarán que 2026 termina en junio, que los períodos parciales requieren meses comparables y que una vista vacía requiere revisar filtros. La cobertura marítima, el cambio metodológico desde 2023 y la ruptura pandémica se conservarán como límites del Lab 10.

**Evidencias pendientes:** capturas finales de Panorama, Mercados y vías y Modelos y límites, más una selección enlazada.

---

# 3. Ocho visualizaciones equivalentes

La tabla define el diseño final a implementar y revisar. Las dos primeras existen en el avance; las restantes aún deben comprobarse en Tableau.

| Lab 10 → Tableau | Elección y finalidad |
|---|---|
| 1. Evolución → línea temporal | Mantiene continuidad y muestra cambios de afluencia. SUM de visitantes por fecha, con filtros y detalle temporal. Responde a selección de vía. |
| 2. Volumen por vía → barras horizontales | Compara magnitudes de las tres vías con base común. Una selección filtra la evolución; se comprobó en el avance. |
| 3. Estacionalidad → matriz año × mes | Intensidad de color para reconocer temporadas y rupturas. Se conservarán meses sin cobertura como ausentes y los ceros registrados como cero. |
| 4. Mercados de origen → ranking horizontal | Facilita leer regiones y comparar cantidades. Se propone ranking completo ordenado; sustituye el Top N ajustable del Lab 10 para evitar ocultar población en el prototipo. |
| 5. Evolución regional → líneas por región | Compara trayectorias en un mismo eje temporal. La selección del ranking y los filtros reducen series para mantener legibilidad. |
| 6. Región–vía → barras al 100% | Compara composición sin confundirla con volumen; las cantidades quedan en el detalle. Una vista auxiliar en cantidades conservará ese modo del Lab 10. |
| 7. Observado/predicho → líneas | Una única serie de gestión, observado y tres modelos, en el mismo período de prueba. Colores y leyendas distinguen resultados reales y estimados. |
| 8. Error → barras de MAE/RMSE | Permite comparar los tres modelos dentro de la misma serie y conjunto evaluado. Se recalcularán errores con el período elegido. |

En la vista 6 se recalculan los porcentajes entre las vías seleccionadas por cada región. Una región con total cero no tiene composición porcentual interpretable.

En las vistas 7–8, las series de gestión son agregaciones distintas y algunas se superponen. Seleccionar una sola serie evita sumar total y subconjuntos. Las métricas en visitantes no se compararán como si midieran desempeño relativo entre series de escalas diferentes.

**Cambios a confirmar:** filtros de modelos sincronizados o separados explícitamente; forma definitiva de cambiar nivel temporal; navegación, restablecimiento y modo de cantidades. La versión final del documento debe describir el comportamiento realmente guardado.

---

# 4. Datos, cálculos y modelos

## Preparación reproducible

`preparar_datos.py` reutiliza `src/datos.py` del Lab 10: lee la hoja Datos del Excel original, normaliza textos, convierte año/mes/cantidad, elimina filas duplicadas, crea la fecha mensual y filtra fechas válidas, valores no negativos y tipos Turista/Excursionista. Agrupa por Fecha–Region–Via y suma visitantes; conserva decimales y ceros válidos. No se modifica la base original.

El Excel del avance contiene 3,946 registros exploratorios, 1,470 observados, 1,323 predicciones y 21 combinaciones serie–modelo con métricas. Se importaron como fuentes separadas; no se hicieron joins de hechos ni relaciones muchos a muchos. Esto evita multiplicar visitantes o el observado repetido por modelo.

`preparar_final.py` añade `Modelos_Tableau.xlsx`: Curvas tiene 1,764 filas, con Observado una vez por Serie–Fecha y tres predicciones por mes; Evaluacion tiene 1,323 filas con error absoluto y cuadrado. Son transformaciones de los CSV existentes, sin entrenamiento. Se comprobaron claves únicas, coincidencia del observado y concordancia de las 21 métricas con los originales, con diferencias inferiores a 0.000000001 por precisión numérica.

## Cálculos con finalidad analítica

Visitantes: SUM del campo de cantidad; fecha de vista: DATETRUNC según año, trimestre o mes. Composición: porcentaje de total calculado sobre Via, particionado por Region y después de filtros. MAE: AVG(ErrorAbsoluto). RMSE: SQRT(AVG(ErrorCuadrado)). El parámetro Métrica permite elegir MAE o RMSE sin mezclar unidades.

No se suman observados de la tabla de predicciones para construir la curva real. No se promedian RMSE preagregados. El archivo de métricas originales es referencia de toda la prueba, no una medida del subintervalo filtrado. El redondeo se limita a presentación.

## Evaluación y límites

Entrenamiento: enero de 2009–marzo de 2021, 147 meses. Prueba: abril de 2021–junio de 2026, 63 meses. Se evalúa un horizonte fijo sin actualizar con observaciones de prueba. Las curvas fueron exportadas en el Lab 10 reproduciendo configuraciones del Lab 1, porque el notebook conservaba métricas e imágenes, no valores numéricos originales; concordar con métricas redondeadas no demuestra identidad exacta de curvas.

MAE y RMSE están en visitantes. Menor error histórico no garantiza mejor desempeño futuro. Los ceros marítimos de la prueba reflejan la cobertura disponible y no demuestran ausencia real de actividad.

---

# 5. Comparación de implementaciones

Evidencia disponible: código, README y PDF del Lab 10; estructura del `.twbx` de avance y capturas revisadas. La matriz no adjudica tiempos ni resultados de las pruebas pendientes. Las implicaciones son interpretaciones que se confirmarán con las mediciones.

| Criterio | Evidencia en Streamlit | Evidencia en Tableau | Implicación para la tarea |
|---|---|---|---|
| Aprendizaje | Controles y estado escritos en Python. | Arrastrar campos, elegir SUM y mes continuo exigió ajustes durante el avance. | Tableau requiere entender agregación; medir facilidad con tareas equivalentes. |
| Tiempo de desarrollo | Ocho gráficas en el código del Lab 10; horas no registradas aquí. | Dos gráficas y cuatro fuentes en el avance; tiempo aún no medido. | No concluir cuál es más rápido a partir del orden de implementación. |
| Preparación y actualización | Limpieza centralizada en datos.py y caché. | Excel preparado, cuatro fuentes independientes; rutas empaquetadas. | Python explicita transformación; Tableau requiere actualizar y comprobar conexiones. |
| Modelos | Lee CSV y recalcula errores con el intervalo seleccionado. | Fuentes conectadas; Curvas y Evaluacion preparadas, pendientes de incorporar. | Reutilización equivalente sin entrenar; comprobar filtrado final. |
| Interacción y navegación | Tres secciones y selecciones enlazadas documentadas. | Acción vías → evolución guardada en el avance; resto pendiente. | Comparar pasos reales de navegación y limpieza. |
| Personalización | Plotly y estado de sesión permiten controles propios. | Hojas y acciones nativas; formato final pendiente. | Streamlit ofrece control por código; Tableau reduce programación de vistas convencionales. |
| Rendimiento | Lectura con caché; no hay tiempos comparativos registrados. | Libro local de avance; no hay tiempos equivalentes registrados. | Medir carga y respuesta en el mismo equipo; no asumir un ganador. |
| Colaboración y versiones | Python y documentación revisables con Git. | `.twbx` versionado; su contenido empaquetado dificulta comparar cambios visuales en Git. | Guardar versiones y capturas además del binario. Trabajo individual. |
| Compartir y desplegar | Ejecución local y opción de despliegue web. | Entrega local empaquetada; publicación no realizada. | Costos y acceso dependen del despliegue y la edición, no solo de crear el tablero. |

**Para cerrar:** añadir referencias a capturas y registros de pruebas, reemplazar «pendiente» por evidencia observada y ajustar las valoraciones si los resultados difieren.

---

# 6. Costos, acceso y distribución

Consulta de documentación oficial: **8 de noviembre de 2026**. Alternativas investigadas; no se contrataron ni publicaron.

| Aspecto | Streamlit + Plotly | Tableau |
|---|---|---|
| Entorno local usado | Aplicación Python del Lab 10. Versiones instaladas pendientes de registrar. | MacBook Air M2, según el estudiante; `.twbx` indica macOS y Tableau 2026.3.0, build 20263.26.1022.1645. RAM y macOS pendientes. |
| Desarrollo local | Código del proyecto y dependencias sin licencia comercial adquirida. Requiere Python y mantenimiento del entorno. | Se utilizó una prueba de Desktop; no constituye una licencia permanente gratuita. |
| Alternativa gratuita web | Community Cloud ofrece alojamiento gratuito conectado a GitHub [S1]. | Public permite publicación abierta de visualizaciones; no es alojamiento privado [S2]. |
| Uso gratuito local | No implica que cualquier alojamiento y mantenimiento sean gratuitos. | Free Edition está orientada al uso local y no permite compartir libros empaquetados; no se debe confundir con la edición de prueba o con Public. Las capacidades de compartir cambian por edición [S3]. |
| Operación compartida | Community Cloud tiene restricciones y requisitos de permisos/dependencias; alojamiento propio añade infraestructura y operación [S4]. | Cloud/Server y los roles de creación y consumo requieren evaluar licencias; Server añade operación propia. Revisar cotización vigente según región y plan [S5]. |

La página oficial anuncia Tableau Standard desde USD 15 por usuario/mes, facturado anualmente, y exige al menos una licencia Creator por despliegue [S5]. Ese precio inicial no debe interpretarse como el costo de una licencia Creator ni como costo total del observatorio. No se obtuvo cotización de una combinación concreta de roles. La entrega local no acredita acceso indefinido bajo una prueba. Una contratación debe registrar plan, moneda, impuestos y usuarios.

## Recomendaciones provisionales por escenario

**Consulta periódica de directivos:** Tableau con acceso institucional y actualización organizada, si se dispone de licencias y se confirman navegación y rendimiento. Su adecuación visual debe contrastarse con las pruebas; sin ese acceso, Streamlit es una alternativa viable.

**Exploración con controles personalizados:** Streamlit, por el control de interfaz y lógica en Python ya presente en el Lab 10. La ventaja requiere capacidad de mantener código y dependencias.

**Usuarios externos desde navegador sin instalar:** Streamlit desplegado en un entorno adecuado al nivel de privacidad. Community Cloud puede servir al prototipo; se deben revisar sus límites. Tableau Public es alternativa para información autorizada como pública; el acceso privado exige evaluar Cloud/Server y licencias.

**Observatorio:** priorizar provisionalmente Streamlit para una consulta externa flexible con el código existente; reservar Tableau para análisis institucional con licencias. La decisión final debe incorporar las pruebas y la experiencia previa.

---

# 7. Pruebas y consistencia

Mismo equipo, datos y filtros cuando sea posible. Registrar sistema operativo, versiones, experiencia previa y diferencias de entorno. Medir la carga por separado; cronometrar cada tarea desde el primer control hasta leer el resultado. Contar clics y cambios de selección con el mismo criterio. No presentar valores calculados por script como resultados de una prueba de usuario.

| Prueba | Pregunta, pasos y resultado esperado |
|---|---|
| 1. Filtros | ¿Cuántos visitantes terrestres ingresaron en enero–junio de 2025? Restablecer, elegir esas fechas y todas las regiones, seleccionar Terrestre en las barras y leer total y seis meses. Esperado: 1,043,269.45 visitantes; limpiar debe recuperar las vías. |
| 2. Detalle y regreso | ¿Cómo se distribuye 2025 por trimestre y mes? Elegir todo 2025 y todas las regiones/vías; año → trimestres → meses → año. Esperado: cuatro trimestres, doce meses y total 3,352,288.66. |
| 3. Modelos | ¿Qué modelo de Total visitantes tiene menor MAE/RMSE en abril 2021–junio 2026? Elegir serie, tres modelos y toda la prueba; revisar curvas y alternar métrica. Esperado: 63 meses y suavizamiento con MAE 165,372.63 y RMSE 180,598.32. |

Los controles se calcularon con las fuentes disponibles. Los trimestres de 2025 son 822,510.735673; 802,459.713199; 795,238.734400 y 932,079.474236 visitantes. Al verificar consistencia se comparará la precisión sin redondear cuando sea posible y se explicará la diferencia de presentación.

**Resultados obtenidos: PENDIENTES.** Completar seis registros (tres tareas por dos herramientas) en REGISTRO_PRUEBAS.csv, con pasos reales, clics, segundos, resultado y dificultades. Incorporarlos aquí con referencias a capturas.

**Consistencia entre versiones: PENDIENTE.** Completar al menos el total filtrado de la prueba 1 y el MAE del modelo suavizamiento de la prueba 3 en CONSISTENCIA.csv. Registrar ambos valores, filtros, reglas de agregación y diferencia. Los controles de Python no sustituyen la lectura en ambas versiones. Documentar cualquier discrepancia y su causa; si requiere corregir datos, aplicar la corrección a ambas versiones.

El resultado del avance confirmó visualmente vías → evolución y la acción guardada en el libro. No sustituye estas tres pruebas finales ni demuestra el funcionamiento de las seis gráficas aún pendientes.

---

# 8. Planificación y reproducción

Responsable único: **Jorge Lopez, 221038**. El avance planificó completar visualizaciones el 6 de noviembre, modelos y pruebas el 7, y revisión y entrega el 8. Esas eran metas: no deben presentarse como fechas reales de terminación sin registro. Al 8 de noviembre la preparación de datos auxiliares y documentación está lista; implementación final y pruebas pendientes.

Completar REGISTRO_ENTORNO_Y_TIEMPOS.csv con fechas reales, tareas y tiempo efectivo por herramienta. Cuando no exista medición del Lab 10, registrar «No registrado» y reconocer la limitación. Git y las versiones documentan cambios, pero no prueban horas efectivas ni el aporte de personas distintas en un trabajo individual.

## Archivos e instrucciones

El avance permanece en entregables/. La preparación final está en entregables/final/. `preparar_final.py` transforma las predicciones existentes y genera Modelos_Tableau.xlsx y controles_final.json. `generar_documentos.py` genera este PDF desde Markdown sin modificar el avance ni el libro de Tableau. El submódulo Lab10-DataScience conserva el código y los datos originales.

El usuario debe guardar el libro terminado como `.twbx`, incluir los Excel utilizados y verificar que vuelva a abrir sin las rutas originales. Para actualizar fuentes: Data → fuente → Edit Connection, elegir el Excel correspondiente y actualizar; revisar claves, fechas y totales antes de volver a empaquetar. Seguir el README del Lab 10 para ejecutar Streamlit.

**Entrega final pendiente:** libro terminado, PDF con capturas y pruebas, README con versión y rutas definitivas, y repositorio con evidencias. Este borrador no reemplaza esos archivos.

## Fuentes oficiales consultadas

- **S1.** Streamlit Community Cloud: https://docs.streamlit.io/deploy/streamlit-community-cloud
- **S2.** Tableau Public FAQ: https://help.salesforce.com/s/articleView?id=001458242&language=en_US&type=1
- **S3.** Comparación de ediciones: https://help.tableau.com/current/pro/desktop/en-us/desktop_comparison.htm
- **S4.** Streamlit, estado y límites: https://docs.streamlit.io/deploy/streamlit-community-cloud/status
- **S5.** Tableau, precios y planes: https://www.tableau.com/pricing
- **S6.** Acciones de filtro: https://help.tableau.com/current/pro/desktop/en-us/actions_filter.htm
- **S7.** Porcentaje de total: https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations_definebasic_runningtotal.htm
- **S8.** Parámetros para medidas: https://help.tableau.com/current/pro/desktop/en-us/parameters_swap.htm

S6–S8 sustentan el método propuesto de interacción y cálculos; su existencia en el producto no prueba que ya se haya configurado en el libro final. La evidencia de implementación se añadirá tras revisarlo. Fuentes del proyecto: README, código, documento de diseño y CSV del Lab 10; enunciado del Lab 12; `.twbx` de avance. Consulta: 8 de noviembre de 2026.
