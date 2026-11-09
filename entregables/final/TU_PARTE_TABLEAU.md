# Tu parte en Tableau · orden de trabajo

Jorge Lopez · 221038 · Entrega final: 8 de noviembre de 2026, 23:59.

El avance se conserva intacto. Esta guía explica la construcción pendiente; no afirma que ya esté implementada. Guarda una copia como `Lab12_Final_Jorge_Lopez_221038.twbx` dentro de `entregables/final/`. Si Tableau pide una ruta que ya no existe, usa `entregables/datos/Datos_Lab12.xlsx`. El Excel anterior sigue incluido dentro del avance empaquetado.

## 1. Reusar las dos hojas y preparar controles

Abre el avance. Conserva la línea mensual y las barras por vía. Cambia `Dashboard 1` a **Panorama**. Las hojas vacías de importación pueden reutilizarse para las nuevas gráficas.

En la fuente Visitantes, identifica el campo numérico `Visitantes (Visitantes)`, que se debe **sumar**, y no `Visitantes (Count)`, que cuenta filas. En las fórmulas siguientes `[Visitantes]` representa el campo de cantidad: si Tableau lo llama distinto, insértalo con doble clic desde el listado de campos del editor.

En cada una de las seis hojas exploratorias, usa la misma fuente Visitantes. En una de ellas:

1. Arrastra Fecha a Filters, elige **Range of dates**, conserva todo el intervalo y muestra el filtro.
2. Arrastra Region y Via a Filters, conserva todos y muestra los filtros.
3. En el menú de cada filtro: **Apply to Worksheets → Selected Worksheets**, elige únicamente las seis hojas de exploración. No apliques estos filtros a modelos.
4. Muestra los filtros en Panorama y Mercados y vías. Ajusta los títulos a «Período», «Región de procedencia» y «Vía de ingreso».

## 2. Permitir año, trimestre y mes

En la fuente Visitantes crea un parámetro de texto `Nivel temporal`, con lista Año, Trimestre, Mes y valor inicial Mes. Crea el campo `Fecha de vista` con esta fórmula:

```text
CASE [Nivel temporal]
WHEN "Año" THEN DATETRUNC('year', [Fecha])
WHEN "Trimestre" THEN DATETRUNC('quarter', [Fecha])
ELSE DATETRUNC('month', [Fecha])
END
```

En las hojas de líneas, reemplaza Fecha de Columns por Fecha de vista; en su menú elige **Exact Date → Continuous**, y conserva SUM de visitantes en Rows. Muestra el parámetro para variar la agregación.

Para cumplir además el requisito explícito de jerarquía, crea `Año`, `Trimestre` y `Mes` como campos de fecha con DATETRUNC('year', [Fecha]), DATETRUNC('quarter', [Fecha]) y DATETRUNC('month', [Fecha]). Desde el panel de datos crea una jerarquía llamada **Detalle temporal** con ese orden. Arrastra Año de esta jerarquía a Columns en la hoja de evolución y usa los signos + y − para bajar/subir. Pruébala con 2025: 1 año → 4 trimestres → 12 meses → regreso. Puedes dejar esta jerarquía como mecanismo final de detalle y retirar el parámetro si prefieres un solo control; no es necesario mantener los dos. Si dejas campos de distintos niveles simultáneos en Columns, confirma que agrupan cada mes una sola vez.

## 3. Gráfica 3 · Estacionalidad

Nueva hoja **Estacionalidad**; fuente Visitantes. Fecha a Columns → MONTH **discreto** (azul, nombre de mes). Fecha a Rows → YEAR discreto. Marks → Square; SUM de visitantes a Color y Tooltip. Ajusta Size para que las celdas llenen la matriz. Ordena meses de enero a diciembre. Incluye cantidad y mes/año en Tooltip. Usa una escala secuencial, sin rojo/verde de «bueno o malo».

No reemplaces meses ausentes por cero. Julio–diciembre de 2026 deben estar vacíos. Evita añadir una selección de mes que filtre accidentalmente todas las vistas: el filtrado mínimo obligatorio ya funciona de vías a evolución. Añade esta hoja debajo de las dos existentes en Panorama.

## 4. Gráfica 4 · Mercados de origen

Nueva hoja **Mercados de origen**; fuente Visitantes. Region a Rows; SUM de visitantes a Columns; Marks → Bar. Ordena de mayor a menor por SUM de visitantes. Conserva todas las regiones: el ranking completo evita introducir un Top N que cambie la población sin explicación. Region a Color permite mantener los mismos colores que en la evolución regional; asígnalos manualmente en ambas hojas. Las etiquetas deben permitir leer nombres completos.

## 5. Gráfica 5 · Evolución por región

Nueva hoja **Evolución por región**; fuente Visitantes. MONTH(Fecha) continuo a Columns, SUM de visitantes a Rows, Region a Color, Marks → Line. Si adoptaste el parámetro de nivel temporal usa Fecha de vista. Si elegiste jerarquía, úsala también aquí. Los filtros comunes deben permitir seleccionar pocas regiones para mantener legibilidad.

## 6. Gráfica 6 · Composición región–vía

Nueva hoja **Composición región–vía**. Region a Rows, SUM de visitantes a Columns, Via a Color y Marks → Bar. Analysis → Stack Marks → On.

En el menú de SUM de visitantes: **Quick Table Calculation → Percent of Total**. Luego **Edit Table Calculation → Specific Dimensions**: marca únicamente **Via** como dirección del cálculo y deja Region sin marcar como partición. Cada región con volumen positivo debe sumar 100%, no todas las regiones juntas. Formatea el eje como porcentaje.

Añade otra copia de SUM de visitantes al Tooltip **sin cálculo porcentual**, para conservar cantidades absolutas. Comprueba un filtro de dos vías: el porcentaje debe recalcularse entre esas vías. Con total cero, no debe aparecer un porcentaje inventado. Para conservar también el modo de cantidades del Lab 10 puedes duplicar la hoja como apoyo «Composición en cantidades», quitar el cálculo y permitir alternar entre ambas; la duplicación no sustituye ninguna de las ocho gráficas principales.

Crea el dashboard **Mercados y vías** y coloca las hojas 4, 5 y 6. Selecciona el ranking → Use as Filter: elegir una región debe actualizar evolución y composición; limpiar la selección debe recuperar todas. Conserva los filtros comunes.

## 7. Conectar los modelos preparados

Data → New Data Source → Microsoft Excel → `entregables/final/datos/Modelos_Tableau.xlsx`. Arrastra únicamente **Curvas** al lienzo. Crea otra fuente del mismo Excel con únicamente **Evaluacion**. No hagas joins entre ellas ni con Visitantes.

Curvas contiene 1,764 filas únicas por Serie–Curva–Fecha, con Observado una sola vez por serie y mes. Evaluacion contiene 1,323 filas únicas por Serie–Modelo–Fecha. Las métricas dinámicas se calculan a partir de esta segunda fuente. Las fuentes del avance pueden conservarse como referencia.

## 8. Gráfica 7 · Observado y predicho

Nueva hoja **Observado y predicho**, fuente Curvas. MONTH(Fecha) continuo a Columns; SUM(Valor) a Rows; Curva a Color; Marks → Line. **Primero filtra Serie a una sola opción**, inicialmente Total visitantes, y muestra el filtro como Single Value Dropdown. Sin este filtro se mezclarían series que se superponen.

Muestra un filtro de Curva con Observado y los tres modelos seleccionados. Añade Fecha como rango, inicialmente abril de 2021–junio de 2026. Asigna Observado turquesa #62D9C4, suavizamiento ámbar #F4B860, ARIMA/SARIMA lavanda #A9BCFF y Holt–Winters rosa #DCA7D8. Conserva leyenda con nombres y Tooltip con Serie, Curva, Fecha, Valor y la etiqueta «Evaluación histórica». No se presenta como pronóstico posterior a junio de 2026.

## 9. Gráfica 8 · Error de modelos

Nueva hoja **Error de modelos**, fuente Evaluacion. Crea estos campos calculados:

```text
// MAE dinámico
AVG([ErrorAbsoluto])
```

```text
// RMSE dinámico
SQRT(AVG([ErrorCuadrado]))
```

Crea un parámetro de texto `Métrica`, lista MAE, RMSE, inicial MAE. Crea `Error seleccionado`:

```text
IF [Métrica] = "MAE" THEN [MAE dinámico]
ELSE [RMSE dinámico]
END
```

Modelo a Rows; Error seleccionado a Columns (se verá AGG), Modelo a Color; Marks → Bar. Orden ascendente de error. Muestra Métrica. Crea filtros Serie (una sola opción) y Fecha (rango). Inicialmente Total visitantes y toda la prueba. No promedies los RMSE guardados: la raíz se aplica después del promedio de errores cuadrados.

Si las medidas aparecen como strings, cambia ErrorAbsoluto y ErrorCuadrado a Number (decimal). Añade COUNTD(Fecha) a Tooltip como «Meses evaluados»; deben ser 63 en la prueba completa.

## 10. Dashboard de modelos y filtros coherentes

Crea **Modelos y límites**, con las hojas 7 y 8. Las dos fuentes comparten los nombres Serie y Fecha, pero Tableau no necesariamente sincroniza filtros entre fuentes independientes. Prueba **Apply to Worksheets → All Using Related Data Sources**, definiendo en Data → Edit Blend Relationships las correspondencias Serie ↔ Serie y Fecha ↔ Fecha si hace falta. Comprueba que cambiar la serie y el período modifica ambas hojas.

Si Tableau no permite sincronizarlos con claridad, muestra dos controles separados con títulos explícitos «Serie de curvas / Serie de errores» y «Período de curvas / Período de errores»; conserva la misma selección en ambos para comparar y explica esa limitación en el PDF. No afirmes que una selección modifica las dos si no lo has probado.

Añade texto: «Prueba histórica abril 2021–junio 2026. Entrenamiento hasta marzo de 2021. MAE: error absoluto promedio. RMSE: penaliza más los errores grandes. Ambas métricas están en visitantes. Menor error histórico no garantiza mejor desempeño futuro. La vía marítima registra ceros en esta prueba y no demuestra ausencia real de actividad».

## 11. Navegación, restablecimiento y diseño

En los tres dashboards añade objetos **Navigation** a Panorama, Mercados y vías y Modelos y límites, con nombres visibles. Conserva también las pestañas. Agrega un texto breve: «Selecciona una barra para filtrar; vuelve a pulsarla o haz clic en un espacio vacío para limpiar».

Deja los valores iniciales claros (exploración completa, ninguna barra seleccionada; modelos: Total visitantes, tres modelos, 63 meses). Guarda así. Muestra el texto «Restablecer vista: usa File → Revert para volver a la versión guardada» y verifica esa función después de guardar una copia: puede descartar cambios de edición no guardados. Para filtros individuales, conserva la opción All. La instrucción debe ser visible al usuario y debes comprobar que la acción de filtro se limpia.

Aplica la paleta del avance: fondo #0B141B, paneles #14251F, texto #E7F0EB, controles #20735F; usa texto secundario #B6C7BE y colores de datos indicados. Si algún control no admite ese formato, prioriza su legibilidad. Via: aérea lavanda, terrestre turquesa, marítima ámbar. Las regiones deben mantener el mismo color entre ranking y líneas.

Evita un dashboard lleno de gráficas pequeñas: tres dashboards permiten títulos legibles y espacio para filtros. Incluye «2026: enero–junio», «Visitantes = Turista + Excursionista» y aclaración de períodos parciales. Si una selección no tiene datos, muestra al menos una instrucción permanente junto a la vista: «Sin marcas: revisa el período, la región y la vía; restablece los filtros»; comprueba que no se interprete como cero.

## 12. Evidencias y pruebas que me debes pasar

- Guarda el `.twbx` final. Vuelve a abrirlo y comprueba las tres páginas.
- Capturas de los tres dashboards completos y de una selección enlazada, sin ventanas ni tooltips que oculten información.
- Capturas de las tres secciones de Streamlit con datos y selecciones comparables.
- Ejecuta las tres pruebas descritas en REGISTRO_PRUEBAS.csv en ambas herramientas. Mide tiempo desde el primer paso hasta leer el resultado; cuenta clics y cambios de selector. Usa el mismo equipo cuando sea posible. No cuentes capturas ni el arranque en frío dentro de ese tiempo; registra la carga por separado.
- Completa REGISTRO_ENTORNO_Y_TIEMPOS.csv y CONSISTENCIA.csv. Si no mediste tiempo del Lab 10, escribe «No registrado», sin inventarlo.
- Devuélveme el archivo guardado y los registros. Con eso puedo revisar, incorporar las capturas y cerrar el PDF final.

No subas el PDF de preparación como documento final sin completar resultados, capturas y recomendaciones basadas en las pruebas.
