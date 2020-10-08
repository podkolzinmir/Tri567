""" This code identifies a triangle! """
import datetime
import math



def classify_triangle(a_side, b_side, c_side):
    now = datetime.datetime.now()
    print(now)

# require that the input values be >= 0 and <= 200
    not_int_check = not(isinstance(a_side, int) and isinstance(b_side, int) \
    and isinstance(c_side, int))
    small_check = a_side <= 0 or b_side <= 0 or c_side <= 0
    big_check = a_side > 200 or b_side > 200 or c_side > 200


    if not_int_check or small_check or big_check:
        return 'InvalidInput'
# This information was not in the requirements spec but
# is important for correctness
# the sum of any two sides must be strictly less than the third side
# of the specified shape is not a triangle
    if (a_side + b_side < c_side or a_side + c_side < b_side or c_side + a_side < b_side):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if a_side == b_side and b_side == a_side and b_side == c_side:
        return 'Equilateral'
    if  math.sqrt(a_side ** 2 + b_side ** 2) == c_side or \
    math.sqrt(c_side ** 2 + b_side ** 2) == a_side \
    or math.sqrt(a_side ** 2 + c_side ** 2) == a_side:
        return 'Right'
    if (a_side != b_side) and  (b_side != c_side) and (a_side != c_side):
        return 'Scalene'

    return 'Isoceles'
