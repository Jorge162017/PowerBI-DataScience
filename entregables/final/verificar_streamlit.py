"""Pruebas funcionales reales mediante AppTest; no son clics de un usuario."""
from pathlib import Path
import os,sys,time,json
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'Lab10-DataScience'))
os.chdir(ROOT/'Lab10-DataScience')
from streamlit.testing.v1 import AppTest
OUT=ROOT/'entregables/final/evidencias'
OUT.mkdir(exist_ok=True)

def chart(a,key):
    for x in a.get('plotly_chart'):
        if key in x.proto.id:
            return json.loads(x.proto.spec)
    raise ValueError(key)

def values(trace,field):
    value=trace[field]
    if isinstance(value,dict):
        import numpy as np,base64
        return np.frombuffer(base64.b64decode(value['bdata']),dtype=value['dtype']).tolist()
    return value

a=AppTest.from_file(str(ROOT/'Lab10-DataScience/app.py'),default_timeout=120)
t=time.perf_counter();a.run();cold=time.perf_counter()-t
assert not a.exception, str(a.exception)
results=[]
t=time.perf_counter()
a.select_slider[0].set_value((pd.Timestamp('2025-01-01').to_pydatetime(),pd.Timestamp('2025-06-01').to_pydatetime())).run()
a.multiselect(key='vias').set_value(['Terrestre']).run()
fig=chart(a,'evolucion')
total=sum(values(fig['data'][0],'y'))
assert abs(total-1043269.4488721137)<.01
results.append({'prueba':1,'metodo':'AppTest con filtro de vía; no selección de barra por ratón','segundos_automatizados':time.perf_counter()-t,'total':total,'meses':len(values(fig['data'][0],'y')),'resultado':'Correcto'})
(OUT/'streamlit_prueba1_plotly.json').write_text(json.dumps(fig))
t=time.perf_counter()
a.multiselect(key='vias').set_value(['Aérea','Marítima','Terrestre']).run()
a.select_slider[0].set_value((pd.Timestamp('2025-01-01').to_pydatetime(),pd.Timestamp('2025-12-01').to_pydatetime())).run()
levels=[]
for level in ['Año','Trimestre','Mes','Año']:
    a.radio(key='detalle').set_value(level).run()
    fig=chart(a,'evolucion');v=values(fig['data'][0],'y')
    assert abs(sum(v)-3352288.657508455)<.01
    levels.append({'nivel':level,'marcas':len(v),'total':sum(v)})
results.append({'prueba':2,'metodo':'AppTest; cambios de control sin ratón','segundos_automatizados':time.perf_counter()-t,'niveles':levels,'resultado':'Correcto'})
(OUT/'streamlit_prueba2_plotly.json').write_text(json.dumps(fig))
t=time.perf_counter()
a.radio(key='seccion').set_value('Modelos y límites').run()
a.selectbox(key='serie_modelo').set_value('Total visitantes').run()
metrics={}
for met in ['MAE','RMSE']:
    a.radio(key='metrica_modelos').set_value(met).run()
    candidates=[]
    for x in a.get('plotly_chart'):
        f=json.loads(x.proto.spec)
        if f.get('data') and f['data'][0].get('type')=='bar':
            for tr in f['data']:candidates.append((tr['name'],values(tr,'y')[0]))
            (OUT/('streamlit_'+met+'_plotly.json')).write_text(json.dumps(f))
    metrics[met]=dict(candidates)
assert abs(metrics['MAE']['Suavizamiento exponencial']-165372.6258489368)<.01
assert abs(metrics['RMSE']['Suavizamiento exponencial']-180598.32147900484)<.01
assert not a.exception,str(a.exception)
results.append({'prueba':3,'metodo':'AppTest; navegación y selección de métrica sin ratón','segundos_automatizados':time.perf_counter()-t,'metricas':metrics,'resultado':'Correcto'})
(OUT/'resultados_streamlit.json').write_text(json.dumps({'carga_inicial_segundos':cold,'nota':'Tiempos automatizados; no comparables con estimaciones humanas de Tableau. No se midieron clics humanos.','pruebas':results},ensure_ascii=False,indent=2))
print(json.dumps(results,ensure_ascii=False,indent=2))
