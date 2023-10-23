import base64
def b64():
    key = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    result = base64.b64encode(bytes.fromhex(key))
    print(str(result,'utf-8'))