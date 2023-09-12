class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary_to_decimal(binary_number):
            decimal_number = 0
            exponent = 0
            
            while binary_number:
                decimal_number += (binary_number % 2) * (2 ** exponent)
                binary_number //= 10
                exponent += 1
            return decimal_number

        def decimal_to_binary(decimal_number):
            if not decimal_number:
                return str(decimal_number)

            binary = ""
            while decimal_number:
                counter = decimal_number % 2
                binary += str(counter)
                decimal_number = int(decimal_number // 2)
            return binary[::-1]

        return decimal_to_binary(binary_to_decimal(int(a)) + binary_to_decimal(int(b)))
    