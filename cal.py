import sys
import os
from two_d_dct import two_d_dct



print(sys.argv[1], sys.argv[2])
if len(sys.argv) <= 1:
    print("Please input algorithm and parameters")
else:
    try:
        globals().get(sys.argv[1])(sys.argv)
    except(ValueError,ArithmeticError):
        print("Error in Input Value!")
