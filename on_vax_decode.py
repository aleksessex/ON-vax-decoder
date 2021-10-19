import base64
from jose import jwk, jws
from jose.constants import ALGORITHMS
import json
import os
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
import re
import sys
import zlib


# Add necessary padding to b64 string and decode
def b64_padding_decode(data):
    padding_needed = len(data) % 4
    if padding_needed > 0:
        data += '=' * (4 - padding_needed)
    return base64.urlsafe_b64decode(data)


if len(sys.argv) < 2:
    print("Verify Ontario vaccine passport decoder")
    print("Usage: python on_vax_decode.py <path-to-pdf>")
    sys.exit()

qr_path = sys.argv[1]

if not os.path.isfile(qr_path):
    print("File", sys.argv[1], "not found")
    sys.exit()

if not os.path.isfile("on_sig_ver_key.json"):
    print("Signature verification key file not found")
    sys.exit()

with open("on_sig_ver_key.json") as f:
    sig_ver_key_raw = json.load(f)

sig_ver_key = jwk.construct(sig_ver_key_raw)

# Decode QR code and extract data payload
pages = convert_from_path(qr_path)
raw_qr = decode(pages[0])
qr_data = raw_qr[0].data.decode()

if qr_data[0:5] != "shc:/":
    raise ValueError('Invalid SHC format')

# Remove SHC identifier
b45_data = qr_data.replace("shc:/", "")

# Group base45 in digit pairs
b45_digit_pairs = re.findall('..', b45_data)

jws_string = ""

# Decode base45
for p in b45_digit_pairs:
    jws_string += chr(int(p) + 45)

# Verify signature
(encoded_header, encoded_payload, encoded_sig) = jws_string.split(".")

if not jws.verify(jws_string, sig_ver_key, ALGORITHMS.ES256) == b64_padding_decode(encoded_payload):
    raise ValueError('INVALID digital signature')

# Decode and print payload
payload = json.loads(zlib.decompress(b64_padding_decode(encoded_payload), wbits=-15))

print(json.dumps(payload, indent=4, sort_keys=True))
