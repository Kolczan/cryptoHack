from general.encoding import myascii
from general.encoding import b64
from general.encoding import bytesAndBigIntegers
from general.encoding import encoding_challenge
from general.encoding import hexy
from general.xor import lemur_xor
from general.xor import xorstarter
from general.xor import xor_properties
from general.xor import favourite_byte
from general.xor import you_either_know
from general.mathematics import gcd
from general.mathematics import egcd
from general.mathematics import modular_arithmetic_1
from general.mathematics import modular_arithmetic_2
from general.mathematics import modular_inverting
from general.data_formats import privacy_enhanced_mail
from general.data_formats import certainly_not
from general.data_formats import ssh_key
from general.data_formats import transparency

from mathematics.modular_math import quadratic_residues
from mathematics.modular_math import legendre_symbol
from mathematics.modular_math import modular_square_root
from mathematics.modular_math import chinese_remainder_theorem

if __name__ == '__main__':
    ### ENCODING
    # myascii.myascii()
    # hexy.hexy()
    # b64.b64()
    # bytesAndBigIntegers.bytesandBigIntegers()
    # encoding_challenge.encoding_challenge()

    ### XOR
    # xorstarter.xorstarter()
    # xor_properties.xor_properties()
    # favourite_byte.favourite_byte()
    # you_either_know.you_either_know()
    # lemur_xor.lemur_xor()

    ### MATHEMATICS
    # gcd.gcd()
    # egcd.egcd(26513, 32321)
    # modular_arithmetic_1.modular_arithmetic()
    # modular_arithmetic_2.modular_arithmetic_2()
    # modular_inverting.modular_inverting(3,13)

    ### DATA FORMATS
    # privacy_enhanced_mail.privacy_enhanced_mail()
    # certainly_not.certainly_not()
    # ssh_key.ssh_key()
    # transparency.transparency()

    ###################################################
    ################# MATHEMATICS #####################
    ###################################################

    ### MODULAR_MATH

    #quadratic_residues.quadratic_residues()
    #legendre_symbol.legendre_symbol()
    # modular_square_root.modular_square_root()
    chinese_remainder_theorem.chinese_remainder_theorem()
    print('done')
