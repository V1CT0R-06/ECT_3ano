from pathlib import Path
import math, json, zipfile
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from openpyxl import load_workbook
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'Relatorio_Final_Movimento_Projeteis_PL6_G3.docx'
AUX=ROOT/'apoio'
w=load_workbook(ROOT/'final_final.xlsx',data_only=True)
a,b,c=w.worksheets
s,ds=a['B3'].value,a['B4'].value
t=np.array([a.cell(i,2).value for i in range(7,12)])
th=np.array([b.cell(i,1).value for i in range(6,11)])
x=np.array([[b.cell(i,j).value for j in range(2,5)] for i in range(6,11)])
al=np.array([c.cell(i,2).value for i in range(8,13)])
m,M,l=[c.cell(i,2).value for i in range(3,6)]
dm,dM,dl=[c.cell(i,4).value for i in range(3,6)]
g=9.80;H=b['B3'].value;dH=.0005
tm=t.mean();dt=max(abs(t-tm));v=s/tm;dv=ds/tm+s*dt/tm**2
am=al.mean();da=max(abs(al-am));ar=math.radians(am);dar=math.radians(da)
h=l*(1-math.cos(ar));dh=(1-math.cos(ar))*dl+l*math.sin(ar)*dar
vc=(m+M)/m*math.sqrt(2*g*h)
dvc=math.sqrt(2*g*h)*(M/m**2*dm+dM/m)+vc/(2*h)*dh
xm=x.mean(axis=1)
def reach(theta,vel=v):
 rad=np.radians(theta)
 return vel*np.cos(rad)/g*(vel*np.sin(rad)+np.sqrt(vel**2*np.sin(rad)**2+2*g*H))
opt=math.degrees(math.atan(v/math.sqrt(v*v+2*g*H)))
# Derivadas analíticas do ângulo ótimo: atan(v / sqrt(v² + 2gH)).
Q=math.sqrt(v*v+2*g*H)
dopt=math.degrees(g*H/(Q*(v*v+g*H))*dv+g*v/(2*Q*(v*v+g*H))*dH)
vinf=np.sqrt(g*xm*xm/(2*np.cos(np.radians(th))**2*(H+xm*np.tan(np.radians(th)))))
res=dict(g=g,tm=tm,dt=dt,vA=v,dvA=dv,alpha=am,dalpha=da,h=h,dh=dh,vC=vc,dvC=dvc,theta=opt,dtheta=dopt,means=xm.tolist(),ranges=reach(th).tolist(),v_from_B=vinf.tolist())
(AUX/'resultados_verificados.json').write_text(json.dumps(res,indent=2))
with zipfile.ZipFile(ROOT/'Relatorio_Movimento_Projeteis.docx') as z:
 for name in ['fig_a.png','fig_b.png','fig_c.png']:
  (AUX/name).write_bytes(z.read('word/media/'+name))
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(7.0,3.4),layout='constrained')
for j in range(3): ax.scatter(th,x[:,j],color='#999999',s=23,label='Disparos individuais' if j==0 else None)
ax.plot(th,xm,'o-',color='#111111',label='Alcance médio (linha de guia)')
ax.scatter([38],[xm[2]],s=125,facecolors='none',edgecolors='#444444',label='Maior média observada')
ax.set(xlabel='Ângulo de lançamento, θ / °',ylabel='Alcance horizontal, x / m',xticks=th,ylim=(1.105,1.175));ax.grid(alpha=.2);ax.legend(fontsize=8,loc='upper right')
fig.savefig(AUX/'alcance_observado.png',dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(7.0,3.2),layout='constrained');ang=np.linspace(28,45,200)
ax.plot(ang,reach(ang),color='#111111',label='Modelo com v₀ da Parte A')
ax.plot(th,xm,'o',color='#444444',label='Médias observadas')
ax.set(xlabel='Ângulo de lançamento, θ / °',ylabel='Alcance horizontal, x / m',xticks=th,ylim=(.85,1.2));ax.grid(alpha=.2);ax.legend(fontsize=8)
fig.savefig(AUX/'alcance_modelo.png',dpi=220);plt.close(fig)
D=Document();sec=D.sections[0]
sec.page_width=Cm(21);sec.page_height=Cm(29.7);sec.top_margin=Cm(2.1);sec.bottom_margin=Cm(2.0);sec.left_margin=Cm(2.4);sec.right_margin=Cm(2.4)
normal=D.styles['Normal'];normal.font.name='Times New Roman';normal.font.size=Pt(11)
normal.paragraph_format.space_after=Pt(4);normal.paragraph_format.line_spacing=1.02
for sty,size in [('Title',23),('Heading 1',15),('Heading 2',12),('Heading 3',11)]:
 D.styles[sty].font.name='Times New Roman';D.styles[sty].font.size=Pt(size);D.styles[sty].font.color.rgb=RGBColor.from_string('000000')
 D.styles[sty].paragraph_format.space_before=Pt(10);D.styles[sty].paragraph_format.space_after=Pt(6)
for name in ['Caption','Header','Footer']:
 D.styles[name].font.name='Times New Roman';D.styles[name].font.color.rgb=RGBColor(0,0,0)
D.styles['Caption'].font.size=Pt(9)
D.styles['Caption'].font.italic=False
lang=OxmlElement('w:lang');lang.set(qn('w:val'),'pt-PT');normal.element.get_or_add_rPr().append(lang)
header=sec.header.paragraphs[0];header.text='Movimento de projéteis — Mecânica e Campo Eletromagnético';header.style='Caption';header.runs[0].font.size=Pt(8)
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
# Only the page number in the footer.
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
sec.different_first_page_header_footer=True

def p(txt,bold=False):
 pp=D.add_paragraph();pp.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY;pp.paragraph_format.first_line_indent=Cm(0.5);pp.add_run(txt).bold=bold;return pp

def h1(txt):D.add_heading(txt,level=1)
def h2(txt):D.add_heading(txt,level=2)
def eq(txt):
 pp=D.add_paragraph();pp.alignment=WD_ALIGN_PARAGRAPH.CENTER;pp.paragraph_format.space_after=Pt(7);r=pp.add_run(txt);r.font.name='Times New Roman';r.font.size=Pt(11)
def table(headers,rows,caption):
 pp=D.add_paragraph(caption,style='Caption');pp.paragraph_format.keep_with_next=True
 tb=D.add_table(rows=1,cols=len(headers));tb.style='Normal Table'
 for i,s in enumerate(headers):tb.rows[0].cells[i].text=str(s)
 borders=OxmlElement('w:tblBorders')
 for side in ['top','bottom','left','right','insideH','insideV']:
  el=OxmlElement('w:'+side);el.set(qn('w:val'),'single' if side in ['top','bottom'] else 'nil')
  el.set(qn('w:sz'),'6');el.set(qn('w:color'),'000000');borders.append(el)
 tb._tbl.tblPr.append(borders)
 for cell in tb.rows[0].cells:
  cb=OxmlElement('w:tcBorders');line=OxmlElement('w:bottom');line.set(qn('w:val'),'single');line.set(qn('w:sz'),'4');line.set(qn('w:color'),'000000');cb.append(line);cell._tc.get_or_add_tcPr().append(cb)
  for rr in cell.paragraphs[0].runs:rr.bold=True
 repeat=OxmlElement('w:tblHeader');tb.rows[0]._tr.get_or_add_trPr().append(repeat)
 for row in rows:
  cells=tb.add_row().cells
  for i,s in enumerate(row):cells[i].text=str(s)
 for row in tb.rows:
  for cell in row.cells:
   for pp in cell.paragraphs:
    pp.paragraph_format.space_after=Pt(3);pp.paragraph_format.space_before=Pt(2)
    for rr in pp.runs:rr.font.size=Pt(9)
  pr=row._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
 # No empty paragraph after a table.
 return tb

def image(name,caption,width=14):
 pp=D.add_paragraph();pp.alignment=WD_ALIGN_PARAGRAPH.CENTER;pp.paragraph_format.keep_with_next=True
 pp.add_run().add_picture(str(AUX/name),width=Cm(width));D.add_paragraph(caption,style='Caption')
def page():
 pp=D.add_page_break();pp.paragraph_format.space_before=Pt(0);pp.paragraph_format.space_after=Pt(0);pp.paragraph_format.line_spacing=Pt(1)
 for rr in pp.runs:rr.font.size=Pt(1)
def fmt(v,n=4):return f'{v:.{n}f}'.replace('.',',')
# 1 — Identificação
for text in ['Universidade de Aveiro','Departamento de Física','Mecânica e Campo Eletromagnético','Ano letivo 2026/2027']:
 pp=D.add_paragraph(text);pp.alignment=WD_ALIGN_PARAGRAPH.CENTER
D.add_paragraph('\n')
pp=D.add_paragraph('Movimento de projéteis',style='Title');pp.alignment=WD_ALIGN_PARAGRAPH.CENTER
pp=D.add_paragraph('Relatório final — Trabalho prático 1');pp.alignment=WD_ALIGN_PARAGRAPH.CENTER
pp=D.add_paragraph('Velocidade inicial • Alcance e ângulo de lançamento\nPêndulo balístico');pp.alignment=WD_ALIGN_PARAGRAPH.CENTER
D.add_paragraph('\n')
table(['Autores','N.º mecanográfico','E-mail institucional'],[
 ['Diogo Pereira','133428','diogomarquespereira@ua.pt'],['José Rocha','132425','jose.m.rocha@ua.pt'],['Victor Morais','125478','victorcostamorais@ua.pt']], 'Identificação dos autores')
p('Turma prática: PL6     •     Grupo: 3')
p('Data de elaboração: 28 de outubro de 2026')
p('Datas de realização: Partes A e B — 16 de outubro de 2026; Parte C — 23 de outubro de 2026.\nDocente: José Rocha.')
p('Relatório elaborado a partir dos registos experimentais e das folhas de tratamento de dados fornecidos, seguindo a estrutura do guião e dos dois relatórios de exemplo.')
page()
# 2 — Resumo e teoria
h1('1. Resumo')
p('Determinou-se a velocidade inicial de uma esfera por cronometragem entre sensores e por um pêndulo balístico, e estudou-se a dependência do alcance com o ângulo de lançamento. Na Parte A, cinco tempos de passagem conduziram a v₀,A = (2,6 ± 0,1) m/s, com erro relativo de 5,1 %. Na Parte B, três disparos para cada um de cinco ângulos identificaram o maior alcance médio, 1,154 m, a θmáx,obs = (38 ± 1)°, compatível com a previsão de 37,2° para a altura de 0,2600 m e a velocidade da Parte A; contudo, os alcances absolutos excedem os previstos por esse modelo. Na Parte C, cinco ângulos de deflexão permitiram obter h = (1,3 ± 0,2) × 10⁻³ m e v₀,C = (4,0 ± 0,3) m/s, com erro relativo de 8,0 %. As duas velocidades cumprem o critério de precisão de 10 % adotado na unidade curricular, mas são incompatíveis dentro das incertezas estimadas. Os objetivos de determinação experimental foram atingidos; a concordância quantitativa entre métodos não foi demonstrada e o máximo do alcance ficou pouco resolvido pela dispersão dos disparos.')
h1('2. Introdução')
p('O movimento de projéteis permite relacionar a cinemática bidimensional com a dinâmica e os princípios de conservação. No modelo do guião [1], despreza-se a resistência do ar e considera-se g constante, com o eixo x horizontal e o eixo y vertical ascendente. Para um lançamento com velocidade v₀ e inclinação θ, a partir de (x₀, yᵢ), tem-se:')
eq('x − x₀ = v₀ t cos θ;     y − yᵢ = v₀ t sin θ − ½gt².     (1)')
p('Eliminando t, obtém-se a trajetória parabólica. O alcance R corresponde à distância horizontal até ao plano y = y_f. Com H = yᵢ − y_f e x₀ = 0:')
eq('y − yᵢ = x tan θ − gx² / (2v₀² cos² θ).     (2)')
eq('R(θ) = (v₀ cos θ / g) [v₀ sin θ + √(v₀² sin² θ + 2gH)].     (3)')
p('Para H constante, a maximização do alcance conduz a:')
eq('θmáx = arctan[1 / √(1 + 2gH/v₀²)].     (4)')
p('Quando H = 0, o máximo ocorre a 45°; quando H > 0, ocorre abaixo de 45°. Na Parte A, s é a separação horizontal efetiva entre sensores e v₀ = s/t̄ determina a componente horizontal da velocidade; com o lançador horizontal, esta coincide com o módulo inicial no modelo sem arrasto. A aceleração vertical não altera a componente horizontal.')
p('No pêndulo balístico, de massa M, a esfera de massa m fica retida após a colisão. No modelo simplificado do guião, conserva-se o momento linear horizontal no impacto e a energia mecânica na subida subsequente. A energia mecânica não se conserva durante a colisão inelástica:')
eq('mv₀ = (m + M)v₂;     ½(m + M)v₂² = (m + M)gh.     (5)')
eq('h = l(1 − cos α);     v₀ = [(m + M)/m]√(2gh).     (6)')
p('Aqui, l é a distância efetiva ao centro de massa no modelo de pêndulo simples, α o ângulo máximo e v₂ a velocidade logo após o impacto. A aplicação a um pêndulo rígido real exige avaliar a distribuição de massa e a geometria do impacto.')
page()
# 3 — A B experimentais
h1('3. Detalhes experimentais relevantes')
h2('3.1. Parte A — Determinação da velocidade inicial')
p('Material: lançador de projéteis (LP), base com grampo, esfera plástica, vareta de carregamento, dois sensores de passagem, unidade de controlo em modo «TWO GATES» e régua. Adota-se Δs = 0,0005 m, conforme a folha de dados. A resolução temporal de 0,0001 s é a indicada nos relatórios de exemplo; não foi disponibilizada a ficha do instrumento.')
image('fig_a.png','Figura 1 — Montagem da Parte A: (1) LP; (2) base; (3) sensor inicial; (4) sensor final; (5) unidade de controlo. Esquema do guião [1], reproduzido a partir dos exemplos fornecidos.',10)
p('Fixar a base à bancada e orientar o LP na horizontal. Com a unidade de controlo desligada, ligar os sensores e colocar o primeiro junto à saída do lançador. Medir a separação efetiva s entre os feixes. Carregar a esfera em «SHORT RANGE», confirmar a posição do indicador de carga, selecionar «TWO GATES» e armar a cronometragem com START/STOP. Disparar puxando o fio verticalmente e com suavidade; registar o tempo. Repetir até obter cinco medidas, verificando a horizontalidade entre disparos.')
p('Cuidados: impedir movimentos da base, manter a mesma posição de carga, alinhar os sensores e medir s entre pontos homólogos dos feixes. Estas verificações são necessárias para reproduzir o protocolo; os ficheiros não incluem um registo individual da sua execução.')
h2('3.2. Parte B — Dependência do alcance com o ângulo')
p('Material: LP e respetiva base, esfera e vareta, escala angular, alvo de papel químico sobre papel milimétrico, régua ou fita métrica. O erro de leitura de cada alcance é 0,0005 m. Usa-se H = 0,2600 m, com y_f = 0 na bancada; adota-se ΔH = 0,0005 m, como nos exemplos, por se considerar uma escala milimétrica.')
image('fig_b.png','Figura 2 — Montagem da Parte B: (1) LP; (2) base; (3) alvo. O alcance mede-se desde a vertical da saída até ao impacto. Esquema do guião [1], reproduzido dos exemplos.',10)
p('Fixar o LP a 30° e localizar a zona de impacto por tentativa. Colocar o alvo e efetuar três disparos em «SHORT RANGE», medindo os alcances a partir da mesma referência horizontal. Repetir para 34°, 38°, 40° e 43°, verificando o ângulo antes de cada disparo. Medir a altura de saída em relação ao plano do alvo. Fixar o papel, identificar o centro de cada marca e evitar paralaxe. A altura deve ser verificada se a saída do cano se deslocar ao rodar o lançador.')
page()
# 4 C experimental and error
h2('3.3. Parte C — Pêndulo balístico')
p('Material: LP na posição de tiro curto, esfera, pêndulo balístico com indicador do ângulo máximo, balança e régua ou fita métrica. Os erros usados, registados em final_final.xlsx, são Δm = ΔM = 0,00001 kg e Δl = 0,0005 m. A menor divisão efetiva da escala do pêndulo não está documentada na folha de dados.')
image('fig_c.png','Figura 3 — Montagem da Parte C: esfera de massa m, pêndulo de massa M, ângulo α, comprimento efetivo l e elevação h. Esquema do guião [1], reproduzido dos exemplos.',11)
p('Medir m, M e l. Alinhar o LP horizontalmente com o recetor do pêndulo e carregar em «SHORT RANGE». Com o pêndulo em repouso e o indicador reposto na posição inicial, disparar e registar o ângulo máximo α. Repetir o procedimento para cinco disparos.')
p('Cuidados: verificar o zero do indicador, evitar torção lateral e confirmar a retenção da esfera em cada ensaio; ler perpendicularmente à escala. A retenção é uma condição do modelo, mas não existe nos registos fornecidos uma observação individual que permita confirmar ou excluir ressaltos.')
h1('4. Análise e discussão')
h2('4.1. Critérios de tratamento de dados')
p('Preservou-se a sequência A–B–C das folhas de tratamento. Todos os cálculos foram refeitos a partir das medidas diretas de final_final.xlsx. Adota-se g = 9,80 m/s² em todas as partes, valor usado no cálculo do pêndulo nessa folha; a sua incerteza não é incluída, conforme o modelo de tratamento adotado.')
p('Para N = 5 medidas, usa-se a média aritmética e o desvio absoluto máximo, segundo o guia de análise experimental [2]:')
eq('q̄ = (Σqᵢ)/N;     Δq = max |qᵢ − q̄|.     (7)')
p('O desvio máximo caracteriza a dispersão observada; não representa um intervalo de confiança estatístico. Para grandezas indiretas, aplica-se o limite superior do erro por propagação linear:')
eq('ΔF = Σ |∂F/∂qⱼ| Δqⱼ.     (8)')
p('As dependências repetidas da mesma variável devem ser simplificadas antes de derivar. Os cálculos preservam a precisão numérica interna; as incertezas finais apresentam um algarismo significativo e os valores finais a mesma casa decimal. Os erros relativos são calculados antes do arredondamento, evitando percentagens artificiais obtidas a partir dos valores finais já arredondados.')
p('No critério pedagógico de [2], considera-se preciso um resultado com erro relativo até 10 %. A compatibilidade é discutida pela sobreposição dos intervalos. Sem um valor de referência independente e validado, a incompatibilidade entre métodos não permite identificar qual deles é mais exato.')
page()
# 5 A
h2('4.2. Parte A — Determinação da velocidade inicial')
D.add_heading('Análise',level=3)
p('A distância entre sensores é s = (0,0840 ± 0,0005) m. Os cinco tempos e os respetivos desvios estão no Anexo A (Tabela 6). Obtém-se:')
eq('t̄ = (0,0320 + 0,0325 + 0,0304 + 0,0327 + 0,0316)/5')
eq('t̄ = 0,03184 s;     Δt = |0,0304 − 0,03184| = 0,00144 s.')
p('O maior desvio ocorre no terceiro ensaio. É superior à resolução temporal indicada nos exemplos (0,0001 s), pelo que a dispersão entre disparos domina esse limite instrumental. A velocidade é:')
eq('v₀,A = s/t̄ = 0,0840/0,03184 = 2,63819 m/s.     (9)')
p('Como ∂v/∂s = 1/t̄ e ∂v/∂t̄ = −s/t̄², a propagação dá:')
eq('Δv₀,A = Δs/t̄ + (s/t̄²)Δt = v₀,A(Δs/s + Δt/t̄).     (10)')
eq('Δv₀,A = 0,015704 + 0,119315 = 0,135019 m/s.')
table(['Grandeza','Valor antes do arredondamento','Resultado final'],[
 ['Tempo médio / s','0,03184 ± 0,00144','0,032 ± 0,001'],['Velocidade inicial / (m/s)','2,63819 ± 0,13502','2,6 ± 0,1'],['Erro relativo de v₀,A','5,1179 %','5,1 %']], 'Tabela 1 — Resultados da Parte A. As percentagens usam os valores não arredondados.')
D.add_heading('Discussão',level=3)
p('A velocidade é precisa segundo o critério de 10 %, pois Δv₀,A/v₀,A = 5,1 %. A contribuição do tempo é 0,119315 m/s, ou 88,4 % da incerteza total; a contribuição da distância é 0,015704 m/s, ou 11,6 %. A principal fonte quantificada de incerteza é, portanto, a dispersão do tempo de passagem.')
p('Os tempos variam entre 0,0304 s e 0,0327 s. Essa variação pode refletir diferenças na velocidade de saída, no acionamento do disparador, na orientação do LP ou no disparo dos sensores. Os dados não permitem separar quantitativamente estes efeitos. Nenhuma medida foi eliminada, incluindo o terceiro ensaio, porque não existe registo de falha que justifique a sua exclusão.')
p('Para melhorar a determinação, deve verificar-se a distância entre os feixes ativos, a horizontalidade e a repetibilidade da posição de carga. Uma maior série de disparos permitiria caracterizar melhor a dispersão e, com N ≥ 10, aplicar o tratamento estatístico previsto em [2]. Aumentar o número de ensaios não corrige, por si, erros de calibração ou de referência geométrica.')
p('A precisão obtida não demonstra a exatidão de v₀,A. Uma distância efetiva entre feixes diferente da distância registada produziria um desvio sistemático em v = s/t; a título de sensibilidade, 1 cm corresponde a cerca de 12 % de s. Esta é uma hipótese a verificar, e não uma correção aplicada aos dados.')
page()
# 6 B
h2('4.3. Parte B — Dependência do alcance com o ângulo')
D.add_heading('Análise',level=3)
p('Para cada ângulo, calculou-se x̄_ob = (x₁ + x₂ + x₃)/3. Seguindo o guião, não se determina a incerteza do alcance médio. As medidas individuais constam do Anexo B (Tabela 7), com erro de leitura de 0,0005 m.')
table(['θ / °','x̄_ob / m','R teórico com v₀,A / m'],[[str(int(q)),fmt(u,4),fmt(rr,4)] for q,u,rr in zip(th,xm,reach(th))], 'Tabela 2 — Médias experimentais e previsão pela equação (3), com H = 0,2600 m.')
image('alcance_observado.png','Figura 4 — Alcance em função do ângulo. Os pontos cinzentos representam os três disparos; a linha une as médias para guiar a leitura. A escala vertical não começa em zero.',15.5)
p('Por exemplo, para 38°, x̄_ob = (1,164 + 1,139 + 1,158)/3 = 1,153666… m. Esta é a maior média entre os cinco ângulos estudados. A incerteza de 1° é a convenção expressamente pedida no guião para a amostragem discreta, não um erro instrumental deduzido dos intervalos entre ângulos:')
eq('θmáx,obs = (38 ± 1)°.     (11)')
p('A equação (4), com v₀,A = 2,63819 m/s, H = 0,2600 m e g = 9,80 m/s², fornece:')
eq('θmáx = arctan[1/√(1 + 2 × 9,80 × 0,2600 / 2,63819²)] = 37,2278°.')
p('O valor teórico pertence a [37°; 39°]. Incluindo as incertezas de v₀,A e H por propagação linear da equação (4), obtém-se Δθmáx ≈ 0,6°; a compatibilidade mantém-se. O erro relativo do ângulo observado é 1/38 × 100 = 2,6 %, cumprindo também o critério de precisão adotado.')
page()
# 7 B discussion
D.add_heading('Discussão da Parte B',level=3)
p('As médias a 30°, 34° e 38° diferem apenas 0,0027 m entre a menor e a maior. A diferença entre 30° e 38° é 0,0013 m, enquanto os disparos a 38° abrangem 0,025 m. Assim, 38° é o ângulo da maior média medida, mas os dados não localizam de forma robusta o máximo físico da curva com uma resolução de 1°. Esta limitação deve acompanhar o resultado convencional da equação (11).')
p('Para 40° e 43°, o alcance médio diminui para 1,1373 m e 1,1230 m, respetivamente. A tendência é compatível qualitativamente com um máximo inferior a 45°. No entanto, a concordância do ângulo com a teoria não valida automaticamente a velocidade da Parte A nem a previsão do alcance absoluto.')
image('alcance_modelo.png','Figura 5 — Comparação dos alcances medidos com a previsão sem arrasto, usando a velocidade da Parte A e H = 0,2600 m. O desvio absoluto permanece evidente.',15)
p('A 38°, o modelo prevê R = '+fmt(reach(38),4)+' m, face a 1,1537 m observados: uma diferença de cerca de '+fmt(xm[2]-reach(38),3)+' m, ou '+fmt((xm[2]/reach(38)-1)*100,1)+' % da previsão. Mesmo usando o limite superior não arredondado v₀,A + Δv₀,A = 2,77321 m/s, obtém-se R ≈ '+fmt(reach(38,v+dv),3)+' m, ainda abaixo dos alcances medidos. A resolução de leitura dos impactos não explica uma discrepância desta ordem.')
p('Invertendo a equação da trajetória para cada média experimental, pode obter-se uma estimativa diagnóstica da velocidade exigida pelo modelo:')
eq('v₀,B = √{g x̄_ob² / [2 cos²θ (H + x̄_ob tan θ)]}.     (12)')
p('Os valores são '+', '.join(fmt(z,3) for z in vinf)+' m/s para 30°, 34°, 38°, 40° e 43°, respetivamente. Situam-se perto de 3,0 m/s. Esta estimativa serve para evidenciar a incoerência; não constitui um terceiro resultado final com incerteza determinada.')
p('Devem verificar-se a referência do alcance, a separação dos sensores, a manutenção da posição de carga entre partes e a altura de saída para cada ângulo. Variações de velocidade e da altura ao rodar o LP podem afetar a curva. A resistência do ar, isoladamente, tenderia a reduzir o alcance face ao modelo ideal, pelo que não explica os alcances superiores à previsão com v₀,A. Uma amostragem angular mais densa e mais repetições por ângulo ajudariam a resolver o máximo.')
page()
# 8 C analysis
h2('4.4. Parte C — Pêndulo balístico')
D.add_heading('Análise',level=3)
p('Usam-se m = (0,00964 ± 0,00001) kg, M = (0,23790 ± 0,00001) kg e l = (0,3480 ± 0,0005) m. Os cinco ângulos e os desvios estão no Anexo C (Tabela 9). A média e o desvio máximo são:')
eq('ᾱ = (5,2 + 4,5 + 5,0 + 4,9 + 4,8)/5 = 4,88°;     Δα = 0,38°.')
eq('ᾱ = 0,0851721 rad;     Δα = 0,00663225 rad.')
p('Pela geometria da Figura 3, h = l − l cos α. Substituindo a média angular e propagando as incertezas:')
eq('h = 0,3480[1 − cos(4,88°)] = 0,001261482 m.     (13)')
eq('Δh = |1 − cos ᾱ|Δl + |l sin ᾱ|Δα.     (14)')
eq('Δh = 0,000001812 + 0,000196342 = 0,000198154 m.')
p('A incerteza angular tem de estar em radianos no termo da derivada. Da equação (6), obtém-se:')
eq('v₀,C = [(0,00964 + 0,23790)/0,00964]√(2 × 9,80 × 0,001261482)')
eq('v₀,C = 4,037727 m/s.')
p('Derivando em ordem às variáveis independentes m, M e h, sem tratar m + M e m como massas independentes:')
eq('∂v/∂m = −(M/m²)√(2gh);     ∂v/∂M = √(2gh)/m;     ∂v/∂h = v/(2h).')
eq('Δv₀,C = (M/m²)√(2gh)Δm + [√(2gh)/m]ΔM + [v₀,C/(2h)]Δh.     (15)')
eq('Δv₀,C = 0,004026 + 0,000163 + 0,317123 = 0,321312 m/s.')
table(['Grandeza','Valor antes do arredondamento','Resultado final'],[
 ['Ângulo médio / °','4,88 ± 0,38','4,9 ± 0,4'],['Altura / m','(1,26148 ± 0,19815) × 10⁻³','(1,3 ± 0,2) × 10⁻³'],['Velocidade / (m/s)','4,03773 ± 0,32131','4,0 ± 0,3'],['Erro relativo de v₀,C','7,9577 %','8,0 %']], 'Tabela 3 — Resultados da Parte C, com g = 9,80 m/s².')
p('A incerteza relativa de v₀,C é 8,0 %, inferior a 10 %. A precisão é menor do que na Parte A. A incerteza relativa de h é 15,7 %, mas a dependência v ∝ √h reduz para metade a sua contribuição relativa à velocidade.')
p('Para α pequeno, h ≈ lα²/2 e v₀,C ≈ [(m + M)/m]√(gl)α. Por isso, a incerteza relativa da velocidade fica próxima de Δα/ᾱ = 7,8 %.')
page()
# 9 discussion compare
D.add_heading('Discussão da Parte C e comparação entre métodos',level=3)
table(['Origem','Contribuição para Δv₀,C / (m/s)','Fração'],[
 ['Massa da esfera, m','0,004026','1,25 %'],['Massa do pêndulo, M','0,000163','0,05 %'],['Altura, h','0,317123','98,70 %']], 'Tabela 4 — Decomposição da incerteza da velocidade pelo pêndulo balístico.')
p('A determinação de h domina Δv₀,C; por sua vez, 99,1 % de Δh provém da parcela angular e apenas 0,9 % do comprimento. A principal fonte quantificada de erro é a dispersão de α. A menor divisão efetiva da escala não consta dos registos: o cálculo conserva o desvio máximo pedido para cinco medidas. Se o erro instrumental angular for superior a 0,38°, a estimativa deverá ser revista e a classificação de precisão poderá alterar-se.')
p('Para melhorar esta determinação, deve medir-se o ângulo por sensor angular ou vídeo, verificar o zero e controlar o indicador de máximo. Um maior ângulo de oscilação reduz o peso relativo de uma mesma resolução angular; qualquer mudança na massa do pêndulo ou na posição de carga deve ser documentada e manter condições comparáveis entre os métodos. Também é necessário medir l de acordo com o centro de massa efetivo, e não apenas como comprimento total da haste.')
table(['Método','v₀ / (m/s)','Intervalo não arredondado / (m/s)','Erro relativo'],[
 ['Sensores — Parte A','2,6 ± 0,1','[2,503; 2,773]','5,1 %'],['Pêndulo — Parte C','4,0 ± 0,3','[3,716; 4,359]','8,0 %']], 'Tabela 5 — Comparação das velocidades. Intervalos calculados antes do arredondamento.')
p('A diferença entre as velocidades centrais é 4,03773 − 2,63819 = 1,39954 m/s, aproximadamente 53,0 % de v₀,A. A soma das incertezas é apenas 0,45633 m/s, pelo que os intervalos não se sobrepõem. Ambos os resultados são precisos no critério adotado, mas não são concordantes. Não existe uma velocidade de referência independente que permita atribuir exatidão absoluta a um deles.')
p('A discrepância pode resultar de erros de referência ou calibração nos sensores, de condições de lançamento diferentes entre partes, de erro de zero ou de leitura no indicador e da aproximação do pêndulo real a uma massa pontual. Estas possibilidades não estão demonstradas pelos dados. Um ressalto também violaria a hipótese de captura, mas não pode ser afirmado sem observação experimental.')
p('No pêndulo físico, a análise geral usa a conservação do momento angular em torno do eixo durante o impacto e o momento de inércia do conjunto. O guião usa a aproximação simplificada da equação (6); faltam o momento de inércia e a geometria de impacto para quantificar uma correção ao modelo. Perdas por atrito durante a subida tenderiam a diminuir α e a subestimar a velocidade inferida, pelo que não explicam isoladamente o valor superior da Parte C.')
p('A estimativa diagnóstica da Parte B, próxima de 3,0 m/s, reforça a necessidade de rever as medições e as hipóteses dos dois métodos. A compatibilidade entre os ângulos de máximo da Parte B não elimina as discrepâncias nas velocidades e nos alcances absolutos.')
page()
# 10 conclusions bib
h1('5. Conclusões')
p('O tratamento das cinco medidas de tempo forneceu v₀,A = (2,6 ± 0,1) m/s, com erro relativo de 5,1 %. A dispersão do tempo de passagem é responsável por 88,4 % da incerteza final. O método cumpre o critério de precisão da unidade curricular, embora a sua exatidão não esteja demonstrada.')
p('No estudo angular, o maior alcance médio observado foi 1,154 m para θmáx,obs = (38 ± 1)°, usando a incerteza de amostragem indicada no guião. O valor é compatível com θmáx = 37,2°, calculado com a velocidade da Parte A e H = 0,2600 m. A dispersão dos disparos é, porém, superior às diferenças entre as médias a 30°, 34° e 38°, limitando a localização do máximo. Os alcances absolutos são superiores às previsões com v₀,A, pelo que a concordância angular constitui uma verificação parcial do modelo.')
p('No pêndulo balístico, obtiveram-se ᾱ = (4,9 ± 0,4)°, h = (1,3 ± 0,2) × 10⁻³ m e v₀,C = (4,0 ± 0,3) m/s. O erro relativo de 8,0 % cumpre o critério de precisão, sob as hipóteses de incerteza adotadas. A determinação do ângulo domina a incerteza da velocidade, através da altura de subida.')
p('Os objetivos de medir v₀ por dois métodos e de estudar o alcance foram executados. A concordância quantitativa entre os métodos não foi alcançada: as velocidades diferem cerca de 1,40 m/s, muito acima da soma das incertezas estimadas. Sem uma referência independente, não é possível decidir qual resultado está mais próximo da velocidade verdadeira.')
p('As prioridades de melhoria são verificar a separação efetiva dos feixes e as referências de alcance e de altura; uniformizar a posição de carga; calibrar a leitura angular e o zero do pêndulo; e caracterizar a sua geometria e distribuição de massa. Mais repetições e uma amostragem angular mais densa ajudam a avaliar a dispersão, mas não substituem estas verificações de possíveis efeitos sistemáticos.')
h1('6. Bibliografia e fontes documentais')
p('[1] Universidade de Aveiro, Departamento de Física. Mecânica e Campo Eletromagnético — Trabalho: Movimento de Projéteis. Ano letivo 2026/2027. Guião disponibilizado nas versões MCE_Movimento de projéteis_2026-2027.pdf e MCE_Movimento de projéteis_2026-2027_f.pdf. Procedimento, modelo e estrutura do relatório.')
p('[2] Universidade de Aveiro, Departamento de Física. Instrumentação e análise de dados experimentais. Documento fornecido como Guia-análise experimental.pdf, sem data indicada. Secções 3–5 e apêndices A, C e D. Critérios de precisão, incertezas e apresentação dos resultados.')
p('[3] Registos fornecidos do grupo 3, turma PL6. final_final.xlsx e MCE_PL6_G3_dados.pdf; preparação manuscrita MCE_PL6_G3_PrepT12.pdf; folhas intermédias MCE_PL6_G3.xlsx, MCE_PL6_G3_Altura_026m.xlsx e Tratamento_Dados_Movimento_Projeteis.xlsx. Dados experimentais e comparação das versões.')
p('[4] Relatorio_Movimento_Projeteis.docx e Relatorio_Movimento_Projeteis_Grupo3_PL6.docx. Exemplos disponibilizados para estrutura, identificação dos autores e esquemas.')
p('Referenciam-se os documentos efetivamente consultados. Não se reproduzem as referências bibliográficas de livros já constantes do guião, nem se pressupõe a consulta direta dessas obras.')
page()
# 11 Annex all data and audit maybe fit 2 pages necessary
h1('7. Anexos — Dados experimentais')
h2('Anexo A — Parte A')
p('Distância entre sensores: s = (0,0840 ± 0,0005) m. Os tempos são transcritos com as casas decimais do registo; os desvios são calculados em relação a t̄ = 0,03184 s.')
table(['Ensaio','tᵢ / s','|tᵢ − t̄| / s'],[[str(i+1),fmt(ti,4),fmt(abs(ti-tm),5)] for i,ti in enumerate(t)],'Tabela 6 — Medidas de tempo e desvios absolutos.')
h2('Anexo B — Parte B')
p('Altura: H = 0,2600 m; ΔH = 0,0005 m adotado a partir dos exemplos. Erro de leitura de cada alcance: Δx = 0,0005 m. O guião dispensa a incerteza das médias.')
table(['θ / °','x₁ / m','x₂ / m','x₃ / m','x̄_ob / m'],[[str(int(q))]+[fmt(z,3) for z in row]+[fmt(mean,4)] for q,row,mean in zip(th,x,xm)],'Tabela 7 — Todos os alcances medidos e respetivas médias (um algarismo de guarda nas médias).')
h2('Anexo C — Parte C')
table(['Parâmetro','Valor','Incerteza absoluta'],[['m / kg','0,00964','0,00001'],['M / kg','0,23790','0,00001'],['l / m','0,3480','0,0005']],'Tabela 8 — Massas e comprimento do pêndulo, conforme final_final.xlsx.')
table(['Ensaio','αᵢ / °','|αᵢ − ᾱ| / °'],[[str(i+1),fmt(ai,1),fmt(abs(ai-am),2)] for i,ai in enumerate(al)],'Tabela 9 — Todos os ângulos medidos e desvios em relação a ᾱ = 4,88°.')
page()
h2('Anexo D — Rastreabilidade e verificação dos cálculos')
p('A fonte numérica principal é final_final.xlsx, cujos registos são iguais no diretório do relatório e no diretório G1. A Parte A e a Parte B são também verificáveis em MCE_PL6_G3_dados.pdf; este PDF corresponde a uma exportação repartida da folha de cálculo. Os parâmetros e ângulos da Parte C provêm da folha completa final_final.xlsx e são consistentes com os exemplos.')
p('As versões intermédias têm campos vazios, erros de cálculo e alcances escritos em centímetros ou como texto em colunas rotuladas em metros. A altura 26,3 inserida numa versão inicial também não foi usada: o ficheiro final e os exemplos adotam 0,26 m. Não foram misturados valores de versões diferentes para preencher os dados finais.')
p('Na folha «Parte B - Alcance vs Ângulo» de final_final.xlsx, a célula B16 contém a previsão correta de 37,2219°. Esse valor usa g = 9,81 m/s²; com a convenção uniforme g = 9,80 m/s² deste relatório obtém-se 37,2278°, sem alterar o resultado arredondado. A célula B17 repete o cálculo usando B16 como se fosse uma altura, quando B16 já contém um ângulo; daí resulta 5,5524°, valor dimensionalmente incorreto. O relatório usa a altura de B3 e a velocidade da Parte A, recalculando a equação (4), sem alterar o ficheiro original.')
p('Na Parte C, g = 9,80 m/s² reproduz v₀,C = 4,037727 m/s e Δv₀,C = 0,321312 m/s. Usar 9,81 m/s² altera apenas os algarismos de guarda e não os resultados finais arredondados, mas foi mantida uma única convenção ao longo do relatório.')
p('A incerteza da altura H e a resolução do cronómetro são as indicadas nos exemplos; a resolução angular efetiva do pêndulo não está documentada. Os limites reportados decorrem das incertezas adotadas e da dispersão observada, sem cobertura quantitativa de erros sistemáticos não identificados.')
p('O docente responsável é José Rocha. As experiências das Partes A e B foram realizadas em 16 de outubro de 2026 e a experiência da Parte C em 23 de outubro de 2026. Esta identificação e estas datas foram confirmadas pelos autores.')
h2('Verificação suplementar do ângulo ótimo')
p('Para tornar reproduzível a estimativa de Δθmáx referida na Parte B, definem-se v = v₀,A e Q = √(v² + 2gH). As derivadas da equação (4), com o ângulo em radianos, são:')
eq('∂θmáx/∂v = gH / [Q(v² + gH)].')
eq('∂θmáx/∂H = −gv / [2Q(v² + gH)].')
eq('Δθmáx = (180/π){|∂θmáx/∂v|Δv + |∂θmáx/∂H|ΔH}.')
p('A substituição dos valores dá Δθmáx = '+fmt(dopt,4)+'°, isto é, θmáx = (37,2 ± 0,6)°. Este limite reflete as incertezas propagadas da Parte A e de H, não incorpora a discrepância sistemática revelada pelos alcances medidos.')
# Core metadata
D.core_properties.title='Movimento de projéteis — Relatório final — PL6, Grupo 3'
D.core_properties.author='Diogo Pereira (133428); José Rocha (132425); Victor Morais (125478)'
D.core_properties.subject='Mecânica e Campo Eletromagnético, 2026/2027'
D.core_properties.keywords='projéteis; pêndulo balístico; propagação de erros; PL6; grupo 3'
for st in D.styles:
 if st.type in (1,2):
  st.font.name='Times New Roman'
  rpr=st.element.get_or_add_rPr()
  fonts=rpr.find(qn('w:rFonts'))
  if fonts is not None:
   for attr in list(fonts.attrib):
    if 'Theme' in attr:del fonts.attrib[attr]
D.save(OUT)
print(OUT)
print(json.dumps(res,indent=2))
