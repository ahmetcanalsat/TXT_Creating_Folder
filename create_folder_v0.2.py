import os

for j in range(1, 7):
    ana_klasor=os.makedirs("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j), mode=0o755, exist_ok=True)
    j += 1
    for i in range(0, 30):
        i += 1
        if (i > 0 and i <= 5):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Staj Defteri Gün_" + str(i) + ".txt", "w")

        elif (i > 5 and i <= 10):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Staj Defteri Gün_" + str(i) + ".txt", "w")

        elif (i > 10 and i <= 15):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Staj Defteri Gün_" + str(i) + ".txt", "w")

        elif (i > 15 and i <= 20):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Staj Defteri Gün_" + str(i) + ".txt", "w")

        elif (i > 20 and i <= 25):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Staj Defteri Gün_" + str(i) + ".txt", "w")

        elif (i > 25 and i <= 30):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Staj Defteri Gün_" + str(i) + ".txt", "w")

        else:
            "Stajınız bitmiştir."
