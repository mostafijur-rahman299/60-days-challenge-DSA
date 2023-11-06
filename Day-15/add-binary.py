class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
# Solution 01
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
    
    
# Solution 02
res = ''

carry = '0'
a = '11'
b = '1'


if len(a) < len(b):
    a = len(b[len(a):]) * '0' + a
if len(b) < len(a):
    b = len(a[len(b):]) * '0' + b
    

def b_sum(num1, num2, carry):
    summ = '0'
    if num1 == '1' and num2 == '1':
        summ = '10'
    elif num1 == '0' or num2 == '0':
        summ =  str(int(num1) or int(num2))
    if carry == '1':
        if summ == '10':
            return '11'
        elif summ == '1':
            return '10'
        else:
            return carry
    return summ

for i in range(len(b)-1, -1, -1):
    summ = b_sum(a[i], b[i], carry)
        
    if summ == '1':
        res = summ + res
        carry = '0'
        continue
        
    if i == 0:
        res = summ + res
        break
        
    res = str(int(summ) % 10) + res
    
    carry = str(int(summ) // 10) 