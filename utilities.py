#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import datetime
import os
from slugify import slugify

now = datetime.datetime.now() # Fecha/tiempo actual

def new_post(titulo, fecha = now):
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
        os.system('mate ' + fichero)

new_post('Prueba blog')