# inch 값을 cm 값으로의 변환

input_inch = float(input("Inch 값 : "))

print("Inch 값을 Cm 로 변환한 값 : ", input_inch * 2.54)

# Kg 단위를 Lb 단위로의 변환

input_kg = float(input("Kg 값 : "))

print("Kg 값을 Lb 로 변환한 값: ", input_kg * 2.20462)

# 원의 반지름을 입력 받아 원의 둘레와 넓이 구하기

input_rad = float(input("원의 반지름 : "))
import math

print("원의 둘레 : ", 2 * math.pi * input_rad)
print("원의 넓이 : ", math.pi * input_rad ** 2)