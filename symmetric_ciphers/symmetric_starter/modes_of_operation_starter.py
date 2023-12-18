import requests

response = requests.get("http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/")
print(response.json())
ciphertext = response.json()['ciphertext']
response = requests.get("http://aes.cryptohack.org/block_cipher_starter/decrypt/" + ciphertext)
print(response.json())
print(bytes.fromhex(response.json()['plaintext']).decode('utf-8'))