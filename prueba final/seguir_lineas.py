class SeguidorLineas:
    def __init__(self, ev3, MD, MI, MG, SD, SI, SC, wait, Stop, sonidos, contador, Lines,time):
        self.sound = sonidos
        self.ev3 = ev3
        self.MD = MD  # Motor Derecho
        self.MI = MI  # Motor Izquierdo
        self.MG = MG  # Motor de Garra (opcional)
        self.SD = SD  # Sensor Derecho (opcional)
        self.SI = SI  # Sensor Izquierdo
        self.SC = SC  # Sensor de Color (opcional)
        self.delay = wait
        self.Stop = Stop
        self.Lineas = Lines
        self.time = time
        self.Kp = 2.8
        self.Ki = 0.008
        self.Kd = 0.01
        self.integral = 0
        self.derivativa = 0
        self.last_error = 0
        self.error = 0
        self.threshold = 0
        self.SPEED = 180
        self.Black = 12
        self.White = 76
        self.contador = contador

    def PID(self, Kp, Ki, Kd, error, integral, last_error):
        integral += error
        derivativa = error - last_error
        output = Kp * error + Ki * integral + Kd * derivativa
        return output, integral

    def mover_por_distancia(self, distancia, direccion):
        circunferencia_rueda = 2*3.1416*28  # en mm
        grados_por_mm = 360 / circunferencia_rueda

        distancia_en_grados = 10*distancia * grados_por_mm
        multiplicador_direccion = 1 if direccion == "adelante" else -1

        self.MD.reset_angle(0)
        self.MI.reset_angle(0)
        self.threshold = (self.Black + self.White) / 2

        try:
            while True:
                self.error = self.SI.reflection() - self.threshold
                turn_rate, self.integral = self.PID(self.Kp, self.Ki, self.Kd, self.error, self.integral, self.last_error)
                self.MD.run(self.SPEED - turn_rate)
                self.MI.run(self.SPEED + turn_rate)
                self.last_error = self.error

                distancia_actual = (self.MD.angle() + self.MI.angle()) / 2 * multiplicador_direccion
                if abs(distancia_actual) >= abs(distancia_en_grados):
                    break

                self.delay(10)

        except Exception as e:
            self.ev3.speaker.say("Error en movimiento por distancia")
            #print(f"Error: {e}")
        finally:
            self.MD.stop()
            self.MI.stop()
