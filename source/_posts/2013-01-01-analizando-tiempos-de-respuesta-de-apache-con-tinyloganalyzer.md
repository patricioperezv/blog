layout: post
title: Analizando tiempos de respuesta de apache con TinyLogAnalyzer
date: 2013-01-01 20:21
comments: true
category: Sysadmin
---
Para cierto sitio necesitábamos ver algunas estadísticas de tiempos de respuesta de este, detectar donde se pegaba más tiempo (O sea donde ponerle _amol_).  
[César](http://twitter.com/csepulvedab "César") pillo uno ([apache-response-time](http://code.google.com/p/apache-response-time/) "Apache Response Time"), pero no andaba ni para atrás, asi que googleando un rato llegamos a [TinyLogAnalyzer](http://pypi.python.org/pypi/TinyLogAnalyzer), que esta hecho en python y funciona impecable.  
El proceso seria el siguiente:

* Agregar `%T/%D` al LogFormat de apache (Así registrara los tiempos de respuesta, en microsegundos)
* Instalar tinyloganalyzer, pan comido usando pip: `sudo pip install tinyloganalyzer`
* Obviamente un reinicio a apache: `sudo /etc/init.d/apache2 restart`
* Ejecutar tinylogan: `tinylogan /var/log/apache2/access.log`

_Esto ya es otra cosa_, como me imagino que todos usan vhosts, y querrán estar ojeando estos "reportes" antes de que logrotate se cepille los logs es por esto que pasamos a usar un pequeño script (Aprovechando que estoy dando jugo con python) y cron:

{% gist 4431051 %}

Finalmente lo agregamos al crontab:

```
0	6	* * * /root/bin/analisis_logs_apache.py
```

Easy cake!
