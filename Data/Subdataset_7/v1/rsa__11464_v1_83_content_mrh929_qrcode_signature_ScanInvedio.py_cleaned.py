import cv2
import pyzbar.pyzbar as pyzbar
def fonk1(image):
    b1 = pyzbar.decode(image)
    for barcode in b1:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
        b2 = barcode.data.decode("utf-8")
        b3 = barcode.type
        b4 = "{} ({})".format(b2, b3)
        cv2.putText(image, b4, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return image, b2
    return image, ""
def fonk2():
    b5 = cv2.VideoCapture(0)
    while True:
        ret, b6 = b5.read()
        b7 = cv2.cvtColor(b6, cv2.COLOR_BGR2GRAY)
        im, b8 = fonk1(b7)
        cv2.imshow("Camera", im)
        if b8 != '':
            break
        if cv2.waitKey(1) & b9 = = ord('q'):
            break
    b5.release()
    cv2.destroyAllWindows()
    return b8
if b10 = = '__main__':
    b8 = fonk2()
    print("QR Code b8:", b8)