# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:17:51 2021

@author: patri
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash_extensions import Download
from dash_extensions.snippets import send_file
from dash.exceptions import PreventUpdate
import pandas as pd
from plotly.subplots import make_subplots
import base64
import plotly.express as px
import dash_auth
import json
from operator import itemgetter

app = dash.Dash()
server = app.server

app.index_string = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <!-- Author: Daniel Silva - Maquina CohnWolfe -->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:title" content="Observatório APLs | Governo do Estado de São Paulo">
    <meta property="og:site_name" content="Observatório APLs | Governo do Estado de São Paulo">
    <meta name="description" content="As informações aqui expostas são preliminares e estão sujeitas à avaliação. As bases estão sendo constantemente avaliadas e harmonizadas para verificação de consistência pela fonte responsável, principalmente em relação à [&hellip;]">
    <meta property="og:description" content="As informações aqui expostas são preliminares e estão sujeitas à avaliação. As bases estão sendo constantemente avaliadas e harmonizadas para verificação de consistência pela fonte responsável, principalmente em relação à [&hellip;]">
    <meta property="og:image:type" content="image/jpg">
    <meta property="og:image:width" content="800"> 
    <meta property="og:image:height" content="600"> 
    <meta property="og:type" content="website">

    <title>Observatório APLs | Governo do Estado de São Paulo</title>
    <link rel="shortcut icon" href="https://www.saopaulo.sp.gov.br/wp-content/themes/saopaulo/favicon.ico">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/assets/bootstrap/css/bootstrap-grid.min.css">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/assets/bootstrap/css/bootstrap-reboot.min.css">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/assets/tether/tether.min.css">
    <link rel="preload" as="style" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/assets/mobirise/css/mbr-additional.css">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/assets/mobirise/css/mbr-additional.css" type="text/css">
    
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/theme-planosp/style-legado.css?v1.38">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/theme-planosp/style-planosp.css?v1.44">

        <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/guia-coronavirus/faq-setores.css?v1.5">
    <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/theme-planosp/faq.css?v1.4">  
        
    
    
        <link rel="stylesheet" href="https://www.saopaulo.sp.gov.br/theme-planosp/faq-dados-abertos.css?v1.29">  
    
    
    <script src="https://www.saopaulo.sp.gov.br/guia-coronavirus/js/jquery-3.3.1.min.js"></script>
    <script src="https://www.saopaulo.sp.gov.br/guia-coronavirus/js/flickity.pkgd.min.js"></script>
    
    <script src="https://www.saopaulo.sp.gov.br/theme-planosp/js/menu.js?v1.9"></script>
    <script src="https://www.saopaulo.sp.gov.br/theme-planosp/js/gerais.js?v1"></script>
    <script type='text/javascript' src='https://www.saopaulo.sp.gov.br/wp-content/plugins/html5-responsive-faq/js/hrf-script.js?ver=5.2.5'></script>

    <script>
      (function(i, s, o, g, r, a, m) {
          i['GoogleAnalyticsObject'] = r;
          i[r] = i[r] || function() {
              (i[r].q = i[r].q || []).push(arguments)
          }, i[r].l = 1 * new Date();
          a = s.createElement(o),
              m = s.getElementsByTagName(o)[0];
          a.async = 1;
          a.src = g;
          m.parentNode.insertBefore(a, m)
      })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

      ga('create', 'UA-7743013-2', 'auto');
      ga('require', 'displayfeatures');
      ga('send', 'pageview');
      setTimeout("ga('send','event','Bouce Adjustment','Page visit 30 seconds or more')", 30000);
    </script>

    <!-- Google Tag Manager MC-->
    <script>
      (function(w, d, s, l, i) {
          w[l] = w[l] || [];
          w[l].push({
              'gtm.start': new Date().getTime(),
              event: 'gtm.js'
          });
          var f = d.getElementsByTagName(s)[0],
              j = d.createElement(s),
              dl = l != 'dataLayer' ? '&l=' + l : '';
          j.async = true;
          j.src =
              'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
          f.parentNode.insertBefore(j, f);
      })(window, document, 'script', 'dataLayer', 'GTM-PCKKH3Q');
    </script>
    <!-- End Google Tag Manager MC-->
    <link rel='stylesheet' id='wpcf-slick-css'  href='https://www.saopaulo.sp.gov.br/wp-content/plugins/wp-carousel-free/public/css/slick.min.css?ver=2.1.9' type='text/css' media='all' />
    <link rel='stylesheet' id='wp-carousel-free-fontawesome-css'  href='https://www.saopaulo.sp.gov.br/wp-content/plugins/wp-carousel-free/public/css/font-awesome.min.css?ver=2.1.9' type='text/css' media='all' />
    <link rel='stylesheet' id='wp-carousel-free-css'  href='https://www.saopaulo.sp.gov.br/wp-content/plugins/wp-carousel-free/public/css/wp-carousel-free-public.min.css?ver=2.1.9' type='text/css' media='all' />
    </head>
    <body>
    <!--Google Tag Manager (noscript) MC-->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PCKKH3Q"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) MC-->
    <section class="govsp-topo"> 
    <link rel="stylesheet" type="text/css" href="https://saopaulo.sp.gov.br/barra-govsp/css/topo-basico-sp.min.css">
    <link rel="stylesheet" type="text/css" href="https://saopaulo.sp.gov.br/barra-govsp/css/contraste.css">  
        <div id="govsp-topbarGlobal" class="blu-e">
                <div id="topbarGlobal">
                    <div id="topbarLink" class="govsp-black">
                    <div class="govsp-portal">
                        <a href="https://www.saopaulo.sp.gov.br/">saopaulo.sp.gov.br</a>
                    </div> 
                </div>
                <nav class="govsp-navbar govsp-navbar-expand-lg">
                        <a class="govsp-link" href="http://www.cidadao.sp.gov.br" target="_blank">Cidad&#227;o SP</a>
                        <a class="govsp-social" href="https://www.facebook.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/facebook.png" alt="Facebook Governo de São Paulo" /></a>
                        <a class="govsp-social" href="https://www.twitter.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/twitter.png" alt="Facebook Governo de São Paulo" /></a>
                        <a class="govsp-social" href="https://www.instagram.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/insta.png" alt="Instagram Governo de São Paulo" /></a>
                        <a class="govsp-social" href="https://www.flickr.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/flickr.png" alt="Flickr Governo de São Paulo" /></a>
                        <a class="govsp-social" href="https://www.youtube.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/youtube.png" alt="Youtube Governo de São Paulo" /></a>
                        <a class="govsp-social" href="https://www.issuu.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/issuu.png" alt="Issuu Governo de São Paulo" /></a>
                        <a class="govsp-social" href="https://www.linkedin.com/company/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/linkedin.png" alt="Linkedin Governo de São Paulo" /></a>
                        <a class="govsp-social"></a>
                        <a class="govsp-acessibilidade" href="javascript:mudaTamanho('body', 1);"><img class="govsp-acessibilidade" src="https://saopaulo.sp.gov.br/barra-govsp/img/big-font.png" alt="Aumentar Fonte"></a>
                        <a class="govsp-acessibilidade" href="javascript:mudaTamanho('body', -1);"><img class="govsp-acessibilidade" src="https://saopaulo.sp.gov.br/barra-govsp/img/small-font.png" alt="Diminuir Fonte"></a>
                        <a class="govsp-acessibilidade" href="#" id="altocontraste" accesskey="3" onclick="window.toggleContrast()" onkeydown="window.toggleContrast()"><img class="govsp-acessibilidade" src="https://saopaulo.sp.gov.br/barra-govsp/img/contrast.png" alt="Contraste" ></a>
                        <a class="govsp-acessibilidade" href="https://www.saopaulo.sp.gov.br/fale-conosco/comunicar-erros/" title="Comunicar Erros" target="_blank"><img class="govsp-acessibilidade" src="https://saopaulo.sp.gov.br/barra-govsp/img/error-report.png" ></a>
                </nav>
            </div>
            <div class="govsp-kebab">
                    <figure></figure>
                    <figure class="govsp-middle"></figure>
                    <p class="govsp-cross"></p>
                    <figure></figure>
                    <ul class="govsp-dropdown" id="govsp-kebab">               
                        <li><a class="govsp-link" href="http://www.cidadao.sp.gov.br" target="_blank">Cidad&#227;o SP</a>
                        <li><a class="govsp-social" href="https://www.facebook.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/facebook.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li><a class="govsp-social" href="https://www.twitter.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/twitter.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li><a class="govsp-social" href="https://www.instagram.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/insta.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li><a class="govsp-social" href="https://www.flickr.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/flickr.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li><a class="govsp-social" href="https://www.youtube.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/youtube.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li><a class="govsp-social" href="https://www.issuu.com/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/issuu.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li><a class="govsp-social" href="https://www.linkedin.com/company/governosp/" target="_blank"><img class="govsp-icon-social" src="https://saopaulo.sp.gov.br/barra-govsp/img/linkedin.png" alt="Facebook Governo de São Paulo" /></a></li>
                        <li></li><p class="govsp-social">/governosp</p></li>
                    </ul> 
            </div>
        </div>
        <script src="https://saopaulo.sp.gov.br/barra-govsp/js/script-topo.js"></script>
        <script src="https://saopaulo.sp.gov.br/barra-govsp/js/script-contrast.js"></script>
        <script src="https://saopaulo.sp.gov.br/barra-govsp/js/script-tamanho-fonte.js"></script>
        <script src="https://saopaulo.sp.gov.br/barra-govsp/js/script-scroll.js"></script>
    </section>



    <section class="topo" id="inicio">
        <h1 class="titulo titulo-novo">
            Observatório de APL<a style="text-transform:lowercase">s</a>
        </h1>

        <div class="barra-logos">
            <figure class="logo">
                <a href="https://www.desenvolvimentoeconomico.sp.gov.br/programas/arranjos-produtivos-locais-apls/"><img src="/assets/logo-fomento.png" alt="Sobre os Arranjos Produtivos Locais" style="width:170%;height:170%"> </a>
            </figure>
        </div>                 
           <!-- <figure class="logo simi">
                <img src="https://www.desenvolvimentoeconomico.sp.gov.br/programas/arranjos-produtivos-locais-apls/" alt="SIMI-SP - Sistema de Monitoramento Inteligente">
            </figure> 
                    </div>-->
    </section>
<section class="setores-subsetores">
    <h2 class=" container titulo-secao-planosp titulo-planosp">
        
    </h2>
{%app_entry%}
{%config%}
{%scripts%}
{%renderer%}
<div class="pre-rodape"></div>
<section id="govsp-rodape">
    <link rel="stylesheet" type="text/css" href="https://saopaulo.sp.gov.br/barra-govsp/css/rodape-sp.css">   
    <div id="govsp-footerGlobal">
                <ul class="govsph-links">
                    <div id="govsp-links-footer">            
                        <li class="govsp-link-rodape"><a class="govsp-links-footer" href="https://www.ouvidoria.sp.gov.br/Portal/Default.aspx" target="_blank">Ouvidoria</a></li>
                        <li class="govsp-link-rodape"><a class="govsp-links-footer" href="http://www.transparencia.sp.gov.br/" target="_blank">Transparência</a></li>
                        <li class="govsp-link-rodape"><a class="govsp-links-footer no-border" href="http://www.sic.sp.gov.br/" target="_blank">SIC</a></li>
                    </div>  
                        <li class="govsp-link-rodape"><img class="govsph-logo-rodape" src="https://saopaulo.sp.gov.br/barra-govsp/img/logo-rodape.png" /></li>
                        <li class="govsp-link-rodape"><img class="govsph-logo-rodape logo-negativo" src="https://saopaulo.sp.gov.br/barra-govsp/img/logo-rodape-negativo.png" /></li>   
                </ul>                 
    </div>
    <div id="govsp-footer-bottom" class="govsp-preto"></div> 
</section>

</body>
<script type='text/javascript' src='https://www.saopaulo.sp.gov.br/wp-content/plugins/wp-carousel-free/public/js/slick.min.js?ver=2.1.9'></script>
<script type='text/javascript' src='https://www.saopaulo.sp.gov.br/wp-content/plugins/wp-carousel-free/public/js/wp-carousel-free-public.min.js?ver=2.1.9'></script>
<script type='text/javascript' src='https://www.saopaulo.sp.gov.br/wp-content/plugins/wp-carousel-free/public/js/preloader.min.js?ver=2.1.9'></script>
</html>

<!--
Performance optimized by W3 Total Cache. Learn more: https://www.boldgrid.com/w3-total-cache/

Page Caching using disk: enhanced 

Served from: www.saopaulo.sp.gov.br @ 2021-04-13 11:33:25 by W3 Total Cache
-->
'''

with open('assets/sp_simple3.geojson', encoding='utf-8') as response:
    mapa = json.load(response)

municipios = pd.read_excel(
    "assets/bases_sde_cdrt.xlsx", sheet_name="Municipios")
# =============================================================================
# mun_apls = pd.read_excel("assets/bases_sde_cdrt.xlsx",
#                           sheet_name="Municipios_APLs")
# =============================================================================

apls = pd.read_excel("assets/bases_sde_cdrt.xlsx", sheet_name="APLs")
# =============================================================================
# apls_cnaes = pd.read_excel(
#     "assets/bases_sde_cdrt.xlsx", sheet_name="APLs_CNAE2.0")
# cnaes = pd.read_excel("assets/bases_sde_cdrt.xlsx", sheet_name="CNAE2.0")
# 
# 
# def f(x): return str(x).replace('-', '').replace('.',
#                                                  '').replace('/', '')  # transformar classe em str normalizada
# 
# 
# cnaes['classe'] = cnaes['classe'].apply(f)
# cnaes['subclasse'] = cnaes['subclasse'].apply(f)
# apls_cnaes['classe'] = apls_cnaes['classe'].apply(f)
# 
# bq = pd.read_csv("assets/rais-bq.csv", dtype={'cnae_2_subclasse': 'str'})
# bq['classe'] = bq['cnae_2_subclasse'].apply(lambda x: x[:-2])
# bq['CD_GEOCMU'] = bq['id_municipio'].apply(lambda x: int(x/10))
# bq['id_munic_6'] = bq['CD_GEOCMU'].copy()
# bq.rename(columns={'cnae_2_subclasse': 'subclasse'}, inplace=True)
# 
# munis_apls_stack = mun_apls.set_index('id_munic_6')
# munis_apls_stack = munis_apls_stack[munis_apls_stack == 1].stack(
# ).reset_index().drop(0, 1)
# munis_apls_stack.rename(columns={'level_1': 'id_apl'}, inplace=True)
# 
# df = pd.merge(munis_apls_stack, apls_cnaes, on='id_apl')
# df = pd.merge(df, apls, on='id_apl')
# df = pd.merge(df, municipios[['id_munic_6', 'município']], on='id_munic_6')
# df['sede'] = [1 if i in j else 0 for i,
#               j in zip(df['município'], df['sede_apl'])]
# df = pd.merge(df, bq[['ano', 'estabs', 'vinculos',
#                       'classe', 'subclasse',
#                       'id_munic_6']], on=['id_munic_6', 'classe'])
# df = pd.merge(df, cnaes[['classe', 'nome_classe']], on='classe', how='left')
# 
# del apls_cnaes, bq, cnaes, munis_apls_stack, mun_apls
# =============================================================================

df = pd.read_csv('assets/data_apls.csv', encoding='latin1')

app.layout = html.Div([html.Button("Download base de APLs", id="btn"), Download(id="download"),
                       html.Div([
    html.Div([html.P("Setor do APL"),
              dcc.Dropdown(id='setor-apl-dropdown',
                           options=sorted([{'label': i, 'value': i} for i in df['setor_apl'].unique()],
                                          key=itemgetter('label')),
                           value='Aeroespacial e Defesa'
                           )
              ],
             style={'width': '48%', 'display': 'inline-block'}),
    html.Div([html.P("Município sede do APL"),
              dcc.Dropdown(id='sede-apl-dropdown')
              ],
             style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
]),
    html.H3(html.Div(id='display-selected-values')),
    dcc.Graph(id="figure-apl"),
    html.H3(html.Center([html.P(id='estabs-apl'), html.P(id='emps-apl')])),
    html.Div([
        html.Div([dcc.Graph(id="table-apl"),
                  ],
                 style={'width': '50%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id="table2-apl"),
                  ],
                 style={'width': '50%', 'float': 'right', 'display': 'inline-block'})
    ]),
    html.Center([
        html.Div([html.P("Município do APL"),
                  dcc.Dropdown(id='municipios-apl-dropdown'  # ,
                               # options=sorted([{'label': i, 'value': i} for i in df[conditions]['município'].unique()],
                               #              key=itemgetter('label')),
                               # value=options['value']
                               )
                  ],
                 style={'width': '30%', 'display': 'inline-block'}),
        dcc.Graph(id='municipios-apl-table')])
])


@app.callback(
    Output('sede-apl-dropdown', 'options'),
    Input('setor-apl-dropdown', 'value'))
def set_sede_apl_options(setor):
    return sorted([{'label': i, 'value': i} for i in df.loc[df['setor_apl'] == setor, 'sede_apl'].unique()],
                  key=itemgetter('label'))


@app.callback(
    Output('sede-apl-dropdown', 'value'),
    Input('sede-apl-dropdown', 'options'))
def set_sede_apl_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('figure-apl', 'figure'),
    Output('table-apl', 'figure'),
    Output('table2-apl', 'figure'),
    Output('estabs-apl', 'children'),
    Output('emps-apl', 'children'),
    Output('municipios-apl-dropdown', 'options'),
    Input('setor-apl-dropdown', 'value'),
    Input('sede-apl-dropdown', 'value'))
def set_display_figure_apl(selected_setor, selected_sede):

    conditions = ((df['setor_apl'] == selected_setor)
                  & (df['sede_apl'] == selected_sede))

    fig = go.Figure()

    fig.add_trace(go.Choropleth(geojson=mapa,
                                featureidkey="properties.CD_GEOCMU",
                                locations=municipios['id_munic_6'],
                                z=[1 for i in municipios['id_munic_6']],
                                text=municipios['município'],
                                hovertemplate='<b>%{text}</b><br>Não faz parte.</br>',
                                colorscale=((0.0, '#636efa'),
                                            (1.0, '#636efa')),
                                showscale=False,
                                marker_line_color='white',
                                marker_line_width=0.5,
                                zmin=0,
                                zmax=1,
                                name="",
                                visible=True))

    temp = df[conditions].groupby('id_munic_6')['vinculos'].sum().reset_index()
    temp = pd.merge(temp, df[conditions].groupby('id_munic_6')['estabs'].sum(),
                    on='id_munic_6', how='left')
    temp = pd.merge(temp, df[conditions].groupby('id_munic_6')['sede'].max(),
                    on='id_munic_6', how='left')
    temp = pd.merge(
        temp, municipios[['id_munic_6', 'município']], on='id_munic_6', how='left')

    def g(x): return "Sim" if x == 1 else "Não"
    fig.add_trace(go.Choropleth(geojson=mapa,
                                featureidkey="properties.CD_GEOCMU",
                                locations=temp['id_munic_6'],
                                z=temp['sede'],
                                text=['<b>'+i+'</b><br>Empregos do APL :'
                                      + "{:,}".format(j)+'<br>Estabs. do APL :'+"{:,}".format(k) +
                                      "<br>Sede do APL: "+g(l)+'</br>'
                                      for i, j, k, l in zip(temp['município'], temp['vinculos'], temp['estabs'], temp['sede'])],
                                hovertemplate='%{text}',
                                colorscale=((0.0, '#fec44f'),
                                            (1.0, '#d95f0e')),
                                showscale=False,
                                marker_line_color='black',
                                marker_line_width=0.5,
                                zmin=0,
                                zmax=1,
                                name="",
                                visible=True))

    corte_apl = apls[(apls['setor_apl'] == selected_setor)
                     & (apls['sede_apl'] == selected_sede)]

    fig.update_layout(
        title={
            'text': u'<b "text-align: center;">{} de {}</b><br>Ano de reconhecimento: {}<br>Nível de maturidade: {}'.format(
                selected_setor,
                selected_sede,
                corte_apl.ano_reconhecimento_apl.values[0],
                corte_apl.maturidade.values[0]
            ),
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},

        annotations=[
            go.layout.Annotation(x=0.5,
                                 y=-0.2,
                                 text=('Nota: empregos e estabalecimentos formais dos setores contemplados<br>Fonte: '
                                       '<a href="http://pdet.mte.gov.br/microdados-rais-e-caged">microdados RAIS 2019</a><br>Elaboração: CDRT/SDE'),
                                 showarrow=False, xref='paper', yref='paper',
                                 xanchor='center',
                                 yanchor='auto',
                                 xshift=0,
                                 yshift=0
                                 )]
    )

    fig.update_geos(fitbounds='locations',
                    visible=False,
                    projection_scale=1)

    temp.sort_values('vinculos', ascending=False, inplace=True)
    table = go.Figure(data=[go.Table(
        header=dict(values=list(['Municípios', 'Empregos', 'Estabelecimentos']),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[temp.município, temp.vinculos, temp.estabs],
                   fill_color='lavender',
                   align=['left', 'center', 'center']))
    ])

    temp2 = df[conditions].groupby('classe')['vinculos'].sum().reset_index()
    temp2 = pd.merge(temp2, df[conditions].groupby('classe')[
                     'estabs'].sum().reset_index(), on='classe', how='left')
    temp2 = pd.merge(temp2, df[conditions].groupby('classe')[
                     'nome_classe'].first().reset_index(), on='classe', how='left')
    temp2.sort_values('vinculos', ascending=False, inplace=True)
    table2 = go.Figure(data=[go.Table(columnwidth=[800, 200],
                                      header=dict(values=list(['Classe', 'Empregos', 'Estabelecimentos']),
                                                  fill_color='paleturquoise',
                                                  align='left'),
                                      cells=dict(values=[temp2['nome_classe'], temp2.vinculos, temp2.estabs],
                                                 fill_color='lavender',
                                                 align=['left', 'center', 'center']))
                             ])

    sum1 = "{:,} estabelecimentos atingidos".format(temp2['estabs'].sum())
    sum2 = "{:,} empregos alcançados".format(temp2['vinculos'].sum())

    dropdown = sorted([{'label': i, 'value': i} for i in df[conditions]['município'].unique()],
                      key=itemgetter('label'))

    return fig, table, table2, sum1, sum2, dropdown

# =============================================================================
# @app.callback(
#     Output('municipios-apl-dropdown', 'value'),
#     Input('municipios-apl-dropdown', 'options'))
# def set_municipio_apl_value(available_options):
#     return available_options[0]['value']
#
# =============================================================================


@app.callback(
    Output('municipios-apl-table', 'figure'),
    Input('municipios-apl-dropdown', 'value'),
    Input('setor-apl-dropdown', 'value'),
    Input('sede-apl-dropdown', 'value'))
def set_municipio_apl_table(option, selected_setor, selected_sede):

    conditions = conditions = (
        (df['setor_apl'] == selected_setor) & (df['sede_apl'] == selected_sede))

    temp = df[conditions]
    temp = temp.loc[temp['município'] == option]
    temp = temp.groupby('classe')['vinculos'].sum().reset_index()
    temp = pd.merge(temp, df[conditions].groupby('classe')[
                    'estabs'].sum().reset_index(), on='classe', how='left')
    temp = pd.merge(temp, df[conditions].groupby('classe')[
                    'nome_classe'].first().reset_index(), on='classe', how='left')
    temp.sort_values('vinculos', ascending=False, inplace=True)
    table = go.Figure(data=[go.Table(columnwidth=[800, 200],
                                     header=dict(values=list(['Classe', 'Empregos', 'Estabelecimentos']),
                                                 fill_color='paleturquoise',
                                                 align='left'),
                                     cells=dict(values=[temp['nome_classe'], temp.vinculos, temp.estabs],
                                                fill_color='lavender',
                                                align=['left', 'center', 'center']))
                            ])

    return table

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return send_file("assets/data_apls.csv")

if __name__ == '__main__':
    print()
    app.run_server(debug=True)
