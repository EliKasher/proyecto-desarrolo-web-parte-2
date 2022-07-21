#!/usr/bin/python3
#-*- coding: utf-8 -*-
from dataclasses import dataclass
from operator import ge
from pickle import GET
import sys
import cgi
import html
import itertools

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'cc500226_db')

parametros = cgi.FieldStorage()

data_pagination = db.get_pagination()

if(parametros.getvalue('pag') == None):
  pag_actual = 1
else:
  pag_actual = int(parametros.getvalue('pag')) + 1

pagination = """
             """

for i in range(0,data_pagination):
  pagina = i+1
  clase = ''
  if(pagina == pag_actual):
    clase = 'active'
  
  anterior = pagina-1
  if(pagina == 1):
    anterior = pagina
  
  siguiente = pagina+1
  if(pagina == data_pagination):
    siguiente == data_pagination

  pagination += f""" 
              <div class="pagination">
                <a href="?pag={anterior}">&laquo;</a>
                <a class="{clase}" href="?pag="{pagina}">{pagina}</a>
                <a href="?pag={siguiente}">&raquo;</a>
              </div>
              """
        
if (pag_actual == 1):
  offset = 0
else:
  offset = (pag_actual)*5


data_actividad = db.get_data_actividad_offset(offset)
data_total_fotos = db.get_total_fotos_offset(offset)


tabla ="""
        <div class="container">
        <table class="table">
        <thead>
        <tr>
        <th scope="col">Inicio</th>
        <th scope="col">Término</th>
        <th scope="col">Comuna</th>
        <th scope="col">Sector</th>
        <th scope="col">Tema</th>
        <th scope="col">Nombre Organizador</th>
        <th scope="col">Total Fotos</th>
        <th scope="col">Detalles</th>
        </tr>
        </thead>
        <tbody>
        """

capa = 1
cerrar = 1
portada = 1
im = 1
c = 1
subcapa = 1
si = 1
detalles = 1

if (data_actividad != None and data_total_fotos != None):
  for (p,q) in itertools.zip_longest(data_actividad, data_total_fotos):
    tabla+=f""" 
          <tr>
        <td>{p[6]}</td>
        <td>{p[7]}</td>
        <td>{p[1]}</td>
        <td>{p[2]}</td>
        <td>{p[3]}</td>
        <td>{p[9]}</td>
        <td>{q[1]}</td>
        <td><button data-modal="capa{detalles}" name="boton" class="detalles" id="detalles{detalles}">+</button></td>
        </tr>
        """
    detalles += 1
   
tabla+="""
      </tbody>
      </table>
      </div> """


modalview = """

            """

if (data_actividad != None):
  for p in data_actividad:
    modalview+= f"""
      <div id="capa{capa}" class="capa">
        <div>
          <div class="buttons">
            <input type="button" name="boton" id="cerrar{cerrar}" class="cerrar" value="Cerrar">
            <input type="button" name="boton" id="portada{portada}" class="portada" value="Portada" onclick="location.href ='https://anakena.dcc.uchile.cl/~eavila/templates/Portada.html'">
          </div><br>
          <div class="titulo">Detalles</div><br>
            <div class="text">¿Dónde?<p> """
    
    capa = capa+1
    cerrar = cerrar+1
    portada = portada+1

    modalview+= f"""
              El evento se realizará en: <br> 
              Sector: {p[2]} <br>
              Comuna: {p[1]} </p>
            </div>
            <div class="text">¿Quién Organiza?<p>
              El organizador es:<br>
              {p[3]} <br>
              Email: {p[4]} <br>
              Celular: {p[5]} <br>
              Contactar por: <br>
              
      """

    data_contactar_por = db.get_contactar_por(p[0])

    if(data_contactar_por != None):
      for r in data_contactar_por:
        modalview+= f"""
              &bull; {r[0]} {r[1]} <br>
        """
    
    modalview+= f"""
            </div>
            <div class="text">¿Cuándo y de qué se trata?<p>
              Ven el día: {p[6]}<br>
              Dura hasta: {p[7]}<br>
              Descripción: {p[8]}<br>
              Tema: {p[9]} <br>
              Fotos: </p>
              <div class="evento" class="modal-container">
                  
      """

    data_foto = db.get_data_foto_listado(p[0])

    if(data_foto != None):
      for s in data_foto:
        modalview+=f"""
                <img id="i{im}" class="i" src="/media/{s[1]}" alt="Imagen" data-modal-2="subcapa{subcapa}">
                <div id="subcapa{subcapa}" class="subcapa">
                  <div>
                      <div class="buttons">
                          <input id="c{c}" class="c" type="button" name="boton" value="Cerrar">
                          <img id="si{si}" class="si" src="/media/{s[1]}" alt="Imagen">
                      </div><br>
                  </div>
              </div>
            </div>
          </div>
        
        """
        im = im+1
        subcapa = subcapa+1
        c = c+1
        si = si+1

    modalview+= """
      </div>
        <script src="/js/zoom.js"></script>
        <script src="/js/cambiaTamano1.js"></script>
        <script src="/js/send.js"></script>
      </div>
      <br>
   """

with open(f'templates/Listado_de_Actividades.html','r',encoding='utf-8') as listado:
    file = listado.read()
    print(file.format('Listado de Actividades', """<div class="jumbotron text-center">
        <h1>Listado de Actividades</h1> """, tabla, modalview, pagination))
