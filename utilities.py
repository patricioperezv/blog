#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import dateutil.parser
import datetime
import os
from slugify import slugify

def new_post(titulo, fecha = None):
    if fecha is None:
        fecha = datetime.datetime.now() # Fecha/tiempo actual
    else:
        fecha = dateutil.parser.parse(fecha) # Trata de parsear la fecha, probablemente deba capturar la excepcion
    template = '''title: {titulo}\ndate: {fecha}\ncategory: misc'''
    
    slug = slugify(titulo) # Hacemos un slug, reemplaza espacios, caracteres extraños y demases
    stamp_fichero = fecha.strftime('%Y-%m-%d') # año/mes/dia
    stamp_md = fecha.strftime('%Y-%m-%d %H:%M:%S') # año/mes/dia hora:minuto:segundo
    
    fichero = '{fecha}-{titulo}.{ext}'.format(fecha = stamp_fichero, titulo = slug, ext = 'md')
    fichero = os.path.join(os.getcwd(), 'content', fichero)
    print(fichero)
    
    if os.path.exists(fichero):
        print('El fichero', fichero, 'ya existe! intentelo de nuevo!')
    else:
        with open(fichero, 'w') as f:
            f.write(template.format(titulo = titulo, fecha = stamp_md))
        print('Se creo el nuevo post', fichero)
        ed = os.getenv('EDITOR') if os.getenv('EDITOR') else 'mate'
        os.system('{editor} {fichero}'.format(editor = ed, fichero = fichero))