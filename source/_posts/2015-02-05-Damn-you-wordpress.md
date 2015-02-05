title: Damn you wordpress
date: 2015-02-05 12:05:22
tags:
categories: php
---

Hace un par de semanas que estoy rabiando con un sitio que se negaba a mostrar errores de php, por debajo usa wordpress y mi querido lenguaje PHP.
Yo muy confiado, habilitaba el registro de errores de php mediante el htaccess y nada, seguia en blanco.
Hasta que metido en el `wp-config.php` me fije en la variable `WP_DEBUG`, siempre estuvo frente a mis ojos:

```php
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
```

Y estaba listo para ver el horror!
Otro tip:

Usar la funcion error_log dentro de wordpress tira el mensaje al fichero `wp-debug.log` dentro de `wp-content`, happy debugging!
