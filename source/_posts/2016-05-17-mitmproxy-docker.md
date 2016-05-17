title: Usar mitmproxy bajo docker
s: mitmproxy-docker
date: 2016-05-17 17:12:09
tags: docker
---

A veces me pregunto que diablos estarán haciendo ciertas aplicaciones en mi teléfono, básicamente a que servidores le estan enviando mis datos personales. En mis tiempos mozos me metia al router y ojeaba el tráfico desde allí con wireshark, era medio complejo pero andaba, actualmente la mayoria de las aplicaciones ya estan pasando si o si por algún cifrado, echando por la tierra mi método chasquilla.

Así es que llegúe a [mitmproxy](https://mitmproxy.org/), esto levanta un proxy y nos permite hacer un ataque man in the middle, soportando _SSL_, permitiendome saber toda la información enviada a China u otros paises. Tuve un par de problemas para compilarlo en Ubuntu 16.04, así que decidí probar un enfoque distinto, usar [docker](https://www.docker.com/). Admito que estoy algo rayado con docker, pero es bastante cómodo para situaciones como estas.

<!-- more -->

Es bien sencillo hecharlo a correr, con esto bastará:

~~~
docker run -it --rm -p 8080:8080 mitmproxy/releases
~~~

Luego vamos a nuestro dispositivo, configuramos el proxy http para conectarse a la ip de nuestro dispositivo, puerto 8080.
Finalmente en el dispositivo a espiar entramos al dominio mágico [mitm.it](http://mitm.it), seleccionamos nuestro sistema operativo, instalamos el certificado descargado (esto nos permitirá descifrar el tráfico encriptado) y voila.

El único detalle que encontré, es que en mi Samsung Galaxy S4 (Android 6) la mayoria de las aplicaciones no pescaban ni en bajada la configuración del proxy, aprovechando que está rooteado le metí [ProxyDroid](https://play.google.com/store/apps/details?id=org.proxydroid&hl=es_419) y asunto solucionado :)

{% asset_img mitm-shot.png 'Esto ya es otra cosa' %}
