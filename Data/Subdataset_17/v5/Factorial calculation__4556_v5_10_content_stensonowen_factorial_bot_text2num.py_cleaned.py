
SMALL_NUMBERS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}
MAGNITUDES = {
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000,
    'decillion': 1000000000000000000000000000000000,
}
class NumberException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
def text_to_num(tokens):
    current_value = 0
    total_value = 0
    for token in tokens:
        small_value = SMALL_NUMBERS.get(token)
        if small_value is not None:
            current_value += small_value
        elif token == "hundred" and current_value != 0:
            current_value *= 100
        else:
            magnitude_value = MAGNITUDES.get(token)
            if magnitude_value is not None:
                total_value += current_value * magnitude_value
                current_value = 0
            else:
                raise NumberException(f"Unknown number: {token}")
    return total_value + current_value
if __name__ == "__main__":
    test_cases = {
        "one": 1,
        "twelve": 12,
        "seventy two": 72,
        "three hundred": 300,
        "twelve hundred": 1200,
        "twelve thousand three hundred four": 12304,
        "six million": 6000000,
        "six million four hundred thousand five": 6400005,
        "one hundred twenty three billion four hundred fifty six million seven hundred eighty nine thousand twelve": 123456789012,
        "four decillion": 4000000000000000000000000000000000
    }
    for text, expected in test_cases.items():
        result = text_to_num(text.split())
        assert result == expected, f"Test failed for: '{text}', expected: {expected}, got: {result}"
    print("All test cases passed!")