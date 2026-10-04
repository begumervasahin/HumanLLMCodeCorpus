import cmd
class CLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.current_path = ''
        self.prompt = "FYP >>> "
    def do_hi(self, arg):
        print("Hello World.")
def main():
    cli = CLI()
    cli.cmdloop()
if __name__ == '__main__':
    main()