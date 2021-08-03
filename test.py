# import re

# # size = "65ad4sa56d165DF1A5F1AS65F1AD5F1AE8F1d61adf5ae1f68awe1fa"

# # fist = size[:-1]
# # second = fist[1:]
# # print(second)
# a = input("Aq:")
# res = re.findall("[a-z]|[A-z]", a)
# for t in res:
#     print(t,end="")


# # Puxar o Leitor passando a Porta COM e suas especificações
#     ser = serial.Serial('COM5', 9600, timeout = 1)
#     # Fazer o programa pegar a saida do Leitor
#     size = ser.readline()
#     # Ver a saida do leitor
#     print(size)
#     # Criar uma variavel para tranformar o Byte da saida em String
#     primeira = str(size)
#     print(f"TEXTO=", primeira)
#     # Fazer o regex
#     teste = (re.findall(r'[A-Z]|[a-z]|[0-9]', primeira))
#     # Formatação da String
#     fist = teste[:-1]
#     final = fist[1:]
#     for t in final:
#         print(t, end="")



######### New #############

import codecs

texo = (b'`\x9c\x1b\xfc\x05\x00\x11\x00G0E\x02 \\/.\x16"/\xb6\x856\x9b.j\xc2\x05\xc0&8r\x1b\xf4\xdc\x1d\x94\xb2&[\xc0\xd3\xe7\xea*\x94\x02!\x00\x98vH)\xa1\xd6\\5\xc2H\xc4\x02\x05\xe3\x9c\x9c\xdf\xea#\xf0+\x1f\xe5\xf0}\x02\x9f\x00<\xbaE\xcf\x00\x00\x00\x0cI\x14\x15ED\x13]E\x14AF@\r')

hexade = texo.hex()

print(hexade)