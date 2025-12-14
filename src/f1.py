import csv
from datetime import date, datetime
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



def parsea_date(cadena: str) -> date:
    return datetime.strptime(cadena, "%d-%m-%y").date()


def parsea_list(cadena: str) -> list[float]:
    cadena = cadena.strip("[]") #quita elementos al principio y final de lo que le des
    valores = cadena.split("/")
    res = []
    for v in valores:
        v = v.strip()
        if v == "-":
            res.append(0.0)
        else:
            res.append(float(v))
    return res


def parsea_bool(cadena):
    if cadena == "1":
        res = True
    else:
        res = False
    return res



def lee_carreras(ruta_fichero: str) -> list[Carrera]:
    res = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for nombre,escuderia,fecha_carrera,temperatura_min,vel_max,duracion,posicion_final,ciudad,top_6_vueltas,tiempo_boxes,nivel_liquido in lector:
            nombre = str(nombre)
            escuderia = str(escuderia)
            fecha_carrera = parsea_date(fecha_carrera)
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            posicion_final = int(posicion_final)
            ciudad = str(ciudad)
            top_6_vueltas = parsea_list(top_6_vueltas)
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = parsea_bool(nivel_liquido)
            res.append(Carrera(nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, posicion_final, ciudad, top_6_vueltas, tiempo_boxes, nivel_liquido))
    return res

carreras = lee_carreras("data\\f1.csv")
# print(carreras[0])





def media_tiempo_boxes(carreras:list[Carrera], ciudad:str, fecha:date | None =None) -> float:
    res = 0
    cont = 0
    for c in carreras:
        if (c.ciudad == ciudad) and (c.fecha_carrera == fecha or fecha is None):
            cont += 1
            res += c.tiempo_boxes 
        elif c.ciudad == None and c.fecha_carrera == None:
            return 0
    media = res/cont
    return media 

# print(media_tiempo_boxes(carreras, "Barcelona"))





def pilotos_menor_tiempo_medio_vueltas_top(carreras: list[Carrera], n: int) -> list[tuple[str, date]]:
    res = []
    for c in carreras:
        if c.top_6_vueltas.count(0) > 0:
            continue

        media = sum(c.top_6_vueltas) / len(c.top_6_vueltas)
        res.append((c.nombre, c.fecha_carrera, media))
    
    resf = sorted(res, key = lambda x: x[2])
    
    # Devolver solo nombre y fecha de los n primeros
    return [(nombre, fecha) for nombre, fecha, _ in resf[:n]]
T

# print(pilotos_menor_tiempo_medio_vueltas_top(carreras, 4))






def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]:
    for c in carreras: