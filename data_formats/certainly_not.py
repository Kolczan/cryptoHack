import cryptography
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# def certainly_not():
#     # Load your DER-encoded certificate
#     with open('data_formats/2048b-rsa-example-cert.der', 'rb') as cert_file:
#         cert_data = cert_file.read()
#
#     # Parse the certificate
#     certificate = x509.load_der_x509_certificate(cert_data, default_backend())
#
#     # Extract the public key
#     public_key = certificate.public_key()
#
#     print(public_key.public_numbers().n)

from Crypto.PublicKey import RSA

# https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html
# Variables:
# n (integer) – RSA modulus
# e (integer) – RSA public exponent
# d (integer) – RSA private exponent
# p (integer) – First factor of the RSA modulus
# q (integer) – Second factor of the RSA modulus
def certainly_not():
    with open('data_formats/2048b-rsa-example-cert.der','rb') as f:
        key = RSA.import_key(f.read())
    print(f"RSA certificate modulus: {key.n}")
    print(f"RSA public exponent: {key.e}")
    # print(f"RSA private exponent: {key.d}") #there is no private exponent for public keys
    # print(f"RSA 1st factor modulus {key.p}") #No CRT component 'p' available for public keys.
    # print(f"RSA 2nd factor modulus {key.q}") #No CRT component 'q' available for public keys.