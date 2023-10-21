#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Color, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.nxtdevices import LightSensor

# Inicializa el ladrillo EV3
ev3 = EV3Brick()

# Conecta los sensores de color a los puertos 1 y 4
sensor_izquierdo = ColorSensor(Port.S1)
sensor_derecho = ColorSensor(Port.S4)

# Conecta los motores a los puertos B y C
motor_izquierdo = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_derecho = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Configura la velocidad de los motores
velocidad = 200  # Velocidad

# Crea el objeto DriveBase para controlar los motores
robot = DriveBase(motor_izquierdo, motor_derecho, 56, 160)

# Función para seguir la línea
def seguir_linea():
    umbral = 50  # Umbral

    while True:
        reflejo_izquierdo = sensor_izquierdo.reflection()
        reflejo_derecho = sensor_derecho.reflection()

        # Comprueba si ambos sensores están sobre la línea
        if reflejo_izquierdo < umbral and reflejo_derecho < umbral:
            robot.drive(velocidad, 0)
        # Si el sensor izquierdo está fuera de la línea
        elif reflejo_izquierdo >= umbral and reflejo_derecho < umbral:
            robot.drive(velocidad, -90)
        # Si el sensor derecho está fuera de la línea
        elif reflejo_izquierdo < umbral and reflejo_derecho >= umbral:
            robot.drive(velocidad, 90)
        # Ambos sensores están fuera de la línea, detente
        else:
            robot.stop()

seguir_linea()
