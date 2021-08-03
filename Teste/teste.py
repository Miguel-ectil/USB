
import codecs
import binascii

texto = (
    b'a\x00<\x87\x05\x00\x11\x00F0D\x02 |\x9c\x89\xa2-Q\x15\xca\xdb)<\xc5b\xb0\x89\xf3\x80\xea\xbd\xb0\x94\r/\x82\xd9(nC[#\xd0\xaa\x02 \x1f\xfa\x8a\x17V\xb7\xf4\xf6\xc9(<\x1e\x16\x88Y<p\x1b\xb1\xa7~\x9f(\x0c\xefg\xf9$\x8d\xeb\x9b\xe3\x00\x00\x00\x0cI\x14\x17ED\x14E\x86\x17M\x84\x80\'')

# deco = bytes.fromhex.decode(texto,"hex","backslashreplace")
# print(deco)
hexade = texto.hex()

# print(bytes.fromhex("9c1bfc05001100473045025c162fb685369b2e6ac205c0202038721bf4dc1d94b22026205bc0d3e7ea202a9402210098764829a1d65c35c248c40205e39c9cdfea20202320f02b1fe5f07d029f003cba45cf0000000c4914154544135d451441464022"))
print(hexade)
# teia = codecs.decode(hexade,'ascii')
