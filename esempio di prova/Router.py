class Router:
    def __init__(self, numerodiporte, interfaccia):
        self.numerodiporte = numerodiporte
        self.interfaccia = interfaccia

    def setRouter(self, numerodiporte, interfaccia):
        router1 = Router(numerodiporte, interfaccia)
        return router1
