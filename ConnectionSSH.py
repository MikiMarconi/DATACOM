import time

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

    @staticmethod
    def getAllInterface(host, port, username, password, device_type):
        try:
            connection = ConnectHandler(host=host, port=port, username=username, password=password, device_type=device_type)
            output = connection.send_command('display interface brief')
            # Dividi l'output in righe
            linee = output.strip().split('\n')
            interfacce = []

            # Itera attraverso le righe per cercare le interfacce desiderate
            for linea in linee:
                colonne = linea.split()
                if len(colonne) >= 1 and colonne[0] in ["GigabitEthernet0/0/0"]:
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
            return []  # Restituisci una lista vuota in caso di errore


    @staticmethod
    def tracertRoute(sysname):
        if sysname == "R5":
            try:
                connection = ConnectHandler(host="10.100.0.9", port="22", username="admin", password="huawei123", device_type="huawei_vrp")
                output = connection.send_command('tracert 192.168.20.6')
                connection.disconnect()
                return output

            except Exception as e:
                print(f"Errore: {str(e)}")
        else:
            try:
                connection = ConnectHandler(host="10.100.0.10", port="22", username="admin", password="huawei123",
                                            device_type="huawei_vrp")
                output = connection.send_command('tracert 192.168.10.5')
                connection.disconnect()
                return output

            except Exception as e:
                print(f"Errore: {str(e)}")

    @staticmethod
    def switchTraffic(sysname):
        if sysname == "R5":
            host = "10.100.0.9"
        elif sysname == "R6":
            host = "10.100.0.10"
        else:
            print("Sysname non riconosciuto")
            return

        while True:
            # Ottieni le informazioni sull'interfaccia desiderata
            interfaces = Connection.splitOutput(host, "22", "admin", "huawei123", "huawei_vrp")

            # Controlla le interfacce
            for interface in interfaces:
                inUti_percentage = float(interface.InUti.strip('%'))
                if inUti_percentage > 30:
                    # La percentuale di utilizzo supera la soglia, esegui i comandi
                    try:
                        connection = ConnectHandler(host=host, port="22", username="admin", password="huawei123", device_type="huawei_vrp")
                        connection.send_config_set("interface 0/0/0")
                        connection.send_config_set("ospf dr-priority 20")
                        connection.disconnect()

                        # Attendere 30 secondi
                        time.sleep(30)

                        # Risetta la priorità a 10
                        connection = ConnectHandler(host=host, port="22", username="admin", password="huawei123", device_type="huawei_vrp")
                        connection.send_config_set("interface 0/0/0")
                        connection.send_config_set("ospf dr-priority 10")
                        connection.disconnect()

                    except Exception as e:
                        print(f"Errore nell'esecuzione dei comandi su {interface.interface}: {str(e)}")

            # Attendere un po' di tempo prima di controllare nuovamente
            time.sleep(60)  # Controlla ogni 60 secondi (puoi regolare il valore in base alle tue esigenze)
