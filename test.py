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



