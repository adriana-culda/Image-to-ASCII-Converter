# Image-to-ASCII-Converter
Un script Python simplu și eficient care transformă imaginile în caractere ASCII. Proiectul folosește biblioteca OpenCV pentru procesarea imaginii și maparea nivelurilor de gri pe o scară de caractere specifice.

**Caracteristici**
* Conversie automată: Transformă orice imagine (.jpg, .png, etc.) în format text.
* Redimensionare inteligentă: Ajustează automat dimensiunea imaginii pentru a păstra aspectul corect în terminal sau editor de text (aspect ratio correction).
* Custom Mapping: Folosește un set de 11 caractere pentru a reprezenta densitatea culorilor, de la spațiu (alb/luminos) la @ (negru/întunecat).

**Tehnologii folosite**
Python
OpenCV (cv2): Pentru citirea imaginii, conversia în grayscale și redimensionare.

**Cum funcționează?**
Încărcare: Imaginea este citită în mod grayscale (nivele de gri).
Redimensionare: Imaginea este micșorată la o lățime de 120 de caractere, păstrând proporțiile (cu un factor de corecție de 0.5 pentru înălțime, deoarece caracterele text sunt mai înalte decât late).

**Mapare:** 
Fiecare pixel (cu valori între 0 și 255) este transformat într-un index corespunzător listei de caractere:
[' ', '.', ',', ':', '-', '=', '+', '*', '#', '^', '@']
Rezultatul final este salvat într-un fișier .txt.
