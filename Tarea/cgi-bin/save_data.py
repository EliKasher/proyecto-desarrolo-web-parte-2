#!/usr/bin/python3
#-*- coding: utf-8 -*-
from asyncio.windows_events import NULL
import cgi
import os
import sys
import filetype
import re
from db import DB
import html
import itertools

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'cc500226_db')

form = cgi.FieldStorage()

fileobj = form['foto-actividad']
#obteniendo las fotos
MAX_FILE_SIZE= 600000

#validando la o las fotos
if isinstance(fileobj, list):
  cant = len(fileobj)

  for i in range(0,cant):
    file = fileobj[i]
    if file.filename:
      tipo = file.type
      size = os.fstat(file.file.fileno()).st_size
      if tipo not in ('image/png','image/jpg','image/webp','image/jpeg'):
        print('Error, formato no válido {}'.format(tipo))
        sys.exit()
      if size > MAX_FILE_SIZE:
        print('Error, archivo muy grande.')
        sys.exit()
    else:
      print("Error, archivo no subido.")
else:
  if fileobj.filename:
    tipo = fileobj.type
    size = os.fstat(fileobj.file.fileno()).st_size
    if tipo not in ('image/png','image/jpg','image/webp','image/jpeg'):
        print('Error, formato no válido {}'.format(tipo))
        sys.exit()
    if size > MAX_FILE_SIZE:
        print('Error, archivo muy grande.')
        sys.exit()
  else:
    print("Error, archivo no subido.")


#guardando las fotos en una variable
data_foto = (fileobj)

if (form['tema'].value != None):
  #recopilando los valores de tema
  tema = html.escape(form['tema'].value)
else:
  tema = '0'

if (form['tema'] == "Otro"):
  otroTema = html.escape(form['otroTema'])
else:
  otroTema = ''

#funcion para validar otros temas
def validateOtro(tema):
  if((len(tema)<3) or (len(tema)>15)):
    print('Tema no valido')

#validacion de tema
if tema == '0':
  print('No selecciono un tema')

#validacion de otro tema y guardado de la data en variable
if (tema == 'Otro'):
  validateOtro(otroTema)
  data_tema = (tema, otroTema)
else:
    data_tema = (tema)

if (form['comuna'].value != None):
  #recopilando la comuna
  comuna = html.escape(form['comuna'].value)
else:
  comuna = 'sin-comuna'

#validando la comuna
if comuna == ('sin-comuna' or 'sin-region'):
  print('No selecciono una comuna')

#guardado de la comuna
data_comuna = (comuna)

#recopilando informacion de la actividad
if (form['sector'] != None):
  sector = html.escape(form['sector'].value)
else:
  sector = ''

if (form['nombre'] != None):
  nombre = html.escape(form['nombre'].value)
else:
  nombre = ''

if (form['email'] != None):
  email = html.escape(form['email'].value)
else:
  email = ''

if (form['celular'] != None):
  celular = html.escape(form['celular'].value)
else:
  celular = ''

if (form['dia-hora-inicio'] != None):
  dia_hora_inicio = html.escape(form['dia-hora-inicio'].value)
else:
  dia_hora_inicio = ''

if (form['dia-hora-termino'] != None):
  dia_hora_termino = html.escape(form['dia-hora-termino'].value) 
else:
  dia_hora_termino = ''

if (form['descripcion-evento'] != None):
  descripcion = html.escape(form['descripcion-evento'].value)
else:
  descripcion = ''

#validando la informacion de la actividad
if (len(sector)>100):
  print('El input del sector es demasiado largo') 

if (len(nombre)>200 or len(nombre)==0):
  print('El nombre es invalido')

emailRegEx = '/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i' 
if (email == '' or re.search(emailRegEx, email) == False):
  print('Debe poner un email valido')

cellRegEx = '/([+56][ ][2-9])[ ](\d{4})(\d{4})/g'
if(celular != ''):
  if (re.search(cellRegEx, celular) == False):
    print('Debe colocar un celular valido')

dateRegEx = '/[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/';
if(re.search(dateRegEx, dia_hora_inicio)):
  print('La fecha no es valida')

dateRegEx = '/[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/';
if(dia_hora_termino != '' and re.search(dateRegEx, dia_hora_termino)):
  print('La fecha no es valida')

#guardando la informacion de la actividad
data_actividad = (sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion)

#funcion para validar contactos
def validateContact(contacto):
  if(((len(contacto)) < 4) or ((len(contacto)) > 50)):
    print('El contacto es invalido')

if (form['contactar-por'] != None):
  contactar_por = form.getvalue('contactar-por')
else:
  contactar_por = ''

#validando contactar-por y contactos
if (form['contactar-por'] != None):
  contactar_por = form.getvalue('contactar-por')
  if isinstance(contactar_por, list):
    contacts = len(contactar_por)
    if(form.getvalue('contacto') != None):
      for i in range(0,contacts):
        contacto = html.escape(form.getvalue('contacto')[i])
        validateContact(contacto)   
      contacto = form.getvalue('contacto')
    else:
      contacto = ''
      validateContact(contacto)
  else:
    contactar_por = form['contactar-por'].value
    if (form['contacto'] != None):
      contacto = html.escape(form['contacto'].value)
    else:
      contacto = ''
    validateContact(contacto)

data_contactar_por = (contactar_por, contacto)
  
#enviando la data
db.save_actividad_data(data_actividad, data_foto, data_contactar_por, data_tema, data_comuna)

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
        print(file.format('Portada', 
        f""" 
        <div class="jumbotron text-center">
          <div id="confirmado">
            <fieldset>
            <legend>Éxito</legend>
              <input type="button" name="boton" id="cerrar-mensaje" class="cerrar" value="Cerrar">
              <h4 id="exito" onclick="exito()">Hemos recibido su información, muchas gracias y suerte en su actividad</h4> <br>
            </fieldset>
          </div>
          <script src="/js/exito.js"></script>
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