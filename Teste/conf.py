from pynput.keyboard import Key
import serial
import serial.tools.list_ports
import re
import pynput
import time

teclado = pynput.keyboard

keyb = teclado.Controller()

class Serialapp():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.bauderate = [9600,115200]
        self.portlist = []
        self.timeout = 0

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
        dataRead = self.serialPort.readline()
        # Conversão Hexadecimal
        hexade = dataRead.hex()
        # Byte Hexadecimal para permitir o python decodificar corretamente
        bytes_object = bytes.fromhex(hexade)
        # Conversão para ASCII com prevenção de erro com 'replace'
        ascii_string = bytes_object.decode("ASCII", 'replace')
        # Regex padrão Aa-Zz 0-9
        final_format = (re.findall(r'[A-Z]|[a-z]|[0-9]', ascii_string))
        # Saida em string
        conta = (len(final_format))

        if conta >= 1:
            for t in final_format:
                keyb.press(t)
                time.sleep(0.0)
                keyb.release(t)
                print(t,end=" ")
            keyb.press(Key.enter)

    # Enviar dados
    def sendSerial(self,data):
        if(self.serialPorta.isOpen()):
            dadosend = str(self.data)+"\n"
            self.serialPorta.write(dadosend.encode())
            self.serialPorta.flushOutput()
        
    # Fechar nossa conexão
    def closeSerial(self):
        self.serialPort.close()
