from text import Text
class Conversation:
    def __init__(self, strings, position):
        self.position = position
        self.dialogue = []
        dialogue_part = []
        part_count = 0
        for string in strings:
            dialogue_part.append(Text(string, scrollable=True))
            part_count += 1
            if part_count >= 3 or string == strings[-1]:
                missing_texts = 3 - len(dialogue_part)
                for _ in range(missing_texts):
                    dialogue_part.append(Text('', scrollable=True))
                self.dialogue.append(dialogue_part)
                dialogue_part = []
                part_count = 0
        self.read = False
        self.current = 0
    def draw(self, surface, position=(0, 0)):
        count = 0
        if self.dialogue:
            for text in self.dialogue[self.current]:
                text.draw(surface, (position[0], position[1] + count * 16))
                if text.current < len(text.text):
                    break
                else:
                    count += 1
