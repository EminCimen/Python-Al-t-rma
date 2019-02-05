print("YAKIT HESAPLAMA PROGRAMI")
yakit = int(input("Aracın KM başına yaktığı miktar (kuruş)>"))
yol = int(input("Kaç KM yol gideceksiniz?>"))
print("Ödemeniz gereken miktar {} TL".format( yol * (yakit/100) ))