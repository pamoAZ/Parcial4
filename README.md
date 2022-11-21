# EXTINCIONMOLAR.db 
En este proyecto se utiliza una libreria de python **SQLMODEL**para interactuar con bases de datos SQL desde código Python
en donde se crea una base de datos con la capacidad de guardar datos locales, que se obtiene  a partir de la terminal del usuario, para hacer
obtener relacion a partir de estos 


## ley de Beer-Lambert 🚀
En óptica, la ley de Beer-Lambert, también conocida como ley de Beer o ley de Beer-Lambert-Bouguer es una relación empírica que relaciona la absorción de luz con las propiedades 
del material atravesado.

La ley de Beer fue descubierta independientemente (y de distintas maneras) por Pierre Bouguer en 1729, Johann Heinrich Lambert en 1760 y
August Beer en 1852. En forma independiente, Wilhel Beer y Johann Lambert propusieron que la absorbancia de una muestra a
determinada longitud de onda depende de la cantidad de especie absorbente con la que se encuentra la luz al pasar por la muestra.


![ley-de-beer-lambert-2 (1)](https://user-images.githubusercontent.com/90355422/203150291-d88d41d8-b5c4-4b80-9187-e7b357d1f3d9.jpg)


###  Relaciones 
la ley de Beer-Lambert se describe como 


![ley-lambert-beer-300x122](https://user-images.githubusercontent.com/90355422/203151054-3c95cdef-b3c9-43da-8510-ba3be6a0036a.png)




### Utilidad de la base de datos🔧

A partir de la libreria sqlmodel se crean 3 clases que son las tablas donde se guardan los datos, **Enlace**, **Sustancia** y **Coeficiente**, a partir de la tabla se tienen una relacion entre dos llaves primarias del id del nombre de la sustancia y coeficiente de extincion molar, en las otras dos se guardan los datos de los parametros de cada sustancia, para calcular  la concentracion de la disolucion, gracias a la facilidad con la que se puede escribir un motor de base de datos uttilizando SQLmodel.
se utiliza controles de flujo para hacer un menu y mostrar al usuario las peticiones requeridas


