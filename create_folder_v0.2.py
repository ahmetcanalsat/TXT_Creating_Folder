import os

for j in range(1, 7):
    os.makedirs("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j), mode=0o755, exist_ok=True)
    for i in range(0, 30):
        i += 1
        if (i > 0 or i <= 5):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j) + "/Staj Defteri Gün_" + str(i) + ".txt","w")

        elif (i > 5 or i <= 10):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j) + "/Staj Defteri Gün_" + str(i) + ".txt","w")

        elif (i > 10 or i <= 15):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j) + "/Staj Defteri Gün_" + str(i) + ".txt","w")

        elif (i > 15 or i <= 20):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j) + "/Staj Defteri Gün_" + str(i) + ".txt","w")

        elif (i > 20 and i <= 25):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j) + "/Staj Defteri Gün_" + str(i) + ".txt","w")

        elif (i > 25 and i <= 30):
            dosyad = open("C:/Users/HP/Desktop/python_cikti/Hafta-" + str(j) + "/Staj Defteri Gün_" + str(i) + ".txt","w")

        else:
            "Stajınız bitmiştir."

    j += 1