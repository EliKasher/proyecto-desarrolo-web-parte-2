#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import cgitb;
import cgi 

from db import DB
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'cc500226_db')


with open('templates/Informar_Actividad.html','r',encoding='utf-8') as informar:
        file = informar.read()
        print(file.format('Informar Actividad', """
            <div class="jumbotron text-center">
        <h1>Nueva Actividad</h1>
    </div>

    <div class="container">
        <form name="formulario" id="formulario" action="save_data.py" onsubmit="return validate()" method="post" enctype="multipart/form-data">
          <fieldset>
            <legend>¿Dónde?</legend>
            <label for="region" class="form-label">Región*</label> <br>
            <select name="region" id="region" class="form-control" required>
              <option value="">--</option>
            </select> <br>
            <label for="comuna" class="form-label">Comuna*</label> <br>
            <select name="comuna" id="comuna" class="form-control" required>
              <option value="">--</option>
            </select> <br>
            <label for="sector" class="form-label">Sector</label> <br>
            <input type="text" name="sector" id="sector" class="form-control" size="100" maxlength="100" placeholder="Beauchef 851...">
          </fieldset> <br>
          <fieldset>
            <legend>¿Quién Organiza?</legend>
            <label for="nombre" class="form-label">Nombre*</label><br>
            <input type="text" name="nombre" id="nombre" class="form-control" size="100" maxlength="200" placeholder="Ana Campos" required><br>
            <label for="email" class="form-label">email*</label><br>
            <input type="text" name="email" id="email" class="form-control" size="100" placeholder="nombreusuario@email.com" required><br>
            <label for="celular" class="form-label">Número de Celular</label><br>
            <input type="text" class="form-control" name="celular" id="celular" size="15"><br>
            <label for="contactar-por" class="form-label">Contactar por:</label><br>
            <input type="checkbox" name="contactar-por" id="whatsapp" value="whatsapp" onclick="agregarWhatsapp()" /> Whatsapp <br>
            <input type="checkbox" name="contactar-por" id="telegram" value="telegram" onclick="agregarTelegram()" /> Telegram <br>
            <input type="checkbox" name="contactar-por" id="twitter" value="twitter" onclick="agregarTwitter()" /> Twitter <br>
            <input type="checkbox" name="contactar-por" id="instagram" value="instagram" onclick="agregarInstagram()" /> Instagram <br>
            <input type="checkbox" name="contactar-por" id="facebook" value="facebook" onclick="agregarFacebook()" /> Facebook <br>
            <input type="checkbox" name="contactar-por" id="tiktok" value="tiktok" onclick="agregarTiktok()" /> Tiktok <br>
            <input type="checkbox" name="contactar-por" id="otra" value="otra" onclick="agregarOtra()" /> Otra
            <div id="contenedorObjetos" class="contenedor"></div>
          </fieldset>
          <fieldset>
            <legend>¿Cuándo y de qué se trata?</legend>
            <label for="dia-hora-inicio" class="form-label" >Día Hora Inicio*</label><br>
            <input type="text" name="dia-hora-inicio" id="dia-hora-inicio" value="" onload="return fechaInicio()" required><br>
            <label for="dia-hora-termino" class="form-label">Día Hora Término</label><br>
            <input type="text" name="dia-hora-termino" id="dia-hora-termino" value="" onload="return fechaTermino()"><br>
            <label for="descripcion-evento" class="form-label">Descripción</label><br>
            <textarea class="form-control" name="descripcion-evento" id="descripcion-evento" rows="10" cols="50"></textarea><br>
            <label for="tema" class="form-label">Tema</label><br>
            <select name="tema" id="tema" class="form-control" onchange="agregarOtroTema()" required>
              <option value="0" selected>Seleccione tema*</option>
              <option value="Musica">Música</option>
              <option value="Deporte">Deporte</option>
              <option value="Ciencias">Ciencias</option>
              <option value="Religion">Religión</option>
              <option value="Politica">Política</option>
              <option value="Tecnologia">Tecnología</option>
              <option value="Juegos">Juegos</option>
              <option value="Baile">Baile</option>
              <option value="Comida">Comida</option>
              <div id="contenedorOpciones" onsubmit=tema_nuevo()>
              </div>
              <option value="Otro">Otro</option>
            </select>
            <div id="contenedorObjetos2"></div> <br>
            <label for="foto-actividad">Foto 1*</label> <br>
            <input type="file" name="foto-actividad" id="foto-actividad" class="form-foto" accept="image/png, image/jpg, image/webp, image/jpeg" required>
            <button  name="boton-foto" id="boton-foto" type="button" onclick="agregarFoto()">Agregar Foto</button>
            <div id="contenedorObjetos3"></div>
          </fieldset>
          <br>
          <input name="send" id="send" type="submit" class="btn btn-primary mandarForm" value="Agregar esta actividad"><br><br>
        </form>
        <div id="contenedorErrores" class="contenedor"></div>
        <div id="capa">
          <div>
            <div id="titulo" class="title">Agregar Actividad</div><br>
            <div class="text">¿Está seguro que desea agregar esta actividad?</div>
            <div class="buttons">
              <input type="button" class="button" value="Sí, estoy segur@" name="ok" id="ok">&nbsp;
              <input type="button" class="button" value="No, no estoy segur@" name="ko" id="ko"><br>
            </div>
          </div>
          <script src="/js/mensaje.js"></script>
          <script src="/js/tema_nuevo.js"></script>
          <script src="/js/quita_otro.js"></script>
        </div>
      </div>
      <script>
        fechaInicio();
        fechaTermino();
        </script>
        """))