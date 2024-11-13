from pymodbus.client.tcp import ModbusTcpClient
import time

client = ModbusTcpClient('192.168.1.20', port=502)
client.connect()

# change the address to the desired digital output
client.write_coil(5, True)
time.sleep(5)
client.write_coil(5, False)

client.close()