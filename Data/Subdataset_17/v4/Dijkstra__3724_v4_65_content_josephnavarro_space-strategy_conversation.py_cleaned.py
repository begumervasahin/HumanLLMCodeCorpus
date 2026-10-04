from text import Text
class Conversation:
    def __init__(self, strings, start_position):
        self.start_position = start_position
        self.dialogues = []
        self._prepare_dialogues(strings)
        self.is_read = False
        self.current_dialogue_index = 0
    def _prepare_dialogues(self, strings):
        chunk_size = 3
        current_chunk = []
        count = 0
        for string in strings:
            current_chunk.append(Text(string, scrollable=True))
            count += 1
            if count >= chunk_size or len(current_chunk) == len(strings):
                while len(current_chunk) < chunk_size:
                    current_chunk.append(Text('', scrollable=True))
                self.dialogues.append(current_chunk)
                current_chunk = []
                count = 0
    def draw(self, surface, position=None):
        if position is None:
            position = self.start_position
        if self.dialogues:
            y_offset = 0
            for text in self.dialogues[self.current_dialogue_index]:
                text.draw(surface, (position[0], position[1] + y_offset))
                if text.current_position < len(text.content):
                    break
                y_offset += 16
if __name__ == "__main__":
    example_strings = [
        "Hello!",
        "How are you?",
        "This is a long message that might span multiple lines.",
        "This is another message.",
        "Final message here."
    ]
    start_position = (10, 20)
    conversation = Conversation(example_strings, start_position)
    surface = []
    conversation.draw(surface)
    for item in surface:
        print(item)