"""Genera PDFs de preparación; no cambia el documento del avance."""
from pathlib import Path
import csv
import fitz
from markdown_it import MarkdownIt

BASE = Path(__file__).resolve().parent
parser = MarkdownIt('default', {'html': False}).enable('table')
CSS = '''body {font-family:sans-serif; font-size:10pt; line-height:1.4; color:#243238;}
h1 {font-size:21pt; color:#20735F; margin-bottom:14pt;} h2 {font-size:13pt; color:#20735F; margin-top:14pt;}
h3 {font-size:11pt; color:#20735F;} p {margin:0 0 8pt;} li {margin-bottom:5pt;}
table {border-collapse:collapse; width:100%; margin:8pt 0;} td,th {padding:6pt; border-bottom:1px solid #DDE3E4; font-size:9pt; vertical-align:top; text-align:left;}
th {background:#EFF4F2; color:#20735F;} pre {font-size:9pt; background:#F1F5F4; padding:8pt;}
code {font-size:9pt;} a {color:#20735F;} hr {margin:16pt 0;}'''

def render(source, output):
    # Cada sección del informe inicia en página nueva; la guía fluye libremente.
    text = (BASE/source).read_text()
    sections = text.split('\n---\n') if source.startswith('INFORME') else [text]
    result = fitz.open()
    for section in sections:
        story = fitz.Story(html=parser.render(section), user_css=(CSS.replace("font-size:10pt", "font-size:9.5pt").replace("line-height:1.4", "line-height:1.32") if source=="INFORME_FINAL.md" else CSS))
        temp = BASE/'_render_temporal.pdf'
        writer = fitz.DocumentWriter(str(temp))
        while True:
            device = writer.begin_page(fitz.Rect(0,0,595.28,841.89))
            more, _ = story.place(fitz.Rect(45,65,550,780))
            story.draw(device)
            writer.end_page()
            if not more: break
        writer.close()
        with fitz.open(temp) as part: result.insert_pdf(part)
        temp.unlink()
    for index,p in enumerate(result):
        p.insert_text((45,35),'UNIVERSIDAD DEL VALLE DE GUATEMALA | CC3066 · DATA SCIENCE',fontsize=8,color=(.34,.4,.42))
        p.draw_line((45,46),(550,46),color=(.80,.85,.83),width=.6)
        p.draw_line((45,797),(550,797),color=(.80,.85,.83),width=.6)
        p.insert_text((45,814),('LAB 12 · DOCUMENTO FINAL · JORGE LOPEZ · 221038' if source=='INFORME_FINAL.md' else 'LAB 12 · PREPARACIÓN FINAL · JORGE LOPEZ · 221038'),fontsize=8,color=(.34,.4,.42))
        p.insert_text((510,814),f'{index+1} / {len(result)}',fontsize=8,color=(.34,.4,.42))
    result.set_metadata({'title':source.removesuffix('.md'),'author':'Jorge Lopez · 221038','subject':('Diseño y evaluación del laboratorio 12' if source=='INFORME_FINAL.md' else 'Preparación del laboratorio 12')})
    result.save(BASE/output,garbage=4,deflate=True)
    print(output,len(result),'páginas')

if __name__=='__main__':
    render('INFORME_FINAL_BORRADOR.md','Lab12_Informe_Final_BORRADOR_221038.pdf')
    render('TU_PARTE_TABLEAU.md','Guia_Tableau_221038.pdf')
