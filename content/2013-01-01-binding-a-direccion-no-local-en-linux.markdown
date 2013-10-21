layout: post
title: Binding a dirección no local en linux
date: 2013-01-01 19:00
comments: true
category: Sysadmin

En el trabajo teníamos un cacho, como hacíamos que nginx respondiera a una ip que no estaba asignada a la maquina, teniamos dos soluciones al ojo:

* Bindear a la ip en cuestión en el 80 (Si lo intentan a secas el kernel les dara jugo)
* Bindear a _*:80_ (No podemos hacerlo, ya que tenemos un servicio ya bindeado al 80 con una de las ip)

Luego de dar un montón de palos de ciego, pensando en duplicar configuraciones de nginx con la ip nueva y que se levantara solo cuando el otro server fallara dimos con el blanco:

**Binding to Non-local Addresses**

Exactamente lo que necesitábamos para la primera opción, activando esto era posible hacer bind a direcciones que no estuvieran actualmente en la maquina(!) y el kernel ni chistaría :D  
La opción para _sysctl.conf_ que hace la magia es:

```
    net.ipv4.ip_nonlocal_bind = 1
```
Y con esto ya funcionara el cacharro :-)
