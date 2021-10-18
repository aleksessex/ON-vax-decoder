import base64
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

# Split into base64 component strings
jws_parts = jws_string.split(".")

b64_decoded_parts = []

# Decode base64 components
for jws_part in jws_parts:
    b64_decoded_parts.append(b64_padding_decode(jws_part))

shc_data = []
shc_data.append(json.loads(b64_decoded_parts[0]))
shc_data.append(json.loads(zlib.decompress(b64_decoded_parts[1], wbits=-15)))

for item in shc_data:
    print(json.dumps(item, indent=4, sort_keys=True))

