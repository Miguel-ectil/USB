import serial
from serial import Serial
from serial.serialutil import Timeout
import re


# Puxar o Leitor passando a Porta COM e suas especificações
ser = serial.Serial('COM5', 9600, timeout = 3)
# Fazer o programa pegar a saida do Leitor
size = ser.readline()
# Ver a saida do leitor
print(size)
# Criar uma variavel para tranformar o Byte da saida em String
primeira = str(size)
print(f"TEXTO=", primeira)
# Fazer o regex
teste = (re.findall(r'[A-Z]|[a-z]|[0-9]', primeira))
# Formatação da String

for t in teste:
    print(t, end="")

