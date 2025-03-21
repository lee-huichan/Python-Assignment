input_a = int(input("입력 진수 결정(16/10/8/2) : "))
input_b = input("값 입력 : ")

if input_a == 16:
    input_b = int(input_b, 16)
if input_a == 10:
    input_b = int(input_b, 10)
if input_a == 8:
    input_b = int(input_b, 8)
if input_a == 2:
    input_b = int(input_b, 2)

print("16진수 ==> ", hex(input_b))
print("10진수 ==> ", input_b)
print("8진수 ==> ", oct(input_b))
print("2진수 ==> ", bin(input_b))