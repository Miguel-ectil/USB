import re
from typing_extensions import final

hex_string = "609c1bfc0500110047304502205c2f2e16222fb685369b2e6ac205c02638721bf4dc1d94b2265bc0d3e7ea2a9402210098764829a1d65c35c248c40205e39c9cdfea23f02b1fe5f07d029f003cba45cf0000000c4914154544135d45144146400d"

bytes_object = bytes.fromhex(hex_string)

ascii_string = bytes_object.decode("ASCII", 'replace')

final_format= (re.findall(r'[A-Z]|[a-z]|[0-9]', ascii_string))

for t in final_format:
    print(t, end="")
