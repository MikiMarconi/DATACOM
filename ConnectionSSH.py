from netmiko import ConnectHandler

connection = ConnectHandler(host='10.100.0.9', port='22', username='admin', password='huawei123', device_type='huawei_vrp')
while(True):
    output = connection.send_command('display interface brief')
    print(output)

connection.disconnect()