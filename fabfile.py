from __future__ import print_function
from fabric.api import *
from utilities import new_post as __new_post
import fabric.contrib.project as project
import os
import datetime

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'pperez@alumnos.informatica.utem.cl:22'
dest_path = '~/public_html'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def new_post(title = None, date = None):
    if title is None: # El titulo es obligatorio po!
        print('Ingrese titulo del post')
        title = raw_input('>>> ')
    if date is None: # No paso una fecha, utilizar la fecha por defecto
        __new_post(title)
    else: # Paso una fecha, que la funcion se encargue de checkearla
        __new_post(title, date)

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
