
class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance
@SingletonDecorator
class Logger:
    def __init__(self):
        self.start = None
    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)
def main():
    logger1 = Logger()
    logger1.start = "> "
    print("Logger 1:", logger1)
    logger1.write("Logger1 object is created.")
    logger2 = Logger()
    logger2.start = "$ >"
    print("Logger 2:", logger2)
    logger1.write("Logger2 object is created.")
if __name__ == "__main__":
    main()