#!/usr/bin/python3
#-*- coding: utf-8 -*-
import mysql.connector
import hashlib
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()


    def save_contactar_por(self, data_contactar_por, actividad_id):
      try:
        if isinstance(data_contactar_por[0], list):
          for i in range(0, len(data_contactar_por[0])):
            sql_contactar_por ='''
                INSERT INTO contactar_por (nombre, identificador, actividad_id) 
                VALUES (%s, %s, %s)
                '''   
            
            self.cursor.execute(sql_contactar_por, (data_contactar_por[0][i], data_contactar_por[1][i], actividad_id))  # ejecuto la consulta
          
        else:
            sql_contactar_por ='''
                INSERT INTO contactar_por (nombre, identificador, actividad_id) 
                VALUES (%s, %s, %s)
                '''
            self.cursor.execute(sql_contactar_por, (data_contactar_por[0], data_contactar_por[1], actividad_id))  # ejecuto la consulta
            
      except:
        print("ERROR AL GUARDAR EL CONTACTO EN LA BASE DE DATOS")
        print("")
        sys.exit()


    def save_tema(self, data_tema):
      try:
        if (data_tema[0] == 'Otro'):
              sql_tema = '''
                INSERT INTO tema (nombre)
                VALUES (%s)
              '''
              self.cursor.execute(sql_tema, (data_tema[1],))

              sql_tema = '''
                  SELECT id FROM tema
                  WHERE nombre = (%s)
                '''
              self.cursor.execute(sql_tema,  (data_tema[1],))
              
              return self.cursor.fetchall()[0][0]
        else:
              sql_tema = '''
                INSERT INTO tema (nombre)
                VALUES (%s)
              '''
              self.cursor.execute(sql_tema,  (data_tema,))

              sql_tema = '''
                  SELECT id FROM tema
                  WHERE nombre = (%s)
                '''
              self.cursor.execute(sql_tema,  (data_tema,))
              
              return self.cursor.fetchall()[0][0]
      except:
        print("ERROR AL GUARDAR TEMA EN LA BASE DE DATOS")
        print("")
        sys.exit()


    def save_comuna(self, data_comuna):
      try:
        sql_comuna = '''
               SELECT id FROM comuna
               WHERE nombre = (%s)
            '''
        self.cursor.execute(sql_comuna, (data_comuna,))
        return self.cursor.fetchall()[0][0] # recupera el último id ingresado
      except:
        print("ERROR AL GUARDAR COMUNA EN LA BASE DE DATOS")
        print("")
        sys.exit()

    def save_foto(self, data_foto, actividad_id):
      # Procesar archivo
      fileobj = data_foto  # Lista de fotos??
      try:
        sql = "SELECT COUNT(id) FROM actividad" # Cuenta los archivos que hay en la base de datos
        self.cursor.execute(sql)
            
        total = self.cursor.fetchall()[0][0] + 1
  
        if isinstance(fileobj, list):
          for i in range(0,len(fileobj)):
            filename = fileobj[i].filename

            filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
            filename_hash += f"_{total}" # concatena la función de hash con el número total de archivos, nombre único
            # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en paralelo.
            #       Lo que se conoce como un datarace
            
            open(f"media/{filename_hash}", "wb").write(fileobj[i].file.read()) # guarda el archivo localmente
            
            sql_file = '''
                INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) 
                VALUES (%s, %s, %s)
                '''
            self.cursor.execute(sql_file, (filename_hash, filename, actividad_id))  # ejecuta la query que guarda el archivo en base de datos
        else:
          filename = fileobj.filename

          filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
          filename_hash += f"_{total}" # concatena la función de hash con el número total de archivos, nombre único
          # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en paralelo.
          #       Lo que se conoce como un datarace

          open(f"media/{filename_hash}", "wb").write(fileobj.file.read()) # guarda el archivo localmente
          sql_file = '''
                INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) 
                VALUES (%s, %s, %s)
                '''
          self.cursor.execute(sql_file, (filename_hash, filename, actividad_id))  # ejecuta la query que guarda el archivo en base de datos
            
      except:
        print("ERROR AL LAS GUARDAR FOTOGRAFIAS EN LA BASE DE DATOS")
        print("")
        sys.exit()


    def save_actividad_data(self, data_actividad, data_foto, data_contactar_por, data_tema, data_comuna):
        
        try:
            comuna_id = self.save_comuna(data_comuna)
      
            tema_id = self.save_tema(data_tema) #usamos la funcion para sacar el id de tema
      
            sql_actividad ='''
                INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
            
            new_tupla = (comuna_id,)+data_actividad+(tema_id,)

            self.cursor.execute(sql_actividad, new_tupla)  # ejecuto la consulta
            actividad_id = self.cursor.lastrowid
            
            self.save_contactar_por(data_contactar_por, actividad_id)
            self.save_foto(data_foto, actividad_id)
            self.db.commit()                # modifico la base de datos
        except:
            print("ERROR AL GUARDAR")
            sys.exit()


    #para portada
    def get_data_actividad(self):
        sql = '''
           SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE 
           WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id 
           ORDER BY AC.id DESC 
           LIMIT 5
           '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #para listado de actividades
    def get_data_actividad_offset(self, offset):
        sql = f"""
           SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE 
           WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id 
           ORDER BY AC.id DESC 
           LIMIT 5 OFFSET {offset}
           """
        
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #para portada
    def get_data_foto(self):

        sql = f'''
            SELECT F.id, F.ruta_archivo, F.nombre_archivo, F.actividad_id FROM foto F, actividad AC
            WHERE F.actividad_id=AC.id AND F.id=AC.id
            ORDER BY AC.id DESC
            LIMIT 5
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #para listado de actividades
    def get_data_foto_listado(self, id):
        
        sql = f"""
            SELECT DISTINCT F.id, F.ruta_archivo, F.nombre_archivo, F.actividad_id FROM foto F, actividad AC
            WHERE F.actividad_id={id}
            ORDER BY AC.id DESC
            """
        
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    #para listado de actividades
    def get_total_fotos_offset(self, offset): #ARREGLAR ESTO
        sql = f"""
            SELECT actividad_id, COUNT(*) FROM foto
            GROUP BY actividad_id
            ORDER BY actividad_id DESC
            LIMIT 5 OFFSET {offset}
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #para listado de actividades
    def get_contactar_por(self, id):

      sql = f'''
            SELECT DISTINCT C.nombre, C.identificador, C.actividad_id FROM contactar_por C, actividad AC
            WHERE C.actividad_id={id}
            ORDER BY C.id DESC
            '''
      self.cursor.execute(sql)
      return self.cursor.fetchall()
    
    def get_pagination(self):
      sql = "SELECT COUNT(id) FROM actividad" # Cuenta los archivos que hay en la base de datos
      self.cursor.execute(sql)
      count = self.cursor.fetchall()[0][0] + 1
      if (count%5 != 0):
        return (count//5 + 1)
      else:
        return  int(count/5)
    
    def get_grafico1(self):
      sql = '''
            SELECT DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d'), COUNT(*) FROM actividad
            GROUP BY DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d')
            '''
      self.cursor.execute(sql)
      return self.cursor.fetchall()

    def get_grafico2(self):
      sql = '''
            SELECT T.nombre, COUNT(AC.tema_id) FROM tema T, actividad AC
            WHERE AC.tema_id = T.id
            GROUP BY T.nombre
            '''
      self.cursor.execute(sql)
      return self.cursor.fetchall()
    
    def get_grafico3_manana(self):
      sql = '''
            SELECT DATE_FORMAT(dia_hora_inicio, '%c'), COUNT(*) FROM actividad
            WHERE DATE_FORMAT(dia_hora_inicio, '%H:%i') < "11:00"
            GROUP BY DATE_FORMAT(dia_hora_inicio, '%H:%i')
            '''
      self.cursor.execute(sql)
      return self.cursor.fetchall()
    
    def get_grafico3_mediodia(self):
      sql = '''
            SELECT DATE_FORMAT(dia_hora_inicio, '%c'), COUNT(*) FROM actividad
            WHERE DATE_FORMAT(dia_hora_inicio, '%H:%i') >= "11:00" AND DATE_FORMAT(dia_hora_inicio, '%H:%i') < "14:59"
            GROUP BY DATE_FORMAT(dia_hora_inicio, '%H:%i')
            '''
      self.cursor.execute(sql)
      return self.cursor.fetchall()

    def get_grafico3_tarde(self):
      sql = '''
            SELECT DATE_FORMAT(dia_hora_inicio, '%c'), COUNT(*) FROM actividad
            WHERE DATE_FORMAT(dia_hora_inicio, '%H:%i') >= "15:00"
            GROUP BY DATE_FORMAT(dia_hora_inicio, '%H:%i')
            '''
      self.cursor.execute(sql)
      return self.cursor.fetchall()
