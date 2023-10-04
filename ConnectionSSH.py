from netmiko import ConnectHandler
import time
import InterfaceObj

interfacce = []

def splitOutput(output):
    # Dividi l'output in righe
    linee = output.strip().split('\n')
    interfacce = []

    # Itera attraverso le righe per cercare le interfacce desiderate
    for linea in linee:
        colonne = linea.split()
        if len(colonne) >= 1 and colonne[0] in ["GigabitEthernet0/0/0.51", "GigabitEthernet0/0/0.52"]:
            interfaccia = colonne[0]
            phy = colonne[1]
            protocol = colonne[2]
            inUti = colonne[3]
            outUti = colonne[4]
            inErrors = colonne[5]
            outErrors = colonne[6]

            # Crea un oggetto Interface
            interfaccia_obj = InterfaceObj.Interface(interfaccia, phy, protocol, inUti, outUti, inErrors, outErrors)
            interfacce.append(interfaccia_obj)

    return interfacce

while True:
    try:
        connection = ConnectHandler(host='10.100.0.9', port='22', username='admin', password='huawei123', device_type='huawei_vrp')
        output = connection.send_command('display interface brief')
        interfacce = splitOutput(output)
        interfaccia51 = interfacce[0]
        interfaccia52 = interfacce[1]
        print(interfaccia52.interface)
        connection.disconnect()
        # Attendere 60 secondi prima della successiva iterazione
        time.sleep(60)


    except Exception as e:
        print(f"Errore: {str(e)}")



