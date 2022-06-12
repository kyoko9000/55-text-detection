import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\9. python project\55 text detection\tesseract ocr\tesseract.exe'

img_cv = cv2.imread("bien-so-xe.jpg")
img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

img_gray = cv2.bilateralFilter(img_gray, 11, 17, 17)
edged = cv2.Canny(img_gray, 190, 200)
contours, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
contour_license_plate = None
license_plate = None
w = None
H = None
x = None
y = None
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)
    if len(approx) == 4:
        contour_license_plate = approx
        x, y, w, h = cv2.boundingRect(contour_license_plate)
        print(x, y, w, h)
        license_plate = img_gray[y+5:y+h-8, x+10:x+w-10]
        break

thread, blackandwhiteimage = cv2.threshold(license_plate, 85, 255, cv2.THRESH_BINARY)
text = pytesseract.image_to_string(blackandwhiteimage, config="--psm 6")

print(text)
cv2.imshow("license plate", blackandwhiteimage)
cv2.waitKey(0)