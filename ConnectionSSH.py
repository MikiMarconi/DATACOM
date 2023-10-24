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
        while True:
            host = "10.100.0.9"
            host2 = "10.100.0.10"

            # Effettua la connessione ai dispositivi e raccogli i dati
            interfacesR5 = Connection.splitOutput(host, "22", "admin", "huawei123", "huawei_vrp")
            inpercR5 = float(interfacesR5[0].InUti.strip('%'))
            outUti_percentageR5 = float(interfacesR5[0].OutUti.strip('%'))
            print(outUti_percentageR5)
            print(inpercR5)

            interfacesR6 = Connection.splitOutput(host2, "22", "admin", "huawei123", "huawei_vrp")
            inpercR6 = float(interfacesR6[0].InUti.strip('%'))
            outUti_percentageR6 = float(interfacesR6[0].OutUti.strip('%'))
            print(outUti_percentageR6)
            print(inpercR6)

            # Effettua la connessione SSH e imposta le rotte statiche
            connection = ConnectHandler(host=host, port="22", username="admin", password="huawei123",
                                        device_type="huawei_vrp")
            connection.send_command("system-view")
            connection.send_command("ip route-static 192.168.20.190 31 192.168.52.2 preference 5")
            connection.disconnect()

            # Introduci un ritardo prima di gestire l'altro dispositivo
            time.sleep(30)  # Attendere 30 secondi

            connection = ConnectHandler(host=host2, port="22", username="admin", password="huawei123",
                                        device_type="huawei_vrp")
            connection.send_command("system-view")
            connection.send_command("ip route-static 192.168.10.190 31 192.168.36.3 preference 5")
            connection.disconnect()

            # Attendere un po' di tempo prima di controllare nuovamente
            time.sleep(10)  # Controlla ogni 10 secondi (puoi regolare il valore in base alle tue esigenze)

        # if outUti_percentageR5 or inpercR5 or inpercR6 or outUti_percentageR6 > 9.85:
        #     # La percentuale di utilizzo supera la soglia, esegui i comandi
        #     try:
        #         connection = ConnectHandler(host=host, port="22", username="admin", password="huawei123",
        #                                     device_type="huawei_vrp")
        #         connection.send_command("ip route-static 192.168.20.190 31 192.168.52.2 preference 5")
        #
        #         connection.disconnect()
        #
        #         connection = ConnectHandler(host=host2, port="22", username="admin", password="huawei123",
        #                                     device_type="huawei_vrp")
        #         connection.send_command("ip route-static 192.168.10.190 31 192.168.36.3 preference 5")
        #
        #         connection.disconnect()
        #
                # Attendere 30 secondi
                # time.sleep(90)
                #
                # # Risetta la priorità a 10
                # connection = ConnectHandler(host=host, port="22", username="admin", password="huawei123",
                #                                 device_type="huawei_vrp")
                # connection.send_command("undo ip route-static 192.168.10.190 31 192.168.36.3 preference 5")
                # connection.send_command("undo ip route-static 192.168.20.190 31 192.168.52.2 preference 5")
                # connection.disconnect()
            # except Exception as e:
            #     print(f"Errore nell'esecuzione dei comandi sull'interfaccia: {str(e)}")

        # Attendere un po' di tempo prima di controllare nuovamente
        # time.sleep(10)  # Controlla ogni 5 secondi (puoi regolare il valore in base alle tue esigenze)
