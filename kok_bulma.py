"""
Denklem = ax^2 + bx + c
Delta = b ^ 2 - 4 ac
KÖK 1= (-b - delta ** 0.5) / (2*a)
KÖK 2= (-b + delta ** 0.5) / (2*a)
"""

a = int(input("a değerini giriniz:"))
b = int(input("b değerini giriniz:"))
c = int(input("c değerini giriniz:"))

delta = b ** 2 - 4 * a * c
kök1 = (-b - delta ** 0.5) / ( 2 * a )
kök2 = (-b + delta ** 0.5) / ( 2 * a )

print("Denklemin birinci kökü {} \n Denklemin ikinci kökü {}".format(kök1,kök2))