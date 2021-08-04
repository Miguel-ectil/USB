from serial.serialutil import SerialException
from serial.tools.list_ports import main
from conf import Serialapp

# Faz um loop infinito do processo
while (1):
    # Cria um objeto para a classe Serialapp
    ser = Serialapp()
    # Realiza um update nas portas de dispositivos do PC
    ser.updatePort()
    # Definir porta e bauderate
    # Adicionei um timeout para assim eu conseguir retirar a leitura do leitor
    ser.serialPort.port = 'COM5'
    ser.serialPort.baudrate = 9600
    ser.serialPort.timeout = 0.5
    # Conexão
    ser.conecxaoSerial()
    # Leitura de Dados
    ser.readSerial()
    # Fechar a conexãoaIF0Dpxb
