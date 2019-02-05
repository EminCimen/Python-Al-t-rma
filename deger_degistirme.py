a = input("A değerini giriniz>")
b = input("B değerini giriniz>")

print("Değişmeden Önceki Değerler \nA = {} \nB={}".format( a , b ))

a,b=b,a

print("Değiştikten Sonraki Değerler \nA = {} \nB={}".format( a , b ))
