import re
import math
from collections import Counter
WORD = re.compile(r'\w+')
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    return float(numerator) / denominator
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
def calculate_angle_in_degrees(cosine):
    angle_in_radians = math.acos(cosine)
    return math.degrees(angle_in_radians)
def main():
    text1 = 'This is a foo bar sentence.'
    text2 = 'This sentence is similar to a foo bar sentence.'
    text3 = 'A string that should not be close to the others!'
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    vector3 = text_to_vector(text3)
    cosine1 = get_cosine(vector1, vector2)
    cosine2 = get_cosine(vector1, vector3)
    degrees1 = calculate_angle_in_degrees(cosine1)
    degrees2 = calculate_angle_in_degrees(cosine2)
    print("String 1 is:   " + text1)
    print("String 2 is:   " + text2)
    print("String 3 is:   " + text3)
    print("The cosine similarity angle between string 1 and 2 is {:.2f} degrees".format(degrees1))
    print("The cosine similarity angle between string 1 and 3 is {:.2f} degrees".format(degrees2))
if __name__ == "__main__":
    main()