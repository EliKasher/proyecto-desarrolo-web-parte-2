#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import cgi 
import json

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'cc500226_db')

estadistica =  """ 
    <div class="jumbotron text-center">
      <h1>Estadísticas</h1><br>
      <div class="btn-group" role="group" aria-label="">

        <h2>Gráfico 1</h2>
        <div id="contenedor-1" style="min width: 310px; height= 400px; margin= 0 auto">
        </div>

        <div class="spacer">
        </div>

        <h2>Gráfico 2</h2>
        <div id="contenedor-2" style="min width: 310px; height= 400px; margin= 0 auto">
        </div>

        <div class="spacer">
        </div>

        <h2>Gráfico 3</h2>
        <div id="contenedor-3" style="min width: 310px; height= 400px; margin= 0 auto">
        </div>
      </div>
      <input type="button" name="boton" id="portada" value="Portada" onclick="location.href ='https://anakena.dcc.uchile.cl/~eavila/Tarea/cgi-bin/portada.py'">
    </div>
    <script type="text/javascript" src="/js/grafico1.js"></script>
    <script type="text/javascript" src="/js/grafico2.js"></script>
    <script type="text/javascript" src="/js/grafico3.js"></script>
    <script type="text/javascript" src="/cgi-bin/grafico1.py"></script>
    <script type="text/javascript" src="/cgi-bin/grafico2.py"></script>
    <script type="text/javascript" src="/cgi-bin/grafico3.py"></script>    
    """

with open('templates/Estadisticas.html','r',encoding='utf-8') as estadisticas:
    file = estadisticas.read()
    print(file.format('Estadisticas', estadistica))