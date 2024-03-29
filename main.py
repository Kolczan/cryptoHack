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
from mathematics.lattices import vectors
from mathematics.lattices import size_and_basis
from mathematics.lattices import gram_schmidt
from mathematics.lattices import whats_a_lattice
from mathematics.lattices import gaussian_reduction
from mathematics.lattices import find_the_lattice
from mathematics.brainteasers import successive_powers
from mathematics.brainteasers import adrien_signs
from mathematics.brainteasers import broken_rsa

from diffie_hellman.starter import dh_starter_1
from diffie_hellman.starter import dh_starter_2
from diffie_hellman.starter import dh_starter_3
from diffie_hellman.starter import dh_starter_4
from diffie_hellman.starter import dh_starter_5
from diffie_hellman.man_in_the_midel import parameter_injection
from diffie_hellman.man_in_the_midel import export_grade
from diffie_hellman.man_in_the_midel import static_client
from diffie_hellman.group_theory import additive
# from diffie_hellman.group_theory import static_client2
from diffie_hellman.misc import script_kiddie

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
    # quadratic_residues.quadratic_residues()
    # legendre_symbol.legendre_symbol()
    # modular_square_root.modular_square_root()
    # chinese_remainder_theorem.chinese_remainder_theorem()

    ### LATTICES
    # vectors.vectors()
    # size_and_basis.size_and_basis()
    # gram_schmidt.gram_schmidt()
    # whats_a_lattice.whats_a_lattice()
    # gaussian_reduction.gaussian_reduction()
    # find_the_lattice.find_the_lattice() ### not finished

    ### BRAINTEASERS
    # successive_powers.successive_powers()
    # adrien_signs.adrien_signs()
    # broken_rsa.broken_rsa()

    ###################################################
    ################ DIFFIE-HELLMAN ###################
    ###################################################
    ### DIFFIE_HELLMAN

    # dh_starter_1.dh_starter_1()
    # dh_starter_2.dh_starter_2()
    # dh_starter_3.dh_starter_3()
    # dh_starter_4.dh_starter_4()
    # dh_starter_5.dh_starter_5()
    # parameter_injection.parameter_injection()
    # export_grade.export_grade()
    # static_client.static_client()
    # additive.additive()
    # static_client2.static_client2()
    # script_kiddie.script_kiddie()


    ###################################################
    ############### SYMMETRIC CIPHERS #################
    ###################################################

    ###################### przerobić na funkcje
    ### HOW AES WORKS
    # from symmetric_ciphers.how_aes_works import keyed_permutations
    # from symmetric_ciphers.how_aes_works import resisting_bruteforce
    # from symmetric_ciphers.how_aes_works import structure_of_aes
    # from symmetric_ciphers.how_aes_works import add_round_key
    # from symmetric_ciphers.how_aes_works import confusion_through_substitution
    # from symmetric_ciphers.how_aes_works import diffusion_through_permutation
    # from symmetric_ciphers.how_aes_works import bring_it_all_together

    ## SYMMETRIC STARTER
    # from symmetric_ciphers.symmetric_starter import modes_of_operation_starter
    # from symmetric_ciphers.symmetric_starter import passwords_as_keys

    ## BLOCK CIPHERS
    # from symmetric_ciphers.block_ciphers import ECB_CBC_WTF
    # from symmetric_ciphers.block_ciphers import ecb_oracle ## uwaga długie bruteforcowanie
    # from symmetric_ciphers.block_ciphers import flipping_cookies
    # from symmetric_ciphers.block_ciphers import lazy_CBC
    # from symmetric_ciphers.block_ciphers import triple_des

    ## STREAM CIPHERS
    # from symmetric_ciphers.stream_ciphers import symmetry
    # from symmetric_ciphers.stream_ciphers import bean_counter
    # from symmetric_ciphers.stream_ciphers import ctrime
    # from symmetric_ciphers.stream_ciphers import stream_of_consciousness

    ###################################################
    ###################### RSA ########################
    ###################################################

    # RSA STARTER
    # from rsa_1977.rsa_starter import rsa_starter_1
    # from rsa_1977.rsa_starter import rsa_starter_2
    # from rsa_1977.rsa_starter import rsa_starter_3
    # from rsa_1977.rsa_starter import rsa_starter_4
    # from rsa_1977.rsa_starter import rsa_starter_5
    # from rsa_1977.rsa_starter import rsa_starter_6

    # PRIMES PART I
    # from rsa_1977.primes_part_1 import factoring
    # from rsa_1977.primes_part_1 import inferius_prime
    # from rsa_1977.primes_part_1 import monoprime
    # from rsa_1977.primes_part_1 import square_eyes
    # from rsa_1977.primes_part_1 import manyprimes

    # PUBLIC EXPONENT
    # from rsa_1977.public_exponent import salty
    # from rsa_1977.public_exponent import modulus_inutilis
    # from rsa_1977.public_exponent import everything_is_big
    # from rsa_1977.public_exponent import crossed_wires
    # from rsa_1977.public_exponent import everything_is_still_big
    from rsa_1977.public_exponent import endless_emails

    # SIGNATURES PART I
    # from rsa_1977.signatures_part_1 import signing_server
    # from rsa_1977.signatures_part_1 import lets_decrypt
    # from rsa_1977.signatures_part_1 import blinding_light

    # PRIMES PART II
    # from rsa_1977.primes_part_2 import infinite_descent
    # from rsa_1977.primes_part_2 import marins_secrets
    # from rsa_1977.primes_part_2 import fast_primes ### cos dlugo dziala
    # from rsa_1977.primes_part_2 import ron_was_wrong
    # from rsa_1977.primes_part_2 import rsa_backdoor_viability
    print('done')
