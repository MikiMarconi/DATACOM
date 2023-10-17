from netmiko import ConnectHandler
from InterfaceObj import Interface  # Assicurati di importare la classe Interface da InterfaceObj

class Connection:
    @staticmethod
    def splitOutput(host, port, username, password, device_type):
        try:
            connection = ConnectHandler(host=host, port=port, username=username, password=password,
                                        device_type=device_type)
            output = connection.send_command('display interface brief')
            # Dividi l'output in righe
            linee = output.strip().split('\n')
            interfacce = []

            # Itera attraverso le righe per cercare le interfacce desiderate
            for linea in linee:
                colonne = linea.split()
                if len(colonne) >= 1 and colonne[0] in ["GigabitEthernet0/0/0","GigabitEthernet0/0/1"]:
                    interfaccia = colonne[0]
                    phy = colonne[1]
                    protocol = colonne[2]
                    inUti = colonne[3]
                    outUti = colonne[4]
                    inErrors = colonne[5]
                    outErrors = colonne[6]

                    # Crea un oggetto Interface
                    interfaccia_obj = Interface(interfaccia, phy, protocol, inUti, outUti, inErrors, outErrors)
                    interfacce.append(interfaccia_obj)

            connection.disconnect()
            return interfacce

        except Exception as e:
            print(f"Errore: {str(e)}")
