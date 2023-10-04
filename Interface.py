class Interface:
    def __init__(self, interface, phy, protocol, InUti, OutUti, inErrors, outErrors):
        self.interface = interface
        self.phy = phy
        self.protocol = protocol
        self.InUti = InUti
        self.OutUti = OutUti
        self.inErrors = inErrors
        self.outErrors = outErrors



 # Getter per ottenere il nome dell'interfaccia
    def get_interface(self):
        return self.interface

    # Altri getter e setter per gli altri attributi
    def get_phy(self):
        return self.phy

    def get_protocol(self):
        return self.protocol

    def get_InUti(self):
        return self.InUti

    def get_OutUti(self):
        return self.OutUti

    def get_inErrors(self):
        return self.inErrors

    def get_outErrors(self):
        return self.outErrors
