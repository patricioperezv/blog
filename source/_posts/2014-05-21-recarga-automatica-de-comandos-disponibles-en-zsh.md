title: Recarga automatica de comandos disponibles en zsh
date: 2014-05-21 01:40:21
category: linux
---
Hace tiempo que no uso ``bash``, nunca me di el tiempo de configurarlo a mi pinta, ademas hace un tiempo me encontre con [oh my zsh](https://github.com/robbyrussell/oh-my-zsh) y ya no hay vuelta a atras :P

*peeeero* una cosa que me molestó de inmediato era que al instalar nuevas aplicaciones estas no estaban disponibles (Aunque estuvieran en el ``$PATH``), en ese momento extrañe a ``bash``; en fin, luego de googlear un rato llegué a la respuesta:

	zstyle ":completion:*:commands" rehash 1

Al agregar esto a nuestro ``~/.zshrc`` tendremos esta función en zsh. Que diantres hace? Le dice a zsh que no pesque el cache de comandos, esto se encuentra deshabilitado por defecto debido al uso extra que se le da al disco, pero meh, ni se nota!
