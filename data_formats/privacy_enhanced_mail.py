from Crypto.PublicKey import RSA

#-----------------DATA FORMATS-------------------
def privacy_enhanced_mail():
    with open('data_formats/privacy_enhanced_mail.pem', 'r') as file:
        priv_key = RSA.importKey(file.read()).d
        print("PEM private key is: " + str(priv_key))