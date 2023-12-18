import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long
# Zamiast przepisywać ten kodzik http://aes.cryptohack.org/ecbcbcwtf/ będe strzelał w endpointy cryptohacka, w sumie chyba o to im chodziło

def decrypt(ciphertext):
    # Do decryptcji użyty jest mode ECB
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    url += ciphertext.hex()
    url += "/"
    r = requests.get(url)
    derulo = r.json()
    return bytes.fromhex(derulo["plaintext"])

def encrypt_flag():
    # encrypcji użyty jest mode CBC
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    r = requests.get(url)
    derulo = r.json()
    return bytes.fromhex(derulo["ciphertext"])


encrypted_flag = encrypt_flag()
print(encrypted_flag) # To jest zaszyfrowana flaga, wiemy ze do jej wytworzenia użyto tryby CBC
print(len(encrypted_flag)) # To co dostaliśmy ma 48bitów, czyli 3 blok 16 bajtów, czyli trzy macierze 4x4bytes
# Najpierw był plaintext (to czego szukamy)
# Jego pierwszy blok (nazwijmy plaintext1) został zxorowany z IV (Initialization Vector)
# Następnie to zostało zaszyfrowane w pierwszy blok ----> block1 =  encrypt(XOR(plaintext1, IV))
# Następnie drugi blok plaintext oraz block1 został zxorowany, aby zostać zaszyfrowane i stworzyć block2 ---> block2 = encrypt(XOR(plaintex2, block1))
# Tak samo trzeci blok plaintext został zxorowany z block2 i dopiero zaszyfrowany tworząc block3 ----> block3 = encrypt(XOR(plaintext3, block2))
# Tak więc aby dostać każdy plaintext i złożyc go do kupy musimy obliczyć:
# plaintext1 ^ IV = decrypt(block1) ---> plaintext1 = decrypt(block1) ^ IV
# plaintext2 ^ block1 = decrypt(block2) ---> plaintext2 = decrypt(block2) ^ block1
# plaintext3 ^ block2 = decrypt(block3) ---> plaintext2 = decrypt(block3) ^ block2
# I na koniec dodać to do siebie
# to wszystko z własności operacji XOR
def xor(a, b):
	return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

iv = encrypted_flag[:16]
block1 = encrypted_flag[16:32]
block2 = encrypted_flag[32:]

decrypt_block1 = xor(decrypt(block1), iv)
decrypt_block2 = xor(decrypt(block2), block1)
print(decrypt_block1 + decrypt_block2)



# Lets compare what different modes of operation are
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
# So AES is a block cipher and on comparing ECB and CBC modes we find that
# ECB mode simply returns the output of the block cipher, no funny tricks
# CBC mode takes the output from the previous block and XORs it with the plaintext
# before feeding it to the block cipher. This way current encryption is dependent upon all previous encryptions And repeated plaintext blocks dont get encrypted to the same stuff!
# Cool! Now coming to the challenge, if we have a CBC mode encrypted ciphertext and ECB decrypter, what else do we need?
# NOTHING just take the ciphertext from the previous block and xor it with the current block before feeding it the decrypter
# flag_block_0 = decrypt(block_0) xor iv
# flag_block_1 = decrypt(block_1) xor block_0