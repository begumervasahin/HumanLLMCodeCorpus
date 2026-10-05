class Puzzle:
    def fail_fast(self):
        return False
    def is_solved(self):
        raise NotImplementedError
    def extensions(self):
        raise NotImplementedError