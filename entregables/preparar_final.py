"""Datos auxiliares para Tableau. No ajusta modelos ni altera el avance."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
LAB = BASE.parent / 'Lab10-DataScience'
OUT = BASE / 'final' / 'datos'
OUT.mkdir(parents=True, exist_ok=True)
vis = pd.read_excel(BASE/'datos/Datos_Lab12.xlsx', sheet_name='Visitantes')
pred = pd.read_csv(LAB/'data/modelos/predicciones_lab1.csv', parse_dates=['Fecha'])
obs = pd.read_csv(LAB/'data/modelos/observados_lab1.csv', parse_dates=['Fecha'])
metrics = pd.read_csv(LAB/'data/modelos/metricas_lab1.csv')
assert not pred.duplicated(['Serie','Modelo','Fecha']).any()
assert not obs.duplicated(['Serie','Fecha']).any()
test = obs.loc[obs.Conjunto.eq('Prueba'), ['Serie','Fecha','Observado']]
merged = pred.merge(test, on=['Serie','Fecha'], validate='many_to_one', suffixes=('','_fuente'))
assert np.allclose(merged.Observado, merged.Observado_fuente)
curves = pd.concat([
    test.rename(columns={'Observado':'Valor'}).assign(Curva='Observado'),
    pred[['Serie','Fecha','Modelo','Predicho']].rename(columns={'Modelo':'Curva','Predicho':'Valor'})
], ignore_index=True).sort_values(['Serie','Curva','Fecha'])
assert not curves.duplicated(['Serie','Curva','Fecha']).any()
assert len(curves)==1764
pred['ErrorAbsoluto'] = (pred.Observado-pred.Predicho).abs()
pred['ErrorCuadrado'] = (pred.Observado-pred.Predicho)**2
computed = pred.groupby(['Serie','Modelo']).agg(MAE=('ErrorAbsoluto','mean'),MSE=('ErrorCuadrado','mean'),Meses=('Fecha','size')).reset_index()
computed['RMSE'] = np.sqrt(computed.pop('MSE'))
check = computed.merge(metrics,on=['Serie','Modelo'],suffixes=('_calculado','_original'),validate='one_to_one')
for field in ['MAE','RMSE']:
    assert np.allclose(check[field+'_calculado'],check[field+'_original'],rtol=1e-12,atol=1e-8)
assert (computed.Meses==63).all()
with pd.ExcelWriter(OUT/'Modelos_Tableau.xlsx',engine='openpyxl',datetime_format='YYYY-MM-DD') as writer:
    curves.to_excel(writer,sheet_name='Curvas',index=False)
    pred.to_excel(writer,sheet_name='Evaluacion',index=False)
    metrics.to_excel(writer,sheet_name='MetricasReferencia',index=False)
    for ws in writer.sheets.values():
        ws.freeze_panes='A2'
        ws.auto_filter.ref=ws.dimensions
        for col in ws.columns:ws.column_dimensions[col[0].column_letter].width=25
year = vis.loc[vis.Fecha.dt.year.eq(2025)]
values={
 'procedencia':'Valores de control calculados desde los archivos del Lab 10, no mediciones de uso de Tableau o Streamlit.',
 'filas_curvas':len(curves),'filas_evaluacion':len(pred),
 'visitantes_2025':float(year.Visitantes.sum()),
 'trimestres_2025':{str(k):float(v) for k,v in year.groupby(year.Fecha.dt.quarter).Visitantes.sum().items()},
 'terrestre_ene_jun_2025':float(vis.loc[vis.Fecha.between('2025-01-01','2025-06-01') & vis.Via.eq('Terrestre'),'Visitantes'].sum()),
 'metricas_total_visitantes':computed.loc[computed.Serie.eq('Total visitantes')].to_dict('records'),
 'max_diferencia_mae':float((check.MAE_calculado-check.MAE_original).abs().max()),
 'max_diferencia_rmse':float((check.RMSE_calculado-check.RMSE_original).abs().max())
}
(OUT/'controles_final.json').write_text(json.dumps(values,ensure_ascii=False,indent=2))
print(json.dumps(values,ensure_ascii=False,indent=2))
