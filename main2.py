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
sensor_izquierdo = LightSensor(Port.S1)
sensor_derecho = LightSensor(Port.S4)

# Conecta los motores a los puertos B y C
motor_izquierdo = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_derecho = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Configura la velocidad de los motores
velocidad = 200  # Puedes ajustar esta velocidad según sea necesario

# Crea el objeto DriveBase para controlar los motores
robot = DriveBase(motor_izquierdo, motor_derecho, 56, 160)

# Función para seguir la línea
def seguir_linea():
    umbral = 50  # Ajusta este valor según tus mediciones
    velocidad = 200  # Puedes ajustar la velocidad según sea necesario

    while True:
        reflejo_izquierdo = sensor_izquierdo.reflection()
        reflejo_derecho = sensor_derecho.reflection()

        if reflejo_izquierdo < umbral and reflejo_derecho < umbral:
            robot.drive(velocidad, 0)
        elif reflejo_izquierdo >= umbral and reflejo_derecho < umbral:
            # Giro a la derecha
            robot.drive(0, -90)  # Detén la rueda izquierda y gira la derecha
        elif reflejo_izquierdo < umbral and reflejo_derecho >= umbral:
            # Giro a la izquierda
            robot.drive(0, 90)  # Detén la rueda derecha y gira la izquierda
        else:
            robot.stop()

        # Lógica para giros en intersecciones
        if reflejo_izquierdo < umbral and reflejo_derecho < umbral:
            # Ambos sensores están sobre la línea
            # Esto podría ser una intersección
            robot.stop()
seguir_linea()

#si no funciuona el dar vuelta, debemos de cambiar el grado a negativo 