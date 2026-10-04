class Text:
    def __init__(self, text, scrollable=False):
        self.text = text
        self.scrollable = scrollable
        self.current = 0
    def draw(self, surface, position):
        surface.append(f"Drawing '{self.text[self.current:]}' at {position}")
class Conversation:
    def __init__(self, strings, pos):
        self.pos = pos
        self.dialogue = []
        self._format_dialogue(strings)
        self.read = False
        self.current = 0
    def _format_dialogue(self, strings):
        string_part = []
        count = 0
        for x in range(len(strings)):
            string_part.append(Text(strings[x], scrollable=True))
            count += 1
            if count >= 3 or x == len(strings) - 1:
                n = len(string_part)
                for i in range(3 - n):
                    string_part.append(Text('', scrollable=True))
                self.dialogue.append(string_part)
                count = 0
                string_part = []
    def draw(self, surface, pos=None):
        if pos is None:
            pos = self.pos
        count = 0
        if len(self.dialogue) > 0:
            for text in self.dialogue[self.current]:
                text.draw(surface, (pos[0], pos[1] + count * 16))
                if text.current < len(text.text):
                    break
                else:
                    count += 1
if __name__ == "__main__":
    strings = ["Hello!", "How are you?", "This is a long message that might span multiple lines.",
               "This is another message.", "Final message here."]
    position = (10, 20)
    conversation = Conversation(strings, position)
    surface = []
    conversation.draw(surface)
    for item in surface:
        print(item)