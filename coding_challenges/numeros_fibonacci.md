# ¿Es Número Fibonacci?
## ¿Que entendí?
Entendí que tenia que hallar la secuencia de fibonacci, utilizando las siguientes formulas 5*(n`*`n)+4 y 5*(n*n)-4, despues obteniendo este resultado tenia que hallar un número elevado al cuadrado que obtenga el mismo resultado. 
## ¿Como lo resolvi?
Me di cuenta de que no tenia que hallar la secuencia; sino los cuadrados perfectos, con el parametro n tenia que pasarlo por la formula 5*(n*n)+4, luego de ese resultado se sacaba la raiz cuadrada que arroja el número que al elevarlo al cuadrado se podria identificar el resultado que necesitamos, pero el problema al sacar la raiz siempre saca flotantes, para solucionar esto se hace un if con la función is_integer() para limpiar los resultados que son enteros y dejar que son solo los flotantes.

Ahora para saber si era un cuadrado perfecto o no el resultado tenia que arrojar siendo tipo entero mas no flotante. Usando esta logica utilizo un if con la función isinstance() que identifica el tipo de dato, si es entero devuelve True, y en caso contrario devuelve False.
## ¿Qué aprendí?
Aprendi sobre la formula Fibonacci para hallar los resultados de los cuadrados perfectos para despues sacarle la raiz cuadrada y encontrar el número que el elevarlo al cuadrado es el número perfecto que tenia que hallar.
## Enlace Del Ejercicio
Coding Challeges: https://coding-challenges.dev/problems/python-es-numero-fibonacci
