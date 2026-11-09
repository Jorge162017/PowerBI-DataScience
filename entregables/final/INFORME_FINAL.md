# Panorama de visitantes a Guatemala

**Laboratorio 12 · Documento de diseño y comparación de herramientas**  
Universidad del Valle de Guatemala · Facultad de Ingeniería · CC3066 Data Science  
Semestre II, 2026 · 8 de noviembre de 2026  
**Jorge Lopez · 221038**

**Documento de diseño y evaluación · 8 de noviembre de 2026.** La revisión combina inspección del libro guardado, resultados funcionales automatizados de Streamlit y estimaciones de uso de Tableau.

## 1. Propósito, público y alcance

Se traslada a Tableau el tablero del Laboratorio 10, desarrollado en Python, Streamlit y Plotly. El estudiante comunicó autorización del docente para sustituir Power BI; se mantienen el alcance y los requisitos de interacción. La comparación relevante será Tableau frente a Streamlit, no una implementación de Power BI que no se realizó.

El público son responsables de operación, promoción y planificación de empresas turísticas sin formación estadística especializada. El tablero apoya la planificación de personal, capacidad y campañas mediante el contexto nacional de visitantes; no estima ventas u ocupación de una empresa específica.

Las preguntas se conservan: ¿cómo evoluciona la afluencia?; ¿qué meses concentran visitas?; ¿qué vías predominan?; ¿qué mercados de origen aportan más y cómo evolucionan?; ¿cómo cambia la composición por vía entre regiones?; ¿qué modelos estuvieron más cerca de los observados?

La exploración abarca enero de 2009–junio de 2026, con visitantes = Turista + Excursionista. Las entradas no equivalen a personas únicas, gasto, ingresos, impacto ambiental ni demanda por destino. El observatorio recibe contexto turístico, sin afirmar que estas variables midan sostenibilidad. No se atribuyen causas a cambios observados.

La evaluación usa siete series: total, vías aérea, terrestre y marítima, y regiones América del Centro, América del Norte y Europa. Se reutilizan suavizamiento exponencial, Holt–Winters y ARIMA/SARIMA. No se entrenan nuevos modelos. LSTM del Lab 2 no se incorpora por tener otro protocolo de evaluación.

El libro final revisado contiene ocho hojas y tres dashboards: Panorama, Mercados y vias y Modelos y limites. Incluye las fuentes Excel y dos acciones de filtro. Las limitaciones de evaluación se indican en las secciones 5–8.

---

# 2. Diseño y navegación

## Paleta y legibilidad

La paleta del Lab 10 se conserva como referencia de diseño. El fondo #0B141B y los paneles #14251F agrupan información; #20735F distingue controles. Texto principal #E7F0EB y secundario #B6C7BE. Observado y terrestre usan turquesa #62D9C4; suavizamiento y marítima ámbar #F4B860; ARIMA/SARIMA y aérea lavanda #A9BCFF; Holt–Winters rosa #DCA7D8. Vías y modelos aparecen en contextos separados, con leyendas explícitas.

Las regiones conservarán colores entre ranking y evolución. Los colores naturales representan identidad, no una calificación de sostenibilidad. Se empleará tipografía sans serif, títulos descriptivos, ejes con unidades y detalles por cursor. Las leyendas y etiquetas permiten identificar series sin depender solo del color. La versión Tableau utiliza fondo blanco, azul para cantidades y colores categóricos predeterminados; la matriz usa una escala secuencial turquesa. Es una adaptación para legibilidad. No se aplicó completamente el tema oscuro previsto.

## Organización propuesta

| Vista | Contenido y controles |
|---|---|
| Panorama | Evolución temporal, volumen por vía y estacionalidad; período, región y vía. |
| Mercados y vías | Ranking, evolución regional y composición; filtros de exploración compartidos. |
| Modelos y límites | Observado/predicho y errores; serie, modelos, período de prueba y métrica. |

Las tres vistas se consultan mediante pestañas; no se incorporaron botones adicionales de navegación. Las barras de vía filtran la evolución y el ranking regional filtra evolución y composición; se comprobaron en capturas y acciones guardadas. Año–trimestre–mes permitirá variar el detalle y regresar. La selección se limpia volviendo a pulsar la marca. El retorno a la versión guardada se realiza con File → Revert; debe evitarse durante cambios de edición no guardados.

Se conservarán las preguntas, las secciones y la intención de las ocho gráficas. El cambio principal será pasar del estado de sesión y controles programados de Streamlit a hojas, dashboards y acciones de Tableau. No se contabilizan tarjetas, filtros o botones como gráficas.

Para interpretar las vistas se debe considerar que 2026 termina en junio, que períodos parciales requieren meses comparables y que una vista vacía puede deberse a filtros. La cobertura marítima, el cambio metodológico desde 2023 y la ruptura pandémica se conservarán como límites del Lab 10.

**Evidencia de implementación:** las capturas revisadas muestran los tres dashboards y el filtrado de una región. El paquete entregado conserva el libro y sus fuentes.

---

# 3. Ocho visualizaciones equivalentes

Las ocho hojas de la tabla se identificaron en el libro final guardado. La revisión estructural se complementó con capturas de construcción.

| Lab 10 → Tableau | Elección y finalidad |
|---|---|
| 1. Evolución → línea temporal | Mantiene continuidad y muestra cambios de afluencia. SUM de visitantes por fecha, con filtros y detalle temporal. Responde a selección de vía. |
| 2. Volumen por vía → barras horizontales | Compara magnitudes de las tres vías con base común. Una selección filtra la evolución; se comprobó en el avance. |
| 3. Estacionalidad → matriz año × mes | Intensidad de color para reconocer temporadas y rupturas. Se conservan meses sin cobertura como ausentes y los ceros registrados como cero. |
| 4. Mercados de origen → ranking horizontal | Facilita leer regiones y comparar cantidades. Se utiliza un ranking completo ordenado; sustituye el Top N ajustable del Lab 10 para evitar ocultar población en el prototipo. |
| 5. Evolución regional → líneas por región | Compara trayectorias en un mismo eje temporal. La selección del ranking y los filtros reducen series para mantener legibilidad. |
| 6. Región–vía → barras al 100% | Compara composición sin confundirla con volumen; las cantidades quedan en el detalle. La versión entregada conserva cantidades en los datos; no añade una vista auxiliar para alternar el modo como en el Lab 10. |
| 7. Observado/predicho → líneas | Una única serie de gestión, observado y tres modelos, en el mismo período de prueba. Colores y leyendas distinguen resultados reales y estimados. |
| 8. Error → barras de MAE/RMSE | Permite comparar los tres modelos dentro de la misma serie y conjunto evaluado. Se muestran MAE y RMSE en paneles contiguos de toda la prueba de 63 meses; no se recalculan con el filtro exploratorio. |

En la vista 6 se recalculan los porcentajes entre las vías seleccionadas por cada región. Una región con total cero no tiene composición porcentual interpretable.

En las vistas 7–8, las series de gestión son agregaciones distintas y algunas se superponen. Seleccionar una sola serie evita sumar total y subconjuntos. Las métricas en visitantes no se compararán como si midieran desempeño relativo entre series de escalas diferentes.

**Adaptaciones finales:** la evolución permite expandir la fecha de año a trimestre y mes y regresar. Los modelos se fijan en Total visitantes para ambas hojas; el conjunto completo de siete series permanece importado. Las barras muestran simultáneamente MAE y RMSE de la prueba completa. La aplicación de fechas se restringe a las seis vistas exploratorias y no altera las métricas. Estas diferencias respecto de Streamlit reducen controles y deben considerarse en la comparación.

---

# 4. Datos, cálculos y modelos

## Preparación reproducible

`preparar_datos.py` reutiliza `src/datos.py` del Lab 10: lee la hoja Datos del Excel original, normaliza textos, convierte año/mes/cantidad, elimina filas duplicadas, crea la fecha mensual y filtra fechas válidas, valores no negativos y tipos Turista/Excursionista. Agrupa por Fecha–Region–Via y suma visitantes; conserva decimales y ceros válidos. No se modifica la base original.

El Excel del avance contiene 3,946 registros exploratorios, 1,470 observados, 1,323 predicciones y 21 combinaciones serie–modelo con métricas. Se importaron como fuentes separadas; no se hicieron joins de hechos ni relaciones muchos a muchos. Esto evita multiplicar visitantes o el observado repetido por modelo.

`preparar_final.py` añade `Modelos_Tableau.xlsx`: Curvas tiene 1,764 filas, con Observado una vez por Serie–Fecha y tres predicciones por mes; Evaluacion tiene 1,323 filas con error absoluto y cuadrado. Son transformaciones de los CSV existentes, sin entrenamiento. Se comprobaron claves únicas, coincidencia del observado y concordancia de las 21 métricas con los originales, con diferencias inferiores a 0.000000001 por precisión numérica.

## Cálculos con finalidad analítica

Visitantes: SUM del campo de cantidad; fecha de vista: DATETRUNC según año, trimestre o mes. Composición: porcentaje de total calculado sobre Via, particionado por Region y después de filtros. MAE: AVG(ErrorAbsoluto). RMSE: SQRT(AVG(ErrorCuadrado)). En el libro entregado se muestran las métricas precalculadas en dos paneles separados; las fórmulas anteriores documentan su definición y verificación en Python. No se utilizó un parámetro de métrica.

No se suman observados de la tabla de predicciones para construir la curva real. No se promedian RMSE preagregados. El archivo de métricas originales es referencia de toda la prueba, no una medida del subintervalo filtrado. El redondeo se limita a presentación.

## Evaluación y límites

Entrenamiento: enero de 2009–marzo de 2021, 147 meses. Prueba: abril de 2021–junio de 2026, 63 meses. Se evalúa un horizonte fijo sin actualizar con observaciones de prueba. Las curvas fueron exportadas en el Lab 10 reproduciendo configuraciones del Lab 1, porque el notebook conservaba métricas e imágenes, no valores numéricos originales; concordar con métricas redondeadas no demuestra identidad exacta de curvas.

MAE y RMSE están en visitantes. Menor error histórico no garantiza mejor desempeño futuro. Los ceros marítimos de la prueba reflejan la cobertura disponible y no demuestran ausencia real de actividad.

---

# 5. Comparación de implementaciones

Evidencia disponible: código, README y PDF del Lab 10; estructura del `.twbx` de avance y capturas revisadas. La sección 7 registra el método y alcance de los resultados.

| Criterio | Evidencia en Streamlit | Evidencia en Tableau | Implicación para la tarea |
|---|---|---|---|
| Aprendizaje | Controles y estado escritos en Python. | Arrastrar campos, elegir SUM y mes continuo exigió ajustes durante el avance. | Tableau requiere entender agregación; medir facilidad con tareas equivalentes. |
| Tiempo de desarrollo | Ocho gráficas en el código del Lab 10; horas no registradas aquí. | Ocho hojas y tres dashboards; tres tareas estimadas en 60 s cada una. No se registraron horas de construcción. | No concluir cuál es más rápido a partir del orden de implementación. |
| Preparación y actualización | Limpieza centralizada en datos.py y caché. | Excel preparado, cinco fuentes independientes y dos Excel empaquetados. | Python explicita transformación; Tableau requiere actualizar y comprobar conexiones. |
| Modelos | Lee CSV y recalcula errores con el intervalo seleccionado. | Curvas conectada para líneas; Metricas conectada para MAE/RMSE completos. Evaluacion preparada, no utilizada en el libro. | Reutilización equivalente sin entrenar; comprobar filtrado final. |
| Interacción y navegación | Tres secciones y selecciones enlazadas documentadas. | Dos acciones: vías → evolución y ranking → vistas regionales; fechas en seis hojas y jerarquía temporal. | Comparar pasos reales de navegación y limpieza. |
| Personalización | Plotly y estado de sesión permiten controles propios. | Hojas y acciones nativas; fondo claro y colores predeterminados en la versión final. | Streamlit ofrece control por código; Tableau reduce programación de vistas convencionales. |
| Rendimiento | Lectura con caché; no hay tiempos comparativos registrados. | Libro local final; tiempos humanos aproximados, sin medición equivalente de carga. | Medir carga y respuesta en el mismo equipo; no asumir un ganador. |
| Colaboración y versiones | Python y documentación revisables con Git. | `.twbx` versionado; su contenido empaquetado dificulta comparar cambios visuales en Git. | Guardar versiones y capturas además del binario. Trabajo individual. |
| Compartir y desplegar | Ejecución local y opción de despliegue web. | Entrega local empaquetada; publicación no realizada. | Costos y acceso dependen del despliegue y la edición, no solo de crear el tablero. |

La implementación final de Tableau simplifica el control de modelos y su período; Streamlit conserva mayor flexibilidad en esa sección.

---

# 6. Costos, acceso y distribución

Consulta de documentación oficial: **8 de noviembre de 2026**. Alternativas investigadas; no se contrataron ni publicaron.

| Aspecto | Streamlit + Plotly | Tableau |
|---|---|---|
| Entorno local usado | Aplicación Python del Lab 10. Verificación: Streamlit 1.67.0, Plotly 6.9.0, Python 3.13.12. | MacBook Air M2, según el estudiante; `.twbx` indica macOS y Tableau 2026.3.0, build 20263.26.1022.1645. macOS 26.2, arm64; RAM no registrada. |
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

Método: verificación funcional de Streamlit con AppTest y datos reales; Tableau mediante las ejecuciones reportadas y la revisión del libro empaquetado. Los tiempos de Tableau son aproximados; los de Streamlit corresponden al procesamiento de las pruebas.

| Tarea | Tableau: ejecución reportada | Streamlit: ejecución automatizada |
|---|---|---|
| 1. Filtrar enero–junio de 2025, todas las regiones y vía terrestre | Aproximadamente 60 s y 8 clics. Se confirmó un total aproximado de 1,043,269.45 visitantes. | 0.143 s de procesamiento; filtro de vía por control, no clic en barra. Seis meses y total 1,043,269.4488721137. |
| 2. Año 2025 → trimestres → meses → año | Aproximadamente 60 s y 12 clics. Cambio de nivel y retorno reportados; jerarquía comprobada en capturas. | 0.450 s; 1, 4, 12 y 1 marcas. En los cuatro niveles, total 3,352,288.657508455. |
| 3. Consultar curvas y errores de Total visitantes, abril 2021–junio 2026 | Aproximadamente 60 s y 1 clic para cambiar de vista.  | 0.203 s; consulta de curvas y alternancia MAE/RMSE. Suavizamiento exponencial obtuvo el menor error en ambas métricas. |

No se registraron dificultades específicas en las tres estimaciones finales. Durante construcción se requirieron ajustes de SUM frente a Count, fechas continuas/discretas y distribución de hojas. No se asignan esas dificultades automáticamente a limitaciones del producto.

## Consistencia de dos indicadores

| Indicador y filtros | Streamlit, salida de AppTest | Fuente empaquetada en Tableau | Diferencia |
|---|---|---|---|
| Visitantes terrestres, enero–junio de 2025, todas las regiones; SUM | 1,043,269.4488721137 | 1,043,269.4488721137 | 0 |
| MAE de suavizamiento, Total visitantes, prueba completa de 63 meses | 165,372.6258489368 | 165,372.6258489368 | 0 |

El total filtrado se confirmó aproximadamente en Tableau; el MAE se contrastó con la fuente incluida en el .twbx. Ambos indicadores coinciden con las salidas de Streamlit. RMSE de suavizamiento: 180,598.32147900484. Los tres modelos se comparan dentro de la misma tarea y escala.

Evidencias reproducibles: resultados_streamlit.json, auditoria_tableau.json, REGISTRO_PRUEBAS.csv y CONSISTENCIA.csv.

---

# 8. Planificación y reproducción

Responsable único: **Jorge Lopez, 221038**. El avance planificó completar visualizaciones el 6 de noviembre, modelos y pruebas el 7, y revisión y entrega el 8. Esas eran metas: no deben presentarse como fechas reales de terminación sin registro. Al 8 de noviembre el archivo final contiene ocho hojas y tres dashboards; las verificaciones funcionales y numéricas se describen en la sección 7. No se midieron horas efectivas de desarrollo.

No se registró tiempo efectivo total de construcción en ninguna herramienta. El entorno utilizado se registra en entorno_verificacion.txt. Los tiempos de tres tareas no representan horas de desarrollo. Git y las versiones documentan cambios, pero no prueban horas efectivas ni el aporte de personas distintas en un trabajo individual.

## Archivos e instrucciones

El avance permanece en entregables/. La preparación final está en entregables/final/. `preparar_final.py` transforma las predicciones existentes y genera Modelos_Tableau.xlsx y controles_final.json. `generar_documentos.py` genera este PDF desde Markdown sin modificar el avance ni el libro de Tableau. El submódulo Lab10-DataScience conserva el código y los datos originales.

El usuario debe guardar el libro terminado como `.twbx`, incluir los Excel utilizados y verificar que vuelva a abrir sin las rutas originales. Para actualizar fuentes: Data → fuente → Edit Connection, elegir el Excel correspondiente y actualizar; revisar claves, fechas y totales antes de volver a empaquetar. Seguir el README del Lab 10 para ejecutar Streamlit.

**Archivos de entrega:** Lab12_Final_Jorge_Lopez_221038.twbx y este documento, junto al README y evidencias. El archivo guardado contiene fuentes empaquetadas, ocho hojas, tres dashboards y dos acciones. En la versión revisada no se identificó una tarjeta de fechas visible en el dashboard, aunque el filtro sí existe en las seis hojas; ese control debe conservarse visible al guardar desde Tableau. No se afirma revisión exhaustiva de todos los estados sin datos o de accesibilidad.

## Fuentes oficiales consultadas

- **S1.** Streamlit Community Cloud: https://docs.streamlit.io/deploy/streamlit-community-cloud
- **S2.** Tableau Public FAQ: https://help.salesforce.com/s/articleView?id=001458242&language=en_US&type=1
- **S3.** Comparación de ediciones: https://help.tableau.com/current/pro/desktop/en-us/desktop_comparison.htm
- **S4.** Streamlit, estado y límites: https://docs.streamlit.io/deploy/streamlit-community-cloud/status
- **S5.** Tableau, precios y planes: https://www.tableau.com/pricing
- **S6.** Acciones de filtro: https://help.tableau.com/current/pro/desktop/en-us/actions_filter.htm
- **S7.** Porcentaje de total: https://help.tableau.com/current/pro/desktop/en-us/calculations_tablecalculations_definebasic_runningtotal.htm

Fuentes del proyecto: código, documento de diseño y CSV del Laboratorio 10; enunciado del Laboratorio 12 y libro final de Tableau. Fecha de consulta: 8 de noviembre de 2026.
