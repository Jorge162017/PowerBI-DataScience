from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
doc = fitz.open()
INK = '#243238'
GREEN = '#20735F'
GRAY = '#58656B'
css = '''body { font-family: Arial; font-size: 10pt; color: #243238; line-height: 1.42; }
h1 {font-size:23pt; color:#20735F; margin:0 0 12pt;} h2 {font-size:13pt; color:#20735F; margin:15pt 0 6pt;}
p {margin:0 0 8pt;} li {margin-bottom:5pt;} ul,ol {padding-left:18pt;}
table {border-collapse:collapse; width:100%; margin:8pt 0;} td,th {border-bottom:1px solid #DDE3E4; padding:7pt 6pt; text-align:left; vertical-align:top; font-size:9pt;}
th {background:#EFF4F2; color:#20735F;} .small {font-size:9pt;color:#58656B;} .note {background:#F1F5F4;padding:10pt;} b {font-weight:bold;}
'''

def page(title, html):
    p = doc.new_page(width=595.28, height=841.89)
    p.insert_font(fontname='arial', fontfile='/System/Library/Fonts/Supplemental/Arial.ttf')
    p.insert_text((45, 35), 'UNIVERSIDAD DEL VALLE DE GUATEMALA  |  CC3066 · DATA SCIENCE', fontname='arial', fontsize=8, color=(.34,.40,.42))
    p.draw_line((45,46),(550,46),color=(.80,.85,.83),width=.6)
    spare, scale = p.insert_htmlbox(fitz.Rect(45,65,550,778), '<h1>'+title+'</h1>'+html, css=css, scale_low=1)
    if spare < 0:
        raise RuntimeError('Contenido excede página: '+title)
    p.draw_line((45,797),(550,797),color=(.80,.85,.83),width=.6)
    p.insert_text((45,814),'LABORATORIO 12 · AVANCE · JORGE LOPEZ · 221038',fontname='arial',fontsize=8,color=(.34,.40,.42))
    p.insert_text((525,814),str(len(doc)),fontname='arial',fontsize=8,color=(.34,.40,.42))

page('Panorama de visitantes<br>a Guatemala', '''
<p><b>Laboratorio 12 · Visualización interactiva con Tableau</b><br>Informe de avance · 5 de noviembre de 2026<br>Semestre II · Facultad de Ingeniería</p>
<p><b>Integrante:</b> Jorge Lopez · 221038</p>
<p class="small"><b>Adaptación autorizada:</b> se utiliza Tableau en sustitución de Power BI, con permiso del docente comunicado por el estudiante. Se conservan los requisitos funcionales del avance.</p><h2>1. Preguntas de gestión y alcance</h2>
<p>El informe trasladará a Tableau el tablero del Laboratorio 10, desarrollado con Python, Streamlit y Plotly. Mantendrá las mismas preguntas, datos y resultados predictivos para permitir una comparación equivalente.</p>
<ol>
<li>¿Cómo evoluciona el volumen mensual de visitantes y qué períodos presentan aumentos o disminuciones?</li>
<li>¿En qué meses se concentra la afluencia y cómo puede orientar la preparación de servicios?</li>
<li>¿Qué vías de ingreso concentran visitantes y cómo cambia su participación?</li>
<li>¿Qué regiones de procedencia aportan más visitantes y cómo evoluciona cada mercado?</li>
<li>¿Cómo difiere la composición por vía entre regiones de procedencia?</li>
<li>¿Qué tan cerca estuvieron las predicciones de los datos observados y qué modelos registraron menor error?</li>
</ol>
<p><b>Público:</b> responsables de operación, comercialización y planificación de empresas turísticas, sin formación estadística especializada. La información apoyará la preparación de capacidad, personal y campañas por temporada y mercado.</p>
<p><b>Alcance:</b> entradas mensuales a Guatemala de enero de 2009 a junio de 2026; visitantes = Turista + Excursionista. Se conservarán regiones, vías y siete series de evaluación del Lab 10.</p>
<p><b>Límites:</b> las entradas no representan personas únicas, ventas, ocupación hotelera ni impacto ambiental. No permiten atribuir causas ni medir por sí solas sostenibilidad. El año 2026 solo incluye enero–junio; las comparaciones deben usar meses equivalentes.</p>
''')

page('2. Paleta e interfaz', '''
<p>La paleta propuesta conserva la identidad del Lab 10: fondo oscuro, colores naturales y significado estable por serie. El prototipo funcional de hoy utiliza fondo blanco y el azul predeterminado de Tableau; la aplicación de esta paleta se planifica para la versión final. El documento usa fondo blanco para facilitar su lectura e impresión.</p>
<table><tr><th>Color</th><th>Uso y justificación en el informe de Tableau</th></tr>
<tr><td bgcolor="#0B141B"><span style="color:#FFFFFF">#0B141B</span></td><td>Fondo principal sobrio, sin competir con las gráficas.</td></tr>
<tr><td bgcolor="#14251F"><span style="color:#FFFFFF">#14251F</span></td><td>Paneles que agrupan filtros y visualizaciones.</td></tr>
<tr><td bgcolor="#20735F"><span style="color:#FFFFFF">#20735F</span></td><td>Controles y selección activa.</td></tr>
<tr><td>#E7F0EB / #B6C7BE</td><td>Texto principal y secundario sobre fondos oscuros.</td></tr>
<tr><td bgcolor="#62D9C4">#62D9C4</td><td>Datos observados y serie principal; vía terrestre.</td></tr>
<tr><td bgcolor="#F4B860">#F4B860</td><td>Suavizamiento exponencial; vía marítima.</td></tr>
<tr><td bgcolor="#A9BCFF">#A9BCFF</td><td>ARIMA/SARIMA; vía aérea.</td></tr>
<tr><td bgcolor="#DCA7D8">#DCA7D8</td><td>Holt–Winters.</td></tr></table>
<p class="small">Los colores de vías y modelos se usan en vistas separadas con leyendas explícitas. Las predicciones se distinguirán también por trazo discontinuo. El color natural expresa identidad, no un nivel de sostenibilidad.</p>
<h2>Bosquejo de interfaz y navegación</h2>
<table><tr><th colspan="2">Panorama de visitantes a Guatemala</th></tr>
<tr><td colspan="2">Panorama | Mercados y vías | Modelos y límites</td></tr>
<tr><td colspan="2">Período · Región · Vía · Restablecer vista</td></tr>
<tr><td>Evolución temporal<br>Año → Trimestre → Mes</td><td>Volumen por vía<br>Seleccionar vía → filtrar evolución</td></tr>
<tr><td colspan="2">Estacionalidad: mapa de calor por año y mes</td></tr></table>
<p><b>Mercados y vías:</b> ranking regional, evolución por región y composición región–vía. <b>Modelos y límites:</b> observado frente a predicho y barras de MAE/RMSE, con controles propios de serie y período de prueba.</p>
<p>Se conservarán las tres secciones y ocho gráficas del Lab 10. La navegación se adaptará a páginas y botones de Tableau; el detalle temporal usará una jerarquía Año–Trimestre–Mes. Se mostrarán selección activa, unidades, limitaciones y mensajes sin datos.</p>
''')

page('3. Datos y avance funcional', '''
<h2>Archivos disponibles del Laboratorio 10</h2>
<table><tr><th>Fuente</th><th>Contenido verificado</th></tr>
<tr><td>Base_Migracion_2009-2026jun.xlsx<br><span class="small">referencias/lab1/ · hoja Datos</span></td><td>Base original utilizada por el tablero. El nombre completo se conserva en el repositorio del Lab 10.</td></tr>
<tr><td>observados_lab1.csv</td><td>1,470 filas: siete series mensuales, con identificación de entrenamiento y prueba.</td></tr>
<tr><td>predicciones_lab1.csv</td><td>1,323 filas: siete series × tres modelos × 63 meses; campos Serie, Modelo, Fecha, Observado y Predicho.</td></tr>
<tr><td>metricas_lab1.csv</td><td>21 combinaciones serie–modelo, MAE, RMSE y cantidad de meses.</td></tr></table>
<p>Los CSV se encuentran en <b>data/modelos/</b> del Lab 10. Se reutilizarán suavizamiento exponencial, Holt–Winters y ARIMA/SARIMA sin volver a entrenar modelos. La prueba abarca abril de 2021–junio de 2026; el entrenamiento termina en marzo de 2021.</p>
<h2>Preparación e importación realizadas</h2>
<p>Se reutilizará la limpieza de <b>src/datos.py</b>: normalizar textos, convertir año, mes y cantidad a valores numéricos, eliminar filas duplicadas, crear la fecha mensual y conservar fechas válidas, cantidades no negativas y tipos Turista y Excursionista. Se agrupará por fecha, región y vía sumando Viajero.</p>
<p>Se importaron Visitantes, Predicciones, Metricas y Observados como cuatro fuentes independientes desde el Excel incluido en el .twbx. No se hicieron uniones entre ellas, para evitar multiplicar cantidades. Las claves verificadas son Fecha–Region–Via, Serie–Modelo–Fecha, Serie–Modelo y Serie–Fecha, respectivamente. Las dimensiones auxiliares del Excel quedan disponibles para la versión final; no se han conectado. No se debe sumar el observado repetido por modelo.</p>
<h2>Dos visualizaciones enlazadas implementadas</h2>
<p><b>1. Evolución temporal:</b> línea de visitantes por mes.<br><b>2. Volumen por vía:</b> barras de visitantes por vía de ingreso.</p>
<p>El dashboard «Dashboard 1» contiene «Evolucion Mensual» y «Visitantes por vía». Se verificó una acción de filtro al seleccionar una barra: la captura con Terrestre seleccionado muestra el cambio de la curva y su escala. La acción está configurada sobre selección y con limpieza automática. La línea usa MONTH(Fecha) continuo y SUM de visitantes. Los filtros adicionales de período y región se incorporarán en la versión final.</p>
<p class="note"><b>Estado del avance:</b> el archivo Lab12_Avance_Jorge_Lopez_221038.twbx incluye el Excel, las cuatro fuentes y las dos visualizaciones con acción de filtro. Se revisó la estructura del paquete y las capturas de funcionamiento. Se utiliza Tableau Desktop con una licencia de prueba que indica 14 días restantes; no se requiere publicar en línea para este avance.</p>
''')

page('4. Plan y comparación', '''
<h2>Planificación de tareas</h2>
<p>Responsable de todas las tareas: <b>Jorge Lopez · 221038</b>. Las fechas siguientes son metas de terminación, no un registro de ejecución.</p>
<table><tr><th>Tarea</th><th>Terminación prevista</th></tr>
<tr><td>Definir preguntas, alcance, paleta, bosquejo y protocolo.</td><td>5 nov., antes de 17:20</td></tr>
<tr><td>Importar datos y resultados de tres modelos; crear y verificar dos gráficas enlazadas; entregar avance.</td><td>5 nov., antes de 17:20</td></tr>
<tr><td>Completar ocho visualizaciones, filtros, navegación, restablecimiento y jerarquía temporal.</td><td>6 nov.</td></tr>
<tr><td>Completar vistas de modelos; ejecutar pruebas comparables y verificar dos indicadores.</td><td>7 nov.</td></tr>
<tr><td>Finalizar comparación, revisar .twbx y preparar PDF, datos, README y repositorio.</td><td>8 nov., antes de 23:59</td></tr></table>
<h2>Criterios de comparación</h2>
<p>Se comparará <b>Streamlit + Plotly</b> con <b>Tableau Desktop</b>. La matriz final tendrá las columnas: criterio, evidencia en la herramienta del Lab 10, evidencia en Tableau e implicación para la tarea.</p>
<table><tr><th>Criterio</th><th>Evidencia que se recopilará en ambas versiones</th></tr>
<tr><td>Facilidad de aprendizaje</td><td>Pasos y dificultades para construir y utilizar las vistas.</td></tr>
<tr><td>Tiempo de desarrollo</td><td>Tiempo efectivo de implementación y correcciones.</td></tr>
<tr><td>Preparación y actualización de datos</td><td>Limpieza, cambios de ruta y actualización reproducible.</td></tr>
<tr><td>Integración de modelos</td><td>Carga de CSV, relaciones y consistencia de métricas.</td></tr>
<tr><td>Interacción y navegación</td><td>Filtros, selecciones enlazadas, detalle y retorno.</td></tr>
<tr><td>Personalización</td><td>Control sobre gráficos, controles y presentación.</td></tr>
<tr><td>Rendimiento</td><td>Tiempo de carga y respuesta con los mismos datos.</td></tr>
<tr><td>Colaboración y versiones</td><td>Historial, documentación y manejo de archivos.</td></tr>
<tr><td>Compartir o desplegar</td><td>Sistema operativo, licencias, alojamiento y acceso local o externo; documentación oficial y fecha de consulta.</td></tr></table>
''')

page('5. Protocolo de pruebas', '''
<p>Se ejecutarán las mismas tres tareas en ambas versiones. Para cada ejecución se registrarán resultado, pasos o clics, tiempo y dificultades. Se usarán los mismos datos y selecciones; se anotarán diferencias de equipo, sistema operativo y experiencia previa.</p>
<h2>Prueba 1 · Responder una pregunta con filtros</h2>
<p><b>Pregunta:</b> ¿Cuántos visitantes ingresaron por vía terrestre entre enero y junio de 2025, considerando todas las regiones?</p>
<p><b>Pasos:</b> abrir Panorama; restablecer; fijar enero–junio de 2025; conservar todas las regiones; seleccionar Terrestre en las barras de vías; consultar la evolución mensual y el total de la vía.</p>
<p><b>Resultado esperado:</b> seis valores mensuales y un total de 1,043,269.45 visitantes en ambas herramientas, usando suma de Turista + Excursionista y redondeo solo de presentación. La línea debe responder a la selección de la barra. Al limpiar la selección deben reaparecer todas las vías.</p>
<h2>Prueba 2 · Pasar al detalle y regresar</h2>
<p><b>Pregunta:</b> ¿Cómo se distribuyen por trimestre y mes las entradas de visitantes de 2025?</p>
<p><b>Pasos:</b> restablecer; seleccionar todo 2025, todas las regiones y vías; consultar el total anual; pasar a trimestres y después a meses; regresar al nivel anual. En Streamlit se usará el selector Año/Trimestre/Mes; en Tableau, la jerarquía temporal.</p>
<p><b>Resultado esperado:</b> cuatro trimestres y doce meses; sus sumas deben coincidir con el total anual. El regreso debe conservar filtros y valor agregado.</p>
<h2>Prueba 3 · Consultar y comparar tres modelos</h2>
<p><b>Pregunta:</b> Para «Total visitantes», ¿qué modelo obtuvo el menor MAE y el menor RMSE en abril de 2021–junio de 2026, y cómo se apartaron las predicciones de lo observado?</p>
<p><b>Pasos:</b> abrir Modelos y límites; seleccionar Total visitantes, los tres modelos y toda la prueba; consultar observado y predicho; comparar MAE; cambiar a RMSE; enfocar un modelo y volver a la comparación completa.</p>
<p><b>Resultado esperado:</b> 63 meses de prueba por modelo. Según el CSV existente, suavizamiento exponencial registra el menor MAE (165,372.63) y RMSE (180,598.32), en visitantes. Ambas versiones deben reproducirlos para ese mismo conjunto. Son resultados históricos, no garantía de desempeño futuro.</p>
<h2>Registro y consistencia</h2>
<p>Se documentarán como mínimo dos comprobaciones: el total filtrado de la prueba 1 y el MAE de la prueba 3, con filtros, agregación, valores y diferencias. Los tiempos de uso de ambas herramientas se registrarán durante el trabajo; no se estimarán como si fueran mediciones.</p>
<p class="small"><b>Base documental:</b> enunciado del Laboratorio 12, sección «AVANCE», p. 4; documento de diseño y README del Lab 10; src/datos.py y CSV de data/modelos/. Las pruebas están definidas; los resultados medidos de las tres pruebas comparativas se incorporarán en la entrega final. La interacción entre las dos gráficas del avance ya fue comprobada visualmente.</p>
''')

doc.set_metadata({'title':'Laboratorio 12 · Informe de avance','author':'Jorge Lopez · 221038','subject':'Panorama de visitantes a Guatemala · 5 de noviembre de 2026'})
out = ROOT/'Lab12_Avance_Tableau_Jorge_Lopez_221038.pdf'
doc.save(out)
print(out)
print(f'{len(doc)} páginas, sin reducción automática de texto.')
