import re

texto = b"a\x08*I\x05\x00\x11\x00F0D\x02 px\x9d\x9fb\xad\t\\$\x16\xae\x04\x1d\x1f-\xb0\xa3!:\xd4\rf\x05\x05R\x88\xd3Y\x8f\xa2\x84\x9e\x02 *\x81\xc8\x95\x03\x1f\xfc\xdafu\xb8x\xd8W\x83\xca\xfd\x17\x163*y9$\xe7\xc5\xec\xb2\xcbe\xe8\x92\x00\x00\x00\x0cI\x14\x18ED\x14I%\xd1YT\x80\r"

hexa = texto.hex()
print(hexa)
# Byte Hexadecimal para permitir o python decodificar corretamente
bytes_object = bytes.fromhex(hexa)
print(bytes_object)
# Conversão para ASCII com prevenção de erro com 'replace'
ascii_string = bytes_object.decode("ASCII", 'replace')

final_format = (re.findall(r'[A-Z]|[a-z]|[0-9]', ascii_string))

for t in final_format:
    print(t,end="")
