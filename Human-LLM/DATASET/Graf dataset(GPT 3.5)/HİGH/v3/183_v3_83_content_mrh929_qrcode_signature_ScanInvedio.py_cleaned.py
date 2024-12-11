import cv2
import pyzbar.pyzbar as pyzbar
def fonk1(image):
    b1 = pyzbar.decode(image)
    for barcode in b1:
        x, y, w, b2 = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + b2), (255, 255, 255), 2)
        b3 = barcode.data.decode("utf-8")
        b4 = barcode.type
        b5 = f"{b3} ({b4})"
        cv2.putText(image, b5, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return image, b3
    return image, ""
def fonk2():
    b6 = cv2.VideoCapture(0)
    while True:
        ret, b7 = b6.read()
        b8 = cv2.cvtColor(b7, cv2.COLOR_BGR2GRAY)
        image_with_qr, b9 = fonk1(b8)
        cv2.imshow("Camera", image_with_qr)
        if b9:
            break
        if cv2.waitKey(1) & b10 = = ord('q'):
            break
    b6.release()
    cv2.destroyAllWindows()
    return b9
if b11 = = '__main__':
    b12 = fonk2()
    print("QR Code b9:", b12)