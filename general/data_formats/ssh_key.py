from Crypto.PublicKey import RSA

# https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html
# Variables:
# n (integer) – RSA modulus
# e (integer) – RSA public exponent
# d (integer) – RSA private exponent
# p (integer) – First factor of the RSA modulus
# q (integer) – Second factor of the RSA modulus
def ssh_key():
    with open('data_formats/bruce_rsa.pub', 'rb') as key_file:
        key_data = key_file.read()

    # Parse the PEM-encoded key
    public_key = RSA.import_key(key_data)

    # Extract the modulus as a decimal integer
    modulus = public_key.n
    print(modulus)