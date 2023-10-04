from netmiko import ConnectHandler
import time

connection = ConnectHandler(host='10.100.0.9', port='22', username='admin', password='huawei123', device_type='huawei_vrp')

while True:
    try:
        output = connection.send_command('display interface brief')

        # # Dividi l'output in linee
        # lines = output.split('\n')
        #
        # # Lista per tenere traccia delle linee desiderate
        # desired_lines = []
        #
        # # Cerca le linee con GigabitEthernet0/0/0.51 e GigabitEthernet0/0/0.52
        # for line in lines:
        #     if "GigabitEthernet0/0/0.51" in line or "GigabitEthernet0/0/0.52" in line:
        #         desired_lines.append(line)
        #
        # # Stampa le linee desiderate
        # for line in desired_lines:
        print(output)

    except Exception as e:
        print(f"Errore: {str(e)}")

    # Attendere 60 secondi prima della successiva iterazione
    time.sleep(60)

connection.disconnect()
