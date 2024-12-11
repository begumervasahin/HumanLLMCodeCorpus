import cv2
def fonk1(v, k, upBound):
    b1 = v * k
    if b1 > upBound:
        return upBound
    else:
        return b1
b2 = './tests/living-room_pfmlt_m310_6629s.png'
b3 = './tests/reference/living-room-reference.png'
b4 = './b4.jpg'
b5 = 'dif_' + b2
b6 = cv2.imread(b2)
b7 = cv2.imread(b3)
b8 = cv2.imread(b4)
b9 = b6.copy()
b10 = b9.copy()
b11 = b6.shape[0]
b12 = b6.shape[1]
b13 = b8.shape[0]
b14 = b8.shape[1]
a1 = 0
for i in range(b11):
    for j in range(b12):
        b15 = b6[i, j][2] * 0.212671 + b6[i, j][1] * 0.715160 + b6[i, j][0] * 0.072169
        b16 = b7[i, j][2] * 0.212671 + b7[i, j][1] * 0.715160 + b7[i, j][0] * 0.072169
        b17 = b15 - b16
        a1 += abs(b17) ** 2
        b18 = fonk1(abs(b17), 5, 255)
        b19 = int((b18 / 255.0) * (b14 - 10))
        b10[i, j] = b8[0, b19]
        b9[i, j] = abs(b18)
b20 = a1 / (b11 * b12)
print('MSE:', b20)
print(b5)
print('different data:')
print('max:', b9.max())
print('min:', b9.min())
print('mean:', b9.mean())
cv2.imwrite(b5, b10)
cv2.imshow('_dif', b10)
cv2.waitKey(0)
cv2.destroyAllWindows()