import numpy

def whats_a_lattice():
    v1 = [6, 2, -3]
    v2 = [5, 1, 4]
    v3 = [2, 7, 1]

    matrix = numpy.array([v1,v2,v3])
    det = numpy.linalg.det(matrix)
    print(abs(det))

# Our volume is found by taking the determine of the vectors given.  # LinearAlgebraBoii
# v1 = [6, 2, -3]
# v2 = [5, 1, 4]
# v3 = [2, 7, 1]
# Then make it look like:
# 6, 2, -3
# 5, 1, 4
# 2, 7, 1
#
# Then the determinite algorithm is: 6(1 * 1 - 7 * 4) - 2(5 * 1 - 2 * 4) + (-3)(5 * 7 - 2 * 1) = -255
# Then our volume is: | -255 | = 255