# BudaMetro
Tarea del metro en Buda para aplicar como desarrollador (practicante).

Para usar la aplicación hay que correr el comando:
`python3 main.py`


Para testear la solución hay que correr el comando:
`python3 test_shortest.py`

## Input
- Archivo csv con los nodos y conexiones del metro. Columna 1 es la estación, 2 qué color es, 3 en adelante son conexiones. Ejemplo:
![image](https://user-images.githubusercontent.com/32397663/168455495-5181054c-62a7-4707-87ab-921ff7da606f.png)
- Estación de partida
- Estación de llegada
- Color del tren: red/green/nada(enter)


## Tests
Los tests son:
- `test_shortest`: Test de ruta más corta en grafo usado de ejemplo en enunciado con un tren sin color
- `test_shortest_red`: Test de ruta más corta en grafo usado de ejemplo en enunciado con un tren rojo
- `test_shortest_green`: Test de ruta más corta en grafo usado de ejemplo en enunciado con un tren verde
