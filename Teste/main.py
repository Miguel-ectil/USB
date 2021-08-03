import serial
import re

from serial.serialutil import Timeout


# Puxar o Leitor passando a Porta COM e suas especificações
# ser = serial.Serial('COM5', 9600,timeout=3)
# # Fazer o programa pegar a saida do Leitor

# size = ser.read_until(expected="\r")
# # Ver a saida do leitor
# print(size)
size = input("Aqui:")
# Criar uma variavel para tranformar o Byte da saida em String
primeira = str(size)
print(f"TEXTO=", primeira)
# Fazer o regex
teste = (re.findall(r'[A-Z]|[a-z]|[0-9]', primeira))
# Formatação da String

for t in teste:
    print(t, end="")

