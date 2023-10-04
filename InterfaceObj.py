class Interface:
    def __init__(self, interface, phy, protocol, InUti, OutUti, inErrors, outErrors):
        self.interface = interface
        self.phy = phy
        self.protocol = protocol
        self.InUti = InUti
        self.OutUti = OutUti
        self.inErrors = inErrors
        self.outErrors = outErrors