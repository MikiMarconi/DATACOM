import telnetlib
import re
from Router import Router
from Interface import Interfaccia

def is_valid_ip_format(ip):
    # Utilizza una regex per controllare il formato: valore.valore.valore.valore maschera
    ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} \d{1,2}$"
    return re.match(ip_pattern, ip) is not None

def is_valid_ip(ip):
    # Divide l'indirizzo IP e la maschera e verifica i valori
    values = ip.split()
    if len(values) != 2:
        return False

    address, mask = values
    address_parts = address.split('.')

    if len(address_parts) != 4:
        return False

    for part in address_parts:
        try:
            value = int(part)
            if not (1 <= value <= 254):
                return False
        except ValueError:
            return False

    try:
        mask_value = int(mask)
        if not (0 <= mask_value <= 31):
            return False
    except ValueError:
        return False

    return True

def accesso(Router):
    host = '192.168.1.1'
    password = "huawei123"
    tn = telnetlib.Telnet(host)
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii') + b"\n")
    tn.read_until(b'<R2>').decode('ascii')
    command = "system-view"
    tn.write(command.encode('ascii') + b"\n")
    wait(tn)
    assegnaIp(Router, tn)

def assegnaIp(Router, tn):
    tn.write((b"interface GigabitEthernet 0/0/"+ str(Router.numerodiporte).encode('ascii')) + b"\n")
    wait(tn)
    tn.write((b"ip address " + Router.interfaccia.ip.encode('ascii')) + b"\n")
    wait(tn)
    return

def wait(tn):
    tn.read_until(b'[R2').decode('ascii')

def start():
    while True:
        numerodiporte = int(input("Inserisci il numero della porta a cui vuoi assegnare l'ip (da 0 a 1): "))
        if 0 <= numerodiporte <= 1:
            convalidaIP( numerodiporte)
            break
        else:
            print("Numero di porte non valido per GigabitEthernet. Riprova.")

def convalidaIP(numerodiporte):
    router1 = Router(None, None)
    interfaccia1 = Interfaccia(None)
    while True:
        ip_interfaccia = input(f"Inserisci l'indirizzo IP dell'interfaccia (valore.valore.valore.valore maschera) per l'interfaccia GigabitEthernet: ")

        if is_valid_ip_format(ip_interfaccia) and is_valid_ip(ip_interfaccia):
            accesso(router1.setRouter(numerodiporte, interfaccia1.setInterface(ip_interfaccia)))
            break
        else:
            print("Indirizzo IP non valido. Riprova.")

if __name__ == '__main__':
    # starta lo script
    try:
        start()
    except:
        print("ERRORE")