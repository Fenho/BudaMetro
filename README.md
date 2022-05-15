# BudaMetro
Tarea del metro en Buda para aplicar como desarrollador (practicante).

Para usar la aplicación hay que correr el comando:
`python3 main.py`


Para testear la solución hay que correr el comando:
`python3 test_shortest.py`

## Input
- Archivo csv con los nodos y conexiones del metro. Columna 1 es la estación, 2 qué color es, 3 en adelante son conexiones. Ejemplo:
![image](https://user-images.githubusercontent.com/32397663/168455495-5181054c-62a7-4707-87ab-921ff7da606f.png)

*Ojo: No es necesario incluir una conexión dos veces como en este ejemplo (Si A tiene a B en sus conexiones, no es necesario que B tenga a A en sus conexiones), lo que se puede apreciar en el segundo csv que se usa para los tests automáticos.*
- Estación de partida
- Estación de llegada
- Color del tren: red/green/nada(enter)

## Output
Un string que describe la ruta más corta según lo especificado:

![image](https://user-images.githubusercontent.com/32397663/168488519-f5aa88b2-6fb3-4127-97fe-be3cf0dc9523.png)


## Ejemplos
En la carpeta Networks hay dos ejemplos.
El primero es el ejemplo que se da en el enunciado:

![image](https://user-images.githubusercontent.com/32397663/168488203-a3574321-7001-4e97-8302-9ab29af09095.png)

El segundo corresponde a este grafo:

![image](https://user-images.githubusercontent.com/32397663/168488186-e45bcc83-3be0-4f42-ac46-c234582812a1.png)


## Tests
Los tests con el primer archivo csv son:
- `test_task_example_no_color`: Test de ruta más corta con un tren sin color.
- `test_task_example_red`: Test de ruta más corta con un tren rojo.
- `test_task_example_green`: Test de ruta más corta con un tren verde.

Los tests con el segundo archivo csv son:
- `test_second_middle`: Test de ruta más corta con un tren sin color con el objetivo de ver que no tenga problemas en que el recorrido termine en una estación intermedia.
- `test_second_three_connections`: Test de ruta más con un tren verde para ver que pasa en un grafo donde un nodo tiene 3 conexiones por delante.
- `test_second_red`: Test de ruta más cortacon un tren rojo.
