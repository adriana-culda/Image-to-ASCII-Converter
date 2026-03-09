import cv2

imagine_primita = cv2.imread(r"D:\\PCLP2\\RGB - ASCII\\imagine.jpg", 0) #imagine gray

#lista de caractere ASCII de la luminos la întunecat
caractere = [' ', '.', ',', ':', '-', '=', '+', '*', '#', '^', '@'] #de la ce mai inchisi la cei mai deschisi

latime = 120  #latime in caractere ASCII
inaltime = int(imagine_primita.shape[0] * (latime / imagine_primita.shape[1]) * 0.5)

imagine = cv2.resize(imagine_primita, (latime, inaltime), interpolation=cv2.INTER_AREA)

sirASCII = ''
for i in range(imagine.shape[0]):      #parcurgerea imaginii
    for j in range(imagine.shape[1]):
        pixel = imagine[i, j]          #valoare pixel
        index = int(pixel) * len(caractere) // 256  #transformarea valorii intr-un indice in lista
        sirASCII += caractere[index]  
    sirASCII += '\n'

#print(sirASCII)
with open(r"D:\\PCLP2\\RGB - ASCII\\imagineASCII.txt", "w") as f:
    f.write(sirASCII)
    print("ASCII salvat cu succes!")