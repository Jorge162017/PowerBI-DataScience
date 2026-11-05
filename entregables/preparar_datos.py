"""Prepara las mismas tablas del Lab 10 sin entrenar ni modificar modelos."""
from pathlib import Path
import sys
import json
import pandas as pd
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / 'Lab10-DataScience'
sys.path.insert(0, str(LAB))
from src.datos import cargar_visitantes

out = ROOT / 'entregables' / 'datos'
out.mkdir(exist_ok=True)
vis = cargar_visitantes().rename(columns={'Región dos':'Region', 'Vía':'Via', 'Viajero':'Visitantes'})
assert not vis.duplicated(['Fecha','Region','Via']).any()
tables = {'Visitantes':vis}
for name, file in [('Observados','observados_lab1.csv'),('Predicciones','predicciones_lab1.csv'),('Metricas','metricas_lab1.csv')]:
    tables[name] = pd.read_csv(LAB/'data/modelos'/file)
    if 'Fecha' in tables[name]:
        tables[name]['Fecha'] = pd.to_datetime(tables[name]['Fecha'])
assert not tables['Predicciones'].duplicated(['Serie','Modelo','Fecha']).any()
assert not tables['Observados'].duplicated(['Serie','Fecha']).any()
assert not tables['Metricas'].duplicated(['Serie','Modelo']).any()
assert len(tables['Predicciones']) == 1323
dates = pd.DataFrame({'Fecha':pd.date_range('2009-01-01','2026-06-01',freq='MS')})
dates['Año'] = dates.Fecha.dt.year
dates['Trimestre'] = 'T'+dates.Fecha.dt.quarter.astype(str)
dates['MesNumero'] = dates.Fecha.dt.month
tables['Calendario'] = dates
tables['Series'] = pd.DataFrame({'Serie':tables['Observados'].Serie.unique()})
tables['Modelos'] = pd.DataFrame({'Modelo':tables['Metricas'].Modelo.unique()})
with pd.ExcelWriter(out/'Datos_Lab12.xlsx', engine='openpyxl',datetime_format='YYYY-MM-DD') as writer:
    for name, df in tables.items():
        df.to_excel(writer,sheet_name=name,index=False)
        ws = writer.sheets[name]
        ws.freeze_panes='A2'
        tab = Table(displayName=name, ref=ws.dimensions)
        tab.tableStyleInfo=TableStyleInfo(name='TableStyleMedium4',showRowStripes=True)
        ws.add_table(tab)
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width=min(35,max(16,len(str(col[0].value))+3))
        for cell in ws[1]:
            cell.font=Font(bold=True,color='FFFFFF')
            cell.fill=PatternFill('solid',fgColor='20735F')
mask = vis.Fecha.between('2025-01-01','2025-06-01') & vis.Via.eq('Terrestre')
check = {
    'filas':{k:len(v) for k,v in tables.items()},
    'prueba_1_total_terrestre_ene_jun_2025':float(vis.loc[mask,'Visitantes'].sum()),
    'prueba_1_meses':{d.strftime('%Y-%m'):float(v) for d,v in vis.loc[mask].groupby('Fecha').Visitantes.sum().items()},
    'modelos_total_visitantes':tables['Metricas'].loc[tables['Metricas'].Serie.eq('Total visitantes'),['Modelo','MAE','RMSE']].to_dict('records'),
    'estado':'Fuentes preparadas y verificadas en Python; importación e interacción en Power BI pendientes de verificar.'
}
(out/'verificacion_datos.json').write_text(json.dumps(check,ensure_ascii=False,indent=2))
print(json.dumps(check,ensure_ascii=False,indent=2))
