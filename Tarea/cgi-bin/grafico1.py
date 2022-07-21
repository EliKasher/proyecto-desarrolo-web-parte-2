#!/usr/bin/python3
#-*- coding: utf-8 -*-

print("Content-type:  application/json")
print("")

import json
import cgi

from db import DB

db = DB('localhost', 'root', '', 'cc500226_db')

data_grafico1 = db.get_grafico1()

print(json.dumps(data_grafico1))
