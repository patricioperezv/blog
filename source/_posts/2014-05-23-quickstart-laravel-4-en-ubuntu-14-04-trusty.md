title: Quickstart Laravel 4 en Ubuntu 14.04 Trusty
date: 2014-05-23 23:20:45
category: linux
---

**UPDATE[Feb 14/2015]**: Con la actualización a laravel 5, el instalador de laravel instala la versión 5 del framework, por lo que he actualizado las instrucciones para que se instale la versión 4.2; No veo muchos cambios entre ambas versiones en la instalación del framework, asi que este articulo debería servirles para laravel 5 tambien.

Afortunadamente en cierto curso de ingenieria en software en cierta [universidad](http://utem.cl) el [profe](http://sebastian.cl) los esta <del>obligando</del> haciendo usar [Laravel](http://laravel.com), este es un framework que me agrada mucho (Si bien esta escrito en *PHP*, ese lenguaje tan alejado de la mano de dios como decimos con [Fernando](http://alumnos.informatica.utem.cl/~frubilar), hace *mucho* más agradable la experiencia de desarrollo).

En fin, vi a muchos sufriendo con la instalación del framework, otros hasta llorando y dandole hijos a <del>diablo</del> [Codeigniter](http://codeigniter.com), asi que me decidí y hacer un quickstart para quedar trabajando rápidamente con laravel 4 en la última versión estable de Ubuntu (14.04 LTS al momento de escribir este post).

<!-- more -->

## Pasos

* Lo primero que necesitamos obviamente es una maquina con Ubuntu 14.04...
* Instalar los siguientes paquetes básicos para php5 y un par de librerías requeridas por laravel:
```bash
sudo apt-get install php5-curl php5-mcrypt php5-cli
```

* Instalar composer:

```bash
wget -O- https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
```

* Agregar el directorio bin de composer al PATH, agregamos la siguiente línea al final de .bashrc o .zshrc:

```bash
export PATH="$HOME/.composer/vendor/bin:$PATH"
```

* Crear el proyecto usando composer:

~~~bash
composer create-project laravel/laravel l4rocks --prefer-dist 4.2
~~~

**Nota**: Si desean usar la última versión del framework (5.0 al momento de escribir este update), pueden quitar el `--prefer-dist 4.2`

Aquí ya tendremos la estructura del proyecto creada en el directorio `l4rocks` :)

{% asset_img new_project_l4rocks.png 'Nailed! ... Almost' %}

### Mcrypt PHP extension required

{% asset_img mcrypt_fail.png 'Mcrypt PHP extension required :(' %}

Un problema que se presenta al intentar correr cualquier cosa con *artisan* (La interfaz de linea de comandos de laravel, **MUY** útil!) es que no anda ni pa' atrás! y el WTF se escucha a lo lejos: Por que me reclamai si ya te instale el `php5-mcrypt`!

Lo que sucede es que en esta versión de Ubuntu los modulos de php deben ser habilitadas explicitamente, utilizando `php5enmod` (Del mismo estilo de `a2enmod` usado para los módulos de apache), por lo que usando el siguiente comando:


```bash
sudo php5enmod mcrypt
```

deberíamos estar *casi* listos para desarrollar:

{% asset_img finally_nailed.png 'Ahora si ... Nailed!' %}

Como detalle, encuentro que es una pérdida de tiempo marearse instalando apache para cosas tan infimas, así que uso directamente el servidor integrado de laravel, este por defecto levanta un server web corriendo la app en localhost por el puerto 8000 y se invoca con

```bash
php artisan serve
```

{% asset_img working_l4rocks.png 'You have arrived!' %}

## Como olvidar la base de datos!

Esto igual es a gusto personal de cada uno, más bien del requerimiento del cliente (O si el profe te obliga a usar postgres, ese caso tb aplica). Una de las gracias de trabajar con frameworks es la abstracción del motor de base de datos, por lo que podemos migrar con un par de lineas nuestra aplicación de mysql a postgresql, y luego a sqlite.
Personalmente estoy usando postgres:

## Pasos para db

1. Instalar postgres:

```bash
sudo apt-get install postgresql-9.3
```

2. Instalar la extensión postgres para PHP:

```bash
sudo apt-get install php5-pgsql
```

3. Crear el usuario y la db (Reemplazar l4rocks por lo que quieran :) ):

```bash
sudo -u postgres createuser --no-superuser --pwprompt l4rocks
sudo -u postgres createdb l4rocks
```

4. Configurar laravel para utilizar esta db, el fichero en cuestion es `app/config/database.php` y es bastante sencillo, la directiva `default` indica que conexión se utilizará por defecto, las definiciones de las conexiones se encuentran más abajo en el fichero.

5. Probar:

```bash
php artisan migrate
```

{% asset_img dbworkingl4.png 'All is good ;)' %}
