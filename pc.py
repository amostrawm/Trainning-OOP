class Computador:
    def __init__(self, marca, processador, memoria_ram, placa_de_video, numero_pc):
        self.marca = marca
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.numero_pc = numero_pc
    pass

    def iniciar(self):
        print("Iniciando PC [" + str(self.numero_pc) + "]")

    def desligar(self):
        print("Desligando PC [" + str(self.numero_pc) + "]")