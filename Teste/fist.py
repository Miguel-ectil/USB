
import serial
import serial.tools.list_ports



class Serialapp():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.bauderate = [9600,115200]
        self.portlist = [] 

    # metodo de update de portas seriais
    def updatePort(self):
        self.portlist = [port.device for port in serial.tools.list_ports.comports()]
        print(self.portlist)
    # Conecão
    def conecxaoSerial(self):
        try:
            self.serialPort.open()
        except:
            print("Houve um erro em abrir a porta serial")
        
    # Receber dados
    def readSerial(self):
        dataRead = self.serialPort.read_until(expected=b'\r')
        print(dataRead)
    # Enviar dados
    def sendSerial(self,data):
        if(self.serialPorta.isOpen()):
            dadosend = str(self.data)+"\n"
            self.serialPorta.write(dadosend.encode())
            self.serialPorta.flushOutput()
        
    # Fechar nossa conexão
    def closeSerial(self):
        self.serialPort.close()
