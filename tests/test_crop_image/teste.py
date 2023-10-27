import cv2

image = cv2.imread('recorte_imagem.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 0.02
for contour in contours:
    approx = cv2.approxPolyDP(contour, epsilon * cv2.arcLength(contour, True), True)
    
    if len(approx) == 4:
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

cv2.imshow('Detecção de Quadrados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
