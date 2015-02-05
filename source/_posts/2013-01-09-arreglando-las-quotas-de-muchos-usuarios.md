layout: post
title: Arreglando las quotas de muchos usuarios
date: 2013-01-09 17:14
comments: true
category: Sysadmin
---
En la U el departamento de Informática les da un espacio a los estudiantes, y como muchos se aprovechaban de esto y gastaban lo poco y nada de almacenamiento que tenemos tuvimos que implementarles quotas.
Esta cosa la tuvimos que hacer por nfs más encima (Y el parto de que funcionara la quota via nfs, esa historia es para otro momento ...) y en cierto momento se nos estropeo y todas las quotas quedaron por defecto (ilimitado); asi que como soy lazy me hice un script que seteara las quotas por defecto :D

{% gist 4496591 %}

Es super basico, pero cumple su cometido :D

{% asset_img nailed.png 'Quotas working!' %}
