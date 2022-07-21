#!/usr/bin/python3
#-*- coding: utf-8 -*-

print("Content-type:  application/json")
print("")

import json
import cgi

from db import DB

db = DB('localhost', 'root', '', 'cc500226_db')

grafico3 = list()

data_grafico3_manana = db.get_grafico3_manana()
data_grafico3_mediodia = db.get_grafico3_mediodia()
data_grafico3_tarde = db.get_grafico3_tarde()


grafico3.append(data_grafico3_manana)
grafico3.append(data_grafico3_mediodia)
grafico3.append(data_grafico3_tarde)


tuple(grafico3)
print(json.dumps(grafico3))