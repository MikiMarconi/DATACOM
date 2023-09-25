class Interfaccia:
    def __init__(self, tipo, ip):
        self.tipo = tipo
        self.ip = ip

    def setInterface(self, tipo_interfaccia, ip_interfaccia):
        interfaccia1 = Interfaccia(tipo_interfaccia, ip_interfaccia)
        return interfaccia1
