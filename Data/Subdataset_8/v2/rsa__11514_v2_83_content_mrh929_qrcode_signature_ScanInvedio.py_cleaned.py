import cv2
import pyzbar.pyzbar as pyzbar
def decode_and_display_qr_codes(image):
    decoded_barcodes = pyzbar.decode(image)
    for barcode in decoded_barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        text = "{} ({})".format(barcode_data, barcode_type)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return image, barcode_data
    return image, ""
def detect_qr_codes():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image_with_qr, content = decode_and_display_qr_codes(gray_frame)
        cv2.imshow("Camera", image_with_qr)
        if content != '':
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
    return content
if __name__ == '__main__':
    qr_code_content = detect_qr_codes()
    print("QR Code content:", qr_code_content)