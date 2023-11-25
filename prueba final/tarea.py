class Tareas:
    def __init__(self,ev3,MD,MI,MG,SD,SI,SC,wait,Stop,sonidos,Colores,Drive,time) -> None:
        self.sound = sonidos
        self.ev3 = ev3
        self.MD = MD
        self.MI = MI
        self.MG = MG
        self.SD = SD
        self.SI = SI
        self.SC = SC
        self.delay = wait
        self.Stop = Stop
        self.Color = Colores
        self.time = time
        self.robot = Drive(MI,MD,wheel_diameter=56, axle_track=154)
        self.robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

    def stoped(self):
        print("Parar")
        self.MD.stop()
        self.MI.stop()

    def girar_n_grados(self,n,direccion=None):        
                # Determinar la dirección de giro para cada motor
        if direccion == "izquierda":
            self.robot.turn(-n)
            self.robot.stop()
        elif direccion == "derecha":
            self.robot.turn(n)
            self.robot.stop()
        else:
            # Por defecto, girar hacia la izquierda si no se especifica una dirección válida
            self.robot.turn(-n)
            self.robot.stop()

    def mover_por_distancia(self,distancia,direccion):
        if direccion == "adelante":
            self.robot.straight(distancia*10)
            self.robot.stop()
        elif direccion == "atras":
            self.robot.straight(distancia*(-10))
            self.robot.stop()
        else:
            self.robot.straight(distancia*0)
            self.robot.stop()

    def detectar_Color(self):
        if self.SC.color() == self.Color.YELLOW:
            self.ev3.speaker.play_file(self.sound.YELLOW)
            self.colorcin = 1
        elif self.SC.color() == self.Color.BLUE:
            self.ev3.speaker.play_file(self.sound.BLUE)
            self.colorcin = 2
            
        elif self.SC.color() == self.Color.RED:
            self.ev3.speaker.play_file(self.sound.RED)
            self.colorcin = 3
            
        elif self.SC.color() == self.Color.GREEN:
            self.ev3.speaker.play_file(self.sound.GREEN)
            self.colorcin = 4

        else:
            self.colorcin = 0

    def actualizar_Color(self):
        return self.colorcin

    def agarrar_Aldeano(self, direccion="Subir"):
        # Define el ángulo objetivo y el tiempo límite (en segundos)
        angulo_objetivo = -120 if direccion == "Subir" else 120
        tiempo_limite = 2  # por ejemplo, 2 segundos

        # Comienza a mover el motor
        self.MG.run_target(100, self.MG.angle() + angulo_objetivo, wait=False)

        # Registra el tiempo de inicio
        inicio = self.time.time()

        # Bucle que verifica el estado del motor y el tiempo transcurrido
        while True:
            if self.time.time() - inicio > tiempo_limite:
                # Si se supera el tiempo límite, detén el motor y sal del bucle
                self.MG.stop()
                break
            if abs(self.MG.angle() - (self.MG.angle() + angulo_objetivo)) < 5:
                # Si el motor está cerca del ángulo objetivo, sal del bucle
                break

    def Configuracion_Robot(self,sp,sa,tr):
        self.robot.settings(straight_speed=sp, straight_acceleration=sa, turn_rate=tr)
