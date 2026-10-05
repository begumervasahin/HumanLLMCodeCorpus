import cv2
def clamp(value, factor, upper_bound):
    result = value * factor
    return min(result, upper_bound)
input_image_1_path = './tests/living-room_pfmlt_m310_6629s.png'
input_image_2_path = './tests/reference/living-room-reference.png'
colour_bar_path = './colourbar.jpg'
difference_image_path = 'dif_' + input_image_1_path
input_image_1 = cv2.imread(input_image_1_path)
input_image_2 = cv2.imread(input_image_2_path)
colour_bar_image = cv2.imread(colour_bar_path)
difference_image = input_image_1.copy()
show_difference_image = difference_image.copy()
image_width, image_height, _ = input_image_1.shape
colour_bar_height, _ = colour_bar_image.shape
sum_squared_difference = 0
for i in range(image_width):
    for j in range(image_height):
        y1 = sum(input_image_1[i, j] * [0.072169, 0.715160, 0.212671])
        y2 = sum(input_image_2[i, j] * [0.072169, 0.715160, 0.212671])
        difference = abs(y1 - y2)
        sum_squared_difference += difference ** 2
        clamped_difference = clamp(difference, 5, 255)
        position = int((clamped_difference / 255.0) * (colour_bar_height - 10))
        show_difference_image[i, j] = colour_bar_image[0, position]
        difference_image[i, j] = clamped_difference
total_pixels = image_width * image_height
mse = sum_squared_difference / total_pixels
print('MSE:', mse)
print('Difference image path:', difference_image_path)
print('Different data:')
print('Max:', difference_image.max())
print('Min:', difference_image.min())
print('Mean:', difference_image.mean())
cv2.imwrite(difference_image_path, show_difference_image)
cv2.imshow('_difference', show_difference_image)
cv2.waitKey(0)
cv2.destroyAllWindows()