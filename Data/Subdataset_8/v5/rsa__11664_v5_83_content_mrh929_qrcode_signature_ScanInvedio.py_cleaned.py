import cv2
import pyzbar.pyzbar as pyzbar
def decode_and_display_barcodes(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (225, 225, 225), 2)
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        text = f"{barcode_data} ({barcode_type})"
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (225, 225, 225), 2)
        return image, barcode_data
    return image, ""
def detect_barcodes():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im, content = decode_and_display_barcodes(gray_frame)
        cv2.imshow("camera", im)
        if content:
            break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
    return content
if __name__ == '__main__':
    barcode_content = detect_barcodes()