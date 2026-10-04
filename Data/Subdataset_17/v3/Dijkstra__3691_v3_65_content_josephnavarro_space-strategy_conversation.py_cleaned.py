class Text:
    def __init__(self, content, scrollable=False):
        self.content = content
        self.scrollable = scrollable
        self.current_position = 0
    def draw(self, surface, position):
        surface.append(f"Drawing '{self.content[self.current_position:]}' at {position}")
class Conversation:
    def __init__(self, texts, start_position):
        self.start_position = start_position
        self.dialogues = []
        self._format_dialogues(texts)
        self.is_read = False
        self.current_dialogue_index = 0
    def _format_dialogues(self, texts):
        chunk_size = 3
        dialogue_chunk = []
        for i, text in enumerate(texts):
            dialogue_chunk.append(Text(text, scrollable=True))
            if len(dialogue_chunk) >= chunk_size or i == len(texts) - 1:
                while len(dialogue_chunk) < chunk_size:
                    dialogue_chunk.append(Text('', scrollable=True))
                self.dialogues.append(dialogue_chunk)
                dialogue_chunk = []
    def draw(self, surface, position=None):
        if position is None:
            position = self.start_position
        if self.dialogues:
            y_offset = 0
            current_dialogue = self.dialogues[self.current_dialogue_index]
            for text in current_dialogue:
                text.draw(surface, (position[0], position[1] + y_offset))
                if text.current_position < len(text.content):
                    break
                y_offset += 16
if __name__ == "__main__":
    example_texts = [
        "Hello!",
        "How are you?",
        "This is a long message that might span multiple lines.",
        "This is another message.",
        "Final message here."
    ]
    start_position = (10, 20)
    conversation = Conversation(example_texts, start_position)
    surface = []
    conversation.draw(surface)
    for item in surface:
        print(item)