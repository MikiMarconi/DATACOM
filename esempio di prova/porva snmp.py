from pysnmp.hlapi import *

# Configura le credenziali SNMP
auth = CommunityData("my_community", mpModel=0)  # Usa SNMPv1 con la community "my_community"
target = UdpTransportTarget(("10.100.0.243", 161), timeout=5000)  # Timeout di 5 secondi

# Definisci l'OID da recuperare utilizzando ObjectIdentity invece di ObjectIdentifier
oid = ObjectIdentity("1.3.6.1.4.1.2011.5.25.207.2.2")

# Esegui una richiesta SNMP GET
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           auth,
           target,
           ContextData(),
           ObjectType(oid))  # Usa ObjectType per specificare l'OID
)

# Gestisci la risposta
if errorIndication:
    print(f"Errore: {errorIndication}")
else:
    if errorStatus:
        print(f"Errore di stato: {errorStatus}")
    else:
        for name, val in varBinds:
            print(f"{name.prettyPrint()} = {val.prettyPrint()}")
