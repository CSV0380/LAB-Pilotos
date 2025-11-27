# Fundamentos de Programación
# Adaptación del examen de la segunda convocatoria del curso 2022/23 a laboratorio.  
# Pilotos

**Autor:**  Belén Vega 
**Revisores:** Patricia Jiménez, Toñi Reina.
**Adaptación:** Toñi Reina
**Última modificación:** 16/10/2024.

El cambio de escudería de Fernando Alonso a Aston Martin ha desencadenado una serie de desafíos para los ingenieros del equipo. La llegada del legendario piloto ha traído consigo una gran cantidad de datos de telemetría y rendimiento del vehículo que necesitan ser procesados de manera eficiente. Además de los datos de Fernando Alonso también se han recogido datos de los demás pilotos, para poder hacer comparativas con ellos y obtener el mejor resultado esta temporada. Los datos que maneja Aston Martin tienen la siguiente estructura e información: 

- **nombre** (str): nombre del piloto.
- **escuderia** (str): nombre de la escudería en la que corre el piloto.
- **fecha\_carrera** (date): fecha en la que tuvo lugar la carrera.
- **temperatura\_min** (int): temperatura mínima que ha medido el sensor colocado en el frontal del monoplaza.
- **vel\_max** (float): velocidad máxima alcanzada por el piloto en la carrera.
- **duracion** (float): duración total en minutos que el piloto tardó en completar la carrera. Si el piloto no pudo terminar la carrera debido a un accidente, este valor indica el tiempo que el piloto estuvo corriendo antes del accidente.
- **posicion\_final** (int): puesto final que ha alcanzado el piloto. Si el piloto no ha podido terminar la carrera este campo toma el valor -1.
- **ciudad** (str): ciudad en la que se encuentra el circuito.
- **top\_6\_vueltas** (list): lista con la duración en segundos de los tiempos que el piloto ha conseguido en sus 6 mejores vueltas. Si debido a un accidente el piloto no ha podido completar ni tan siquiera 6 vueltas, habrá valores en el conjunto de datos que aparecerán con el valor ‘-‘.
- **tiempo\_boxes** (float): duración total en segundos del tiempo que el piloto estuvo en boxes. 
- **nivel\_liquido** (bool): valor que indica si el piloto se ha bebido toda el agua disponible en el tanque situado a sus espaldas (1 = True, no = False).

La primera línea del fichero tiene el siguiente aspecto: 
```
Fernando Alonso;Aston Martin;21-11-22;25;330.1;30.5;-1;Abu Dhabi;[31.254/ 31.567/ 31.789/ 32.045/ -/ -];15.23;no
```

e indica que Fernando Alonso a través de la escudería Aston Martin participó en una carrera en Abu Dhabi que tuvo lugar el 21 de noviembre de 2022. La temperatura mínima que el sensor del coche pudo recoger fue de 25 ºC y que la velocidad máxima que alcanzó en toda la carrera fue de 330.1 km/h. Fernando no pudo acabar esa carrera porque tuvo un accidente. Los tiempos de sus mejores vueltas hasta el momento del accidente fueron  31.254, 31.567, 31.789, 32.045. El tiempo total que estuvo parado en boxes fue de 15.23 minutos y no se bebió todo el agua disponible.

Para la realización de los ejercicios se usará la siguiente definición de namedtuple, y su uso será **obligatorio**: 

```python
from datetime import date
from typing import NamedTuple

Carrera = NamedTuple("Carrera", 
            [("nombre", str),
             ("escuderia", str),
             ("fecha_carrera", date) ,
             ("temperatura_min", int),
             ("vel_max", float),
             ("duracion",float),
             ("posicion_final", int),
             ("ciudad", str),
             ("top_6_vueltas", list[float]),
             ("tiempo_boxes",float),
             ("nivel_liquido", bool)
            ])

```

Como ejemplo, para la carrera anterior obtendremos la siguiente tupla. Fíjese con detalle en el tipo de cada uno de los campos:

```python
Carrera(nombre='Fernando Alonso', escuderia='Aston Martin', fecha_carrera=datetime.date(2022, 11, 21), temperatura_min=25, vel_max=330.1, duracion=30.5, posicion_final=-1, ciudad='Abu Dhabi', top_6_vueltas=[31.254, 31.567, 31.789, 32.045, 0, 0], tiempo_boxes=15.23, nivel_liquido=False)
```

Cree un módulo f1.py e implemente en él las funciones que se piden. Puede definir funciones auxiliares cuando lo considere necesario. Además, también debe crear un módulo f1\_test.py en el que pruebe todas las funciones anteriores. Para ello realice una función de test por cada una de las funciones principales que se pidan y haga las llamadas correspondientes dentro de la función principal (main). 

1. **lee\_carreras**: recibe una cadena de texto con la ruta de un fichero *csv*, y devuelve una lista de tuplas Carrera con la información contenida en el fichero. Preste especial atención a la lista, aquellos valores en los que no haya resultado, es decir aquellos con el carácter “-“,  deberán transformarse a 0. Esto quiere decir que si la cadena de texto es [31.254; 31.567; 31.789; 32.045; - ; -], el resultado de salida deberá ser una lista con los valores [31.254, 31.567, 31.789, 32.045, 0, 0].  

```python
def lee_carreras(ruta_fichero:str)->list[Carrera]
```

2. **media\_tiempo\_boxes**: recibe una lista de tuplas de tipo Carrera, una ciudad y una fecha (con valor por defecto None), y devuelve la media de tiempo en boxes que los pilotos han pasado en la fecha y ciudad seleccionada. Si la fecha es None se sumarán todos los tiempos de la ciudad sin tener en cuenta la fecha. Por otro lado, si no ha habido carreras en la fecha y ciudad seleccionada, la media debe ser 0. 

```python
def media_tiempo_boxes(carreras:list[Carrera], ciudad:str, fecha:date | None =None)->float

```
3. **pilotos\_menor\_tiempo\_medio\_vueltas\_top:** recibe una lista de tuplas de tipo Carrera y un número entero n, y devuelve una lista de tuplas (nombre, fecha) con los n nombres y fechas de carrera de los pilotos cuya media de tiempo en sus 6 vueltas top sea menor. No se tendrán en cuenta aquellos pilotos que han sufrido un accidente y no han podido completar las 6 vueltas. 

```python
def pilotos_menor_tiempo_medio_vueltas_top(carreras:list[Carrera], n)->list[tuple[str,date]]
```

4. **ratio\_tiempo\_boxes\_total:** recibe una lista de tuplas de tipo Carrera, y devuelve una lista de tuplas (nombre, fecha, ratio) con el nombre del piloto, la fecha de la carrera y la ratio entre su tiempo en boxes con respecto al total de tiempo en boxes de todos los pilotos que han participado ese día en la carrera. La lista de tuplas resultante deberá estar ordenada de mayor a menor ratio. 

```python
def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]
```

5. **puntos\_piloto\_anyos:** recibe una lista de tuplas de tipo Carrera y devuelve un diccionario que asocia cada piloto (claves) con una lista con los puntos totales obtenidos cada año. La lista de puntos estará ordenada por año. Para calcular los puntos obtenidos en cada carrera debe tener en cuenta que solamente obtienen puntos aquellos pilotos que queden en las 3 primeras posiciones. Si el puesto es el primero, los puntos serían 50, el segundo puesto son 25 y el tercero 10. Para esta función tiene que utilizar obligatoriamente una función auxiliar que, dada una carrera, calcule el número de puntos de esa carrera. 

```python
def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]
```
6. **mejor\_escuderia\_anyo:** recibe una lista de tuplas de tipo Carrera y un entero a, y devuelve la escudería que más victorias haya conseguido en el año a. Se considera victoria cuando algún piloto queda en el primer puesto. 

```python
def mejor_escuderia_anyo(carreras:list[Carrera], anyo:int)->str

```

7. Pruebe las funciones implementadas en un módulo f1\_test.py. Se recomienda que lo vaya haciendo a medida que vaya resolviendo los distintos apartados. Use las funciones round o format en el test del ejercicio 4 para que el ratio aparezca formateado con 3 decimales. 



**Anexo: Pruebas de las funciones**

En esta sección, se muestra una posible ejecución de las pruebas de las funciones.

```python
1. Test de lee_carreras: 
Total registros leídos: 45. Mostrando los dos primeros registros:

        Carrera(nombre='Fernando Alonso', escuderia='Aston Martin', fecha_carrera=datetime.date(2022, 11, 21), temperatura_min=25, vel_max=330.1, duracion=30.5, posicion_final=-1, ciudad='Abu Dhabi', top_6_vueltas=[31.254, 31.567, 31.789, 32.045, 0, 0], tiempo_boxes=15.23, nivel_liquido=False)

        Carrera(nombre='Fernando Alonso', escuderia='Aston Martin', fecha_carrera=datetime.date(2022, 12, 5), temperatura_min=28, vel_max=328.5, duracion=123.86, posicion_final=2, ciudad='Sao Paulo', top_6_vueltas=[30.976, 31.189, 31.435, 31.679, 31.827, 32.015], tiempo_boxes=12.87, nivel_liquido=False)

#################
2. Test media_tiempo_boxes

La media de tiempo en boxes en la ciudad de Barcelona es de 6.536 segundos.

#################
3. Test pilotos_menor_tiempo_medio_vueltas_top.

Los 4 pilotos con menor tiempo medio son [('Lewis Hamilton', datetime.date(2023, 5, 21)), ('Max Verstappen', datetime.date(2023, 5, 21)), ('Fernando Alonso', datetime.date(2023, 5, 21)), ('Carlos Sainz', datetime.date(2023, 5, 21))].

#################
4. Test ratio_tiempo_boxes_total
Los ratios del tiempo en boxes son:

(Fernando Alonso, 2023-05-21,0.236)
(Carlos Sainz, 2022-11-21,0.23)
(Fernando Alonso, 2023-05-07,0.225)
(Fernando Alonso, 2023-06-04,0.223)
(Fernando Alonso, 2022-11-21,0.214)
(Carlos Sainz, 2022-12-05,0.21)
(Max Verstappen, 2023-04-09,0.209)
(Fernando Alonso, 2023-03-26,0.209)
(Fernando Alonso, 2022-12-19,0.209)
(Charles Leclerc, 2023-04-23,0.208)
(Max Verstappen, 2023-05-07,0.207)
(Fernando Alonso, 2023-04-23,0.207)
(Max Verstappen, 2023-04-23,0.207)
(Carlos Sainz, 2023-03-26,0.206)
(Carlos Sainz, 2022-12-19,0.206)
(Fernando Alonso, 2023-04-09,0.204)
(Charles Leclerc, 2022-12-05,0.203)
(Charles Leclerc, 2023-06-04,0.202)
(Charles Leclerc, 2023-03-26,0.202)
(Charles Leclerc, 2023-05-21,0.201)
(Fernando Alonso, 2022-12-05,0.201)
(Lewis Hamilton, 2023-05-21,0.201)
(Carlos Sainz, 2023-04-09,0.2)
(Carlos Sainz, 2023-06-04,0.2)
(Charles Leclerc, 2022-12-19,0.199)
(Charles Leclerc, 2022-11-21,0.199)
(Charles Leclerc, 2023-04-09,0.199)
(Max Verstappen, 2023-03-26,0.198)
(Max Verstappen, 2022-12-05,0.196)
(Max Verstappen, 2022-12-19,0.195)
(Lewis Hamilton, 2023-06-04,0.195)
(Max Verstappen, 2022-11-21,0.195)
(Charles Leclerc, 2023-05-07,0.193)
(Lewis Hamilton, 2023-04-23,0.191)
(Lewis Hamilton, 2022-12-19,0.191)
(Lewis Hamilton, 2023-05-07,0.191)
(Lewis Hamilton, 2022-12-05,0.19)
(Lewis Hamilton, 2023-04-09,0.188)
(Carlos Sainz, 2023-05-21,0.188)
(Carlos Sainz, 2023-04-23,0.187)
(Lewis Hamilton, 2023-03-26,0.185)
(Carlos Sainz, 2023-05-07,0.184)
(Max Verstappen, 2023-06-04,0.181)
(Max Verstappen, 2023-05-21,0.174)
(Lewis Hamilton, 2022-11-21,0.162)

#################
5. Test puntos_piloto_anyos
Puntos por año de cada uno de los pilotos:

`        Max Verstappen --> [85, 145]
`        Carlos Sainz --> [0, 25]
`        Lewis Hamilton --> [125, 175]
`        Fernando Alonso --> [25, 85]
`        Charles Leclerc --> [10, 70]

#################
6. Test mejor_escuderia_anyo
La mejor escudería en el año 2022 ha sido Mercedes.
```

