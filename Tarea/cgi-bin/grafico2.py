#!/usr/bin/python3
#-*- coding: utf-8 -*-

print("Content-type:  application/json")
print("")

import json
import cgi

from db import DB

db = DB('localhost', 'root', '', 'cc500226_db')

data_grafico2 = db.get_grafico2()

print(json.dumps(data_grafico2))