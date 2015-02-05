title: Virtualenvs en python
date: 2013-10-26 20:20:38
category: Python
---

<center>{% asset_img virtualenv.gif 'Virtualenv' %}</center>

Una de las cosas que nunca use de [rvm](http://rvm.io/ "Ruby Version Manager") (**R**uby **V**ersion **M**anager) fueron los gemset, estos sirven para separar los entornos de trabajo de nuestros proyectos desde el lado de los paquetes (gemas) instalados.

La idea la encontré bien chora, y fue genial cachar que en python existía esto tambien, pero se llamaban [virtualenvs](http://www.virtualenv.org), la diferencia es que post que veía de python, hablaba de los condenados virtualenvs: _Era hora de ver de que coña trataban_.

La receta del chef de hoy dice como instalar virtualenvwrapper (Un wrapper del virtualenv original) y un par de comandos.


### Manos a la obra ###

Un requerimiento previo es la instalación de [pip](http://www.pip-installer.org/) (El manejador de paquetes de python que la lleva) y [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org), estos deben ir a nivel de sistema para permitir que nuestros usuarios jueguen tranquilos con sus nuevos entornos.

##### Instalar setuptools:
Pip requiere setuptools para andar, lo instalaremos:

```bash
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
sudo python ez_setup.py
rm ez_setup.py
```

##### Instalar pip:
Ya podemos instalar pip:

```bash
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
rm get-pip.py
```

#####Instalar virtualenvwrapper y cargarlo con nuestra shell
Ahora tenemos disponible el administrador de paquetes pip! Podemos instalar paquetes a nivel de sistema con sudo pip install paquete, estos paquetes los saca desde [Pypi](https://pypi.python.org/ "Python Package Index"), es necesario usar sudo debido a los permisos del directorio donde se instalan los paquetes (ej: _/usr/local/lib/python2.7/dist-packages/_)

Procedemos a instalar virtualenvwrapper a nivel de sistema:

```bash
sudo pip install virtualenvwrapper
```

Y debemos cargarlo para nuestra shell (Un lugar ideal sería en _.bashrc_ para bash o _.zshrc_ para zsh, incluso en _.profile_ si lo estan cargando), agregamos las siguientes lineas:

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

La primera linea especifica donde viviran nuestros entornos virtuales (Aqui se instalan los paquetes, hay una version de python especifica, tambien una de pip, todo lo que instalemos en el entorno quedara aquí).
La segunda especifica donde vivirán nuestros proyectos, es decir el código de estos.
Finalmente la tercera dice que se cargue virtualenvwrapper.

Recargamos nuestra shell y a jugar, crearemos nuestro primer proyecto:

```bash
mkdir -p $PROJECT_HOME $WORKON_HOME
mkproject holi
```

<center>{% asset_img ss.2013-10-26.20.02.34.png 'Virtualenv FTW' %}</center>

_Voila_, los comandos más emblematicos de virtualenvwrapper serían:

* _mkproject_ proyecto (Crea un virtualenv y un directorio para codigo, ambos llamados 'proyecto')
* _mkvirtualenv_ entorno (Crea un virtualenv llamado 'entorno')
* _workon_ proyecto (Establece el entorno de trabajo o proyecto al que se le dice)
* _deactivate_ (Sale del entorno de trabajo, requiere estar trabajando en un entorno obviamente)

Mientras estemos trabajando en un entorno podemos instalar cosas via pip sin ningun problema, ya que se instalaran en un directorio en que tenemos permiso :)

<center>{% asset_img ss.2013-10-26.20.15.46.png 'Pip pip' %}</center>

Con el _pip freeze_ ya podemos especificarle al mundo que paquetes y que versiones de ellos usamos, love it!
