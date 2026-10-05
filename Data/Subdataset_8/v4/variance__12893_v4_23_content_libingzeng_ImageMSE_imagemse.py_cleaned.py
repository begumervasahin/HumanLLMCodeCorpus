import cv2
def clamp(value, factor, upper_bound):
    result = value * factor
    if result > upper_bound:
        return upper_bound
    else:
        return result
input_image_1 = './tests/living-room_pfmlt_m310_6629s.png'
input_image_2 = './tests/reference/living-room-reference.png'
colorbar_path = './colourbar.jpg'
difference_image_path = 'dif_' + input_image_1
image_1 = cv2.imread(input_image_1)
image_2 = cv2.imread(input_image_2)
colorbar_image = cv2.imread(colorbar_path)
difference_image = image_1.copy()
show_difference_image = difference_image.copy()
width = image_1.shape[0]
height = image_1.shape[1]
colorbar_width = colorbar_image.shape[0]
colorbar_height = colorbar_image.shape[1]
sum_of_squared_diff = 0
for i in range(width):
    for j in range(height):
        y1 = image_1[i, j][2] * 0.212671 + image_1[i, j][1] * 0.715160 + image_1[i, j][0] * 0.072169
        y2 = image_2[i, j][2] * 0.212671 + image_2[i, j][1] * 0.715160 + image_2[i, j][0] * 0.072169
        diff = y1 - y2
        diff0 = diff
        sum_of_squared_diff += abs(diff) ** 2
        diff0 = clamp(abs(diff0), 5, 255)
        position = int((abs(diff0) / 255.0) * (colorbar_height - 10))
        show_difference_image[i, j] = colorbar_image[0, position]
        difference_image[i, j] = abs(diff0)
mse = sum_of_squared_diff / (width * height)
print('MSE:', mse)
print('Difference image:', difference_image_path)
print('Different data:')
print('Max:', difference_image.max())
print('Min:', difference_image.min())
print('Mean:', difference_image.mean())
cv2.imwrite(difference_image_path, show_difference_image)
cv2.imshow('_dif', show_difference_image)
cv2.waitKey(0)
cv2.destroyAllWindows()