#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import itertools

from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'cc500226_db')

data_actividad = db.get_data_actividad()
data_foto = db.get_data_foto()
tabla = """
            <div class="container ">
            <table class="table">
        <thead>
        <tr>
        <th scope="col">Inicio</th>
        <th scope="col">Término</th>
        <th scope="col">Comuna</th>
        <th scope="col">Sector</th>
        <th scope="col">Tema</th>
        <th scope="col">Foto</th>
        </tr>
        </thead>
        <tbody>
        """
        
if (data_actividad!= None and data_foto != None):
    for (p,q) in itertools.zip_longest(data_actividad, data_foto):
      tabla+=f""" 
          <tr>
        <td>{p[6]}</td>
        <td>{p[7]}</td>
        <td>{p[1]}</td>
        <td>{p[2]}</td>
        <td>{p[9]}</td>
        <td><img class="i" width="70%" height="70%" src="/media/{q[1]}" alt="Imagen"> </td>
        </tr>
        """

tabla+="""
    </tbody>
    </table>
    </div> """


with open('templates/Portada.html','r', encoding='utf-8') as portada:
    file = portada.read()
    print(file.format('Portada', f"""<div class="jumbotron text-center">
        <h1>Portada</h1>
        <p>Bienvenid@s al portal de actividades de la fcfm</p> 
      </div>

      <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
          <a class="nav-link" target="_blank" href="https://anakena.dcc.uchile.cl/~eavila/cgi-bin/informar_actividad.py">Agregar Actividad</a>
          <a class="nav-link" target="_blank" href="https://anakena.dcc.uchile.cl/~eavila/cgi-bin/listado_de_actividades.py">Ver Listado de Actividades</a>
          <a class="nav-link" target="_blank" href="https://anakena.dcc.uchile.cl/~eavila/cgi-bin/estadisticas.py">Estadisticas</a>  
        </div>
      </nav>
      <br>
      """, tabla))
