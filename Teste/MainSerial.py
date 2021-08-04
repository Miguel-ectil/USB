
from serial.serialutil import SerialException
from serial.tools.list_ports import main
from fist import Serialapp

# Cria um objeto para a classe Serialapp
ser = Serialapp()
# Realiza um update nas portas de dispositivos do PC
ser.updatePort()
# Definir porta e bauderate
ser.serialPort.port = 'COM6'
ser.serialPort.baudrate = 9600
# Conexão
ser.conecxaoSerial()
# Recebe 10 buffers da serial
contador = 0
while (1):
    ser.readSerial()

# Fechar a conexão
ser.closeSerial()