import cv2
def clamp(value, factor, upper_bound):
    result = value * factor
    return min(result, upper_bound)
input_image_1_path = './tests/living-room_pfmlt_m310_6629s.png'
input_image_2_path = './tests/reference/living-room-reference.png'
colorbar_path = './colourbar.jpg'
difference_image_path = 'dif_' + input_image_1_path
input_image_1 = cv2.imread(input_image_1_path)
input_image_2 = cv2.imread(input_image_2_path)
colorbar_image = cv2.imread(colorbar_path)
difference_image = input_image_1.copy()
show_difference_image = difference_image.copy()
width, height, _ = input_image_1.shape
colorbar_width, colorbar_height, _ = colorbar_image.shape
sum_of_squared_diff = 0
for i in range(width):
    for j in range(height):
        y1 = sum(input_image_1[i, j] * [0.072169, 0.715160, 0.212671])
        y2 = sum(input_image_2[i, j] * [0.072169, 0.715160, 0.212671])
        diff = y1 - y2
        diff_abs = abs(diff)
        sum_of_squared_diff += diff_abs ** 2
        diff_clamped = clamp(diff_abs, 5, 255)
        position = int((diff_clamped / 255.0) * (colorbar_height - 10))
        show_difference_image[i, j] = colorbar_image[0, position]
        difference_image[i, j] = diff_clamped
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