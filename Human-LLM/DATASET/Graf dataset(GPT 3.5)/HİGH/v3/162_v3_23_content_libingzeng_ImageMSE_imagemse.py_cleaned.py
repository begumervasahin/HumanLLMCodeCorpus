import cv2
def fonk1(value, factor, upper_bound):
    b1 = value * factor
    return min(b1, upper_bound)
b2 = './tests/living-room_pfmlt_m310_6629s.png'
b3 = './tests/reference/living-room-reference.png'
b4 = './colourbar.jpg'
b5 = 'dif_' + b2
b6 = cv2.imread(b2)
b7 = cv2.imread(b3)
b8 = cv2.imread(b4)
b9 = b6.copy()
b10 = b9.copy()
image_width, image_height, b11 = b6.shape
colour_bar_height, b11 = b8.shape
a1 = 0
for i in range(image_width):
    for j in range(image_height):
        b12 = sum(b6[i, j] * [0.072169, 0.715160, 0.212671])
        b13 = sum(b7[i, j] * [0.072169, 0.715160, 0.212671])
        b14 = abs(b12 - b13)
        a1 += b14 ** 2
        b15 = fonk1(b14, 5, 255)
        b16 = int((b15 / 255.0) * (colour_bar_height - 10))
        b10[i, j] = b8[0, b16]
        b9[i, j] = b15
b17 = image_width * image_height
b18 = a1 / b17
print('MSE:', b18)
print('Difference image path:', b5)
print('Different data:')
print('Max:', b9.max())
print('Min:', b9.min())
print('Mean:', b9.mean())
cv2.imwrite(b5, b10)
cv2.imshow('_difference', b10)
cv2.waitKey(0)
cv2.destroyAllWindows()