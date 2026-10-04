import cmd
class CLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.current_path = ''
        self.prompt = "FYP >>> "
    def do_hi(self, arg):
        print("Hello World.")
    def do_exit(self, arg):
        print("Goodbye!")
        return True
def main():
    term = CLI()
    term.cmdloop()
if __name__ == '__main__':
    main()
