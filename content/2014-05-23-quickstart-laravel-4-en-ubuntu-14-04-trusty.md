title: Quickstart Laravel 4 en Ubuntu 14.04 Trusty
date: 2014-05-23 23:20:45
category: linux

Afortunadamente en cierto curso de ingenieria en software en cierta [universidad](http://utem.cl) el [profe](http://sebastian.cl) los esta <del>obligando</del> haciendo usar [Laravel](http://laravel.com), este es un framework que me agrada mucho (Si bien esta escrito en *PHP*, ese lenguaje tan alejado de la mano de dios como decimos con [Fernando](http://alumnos.informatica.utem.cl/~frubilar), hace *mucho* más agradable la experiencia de desarrollo).

En fin, vi a muchos sufriendo con la instalación del framework, otros hasta llorando y dandole hijos a <del>diablo</del> [Codeigniter](http://codeigniter.com), asi que me decidí y hacer un quickstart para quedar trabajando rápidamente con laravel 4 en la última versión estable de Ubuntu (14.04 LTS al momento de escribir este post).

## Pasos

1. Lo primero que necesitamos obviamente es una maquina con Ubuntu 14.04...
2. Instalar los siguientes paquetes básicos para php5 y un par de librerías requeridas por laravel:

    ```sudo apt-get install php5-curl php5-mcrypt php5-cli```

3. Instalar composer:

    ```wget -O- https://getcomposer.org/installer | php```
    ```sudo mv composer.phar /usr/local/bin/composer```

4. Agregar el directorio bin de composer al PATH, agregamos la siguiente línea al final de .bashrc o .zshrc:

  ```export PATH="~/.composer/vendor/bin:$PATH"```

3. Instalar el _instalador_ de laravel, este nos permite crear una estructura básica para un proyecto:

    ```composer global require "laravel/installer=~1.1"```

4. Recargamos la consola

5. Usamos el comando laravel para generar un nuevo proyecto:

    ```laravel new blogsito```

Aquí ya tendremos la estructura del proyecto creada en el directorio ```blogsito``` :)

{% img http://alumnos.informatica.utem.cl/~pperez/images/new_project_l4rocks.png Nailed! ... Almost %}

## Mcrypt PHP extension required


{% img http://alumnos.informatica.utem.cl/~pperez/images/mcrypt_fail.png Mcrypt PHP extension required :( %}

Un problema que se presenta al intentar correr cualquier cosa con *artisan* (La interfaz de linea de comandos de laravel, **MUY** útil!) es que no anda ni pa' atrás! y el WTF se escucha a lo lejos: Por que me reclamai si ya te instale el ```php5-mcrypt```!

Lo que sucede es que en esta versión de Ubuntu los modulos de php deben ser habilitadas explicitamente, utilizando ```php5enmod``` (Del mismo estilo de ```a2enmod``` usado para los módulos de apache), por lo que aplicando

```sudo php5enmod mcrypt```

deberíamos estar *casi* listos para desarrollar:

{% img http://alumnos.informatica.utem.cl/~pperez/images/finally_nailed.png Ahora si ... Nailed! %}


Como detalle, encuentro que es una pérdida de tiempo marearse instalando apache para cosas tan infimas, así que uso directamente el servidor integrado de laravel, este por defecto levanta un server web corriendo la app en localhost por el puerto 8000 y se invoca con

```php artisan serve```

{% img http://alumnos.informatica.utem.cl/~pperez/images/working_l4rocks.png You have arrived! %}

## Como olvidar la base de datos!

Esto igual es a gusto personal de cada uno, más bien del requerimiento del cliente (O si el profe te obliga a usar postgres, ese caso tb aplica). Una de las gracias de trabajar con frameworks es la abstracción del motor de base de datos, por lo que podemos migrar con un par de lineas nuestra aplicación de mysql a postgresql, y luego a sqlite.
Personalmente estoy usando postgres:

## Pasos para db

1. Instalar postgres:

    ```sudo apt-get install postgresql-9.3```

2. Instalar la extensión postgres para PHP:

    ```sudo apt-get install php5-pgsql```

3. Crear el usuario y la db (Reemplazar l4rocks por lo que quieran :) ):

    ```sudo -u postgres createuser --no-superuser --pwprompt l4rocks```

    ```sudo -u postgres createdb l4rocks```

4. Configurar laravel para utilizar esta db, el fichero en cuestion es ```app/config/database.php```y es bastante sencillo, la directiva ```default``` indica que conexión se utilizará por defecto, las definiciones de las conexiones se encuentran más abajo en el fichero.
5. Probar:

    ```php artisan migrate```

{% img http://alumnos.informatica.utem.cl/~pperez/images/dbworkingl4.png All is good ;) %}
