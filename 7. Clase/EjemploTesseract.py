import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

imagen=cv2.imread('D:/3.Trabajo Academia/Clases Python/Imagen.png')


texto=pytesseract.image_to_string(imagen)

print(texto)

cv2.imshow('Imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()