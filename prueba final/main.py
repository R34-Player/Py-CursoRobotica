#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.iodevices import Ev3devSensor
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import LightSensor, ColorSensor
from tarea import Tareas
from contar_lineas import ContadorLineas
from seguir_lineas import SeguidorLineas
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
MD = Motor(Port.C,Direction.COUNTERCLOCKWISE)
MI = Motor(Port.B,Direction.COUNTERCLOCKWISE)
MG = Motor(Port.A,Direction.COUNTERCLOCKWISE)
SD = ColorSensor(Port.S2)
SI = LightSensor(Port.S4)
#SC = ColorSensor(Port.S3)
SC =  Ev3devSensor(Port.S3)
Sonidos = SoundFile()


movimientos = Tareas(ev3,MD,MI,MG,SD,SI,SC,wait,Stop,Sonidos,Color,DriveBase,time)
condiciones = Tareas(ev3,MD,MI,MG,SD,SI,SC,wait,Stop,Sonidos,Color,DriveBase,time)
contador = ContadorLineas()
seguidor = SeguidorLineas(ev3,MD,MI,MG,SD,SI,SC,wait,Stop,Sonidos,contador,2,time)

# Write your program here.
ev3.speaker.beep()
movimientos.mover_por_distancia(40,"adelante")
#seguidor.mover_por_distancia(40,"adelante")
#movimientos.agarrar_Aldeano("Subir")
#movimientos.mover_por_distancia(40,"adelante")
'''
while True:
    condiciones.detectar_Color()
    if condiciones.actualizar_Color() == 1:
        print("Amarillo")
        movimientos.mover_por_distancia(15,"atras")
        movimientos.girar_n_grados(45,"izquierda")
        movimientos.agarrar_Aldeano("Bajar")
        movimientos.mover_por_distancia(10,"adelante")
        movimientos.agarrar_Aldeano("Subir")
        movimientos.girar_n_grados(45,"derecha")
        movimientos.mover_por_distancia(45,"adelante")
        movimientos.girar_n_grados(92,"izquierda")
    elif condiciones.actualizar_Color() == 2:
        print("Azul")
        movimientos.mover_por_distancia(15,"atras")
        movimientos.girar_n_grados(45,"izquierda")
        movimientos.agarrar_Aldeano("Bajar")
        movimientos.mover_por_distancia(10,"adelante")
        movimientos.agarrar_Aldeano("Subir")
        movimientos.girar_n_grados(50,"izquierda")
        movimientos.mover_por_distancia(85,"adelante")
        movimientos.girar_n_grados(95,"izquierda")
    elif condiciones.actualizar_Color() == 3:
        print("Rojo")
    else:
        print("Verde")


'''
