"""
We are tasked with dividing two integers without using multiplication,
division, or modulus operators, and the result must truncate toward zero.
This makes bit manipulation a good candidate for solving the problem efficiently.
"""
def div(dividend, divisor):
            visor = abs(divisor)
            vidend = abs(dividend)
            result = 0
            while vidend >= visor:
                temp_visor, mult = visor, 1
                while vidend >= (temp_visor << 1): # (10 >= (2)4)
                    temp_visor <<= 1 # (4) (8)
                    mult <<= 1 # (4)
                vidend -= temp_visor # 10 - 8 = 2 - 2 = 0
                result += mult # 4 + 1 = 5
            return result

# div(10,2)
